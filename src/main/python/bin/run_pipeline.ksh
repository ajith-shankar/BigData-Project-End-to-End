############################################################
# Developed By:                                            #
# Developed Date:                                          #
# Script NAME:                                             #
# PURPOSE: Master script to run the entire pipeline        #
############################################################

PROJ_FOLDER="/home/${USER}/Projects/BigData-Project-End-to-End/src/main/"
echo $PROJ_FOLDER

# Call the copy_files_local_to_hdfs.ksh wrapper to copy files from local to hdfs
printf "\nCalling copy_files_local_to_hdfs.ksh at `date +"%x_%T"` ....\n"
${PROJ_FOLDER}/python/bin/copy_files_local_to_hdfs.ksh
printf "Executing the copy_files_local_to_hdfs.ksh is completed at `date +"%x_%T"`.\n"

# Call the delete HDFS Output path wrapper
printf "\nCalling delete_hdfs_output_path.ksh at `date +"%x_%T"` ....\n"
${PROJ_FOLDER}/python/bin/delete_hdfs_output_path.ksh
printf "Executing delete_hdfs_output_path.ksh is completed at `date +"%x_%T"`.\n"

# Call the pipeline.py spark job
printf "\nCalling run_presc_pipeline.py at `date +"%x_%T"` ....\n"
spark-submit --master yarn --num-executors 1 --jars ${PROJ_FOLDER}/python/lib/postgresql-42.7.1.jar run_presc_pipeline.py
printf "Executing run_presc_pipeline.py is completed at `date +"%x_%T"`.\n"

# Call copy_files_hdfs_to_local.ksh wrapper to copy output files from hdfs to local
printf "\nCalling copy_files_hdfs_to_local.ksh at `date +"%x_%T"` ....\n"
${PROJ_FOLDER}/python/bin/copy_files_hdfs_to_local.ksh
printf "Executing copy_files_hdfs_to_local.ksh is completed at `date +"%x_%T"`.\n"

# call copy_files_local_to_azure.ksh to copy output files from local to copy_files_local_to_azure
printf "\nCalling copy_files_local_to_azure.ksh at `date +"%x_%T"` ....\n"
$PROJ_FOLDER}/python/bin/copy_files_local_to_azure.ksh
printf "Executing copy_files_local_to_azure.ksh is completed at `date +"%x_%T"`.\n"
