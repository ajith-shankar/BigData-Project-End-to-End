############################################################
# Developed By:                                            #
# Developed Date:                                          # 
# Script NAME:                                             #
# PURPOSE: Copy input vendor files from local to HDFS.     #
############################################################

# Declare a variable to hold the unix script name.
JOBNAME="copy_files_local_to_hdfs.ksh"

# Declare a variable to hold the current date
date=$(date '+%Y-%m-%d_%H:%M:%S')

# Define a Log File where lpgs would be generated
LOGFILE="/home/hadoop/Projects/US-Prescribers-Report/src/main/python/logs/copy_files_local_to_hdfs_${date}.log"

###########################################################################
### COMMENTS: From this point on, all standard output and standard error will
###           be logged in the log file.
###########################################################################
{  # <--- Start of the log file.
echo "${JOBNAME} Started...: $(date)"

LOCAL_STAGING_PATH="/home/hadoop/Projects/US-Prescribers-Report/src/main/staging"
LOCAL_DIM_DIR=${LOCAL_STAGING_PATH}/Dim
LOCAL_FACT_DIR=${LOCAL_STAGING_PATH}/Fact

HDFS_STAGING_PATH=/user/hadoop/Projects/PrescPipeline/staging
HDFS_DIM_DIR=${HDFS_STAGING_PATH}/Dim
HDFS_FACT_DIR=${HDFS_STAGING_PATH}/Fact

### delete hdfs Dim and Fact
hdfs dfs -rm -r ${HDFS_STAGING_PATH}

### create directory in hdfs
hdfs dfs -mkdir -p ${HDFS_DIM_DIR}
hdfs dfs -mkdir -p ${HDFS_FACT_DIR}

### Copy the City  and Fact file to HDFS
hdfs dfs -put -f ${LOCAL_DIM_DIR}/* ${HDFS_DIM_DIR}/
hdfs dfs -put -f ${LOCAL_FACT_DIR}/* ${HDFS_FACT_DIR}/

echo "${JOBNAME} is Completed...: $(date)"
} > ${LOGFILE} 2>&1  # <--- End of program and end of log.
