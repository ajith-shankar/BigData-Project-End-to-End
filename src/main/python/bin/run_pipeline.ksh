############################################################
# Developed By:                                            #
# Developed Date:                                          #
# Script NAME:                                             #
# PURPOSE: Master script to run the entire pipeline        #
############################################################

PROJ_FOLDER="/home/hadoop/Projects/BigData-Project-End-to-End/src/main/"
echo PROJ_FOLDER

# Call the copy_files_local_to_hdfs.ksh wrapper to copy files from local to hdfs
printf "\n Calling copy_files_local_to_hdfs.ksh at 'date +"%d/%m/%Y_%H:%M:%S"'....\n"
${PROJ_FOLDER}/python/bin/copy_files_local_to_hdfs.ksh
printf "Executing the copy_files_local_to_hdfs.ksh is completed at 'date +"%d/%m/%Y_%H:%M:%S"'.\n"

# Call the delete HDFS path wrapper
printf "Calling delete_hdfs_output_path.ksh at 'date +"%d/%m/%Y_%H:%M:%S"'....\n"
${PROJ_FOLDER}/python/bin/delete_hdfs_output_path.ksh
printf "Executing delete_hdfs_output_path.ksh is completed at 'date +"%d/%m/%Y_%H:%M:%S"'.\n"

# Call the pipeline.py spark job
printf "Calling run_presc_pipeline.py at 'date +"%d/%m/%Y_%H:%M:%S"'....\n"
spark-submit --master yarn --num-executors 1 --jars ${PROJ_FOLDER}/python/lib/postgresql-42.7.1.jar run_presc_pipeline.py
printf "Executing run_presc_pipeline.py is completed at 'date +"%d/%m/%Y_%H:%M:%S"'.\n"

# Call copy_files_hdfs_to_local.ksh wrapper to copy output files from hdfs to local
printf "Calling copy_files_hdfs_to_local.ksh at 'date +"%d/%m/%Y_%H:%M:%S"'....\n"
${PROJ_FOLDER}/python/bin/copy_files_hdfs_to_local.ksh
printf "Executing copy_files_hdfs_to_local.ksh is completed at 'date +"%d/%m/%Y_%H:%M:%S"'.\n"