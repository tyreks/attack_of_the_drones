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

import os

# application title
APP_TITLE='Smeeta - Drone'

# application base directory
BASE_DIR=os.getcwd()+'/'

# Dictionnarie for wifi key cracking
DICT_DIR="/usr/share/wordlists/"
DEFAULT_DICT=DICT_DIR+"rockyou.txt"

# managed interface to use
#MNG_INTERF='wlp2s0'
MNG_INTERF='wlx00c0caaf2751'

# monitoring interface name, based on the managed one
#MON_INTERF=MNG_INTERF+'mon'
MON_INTERF='wlx00c0caaf2751'


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
NW_DUMP_DURATION=10

# aerodump networks clients dump duration in seconds
CLI_DUMP_DURATION=40

#[RETRIEVER]
HOST = "gdc.cddis.eosdis.nasa.gov"
MAIL = "smeeta@live.fr"
GPS_RES_DIR = BASE_DIR+"/res/gps_res/"

#[GENERATOR]
GPS_SDR_SIM = "/opt/gps-sdr-sim/gps-sdr-sim"
COORDS_DIR = BASE_DIR+"/res/gps_res/coords/"
INPUT_EPHEM_FILE = BASE_DIR+"/res/gps_res/gps_data.n"
OUTPUT = BASE_DIR+"/res/gps_res/gpssim.bin"
SAMPLE_RATE = "2600000"
BITS = "8"
DURATION = "120"

#[TRANSMITTER]
BIN_FILE = BASE_DIR+"/res/gps_res/gpssim.bin"
FREQUENCY = "1575420000"
SAMPLE_RATE = "2600000"
ENABLE_AMPL = "1"
GAIN = "0"
REPEAT = "-R"

DEBUG = False