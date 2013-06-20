#!/usr/bin/env python
# -*- coding: utf-8 -*-
STATION_CODE = '145000'
MSM_GLOBALS=['B1', 'B4', 'B9', 'B11', 'B12', 'B13', 'B14', 'B15', 'B18', 'B19',
'B27', 'B28', 'B33', 'B34', 'B35', 'B36', 'B37', 'B38', 'B39', 'B40', 'B41', 'B42',
'B43', 'B44', 'B45', 'B46', 'B47', 'B48', 'B49', 'B50', 'B51', 'B52', 'B53', 'B54']

GLOBALS_FOLDER='/home/admmsm/db/globals/'
LIB_PATH='/ZDOS/C/lib/'
DB_PATH='/home/admmsm/db/current/db.json'
DB_ARCHIVE_PATH='/home/admmsm/db/old/'
DIFF_ARCHIVE_PATH='/home/admmsm/db/diffs/'
OUT_PATH='/home/admmsm/db/out/'
DB_ARCHIVE_MAX_AGE=5
DIFF_ARCHIVE_MAX_AGE=10

ROOT_IP='192.168.20.251'
ROOT_USERNAME='alex'
ROOT_PASSWORD='pa55w0rd'
ROOT_PATH='/home/alex/tmp/'

LOG_TYPE='FILE' # or 'SCREEN' or 'BOTH' or 'NONE'
LOG_FILENAME='node-msm.log'
LOG_FORMAT=u'[%(asctime)s] %(levelname)-8s  %(message)-65s #%(filename)s[LINE:%(lineno)d]'
LOG_FILESIZE=1024000
LOG_FILECOUNT=5

if __name__ == '__main__':
	pass