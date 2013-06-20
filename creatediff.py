#! /usr/bin/env python
# -*- coding utf-8 -*-
import sys
import datetime
from datetime import datetime as dt
from settings import STATION_CODE as station, GLOBALS_FOLDER as gl_path,\
    DB_PATH as db_path, DB_ARCHIVE_PATH as arch_path,\
    DIFF_ARCHIVE_PATH as diff_path, OUT_PATH as out_path,\
    DB_ARCHIVE_MAX_AGE as arch_age, DIFF_ARCHIVE_MAX_AGE as diff_age,\
    LOG_TYPE, LOG_FILENAME, LOG_FORMAT, LOG_FILESIZE, LOG_FILECOUNT
from msmlib import get_complete_db, dump_db, dump_compressed_db,\
    remove_all_files, remove_old_files, getdiff, compress,\
    debug_message
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

if logger is not None: logger.info("CREATEDIFF BEGIN".center(50, '-'))
info = {}
info["time"] = str(datetime.datetime.now().strftime('%y-%m-%d %H:%M:%S'))
info["station"] = station
data2 = get_complete_db(gl_path, source="file", info=info, logger=logger)

data1 = get_complete_db(db_path, source="json", logger=logger)

diff = getdiff(data2, data1)

t = str(
    dt.strptime(data1["info"]["time"], '%y-%m-%d %H:%M:%S')
    .strftime('%y-%m-%d_%H-%M-%S'))
compress(
    '%s%s_%s.tar.bz2' % (arch_path, station, t),
    [db_path],
    crop_names=True,
    md5=True,
    logger=logger)

dump_db(data2, db_path, logger=logger)

t = str(
    dt.strptime(diff["info"]["time"], '%y-%m-%d %H:%M:%S')
    .strftime('%y-%m-%d_%H-%M-%S'))
dump_compressed_db(
    diff,
    '%s%s_%s.tar.bz2' % (diff_path, station, t),
    'diff.json',
    md5=True,
    logger=logger)
dump_compressed_db(
    diff,
    '%s%s_%s.tar.bz2' % (out_path, station, t),
    'diff.json',
    md5=True,
    logger=logger)

remove_old_files(arch_path, arch_age, logger=logger)
remove_old_files(diff_path, diff_age, logger=logger)

if logger is not None: logger.info("CREATEDIFF END".center(50, '-'))