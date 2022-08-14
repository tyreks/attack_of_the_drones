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


import os
import sys
import time
import src.views.view_tools as vt
import src.views.home_view as h

from ..wifi import wifi_attacker as wa

class WifiView:

    menus : list
    wifi_attacker : wa.WifiAttacker

    def __init__(self) -> None:

        # Menus choices initialization
        self.menus = [
              "Display wifi networks"
            , "Detect drones"
            , "Deauthenticate legitime user"
            , "Crack wifi key"
            , "Change wifi password"
            , "Hijack drone"
            , "Return to the home screen "
            , "Quit"]

        # Jammer initilization
        self.wifi_attacker = wa.WifiAttacker()
        

    def display(self):
        vt.new_page()

        print("Select an attack to perform: \n")

        # menu selection
        choice = vt.choose_menu(self.menus)

        if (choice=='1'): # List wifi networks
            self.wifi_attacker.list_wifi_nw(capture_output=False)

            input("\t\n\n>> Press 'Enter' to continue <<\n ")

        elif (choice=='2'): # Detect drones
            self.wifi_attacker.detect_drones()
            pass


        elif (choice == '3'): # Deauthenticate legitime user
            pass


        elif (choice == '4'): # Crack wifi key
            pass


        elif (choice == '5'): # Change wifi password"
            pass


        elif (choice=='6'): # Hijack Drone
            pass

        elif (choice == '7'): # GO to home screen
            view = h.HomeView()
            view.display()

        elif (choice == '8'): # Exit
            sys.exit(0)
    
def main():
    view = WifiView()
    view.display()


if __name__ == "__main__":
    main()