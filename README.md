# Dependancies

# pip (required for further pip modules installations)
sudo apt install pip

# pandas : *.csv file handling
pip install pandas || echo “er

# pwntools : progress bar formatting
pip install pwntools

# pyfiglet : title in ASCII art
pip install pyfiglet

# click : menu with choices
pip install click

# gr-osmosdr : hackr one and other sdr hardware handling in python
sudo apt install gr-osmosdr -y


# gnuradio : radio module required by gr-osmosdr
sudo apt install gnuradio -y

# aircrack-ng : wifi cracking module
sudo apt install aircrack-ng -y

# hackrf : hackrf one sdr hardware library
sudo apt install hackrf -y

# ar-drone : nodejs module for parrot ar 2.0 controlling
npm install ar-drone

# nodejs : required for executing ar-drone nodejs module
sudo apt install nodejs npm -y

# ffmpeg : require by ar-drone module for accessing drone video stream
sudo apt install ffmpeg -y

# gps-sdr-sim : required for gps spoofing
git clone https://github.com/osqzss/gps-sdr-sim.git && \
cd ./gps-sdr-sim && \
gcc gpssim.c -lm -O3 -o gps-sdr-sim

