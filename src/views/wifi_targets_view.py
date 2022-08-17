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
from . import wifi_attacks_view as wav

from ..wifi.wifi_attacker import WifiAttacker
from ..drone import drone as d

class WifiTargetsView:

    menus : list
    wifi_attacker : WifiAttacker

    def __init__(self) -> None:

        # Menus choices initialization
        self.menus = [
            #  "Display wifi networks" 
            #, 
              "Detect again"
            , "Local system wifi tools"
            , "Return to the home screen "
            , "Quit"]

        # Wifi attacker initilization
        self.wifi_attacker = WifiAttacker()
        

    def display(self):

        # start by inserting detected drones to menus choices
        vt.new_page()
        targets = self.wifi_attacker.detect_drones()

        nb_targets = len(targets)

        if nb_targets == 0:
            print("No target detected")
        else:
            print("\nSelect a target to attack: \n")
            for t in targets:
                if t[1] != '':
                    self.menus.insert(0, 
                        "'"+t[0]+"' providing '"+t[1]+"' network (channel "
                        +t[3]+", BSSID: "+t[2]+")")


        # menu selection
        choice = vt.choose_menu(self.menus)

        # for each detected drone, make a specific call for attack
        if int(choice) <= nb_targets:
            targeted_drone = d.Drone(brand=t[0], ssid=t[1], bssid=t[2], channel=t[3])
            view = wav.WifiAttacksView(targeted_drone)
            view.display()

        if choice==str(nb_targets + 1): # Detect drones again
            self.display()


        elif choice==str(nb_targets + 2): # Local system tools view
            view = lstv.LocalSysToolsView()
            view.display()

        elif choice==str(nb_targets + 3): # Return to home screen
            view = hv.HomeView()
            view.display()

        elif choice==str(nb_targets + 4): # Exit
            sys.exit(0)
    
def main():
    view = WifiTargetsView()
    view.display()


if __name__ == "__main__":
    main()