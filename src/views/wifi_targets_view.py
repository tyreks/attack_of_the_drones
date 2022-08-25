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
              "Detect again"
            , "Return to the home screen "
            , "Quit"]

        # Wifi attacker initilization
        self.wifi_attacker = WifiAttacker()
        

    def display(self):

        try:
            # start by idetecting drones
            vt.new_page()
            print("\nDetecting drones, please wait...\n")
            targets = self.wifi_attacker.detect_drones()
            nb_targets = len(targets)

            # clear screen and display one menu choice per target
            vt.new_page()
            self.display_targets_choices(targets)

            # menu selection
            choice = vt.choose_menu(self.menus)

            # for each detected drone, make a specific call for attack
            if int(choice) <= nb_targets:
                i = int(choice) - 1
                targeted_drone = d.Drone(
                    brand=targets[i][0], ssid=targets[i][1]
                    , bssid=targets[i][2], channel=targets[i][3])
                view = wav.WifiAttacksView(targeted_drone)
                view.display()

            if choice==str(nb_targets + 1): # Detect drones again
                self.display()

            elif choice==str(nb_targets + 2): # Return to home screen
                view = hv.HomeView()
                view.display()

            elif choice==str(nb_targets + 3): # Exit
                sys.exit(0)

        except Exception as e:
            raise(Exception(f"{e}"))        
        
        
    def display_targets_choices(self, targets):
        """
        display one menu choice for each target
        """
        try:
            if len(targets) == 0:
                print("\nNo target detected\n")
            else:
                print("\nSelect a target to attack: \n")
                tmp_menus = []
                for t in targets:
                    if t[1] != '': # if ssid not empty
                        # insert the menu choice corresponding to this target
                        """
                        self.menus.insert(0, 
                            "'"+t[0]+"' providing '"+t[1]+"' network (channel "
                            +t[3]+", BSSID: "+t[2]+")")
                        """
                        tmp_menus.append("'"+t[0]+"' providing '"+t[1]+"' network (channel "
                            +t[3]+", BSSID: "+t[2]+")")
                
                # modify the initial choices menu
                self.menus = tmp_menus + self.menus
                
        except Exception as e:
            raise(Exception(f"{e}"))   

def main():
    view = WifiTargetsView()
    view.display()


if __name__ == "__main__":
    main()