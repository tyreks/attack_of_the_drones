#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import os
import datetime
import gzip
import shutil
from ftplib import FTP_TLS
import sys

from ..config import *


class GnssDataRetriever(object) :
    
    # remote NASA host
    host : str

    # mail used as a password for sftp transfert
    mail : str

    # gps ressourses files directory
    gps_res_dir : str

    #constructor
    def __init__(self, host=HOST, mail=MAIL, gps_res_dir=GPS_RES_DIR) -> None:
        """
        """
        self.host = host 
        self.mail = mail 
        self.gps_res = gps_res_dir


    def retrieve_gnss_file(self):
        """
        retrieve the most recent GNSS daily file from the NASA site
        """
 
        # remote NASA host

        # date retrieving
        #TODAY = datetime.datetime.today()
        TODAY = datetime.datetime.utcnow().date()

        YEAR = TODAY.strftime("%Y")
        DAY_OF_YEAR = TODAY.strftime("%j")
        YEAR_2_LAST_DIGITS = TODAY.strftime("%y")

        # temporary and final result files names
        TMP_GPS_FILE="brdc"+DAY_OF_YEAR+"0."+YEAR_2_LAST_DIGITS+"n.gz"    
        FINAL_GPS_FILE=self.gps_res+"gps_data.n"
     
        # ftp remote directory
        DIRECTORY = "gnss/data/daily/"+YEAR+"/"+DAY_OF_YEAR+"/"+YEAR_2_LAST_DIGITS+"n/"

        # latest gps data file retrieving from NASA site
        ftps = FTP_TLS(host = self.host)
        ftps.login(user="anonymous", passwd=self.mail)
        ftps.prot_p()
        ftps.cwd(DIRECTORY)
        ftps.retrbinary("RETR " + TMP_GPS_FILE, open(self.gps_res+TMP_GPS_FILE, "wb").write)

        # temporary file extracting and renaming to final file
        with gzip.open(self.gps_res+TMP_GPS_FILE, "rb") as f_in:
            with open(FINAL_GPS_FILE, "wb") as f_out:
                shutil.copyfileobj(f_in, f_out)

        # remove the temporary file
        if os.path.exists(self.gps_res+TMP_GPS_FILE):
            os.remove(self.gps_res+TMP_GPS_FILE)

        return 0


def main():
    try:
        retriever = GnssDataRetriever()
        retriever.retrieve_gnss_file()
    except Exception as exc:
        print (format(exc))
        sys.exit(1)
    return 0

if __name__ == "__main__":
    main()