Prerequired

First, install gps-sdr-sim. Select a local location then clone the remote repository :
$ git clone gps-sdr-sim

Fhe build the executable with gcc :
$ cd gps-sdr-sim
$ gcc gpssim.c -lm -O3 -o gps-sdr-sim

(Optionnally) Add the gps-sdr-sim to the system path
$ export PATH=$PATH:<current path>

Install hackrf
$ sudo apt install hackrf -y


Installing smeeta-gps-spoof :
1. Select a local location where to clone the remote repository, then clone it :
$ git clone <url>

2. Go to this directory
$ cd ./smeeta-gps-spoof

3. In the config.ini file, replace the default gps-sdr-sim binary path with your's

Usage:
type smeeta_gps-spoofer.py -h to see usage :

$ ./smeeta_gps_spoofer.py -h
usage: smeeta_gps_spoofer.py [-h] [--retrieve] [--generate] [--transmit]

Retrieve the moste recent daily GNSS data file from the NASA site, generate the associated binary and transmit it to spoof the real GPS signal.

optional arguments:
  -h, --help  show this help message and exit
  --retrieve  Retrieve the most recent daily GNSS data file from the NASA site.
  --generate  Generate the binary GPS data from the local GNSS file.
  --transmit  Transmit the GPS signal from the local binary GPS data.
smeeta@debian:~/smeeta-drone$ 