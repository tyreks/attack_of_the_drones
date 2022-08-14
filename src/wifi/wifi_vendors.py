#!/usr/bin/env python3
# -*- coding: utf-8 -*-

##############################################################################
# Owner     : Expleo Group
# Author    : Tarek AZAIZ
# Project   : Drones Attack Demonstrator
# Subject   : Get correspondance between mac adress and constructor
#             according to the IEE's Organizationally Unique Identifiers list
#             https://standards-oui.ieee.org/
#
#             Not found Vendors : Abot, Autel Robotics, Chasing innovation,
#             Eachine, Hobbico, Hubsan, iBubble, JJRC,PJN /AEE, Powervision,
#             Star Wars Drones, SwellPro, Yuneec
#
#             O.U.I to confirm, because their vendor contains the "drone" word
#             in their name : Vimodrone (000ECE), Teal Drones(B030C8)
#
# Version   : 0.1
# Created   : 2022/03/31
# Modified  : 2022/05/04
##############################################################################


# Dictionnary containing the list of the OUI MAC prefixes for each know vendor
VENDOR_MAC_OUI = {}
VENDOR_MAC_OUI["PARROT"]    = {"90:3A:E6", "00:12:1C", "90:03:B7"
    , "A0:14:3D", "00:26:7E"}
VENDOR_MAC_OUI["DJI"]       = {"60:60:1F","34:D2:62"}
VENDOR_MAC_OUI["GOPRO"]     = {"24:74:F7", "D8:96:85", "04:41:69"}
#VENDOR_MAC_OUI["XIAOMI"]    = {"48:87:59", "AC:1E:9E", "64:DD:E9"}

# my phone's hotspotstart
VENDOR_MAC_OUI["FAKE_DRONE_XIAOMI"] = {"4A:15:A4"}


def get_vendor(mac_oui:str) -> str:
    """
    returns the vendor's name matching the OUI MAC prefix 
    or an empty string if no match
    """
    for vendor in VENDOR_MAC_OUI:
        if mac_oui in VENDOR_MAC_OUI[vendor]:
            return vendor
    return ""


def get_mac_oui_list(vendor:str) -> list[str]:
    """
    returns the list of OUI MAC prefixes corresponding to the vendor name
    or an empty list in case of unknown vendor
    """
    try:
        return VENDOR_MAC_OUI[vendor]
    except KeyError:
        return []