#!/usr/bin/env python3
# -*- coding: utf-8 -*-

##############################################################################
# Owner     : Expleo Group
# Author    : Tarek AZAIZ
# Project   : Drones Attack Demonstrator
# Subject   : Listing of the potential targets in the available WiFi networks
# Version   : 0.1
# Created   : 2022/03/31
# Modified  : 2022/05/04
##############################################################################

import pandas
from pwn import *

from src.wifi.wifi_nw_tools import *
from src.wifi.wifi_vendors import *
import src.views.clients_of_target as cli 
""" has to be the last import because of a bug in 'click' external lib """
from src.views.view_tools import *


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


def main():

    menus = []

    targets = get_target_networks()
    
    if len(targets) == 0:
        print ("No targets detected")
    else:
        print("The following targets have been detected. Please select one:\n")
        for t in targets:
            menus.append("'"+t[0]+"' providing '"+t[1]+"' network (channel "+t[3]+", BSSID: "+t[2]+")")
    
        choice = int(choose_menu(menus))
        target = []
        target = targets[choice - 1]
    
        # deauthenticate the legitime user
        # vendor = target[0]
        essid = target [1]
        ap_bssid = target[2]
        chan = target[3]


        # prepare dump for next menu
        dump_target_network(chan, ap_bssid)
        
        # next menu : clients of target
        new_page()
        cli.main(ap_bssid, essid, chan)




if __name__ == "__main__":
    main()

