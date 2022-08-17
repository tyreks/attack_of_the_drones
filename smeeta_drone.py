#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""! @brief Example Python program with Doxygen style comments."""


### @package smeeta_drone ####################################################
# Owner     : Expleo Group
# Author    : Tarek AZAIZ
# Project   : Drones Attack Demonstrator
# Subject   : Demonstrator home page
# Version   : 0.1
# Created   : 2022/03/31
# Modified  : 2022/05/04
##############################################################################


import signal
import sys
from src.wifi.wifi_nw_tools import *

from src.views import home_view as h

""" has to be the last import because of a bug in 'click' external lib """
from src.views.views_common_lib import *


## Main function
#
#  More details.
def sig_handler(sig=None, frame=None):
    print("\n\n>> User interruption detected, exiting... <<\n")
    sys.exit(0)

signal.signal(signal.SIGINT, sig_handler)
signal.signal(signal.SIGTERM, sig_handler)

def main():

    view = h.HomeView()
    view.display()


if __name__ == "__main__":
    main()