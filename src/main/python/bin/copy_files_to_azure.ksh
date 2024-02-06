############################################################
# Developed By:                                            #
# Developed Date:                                          #
# Script NAME:                                             #
# PURPOSE: Delete HDFS Output paths so that Spark
#          extraction will be smooth.                      #
############################################################

# Declare a variable to hold the unix script name.
JOBNAME="copy_files_to_azure.ksh"

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