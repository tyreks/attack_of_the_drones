import sys
import time

from . import views_common_lib as vt
#from . import detect as tgt
from . import jam_view as jam
from . import spoof_gps_view as gps
from . import wifi_targets_view as wifi

#from .. wifi import  wifi_availables_nw as nw



class HomeView:

    menus : list

    def __init__(self) -> None:
        self.menus = [
            "Wifi attacks"
            , "GPS spoofing"
            , "Radio jamming"
            , "Quit"]

    def display(self):
        vt.new_page()
        print("Select an attack to perform: \n")
        # menu selection
        choice = vt.choose_menu(self.menus)
        """
        if (choice=='1'): # "Detect" choice
            # detect all availables targets
            nw.detect_nw()
            time.sleep(3)
            vt.new_page()

            # detect targets : networks hosted by drones
            tgt.main()
        """     

        if (choice == '1'): # Wifi attacks
            view = wifi.WifiTargetsView()
            view.display()

        elif (choice == '2'): # GPS Spoofing
            view = gps.SpoofGpsView()
            view.display()
        
        elif (choice == '3'): # Radio jamming
            try:
                view = jam.JamView()
                view.display()
            except Exception as e:
                print("\n\t>> Error : no HackRF detected."\
                    "please connect it and retry. <<\n")
                time.sleep(2)
            
        elif (choice == '4'): # Exit
            sys.exit(0)

        # in the end, back to home screen3
        time.sleep(3)
        self.display()




def main():
    home_page = HomeView()
    home_page.display()


if __name__ == "__main__":
    main()