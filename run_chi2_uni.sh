#! /bin/bash

echo "*******`date` start: $0 $* *******"

JOB_NAME=kn45_chi_square
INPUT_PATH_T=/user/kn45/chi2_segs_uni
OUTPUT_PATH=/user/kn45/chi2_uni

hadoop fs -rmr $OUTPUT_PATH

hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-2.4.0.jar \
-input $INPUT_PATH_T -output $OUTPUT_PATH \
-mapper "mapred_chi2.py m" -reducer "mapred_chi2.py r all_cat_segs_cnt" \
-jobconf mapred.map.tasks=400 -jobconf mapred.reduce.tasks=300 -jobconf mapred.job.name=$JOB_NAME \
-file mapred_chi2.py all_cat_segs_cnt

TABLE_NAME=kn45_chi2_uni
hive -e "
create external table if not exists $TABLE_NAME
(
  cat_id string,
  word string,
  chi2 double,
  a double,
  b double,
  c double,
  d double,
  pos int
)
row format delimited fields terminated by '\t'
location '$OUTPUT_PATH';
alter table $TABLE_NAME set location 'hdfs://xxx$OUTPUT_PATH';
"

echo "*******`date` done: $0 $* *******"
