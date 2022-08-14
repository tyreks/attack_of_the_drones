
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

##############################################################################
# Owner     : Expleo Group
# Author    : Tarek AZAIZ
# Project   : Drones Attack Demonstrator
# Subject   : Useful tools for displaying views (menus, datas)
# Version   : 0.1
# Created   : 2022/03/31
# Modified  : 2022/05/04
##############################################################################

import re
import pyfiglet

from src.config.drn_config import *
import click # this external lib has to be the last import

def clear_scr():
    """ Clear the screen using 'click' library"""
    click.clear()

def print_header(title=APP_TITLE):
    """ Print the application header """
    print(pyfiglet.figlet_format(title))

def new_page(title=APP_TITLE):
    """ Clear the screen then display the hearer """
    clear_scr()
    print_header()

def choose_menu(menus):
    """ Display a menus list and a user prompt """
    for ind, menu in enumerate(menus):
        print(ind+1,": ",menu)
    input = click.prompt("\n Your choice: ")
    return validate_choice(input, menus)


def validate_choice(value, menus):
    """
    Validates the user input by verifying if it corresponds 
    to a valid menu number. If not, displays again the prompt.
    If valid, returns the input after removing the \n last character.
    """
    try:
        if ( (not re.match(r"(^[0-9]$)", value))
            or (int(value) > len(menus))
            or ((int(value) < 1))
        ):
            raise ValueError(value)
        else:
            return value[:-1] #remove end of line
    except ValueError as e:
        click.clear()
        print_header()
        click.echo('/!\ Incorrect menu number. Please try again. /!\ \n')
        return choose_menu(menus)


