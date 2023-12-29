# import all the necessary modules
import get_all_variables as gav
from create_objects import get_spark_object
from validations import get_curr_date
import sys
import logging
import logging.config
from os import path
import os
from run_presc_data_ingest import load_files

# load the logging configuration file

# path = os.path.join(os.path.expanduser('~'), 'Documents' ,'BigData-Project-End-to-End', 'src', 'main', 'util', 'logging_to_file.conf')
# path_rslv = path.split(path.dirname(path.abspath(__file__)))[0:]
# file_name = path.join(*[".." for dotdot in range(len(path_rslv))], "logging_to_file.conf")
logging.config.fileConfig(fname='../utils/logging_to_file.conf')
# custom logger is not required bcz it is root

def main():
    try:
        logging.info("main() is started...")  # instead of print() use logging.info() or logging.warn()
        ### get Spark objects
        spark = get_spark_object(gav.envn, gav.appName)

        # validate spark object
        get_curr_date(spark)

        ### initiate run_presc_data_ingest script
        # load the City File
        for file in os.listdir(gav.staging_dim_path):
            print("File is " + file)
            file_dir = gav.staging_dim_path + '/' + file
            print(file_dir)

            if file.split('.')[1] == 'csv':
                file_format = 'csv'
                header = gav.header
                inferSchema = gav.inferSchema

            elif file.split('.')[1] == 'parquet':
                file_format = 'parquet'
                header = 'NA'
                inferSchema = 'NA'

        df_city = load_files(spark = spark, file_dir = file_dir, file_format =file_format, header = header, inferSchema = inferSchema)

        # load the Prescriber Fact file
        # validate
        # Setup logging config mechanism
        # setup Error handling mechanism

        # initiate run_presc_data_preprocessing script
        # perform data cleaning operations
        # validate
        # Setup logging config mechanism
        # setup Error handling mechanism

        # initiate run_presc_data_transform script
        # apply all the transformation logics
        # validate
        # Setup logging config mechanism
        # setup Error handling mechanism
        logging.info("run_presc_pipeline.py is completed")

    except Exception as exp:
        logging.error("Error occurred in the main() method. " + str(exp), exc_info=True)
        sys.exit(1)


if __name__ == "__main__":
    logging.info("run_presc_pipeline.py is started...")
    main()
