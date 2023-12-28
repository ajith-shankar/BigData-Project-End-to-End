# import all the necessary modules
import get_all_variables as gav
from create_objects import get_spark_object


def main():
    # get all the variables
    spark = get_spark_object(gav.envn, gav.appName)
    print("Spark object is created...")

    # get Spark objects
    # validate spark object
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


if __name__ == "__main__":
    main()
