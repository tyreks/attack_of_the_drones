#!/usr/bin/env python3
# -*- coding: utf-8 -*-

##############################################################################
# Owner     : Expleo Group
# Author    : Tarek AZAIZ
# Project   : Drones Attack Demonstrator
# Subject   : Radio jamming using HackRF One (HRF1). Note : HRF1 can't
#             jam 5GHz frequencies without amplifier
# Version   : 0.1
# Created   : 2022/04/25
# Modified  : 2022/06/02
##############################################################################

# https://fccid.io site qui reference les FCC ID (10 char qui caractérisent
# un terminal réseau, notamment le mode de modulation et la fréquence)


from gnuradio import analog
from gnuradio import gr
import sys
import signal
import osmosdr


class Jammer(gr.top_block):

    def __init__(self):
        gr.top_block.__init__(self, "Smeeta Drone - Radio Jammer")

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 2e6
        self.center_freq = center_freq = 2437e6
        self.bw = bw = 5e6

        ##################################################
        # Blocks
        ##################################################
        self.osmosdr_sink_0 = osmosdr.sink(
            args="numchan=" + str(1) + " " + "hackrf=0"
        )
        self.osmosdr_sink_0.set_time_unknown_pps(osmosdr.time_spec_t())
        self.osmosdr_sink_0.set_sample_rate(samp_rate)
        self.osmosdr_sink_0.set_center_freq(center_freq, 0)
        self.osmosdr_sink_0.set_freq_corr(0, 0)
        self.osmosdr_sink_0.set_gain(47, 0)
        self.osmosdr_sink_0.set_if_gain(47, 0)
        self.osmosdr_sink_0.set_bb_gain(47, 0)
        self.osmosdr_sink_0.set_antenna('', 0)
        self.osmosdr_sink_0.set_bandwidth(bw, 0)
        self.analog_noise_source_x_0 = analog.noise_source_c(analog.GR_GAUSSIAN, 1, 0)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_noise_source_x_0, 0), (self.osmosdr_sink_0, 0))

    
    def start_jamming(self):

        def sig_handler(sig=None, frame=None):
            self.stop()
            self.wait()
            sys.exit(0)

        signal.signal(signal.SIGINT, sig_handler)
        signal.signal(signal.SIGTERM, sig_handler)

        self.start()

        try:
            input('\n\t >> Press [Enter] to stop jamming... << \n')
        except EOFError:
            pass
        self.stop()
        #self.wait()

    # getters
    def get_center_freq(self):
        return self.center_freq

    def get_samp_rate(self):
        return self.samp_rate

    def get_bw(self):
        return self.bw

    # setters

    def set_center_freq(self, center_freq):
        self.center_freq = center_freq
        self.osmosdr_sink_0.set_center_freq(self.center_freq, 0)

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.osmosdr_sink_0.set_sample_rate(self.samp_rate)


    def set_bw(self, bw):
        self.bw = bw
        self.osmosdr_sink_0.set_bandwidth(self.bw, 0)


def main():

    try:
        jammer = Jammer()
        jammer.start_jamming()
    except Exception as exc:
        print ("Error during jamming : ",format(exc))
        sys.exit(1)


if __name__ == '__main__':
    main()
