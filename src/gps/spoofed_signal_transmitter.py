#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import subprocess

from ..config.config import *

class SpoofedSignalTransmitter(object):
    """
    """
    
    def __init__(self, bin_file=BIN_FILE, frequency=FREQUENCY
        , sample_rate=SAMPLE_RATE, enable_ampl=ENABLE_AMPL
        , gain=GAIN, repeat=REPEAT):
        """
        """

        self.bin_file = bin_file

        self.frequency = frequency

        self.sample_rate = sample_rate
            
        self.enable_ampl = enable_ampl

        self.gain = gain

        self.repeat = repeat


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