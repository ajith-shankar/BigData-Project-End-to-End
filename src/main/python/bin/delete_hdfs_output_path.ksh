############################################################
# Developed By:                                            #
# Developed Date:                                          # 
# Script NAME:                                             #
# PURPOSE: Delete HDFS Output paths so that Spark 
#          extraction will be smooth.                      #
############################################################

# Declare a variable to hold the unix script name.
JOBNAME="delete_hdfs_output_path.ksh"

# Declare a variable to hold the current date
date=$(date '+%Y-%m-%d_%H:%M:%S')

# Define a Log File where logs would be generated
LOGFILE="/home/hadoop/Projects/BigData-Project-End-to-End/src/main/python/logs/${JOBNAME}_${date}.log"

###########################################################################
### COMMENTS: From this point on, all standard output and standard error will
###           be logged in the log file.
###########################################################################

{  # <--- Start of the log file.
echo "${JOBNAME} Started...: $(date)"

DIM_PATH=/user/hadoop/Projects/PrescPipeline/Output/Dim
hdfs dfs -test -d $DIM_PATH
status=$?
if [ $status == 0 ]
  then
  echo "The HDFS output directory $DIM_PATH is available. Proceed to delete."
  hdfs dfs -rm -r -f $DIM_PATH
  echo "The HDFS Output directory $DIM_PATH is deleted before extraction."
fi

FACT_PATH=/user/hadoop/Projects/PrescPipeline/Output/Fact
hdfs dfs -test -d $FACT_PATH
status=$?
if [ $status == 0 ]
  then
  echo "The HDFS output directory $FACT_PATH is available. Proceed to delete."
  hdfs dfs -rm -r -f $FACT_PATH
  echo "The HDFS Output directory $FACT_PATH is deleted before extraction."
fi

HIVE_DIM_PATH=/user/hive/warehouse/prescpipeline.db/df_city_final
hdfs dfs -test -d $HIVE_DIM_PATH
status=$?
if [ $status == 0 ]
  then
  echo "The HDFS output directory $HIVE_DIM_PATH is available. Proceed to delete."
  hdfs dfs -rm -r -f $HIVE_DIM_PATH
  echo "The HDFS Output directory $HIVE_DIM_PATH is deleted before extraction."
fi

HIVE_FACT_PATH=/user/hive/warehouse/prescpipeline.db/df_fact_final
hdfs dfs -test -d $HIVE_FACT_PATH
status=$?
if [ $status == 0 ]
  then
  echo "The HDFS output directory $HIVE_FACT_PATH is available. Proceed to delete."
  hdfs dfs -rm -r -f $HIVE_FACT_PATH
  echo "The HDFS Output directory $HIVE_FACT_PATH is deleted before extraction."
fi

echo "${JOBNAME} is Completed...: $(date)"

} > ${LOGFILE} 2>&1  # <--- End of program and end of log.




