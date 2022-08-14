import sys
import time

import src.views.view_tools as vt
import src.wifi.wifi_availables_nw as nw
import src.views.detect as tgt
import src.views.home_view as h
from .. gps import smeeta_gps_spoofer as gps

class SpoofGpsView:

    menus : list
    spoofer : gps.SmeetaGpsSpoofer

    def __init__(self) -> None:

        # Menus choices initialization
        self.menus = [
              "Paris (France), Eiffel Tower"
            , "Paris (France), Charles de Gaulle Airport (No flight zone)"
            , "New York, USA"
            , "Moscow, Russia"
            , "Enter location manually"
            , "Home screen"
            , "Quit"]

        # spoofer initilization
        self.spoofer = gps.SmeetaGpsSpoofer()


    def display(self):
        vt.new_page()

        print("Select a fake location for spoofing :\n")

        # menu selection
        choice = vt.choose_menu(self.menus)

        if (choice == '1'): # Paris, Eiffel Tower
            self.spoofer.set_location("paris_eiffel_tower.txt")
            self.spoofer.spoof()
        
        
        elif (choice == '2'): # Paris, Charles de Gaulle Airport
            self.spoofer.set_location("paris_cdg_airport.txt")
            self.spoofer.spoof()

        elif (choice == '3'): # New York, USA
            self.spoofer.set_location("new_york.txt")
            self.spoofer.spoof()

        elif (choice == '4'): # Moscow, Russia
            self.spoofer.set_location("moscow.txt")
            self.spoofer.spoof()

        elif (choice == '5'): # Enter location manually
            location = input("\nEnter the location latitude,longitude,height"
                    +"(ex: 55.75549811797889,37.6171829009649,100) : \n")
        
            # remove the last char ('\n') and set location
            self.spoofer.set_location(location[:-1])
            
            # perform spoofing
            self.spoofer.spoof()

        elif (choice == '6'): # Home Screen
            view = h.HomeView()
            view.display()
        
        elif (choice == '6'): # Home Screen
            sys.exit(0)
        
    
def main():
    spoof_gps_view = SpoofGpsView()
    spoof_gps_view.display()


if __name__ == "__main__":
    main()