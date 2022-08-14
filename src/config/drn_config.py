#!/usr/bin/env python3
# -*- coding: utf-8 -*-

##############################################################################
# Author    : Tarek AZAIZ
# Project   : Drones Attack Demonstrator
# Subject   : Configuration file
# Version   : 0.1
# Created   : 2022/03/31
# Modified  : 2022/05/04
##############################################################################

# managed interface to use
MNG_INTERF='wlan0'

# monitoring interface name, based on the managed one
MON_INTERF=MNG_INTERF+'mon'

# application base directory
BASE_DIR='/mnt/prst/smeeta/'

# directory where are generated dump files
DUMP_DIR=BASE_DIR+'res/dump/'

# directory where are generated networks dump files
NW_DUMP_DIR=DUMP_DIR+'nw/'

# directory where are generated networks clients dump files
CLI_DUMP_DIR=DUMP_DIR+'cli/'

# aerodump networks dump file prefix
NW_DUMP_FILE_PREFIX='dump_nw_list'

# aerodump specific network clients dump file prefix
CLI_DUMP_FILE_PREFIX = 'dump_cli_list'

# CSV networks dumping output file
CSV_NW_DUMP = NW_DUMP_DIR+NW_DUMP_FILE_PREFIX+'-01.csv'

# CSV clients dumping output file
CSV_CLI_DUMP = CLI_DUMP_DIR+CLI_DUMP_FILE_PREFIX+'-01.csv'

CAP_CLI_DUMP = CLI_DUMP_DIR+CLI_DUMP_FILE_PREFIX+'-01.cap'

# aerodump networks dump duration in seconds
NW_DUMP_DURATION=30

# aerodump networks clients dump duration in seconds
CLI_DUMP_DURATION=40

# application title
APP_TITLE='Smeeta - Drone'
