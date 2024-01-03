# import all the necessary modules
import get_all_variables as gav
from create_objects import get_spark_object
from presc_run_data_preprocessor import perform_data_clean
from validations import get_curr_date, df_count, df_top10_rec, df_print_schema
from presc_run_data_ingest import load_files
from presc_run_data_transform import city_report, top5_presc_report
import sys
import logging
import logging.config
from os import path
import os

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

        ### initiate presc_run_data_ingest script

        # load the City Dim File
        for file in os.listdir(gav.staging_dim_path):
            print("File is " + file)
            file_dir = 'file://' + gav.staging_dim_path + '/' + file
            print(file_dir)

            if file.split('.')[1] == 'csv':
                file_format = 'csv'
                header = gav.header
                inferSchema = gav.inferSchema

            elif file.split('.')[1] == 'parquet':
                file_format = 'parquet'
                header = 'NA'
                inferSchema = 'NA'

        df_city = load_files(spark=spark, file_dir=file_dir, file_format=file_format, header=header,
                             inferSchema=inferSchema)

        # validate presc_run_data_ingest script for City_Dim dataframe
        df_count(df_city, 'df_city')
        df_top10_rec(df_city, 'df_city')

        # load the Presc Fact File
        for file in os.listdir(gav.staging_fact_path):
            print("File is " + file)
            file_dir = 'file://' + gav.staging_fact_path + '/' + file
            print(file_dir)

            if file.split('.')[1] == 'csv':
                file_format = 'csv'
                header = gav.header
                inferSchema = gav.inferSchema

            elif file.split('.')[1] == 'parquet':
                file_format = 'parquet'
                header = 'NA'
                inferSchema = 'NA'

        df_fact = load_files(spark=spark, file_dir=file_dir, file_format=file_format, header=header,
                             inferSchema=inferSchema)

        # validate presc_run_data_ingest script for Presc_Fact dataframe
        df_count(df_fact, 'df_fact')
        df_top10_rec(df_fact, 'df_fact')

        ### initiate presc_run_data_preprocessing script
        # perform dats cleaning for city_dim
        df_city_sel, df_fact_sel = perform_data_clean(df_city, df_fact)

        # validate presc_run_data_preprocessor script for City_Dim dataframe and Fact Dataframe
        df_top10_rec(df_city_sel, 'df_city_sel')
        df_top10_rec(df_fact_sel, 'df_fact_sel')
        df_print_schema(df_fact_sel, 'df_fact_sel')


        # initiate run_presc_data_transform script
        df_city_final = city_report(df_city_sel, df_fact_sel)
        df_fact_final = top5_presc_report(df_fact_sel)

        # validate
        df_top10_rec(df_city_final, 'df_city_final')
        df_print_schema(df_city_final, 'df_city_final')

        df_top10_rec(df_fact_final, 'df_fact_final')
        df_print_schema(df_fact_final, 'df_fact_final')

        logging.info("run_presc_pipeline.py is completed")

    except Exception as exp:
        logging.error("Error occurred in the main() method. " + str(exp), exc_info=True)
        sys.exit(1)


if __name__ == "__main__":
    logging.info("run_presc_pipeline.py is started...")
    main()
