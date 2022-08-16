#!/usr/bin/env python3
# -*- coding: utf-8 -*-

##############################################################################
# Owner     : Expleo Group
# Author    : Tarek AZAIZ
    # Project   : Drones Attack Demonstrator
    # Subject   : Drone class
    # Version   : 0.1
    # Created   : 2022/06/31
# Modified  : 2022/08/04
##############################################################################


class Drone:

    brand : str
    ssid : str
    bssid : str
    channel : str



    def __init__(self, brand = "", ssid = ""
        , bssid = "", channel = "") -> None:
        """
        Constructor
        """
        self.brand = brand
        self.ssid = ssid
        self.bssid = bssid
        self.channel = channel
    

    # getters

    def get_brand(self):
        return self.brand
    
    
    def get_ssid(self):
        return self.ssid

    
    def get_bssid(self):
        return self.bssid


    def get_channel(self):
        return self.channel

    # setters
    def set_brand(self, brand):
        self.brand = brand
    
    
    def set_ssid(self, ssid):
        self.ssid = ssid

    
    def set_bssid(self, bssid):
        self.bssid = bssid


    def set_channel(self, channel):
        self.channel = channel
    


def main():
    drone = Drone()

if __name__ == "__main__":
    main()