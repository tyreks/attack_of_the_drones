# [Smeeta Drone] (https://smeeta.org)

Smeeta Drone is a drone attacks demonstrator, designed to highlight the flaws present on this type of intelligent (or even autonomous) vehicles in order to better understand how to protect oneself against them.

Smeeta Drone is extremly easy-to-use and doesn't need any complicated complicated manipulations or special technical knowledge : all attacks are performed from ordered and explained menu choices.

Moreover, Smeeta Drone has been designed to be easily enriched by collaborative work through an easy-to-understand class architecture.

For now, some attacks have been implemented, such as Wifi scan detection, gps spoofing, wifi cracking or the resulting takeover. These attacks work more or less depending on the level of security in place on the targeted drones.

They have been successfully tested on the Parrot AR Drone 2.0 and the DJI Phantom 2 Vision.

Other attacks are to come and they will be tested on more and more secure drones, in order to improve Smeeta Drone's attack level.

Smeeta Drone is part of the "Smeeta OS" operating system, specialized in the evaluation of the security of intelligent vehicles and autonomous vehicles.

by [@Smeeta-OS] [@Tyreks]

## Usage: 
$ git clone https://github.com/tyreks/attack_of_the_drones.git
then

run ./smeeta_drone (ideally in sudo mode) and let it guide you :)


## Hardware required
All the necessary equipment is pre-integrated in the Expleo Smeeta Case (link to come).

Here is the list of minimum equipment required to use Smeeta Drone:

- A HackRF One equipped with a TCXO PPM0.1
- A wifi card supporting monitoring and packet injection
- A computer running Linux (ideally Smeeta OS, which includes all the dependencies)
- A drone controlled by Wifi (e.g. Parrot AR Drone 2.0)
- Ideally, also a drone controlled by long-range radio and having Wifi localization (ex: DJI Phantom 2 Vision)


## Software Dependancies

All dependancies are preinstalled in Smeeta OS (https://smeeta.org). Here is the list and the associated installation commands.

### pip (required for further pip modules installations)
sudo apt install pip

### pandas : *.csv file handling
pip install pandas

### pwntools : progress bar formatting
pip install pwntools

### pyfiglet : title in ASCII art
pip install pyfiglet

### click : menu with choices
pip install click

### gr-osmosdr : hackr one and other sdr hardware handling in python
sudo apt install gr-osmosdr -y

### gnuradio : radio module required by gr-osmosdr
sudo apt install gnuradio -y

### aircrack-ng : wifi cracking module
sudo apt install aircrack-ng -y

### hackrf : hackrf one sdr hardware library
sudo apt install hackrf -y

### nodejs : required for executing ar-drone nodejs module
sudo apt install nodejs npm -y

### ar-drone : nodejs module for parrot ar 2.0 controlling
npm install ar-drone

### ffmpeg : require by ar-drone module for accessing drone video stream
sudo apt install ffmpeg -y

### gps-sdr-sim : required for gps spoofing
cd /opt
git clone https://github.com/osqzss/gps-sdr-sim.git
cd ./gps-sdr-sim
gcc gpssim.c -lm -O3 -o gps-sdr-sim


## Remarks and questions

Do not hesitate to send your remarks and questions to the following addresses, we will be happy to answer them:

helmi.rais@expleogroup.com
yasmeen.trifiss@expleogroup.com
hichem.aggoun@expleogroup.com
tyreksforever@gmail.com
