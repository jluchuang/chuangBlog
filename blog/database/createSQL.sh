#!/bin/sh

SCRIPT_DIR=`cd $(dirname $0); pwd -P`

DEV_SQL=$SCRIPT_DIR/dev.sql

if [ -f ${DEV_SQL} ];then
     echo file ${DEV_SQL} already exists!
else
     echo 'USE blog;'>${DEV_SQL}
     echo 'SET NAMES '\''utf8'\'';'>>${DEV_SQL}
     echo 'SET time_zone = "+08:00";'>>${DEV_SQL}
     echo ''>>${DEV_SQL}
fi
