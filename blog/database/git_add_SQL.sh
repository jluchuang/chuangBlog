#!/bin/bash
set -e
#echo $0
#echo $(dirname $0)
SCRIPT_DIR=`cd $(dirname $0); pwd -P`
cd $SCRIPT_DIR
DEV_SQL=dev.sql
git pull 
ADD_SQL=$(ls | grep -oP '[0-9]+(?=\.sql)' | sort -n | tail -n 1 | awk '{printf("%03d.sql", $0+1)}')
set -x
mv ${DEV_SQL} ${ADD_SQL}
git add ${ADD_SQL}
cd -
