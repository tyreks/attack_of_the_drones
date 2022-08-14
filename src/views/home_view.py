import sys
import time

from . import view_tools as vt
from . import detect as tgt
from . import jam_view as jam
from . import spoof_gps_view as gps

from .. wifi import  wifi_availables_nw as nw



class HomeView:

    menus : list

    def __init__(self) -> None:
        self.menus = [
              "Detect"
            , "Hijack"
            , "Spoof GPS"
            , "Jam"
            , "Settings"
            , "Quit"]

    def display(self):
        vt.new_page()
        print("Select an attack to perform: \n")
        # menu selection
        choice = vt.choose_menu(self.menus)

        if (choice=='1'): # "Detect" choice
            # detect all availables targets
            nw.detect_nw()
            time.sleep(3)
            vt.new_page()

            # detect targets : networks hosted by drones
            tgt.main()
        
        elif (choice == '2'):
            pass
                
        elif (choice == '3'): # GPS Spoofing
            view = gps.SpoofGpsView()
            view.display()
            #gps_spoofer = gps.SmeetaGpsSpoofer(location="res/coords/moscow.txt")
            #gps_spoofer.spoof()


            pass
        
        elif (choice == '4'): # Radio jamming
            view = jam.JamView()
            view.display()
    
            
        elif (choice == '6'): # Exit
            sys.exit(0)

        # in the end, back to home screen3
        time.sleep(3)
        self.display()




def main():
    home_page = HomeView()
    home_page.display()


if __name__ == "__main__":
    main()