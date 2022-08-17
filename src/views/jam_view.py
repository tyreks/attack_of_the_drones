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


import src.views.views_common_lib as vt
import src.views.home_view as h
import src.radio.jammer as j


class JamView:

    menus : list
    jammer : j.Jammer

    def __init__(self) -> None:

        # Menus choices initialization
        self.menus = [
              "433 MHz (ex: car remote controller)"
            , "1.57542 GHz (ex: L1 GPS band)"
            , "2.412 GHz (ex: Wifi channel 1)"
            , "2.437 GHz (ex: Wifi channel 6)"
            , "2.462 GHz (ex: Wifi channel 11)"
            , "Enter the frequency manually"
            , "Return to the home screen "
            , "Quit"]

        # Jammer initilization
        self.jammer = j.Jammer()
        

    def display(self):
        vt.new_page()

        print("Select a frequency to jam :\n")

        # menu selection
        choice = vt.choose_menu(self.menus)

        if (choice=='1'): # 433 Mhz
            self.jammer.set_center_freq(433e6)
            self.jammer.start_jamming()

        elif (choice=='2'): # 1.57542 GHz
            self.jammer.set_center_freq(157542e4)
            self.jammer.start_jamming()

        elif (choice == '3'): # 2.412 GHz (ex: Wifi channel 1)
            self.jammer.set_center_freq(2412e6)
            self.jammer.start_jamming()

        elif (choice == '4'): # 2.437 GHz (ex: Wifi channel 6)
            self.jammer.set_center_freq(2437e6)
            self.jammer.start_jamming()

        elif (choice == '5'): # 2.462 GHz (ex: Wifi channel 11)
            self.jammer.set_center_freq(2462e6)
            self.jammer.start_jamming()

        elif (choice=='6'): # Enter the frequency manually
            freq = int(input("\nEnter the frequency to jam in MHz (1 - 6000) "))
            self.jammer.set_center_freq(freq * 10e6)
            self.jammer.start_jamming()

        elif (choice == '7'): # GO to home screen
            view = h.HomeView()
            view.display()
    
def main():
    jam_view = JamView()
    JamView.display()


if __name__ == "__main__":
    main()