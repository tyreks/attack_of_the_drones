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


import src.wifi.wifi_availables_nw as nw
import src.views.home_view as h

""" has to be the last import because of a bug in 'click' external lib """
from src.views.view_tools import *


## Main function
#
#  More details.
def main():

    view = h.HomeView()
    view.display()


if __name__ == "__main__":
    main()