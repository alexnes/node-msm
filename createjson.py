#! /usr/bin/env python
# -*- coding utf-8 -*-
import sys
import datetime
from msmlib import get_complete_db, dump_compressed_db
from settings import STATION_CODE as station,\
    LOG_TYPE, LOG_FILENAME, LOG_FORMAT, LOG_FILESIZE, LOG_FILECOUNT
import logging
import logging.handlers

if LOG_TYPE.upper() == 'NONE':
    logger = None
else:
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    form = logging.Formatter(LOG_FORMAT)
    filehandler = logging.handlers.RotatingFileHandler(
	LOG_FILENAME, 
	maxBytes=LOG_FILESIZE, 
	backupCount=LOG_FILECOUNT)
    filehandler.setFormatter(form)
    strhandler = logging.StreamHandler(sys.stdout)
    strhandler.setFormatter(form)
    if LOG_TYPE.upper() == 'FILE':
        logger.addHandler(filehandler)
    elif LOG_TYPE.upper() == 'SCREEN':
        logger.addHandler(strhandler)    
    else:
        logger.addHandler(filehandler)
        logger.addHandler(strhandler) 

if len(sys.argv) != 3:
    print "Usage:\n\t%s globals_folder out_path/\nout_path does not have a filename" % sys.argv[0]
    sys.exit()
info = {}
info["time"] = str(datetime.datetime.now().strftime('%y-%m-%d %H:%M:%S'))
info["prev_time"] = ""
info["station"] = station
data = get_complete_db(sys.argv[1], source="file", info = info, logger=logger)
dump_compressed_db(
    data,
    sys.argv[2] + station + '_init.tar.bz2',
    'db.json',
    md5=True,
    logger=logger)