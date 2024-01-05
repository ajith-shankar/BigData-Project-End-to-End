# Call the copy_files_local_to_hdfs.ksh wrapper
# printf "Calling copy_files_local_to_hdfs.ksh ...."
# /home/hadoop/Projects/BigData-Project-End-to-End/src/main/python/bin/copy_files_local_to_hdfs.ksh
# printf "Executing copy_files_local_to_hdfs.ksh is completed.\n" 

# Call the delete HDFS path wrapper
printf "Calling delete_hdfs_output_path.ksh ...."
/home/hadoop/Projects/BigData-Project-End-to-End/src/main/python/bin/delete_hdfs_output_path.ksh
printf "Executing delete_hdfs_output_path.ksh is completed. \n"

# Call the pipeline.py spark job
printf "Calling run_presc_pipeline.py ...."
spark-submit --master yarn --num-executors 1 run_presc_pipeline.py
printf "Executing run_presc_pipeline.py is completed" 
