#! /usr/bin/env python
# -*- coding utf-8 -*-
import os
import datetime
from datetime import datetime as dt
from settings import OUT_PATH as out_path,\
    ROOT_IP as ip, ROOT_USERNAME as user, ROOT_PASSWORD as password,\
    ROOT_PATH as path,\
    LOG_TYPE, LOG_FILENAME, LOG_FORMAT, LOG_FILESIZE, LOG_FILECOUNT
from msmlib import debug_message, send_file, remove_file
import logging
import logging.handlers

if LOG_TYPE.upper() == 'NONE':
    logger = None
else:
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    form = logging.Formatter(LOG_FORMAT)
    filehandler = logging.handlers.RotatingFileHandler(LOG_FILENAME, LOG_FILESIZE, LOG_FILECOUNT)
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

if logger is not None: logger.info("SEND BEGIN".center(50, '-'))
for f in sorted(os.listdir(out_path)):
    send_ok = send_file(out_path + f, path, ip, user, password, logger=logger)
    if send_ok:
	remove_file(out_path + f, logger=logger)
    else:
	break
if logger is not None: logger.info("SEND END".center(50, '-'))
