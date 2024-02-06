############################################################
# Developed By:                                            #
# Developed Date:                                          #
# Script NAME:                                             #
# PURPOSE: Delete HDFS Output paths so that Spark
#          extraction will be smooth.                      #
############################################################

# Declare a variable to hold the unix script name.
JOBNAME="copy_files_local_to_azure.ksh"

# Declare a variable to hold the current date
date=$(date '+%Y-%m-%d_%H:%M:%S')

# Blob subdirectory name
subdir_name=$(date '+%Y-%m-%d-%H-%M-%S')

# Define a Log File where logs would be generated
LOGFILE="/home/hadoop/Projects/BigData-Project-End-to-End/src/main/python/logs/${JOBNAME}_${date}.log"

###########################################################################
### COMMENTS: From this point on, all standard output and standard error will
###           be logged in the log file.
###########################################################################

{  # <--- Start of the log file.
echo "${JOBNAME} Started...: $(date)"

### Local OutPut path
LOCAL_OUTPUT_PATH="/home/hadoop/Projects/BigData-Project-End-to-End/src/main/output"
LOCAL_DIM_DIR=${LOCAL_OUTPUT_PATH}/dim
LOCAL_FACT_DIR=${LOCAL_OUTPUT_PATH}/fact

### SAS url
dimURL="path/container/${subdir_name}?url"
factURL="path/container/${subdir_name}?url"

### push output files from local to azure container
azcopy copy "${LOCAL_DIM_DIR}/*" "$dimURL"
azcopy copy "${LOCAL_FACT_DIR}/*" "$factURL"

echo "${JOBNAME} is Completed...: $(date)"
} > ${LOGFILE} 2>&1  # <--- End of program and end of log.