#!/usr/bin/env python3
# -*- coding: utf-8 -*-

##############################################################################
# Owner     : Expleo Group
# Author    : Tarek AZAIZ
    # Project   : Drones Attack Demonstrator
    # Subject   : View (screen) of radio jamming choices
    # Version   : 0.1
    # Created   : 2022/06/31
# Modified  : 2022/08/04
##############################################################################


import sys
from . import local_sys_tools_view as lstv
from . import views_common_lib as vt
from . import home_view as hv

from ..wifi.wifi_attacker import WifiAttacker

class WifiView:

    menus : list
    wifi_attacker : WifiAttacker

    def __init__(self) -> None:

        # Menus choices initialization
        self.menus = [
            #  "Display wifi networks" 
            #, 
              "Detect again"
            , "Deauthenticate legitime user"
            , "Crack wifi key"
            , "Change wifi password"
            , "Hijack drone"
            , "Local system wifi tools"
            , "Return to the home screen "
            , "Quit"]

        # Wifi attacker initilization
        self.wifi_attacker = WifiAttacker()
        

    def display(self):
        vt.new_page()

        print("Select an attack to perform: \n")

        # menu selection
        choice = vt.choose_menu(self.menus)
        """"
        if (choice=='1'): # List wifi networks
            self.wifi_attacker.list_wifi_nw(capture_output=False)

            input("\t\n\n>> Press 'Enter' to continue <<\n ")
        """
        if (choice=='1'): # Detect drones
            self.wifi_attacker.detect_drones()
            pass


        elif (choice == '2'): # Deauthenticate legitime user
            pass


        elif (choice == '3'): # Crack wifi key
            pass


        elif (choice == '4'): # Change wifi password"
            pass


        elif (choice=='5'): # Hijack Drone
            pass

        elif (choice=='6'): # Local system tools view
            view = lstv.LocalSysToolsView()
            view.display()

        elif (choice == '7'): # Return to home screen
            view = hv.HomeView()
            view.display()

        elif (choice == '8'): # Exit
            sys.exit(0)
    
def main():
    view = WifiView()
    view.display()


if __name__ == "__main__":
    main()