# import all the necessary modules
import get_all_variables as gav
from create_objects import get_spark_object
from validations import get_curr_date
import sys
import logging
import logging.config
from os import path

# load the logging configuration file
# path = os.path.join(os.path.expanduser('~'), 'Documents' ,'BigData-Project-End-to-End', 'src', 'main', 'util', 'logging_to_file.conf')
log_file_path = path.join(path.dirname(path.abspath(__file__)), 'logging_to_file.conf')
logging.config.fileConfig(log_file_path)


def main():
    try:
        logging.info("main() is started...") # instead of print() use logging.info() or logging.earn()
        # get Spark objects
        spark = get_spark_object(gav.envn, gav.appName)
        #print("Spark object is created...")

        # validate spark object
        get_curr_date(spark)

        # setup logging mechanism
        # setup error handling mechanism

        # initiate run_presc_data_ingest script
        # load the City File
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
        logging.info("Error occurred in the main() method. " + str(exp))
        sys.exit(1)


if __name__ == "__main__":
    logging.info("run_presc_pipeline.py is started...")
    main()
