#!/bin/bash
# command format is sh for_loop_date.sh 02/17/2017 02/20/2017
echo 'start date = ' $1
echo 'end date = ' $2

start=`date -j -f %m/%d/%Y:%H.%M $1:0.0 +%s`
enddate=`date -j -f %m/%d/%Y:%H.%M $2:0.0 +%s`

echo

for((i=$start; i<=$((enddate-86400)); i+=86400)) ; do
	begin=`date -j -f %s "$i" +%m/%d/%Y`
	End=`date -j -f %s "$((i+86400))" +%m/%d/%Y`

	echo 'from start_date: ' $begin ' to end_date: ' $End
done;

