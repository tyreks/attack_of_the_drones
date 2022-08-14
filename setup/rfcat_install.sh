#!/bin/bash

cd /opt

sudo mkdir rfcat

cd rfcat

sudo apt install -y python3-pip python3-usb libusb-1.0-0 python3-future python3-numpy python3-serial ipython3

umask 022

sudo pip3 install PySide2 pyreadline

sudo curl -l -C- http://ftp.de.debian.org/debian/pool/main/s/sdcc/sdcc-libraries_3.5.0+dfsg-2_all.deb -o sdcc-libraries_3.5.0+dfsg-2_all.deb

sudo curl -l -C- http://ftp.de.debian.org/debian/pool/main/s/sdcc/sdcc_3.5.0+dfsg-2+b1_amd64.deb -o sdcc_3.5.0+dfsg-2+b1_amd64.deb

sudo dpkg -i sdcc-libraries_3.5.0+dfsg-2_all.deb

sudo dpkg -i sdcc_3.5.0+dfsg-2+b1_amd64.deb

sudo git clone https://github.com/atlas0fd00m/rfcat.git

cd rfcat/

sudo rm -r .git*

sudo python3 setup.py install

sudo cp ./etc/udev/rules.d/20-rfcat.rules /etc/udev/rules.d
