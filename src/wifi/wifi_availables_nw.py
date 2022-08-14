#!/usr/bin/env python3
# -*- coding: utf-8 -*-

##############################################################################
# Owner     : Expleo Group
# Author    : Tarek AZAIZ
# Project   : Drones Attack Demonstrator
# Subject   : Listing of the available Wifi networks
# Version   : 0.1
# Created   : 2022/03/31
# Modified  : 2022/05/04
##############################################################################

# devices
import pandas
from src.wifi.wifi_nw_tools import *

def detect_nw():
    restore_interf()
    start_mon()
    dump_all_nw()
    restore_interf()

def display_nw_list():
    # import and sort the CSV dumping input file
    df = pandas.read_csv(CSV_NW_DUMP, usecols=[' Power', ' ESSID', 'BSSID', ' channel'])
    df.sort_values([" Power"], axis=0, ascending=[False], inplace=True)
    print(df)

def main():
    detect_nw()

if __name__ == "__main__":
    main()