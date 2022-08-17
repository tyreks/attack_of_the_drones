#!/usr/bin/env python3
# -*- coding: utf-8 -*-

##############################################################################
# Owner     : Expleo Group
# Author    : Tarek AZAIZ
    # Project   : Drones Attack Demonstrator
    # Subject   : View (screen) of local system tools for wifi connection.
    # Version   : 0.1
    # Created   : 2022/06/31
# Modified  : 2022/08/04
##############################################################################


import sys
import time

from pwn import *

from . import wifi_targets_view as wv
from . import home_view as hv
from . import views_common_lib as vcl
from .. wifi import wifi_attacker as wa
from .. wifi import wifi_nw_tools as wnt
from .. import config as c


class LocalSysToolsView:

    menus : list

    def __init__(self) -> None:

        # Menus choices initialization
        self.menus = [
              "Display wifi networks" # 1
            , "Kill programs that could interfere with the wireless card" # 2
            , "Restart network service" # 3
            , "Enable wireless interface" # 4
            , "Disable wireless interface" # 5
            , "Restore wireless interface to initial state" # 6
            , "Start wireless interface in monitoring mode" # 7
            , "Set back wireless interface to managed mode" # 8
            , "Previous screen" # 9
            , "Return to home screen" # 10
            , "Quit"] # 11
        

    def display(self):
        vcl.new_page()

        print("Select a tool operation to perform on local system: \n")

        # menu selection
        choice = vcl.choose_menu(self.menus)

        if (choice=='1'): # List wifi networks
            self.display_wifi_nw_choice()

        elif (choice=='2'): # Kill problematics programs
            self.check_kill_choice()

        elif (choice == '3'): # Restart network service
            self.restart_nw_choice()

        elif (choice == '4'):
            # Enable wireless interface
            self.enable_interf_choice()

        elif (choice == '5'): # Disable wireless interface
            self.disable_interf_choice()

        elif (choice=='6'): # Reset wireless interface
            self.restore_interf_choice()

        elif (choice=='7'): # Start wireless interface monitoring mode
            self.set_monitoring_mode_choice()

        elif (choice=='8'): # Set back wireless interface to managed mode
            self.set_managed_mode_choice()

        elif (choice=='9'): # Previous screen (wifi view)
            view = wv.WifiTargetsView()
            view.display()
            return # to avoid recursive call from other view

        elif (choice=='10'): # Return to home screen
            view = hv.HomeView()
            view.display()
            return # to avoid recursive call from other view

        elif (choice == '11'): # Exit program
            sys.exit(0)

        # sleep 3 seconds then display the view again
        time.sleep(3)
        self.display()


    def display_wifi_nw_choice(self):
        """
        """
        wifi_attacker = wa.WifiAttacker()
        wifi_attacker.list_wifi_nw(capture_output=False)
        input("\n\t >> Press [ENTER] to continue... <<\n")


    def check_kill_choice(self):
        """
        """
        progress = log.progress("Killing programs that could"
            " interfere with the wireless card...")
        try:
            wnt.check_kill(hide_output=False)
        except Exception as e:
            progress.failure(format(e))
        progress.success()


    def restart_nw_choice(self):
        """
        """
        progress = log.progress("Restarting network service...")
        try:
            wnt.restart_nw(hide_output=False)
        except Exception as e:
            progress.failure(format(e))
        progress.success()
    

    def enable_interf_choice(self):
        """
        """
        progress = log.progress("Enabling interface...")
        try:
            wnt.enable_interf(interface=c.MNG_INTERF, hide_output=False)
        except Exception as e:
            progress.failure(format(e))
        progress.success()


    def disable_interf_choice(self):
        """
        """
        progress = log.progress("Disabling interface...")
        try:
            wnt.disable_interf(interface=c.MNG_INTERF, hide_output=False)
        except Exception as e:
            progress.failure(format(e))
        progress.success()


    def restore_interf_choice(self):
        """
        """
        progress = log.progress("Restoring interface to initial state...")
        try:
            wnt.restore_interf(interf=c.MNG_INTERF, hide_output=False)
        except Exception as e:
            progress.failure(format(e))
        progress.success()        


    def set_monitoring_mode_choice(self):
        """
        """
        progress = log.progress("Starting interface in monitoring mode...")
        try:        
            wnt.start_mon(channel='', interface=c.MNG_INTERF, hide_output=False)
        except Exception as e:
            progress.failure(format(e))
        progress.success()   


    def set_managed_mode_choice(self):
        """
        """
        progress = log.progress("Starting interface in monitoring mode...")
        try:      
            wnt.stop_mon(interface=c.MON_INTERF, hide_output=False)
        except Exception as e:
            progress.failure(format(e))
        progress.success()  

    
def main():
    view = LocalSysToolsView()
    view.display()


if __name__ == "__main__":
    main()