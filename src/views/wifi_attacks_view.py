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

from ..wifi.wifi_attacker import WifiAttacker
from ..drone import drone as d

class WifiAttacksView:

    menus : list
    wifi_attacker : WifiAttacker
    targeted_drone : d.Drone

    def __init__(self, targeted_drone:d.Drone) -> None:

        # Menus choices initialization
        self.menus = [
              "Deauthenticate legitime user"
            , "Crack wifi key"
            , "Hijack drone"
            , "Return to the home screen "
            , "Quit"]

        # Getting target information
        self.targeted_drone = targeted_drone

        # Wifi attacker initilization
        self.wifi_attacker = WifiAttacker()
        

    def display(self):
        vt.new_page()


        print("\nSelected target : '", self.targeted_drone.get_brand()
            ,"' on network '", self.targeted_drone.get_ssid(),"' BSSID: '", self.targeted_drone.get_bssid()
            ,"', channel: ", self.targeted_drone.get_channel(),"\n")

        print("\nSelect an attack to perform: \n")


        # menu selection
        choice = vt.choose_menu(self.menus)
     
        if (choice=='1'): # Deauthenticate legitime user
            self.deauth_clients_choice()

        elif (choice == '2'): # Crack wifi key
            self.crack_wifi_choice()

        elif (choice=='3'): # Hijack Drone
            self.hijack_drone_choice()

        elif (choice=='4'): # Return to home screen
            view = hv.HomeView()
            view.display()

        elif (choice == '5'): # Exit
            sys.exit(0)


    def deauth_clients_choice(self):
        """
        """
        clients = self.wifi_attacker.get_clients_bssid()
        for cli_bssid in clients:
            self.wifi_attacker.deauth_client(
                self.targeted_drone.get_bssid()
                , cli_bssid
                , self.targeted_drone.get_channel()
                , self.targeted_drone.get_ssid())
            
    
    def hijack_drone_choice(self):
        """
        """
        self.wifi_attacker.hijack_drone(self.targeted_drone)
        pass


    def crack_wifi_choice(self):
        """
        """
        self.wifi_attacker.crack_wifi()


def main():
    view = WifiAttacksView()
    view.display()


if __name__ == "__main__":
    main()