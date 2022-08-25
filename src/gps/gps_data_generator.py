#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import datetime
import re
import subprocess
import sys

from ..config.config import *

class GpsDataGenerator(object):

    date : str
    input_ephem_file : str
    bits : str
    sample_rate : str
    location : str
    duration : str
    output : str
    duration : str

    def __init__(self, date=None, input_ephem_file=INPUT_EPHEM_FILE
        ,bits=BITS, sample_rate=SAMPLE_RATE, location=None
        , duration=DURATION, output=OUTPUT):
        """
        """

        self.location = self.validateLocation(location, COORDS_DIR)

        self.gps_sdr_sim = GPS_SDR_SIM

        self.date = date if date != None\
            else datetime.datetime.utcnow().date().strftime("%Y/%m/%d,H:%M:%S")
            #else datetime.datetime.today().strftime("%Y/%m/%d,07:%M:%S")

        self.input_ephem_file = input_ephem_file

        self.bits = bits
        
        self.sample_rate = sample_rate

        self.output = output

        self.duration  = duration

    @staticmethod
    def validateLocation(location:str, coords_dir:str) -> str:

        resLocation = location

        # regular expression matching GPS coordinates
        regexCoords = "^[-+]?([1-8]?\d(\.\d+)?|90(\.0+)?),\s*"\
            "[-+]?(180(\.0+)?|((1[0-7]\d)|([1-9]?\d))(\.\d+)?)"\
            "(,[0-9]+)?$"
        
        # regular expression for file path
        regexFilePath = "^(.+)\/([^\/]+)$"
            
        if re.match(regexFilePath, coords_dir+location):
            with open(coords_dir+location) as loc_file:
                resLocation = loc_file.readline()
            loc_file.close()
        
        if not re.match(regexCoords, resLocation):
            raise ValueError("Invalid location : "+resLocation
            +" "+coords_dir+location)

        return resLocation


    def generate_gps_data(self):
        """
        """
        try:
            subprocess.run([self.gps_sdr_sim, "-t", self.date, "-e"
                , self.input_ephem_file, "-b", self.bits
                , "-s", self.sample_rate
                , "-l", self.location
                , "-d", self.duration
                , "-o", self.output]
                , capture_output=False)
        except Exception as e:
            raise Exception ("\nError during GPS data generation :\n"+format(e)+"\n\n")
            


def get_parser() -> argparse.ArgumentParser:
    """
    """       
    parser = argparse.ArgumentParser(
        add_help=True, description="Generate the associated"\
            " binary from the local GNSS data file.")

    parser.add_argument("-l", dest="location", required=True
        , help="GPS location to transmit.")

    parser.add_argument("-t", dest="date"
        , help="date (YYYY/MM/DD,HH:MM:SS).")

    parser.add_argument("-e", dest="input_ephem_file"
        , help="GNSS ephemeris file.")

    parser.add_argument("-b", dest="bits"
        , help="Number of bits.")

    parser.add_argument("-s", dest="sample_rate"
        , help="Sample rate (Hz).")

    parser.add_argument("-d", dest="duration"
        , help="Duration of the signal transmission.")


    parser.add_argument("-o", dest="output"
        , help="Generate output file name.")

    return parser


def main():
    """
    """
    try:
        args = get_parser().parse_args()

        my_generator = GpsDataGenerator(date=args.date
            , input_ephem_file=args.input_ephem_file, bits=args.bits
            , sample_rate=args.sample_rate, location=args.location
            , duration=args.duration)

        my_generator.generate_gps_data()
        
    except Exception as exc:
        print (format(exc))
        sys.exit(1)

    return 0

if __name__ == "__main__":
    main()