#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
from configparser import ConfigParser
import subprocess


class SpoofedSignalTransmitter(object):
    """
    """
    
    def __init__(self, bin_file=None, frequency=None
        , sample_rate=None, enable_ampl=None
        , gain=None, repeat=None):
        """
        """

        parser = ConfigParser()
        parser.read("config.ini")

        self.bin_file = bin_file if bin_file != None \
            else parser["TRANSMITTER"]["BIN_FILE"]

        self.frequency = frequency if frequency != None \
            else parser["TRANSMITTER"]["FREQUENCY"]

        self.sample_rate = sample_rate if sample_rate != None \
            else parser["TRANSMITTER"]["SAMPLE_RATE"]
            
        self.enable_ampl = enable_ampl if enable_ampl != None \
            else parser["TRANSMITTER"]["ENABLE_AMPL"]

        self.gain = gain if gain != None \
            else parser["TRANSMITTER"]["GAIN"]

        self.repeat = repeat if repeat != None \
            else parser["TRANSMITTER"]["REPEAT"]


    def transmit(self):
        """
        """
        try:
            subprocess.run(["hackrf_transfer", "-t", self.bin_file
                , "-f", self.frequency, "-s", self.sample_rate
                , "-a", self.enable_ampl, "-x", self.gain, self.repeat]
                , capture_output=False)
        except Exception as e:
            print("\nError during the spoofed signal transmission :\n"
                +format(e)+"\n\n")
            return 1


def get_parser() -> argparse.ArgumentParser:
    """
    """       
    parser = argparse.ArgumentParser(
        add_help=True, description="Transmit the spoofed GPS signal.")

    parser.add_argument("-t", dest="bin_file"
        , help="The binary file generated from the last retrieved"\
        " GNSS data file.")

    parser.add_argument("-f", dest="frequency"
        , help="The frequency of the GPS signal.")

    parser.add_argument("-s", dest="sample_rate"
        , help="Sample frequency (Hz)")

    parser.add_argument("-a", dest="enable_ampl"
        , help="Enable amplification (0 or 1)")

    parser.add_argument("-x", dest="gain"
        , help="Gain (dB)")

    parser.add_argument(
        "-R", "--repeat", action='store_const', const="-R", default=""
        , help="Send the signal repeatedly.")

    return parser


def main() ->int:
    """
    """
    args = get_parser().parse_args()

    transmitter = SpoofedSignalTransmitter(bin_file=args.bin_file
        , frequency=args.frequency, sample_rate=args.sample_rate
        , enable_ampl=args.enable_ampl, gain=args.gain
        , repeat=args.repeat)

    transmitter.transmit()

    return 0

if __name__ == "__main__":
    main()