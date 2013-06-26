#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Получает из msm все глобали из MSM_GLOBALS в формате JSON
# и сохраняет их в каталог GLOBALS_FOLDER
from __future__ import with_statement
from commands import getoutput
from msmlib import remove_all_files
from settings import MSM_GLOBALS, GLOBALS_FOLDER, LIB_PATH,\
	LOG_TYPE, LOG_FILENAME, LOG_FORMAT, LOG_FILESIZE, LOG_FILECOUNT
import sys
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
if logger is not None: logger.info("GETGOBALS BEGIN".center(50, '-'))
remove_all_files(GLOBALS_FOLDER, logger=logger)
for g in MSM_GLOBALS:
	if logger is not None: logger.info("GETGL: Retrieving global: %s" % (g))
	try:
		result = getoutput('%sMSMCmd.pl "d ^GETGL(\\"%s\\")"' % (LIB_PATH, g))
		with open(GLOBALS_FOLDER + g, "w") as text_file:
			text_file.write(result)
	except Exception, e:
		if logger is not None: logger.error("EXCEPTION: %s" % e)
		if logger is not None: logger.info("GETGLOBALS END".center(50, '-'))
		sys.exit(1)
	if logger is not None: logger.info("Global %s saved to file: %s" % (g, GLOBALS_FOLDER + g))
if logger is not None: logger.info("GETGOBALS END".center(50, '-'))