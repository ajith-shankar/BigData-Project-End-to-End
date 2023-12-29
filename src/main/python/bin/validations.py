import logging
import logging.config


# load the logging configuration file
logging.config.fileConfig(fname='../utils/logging_to_file.conf')
# custom logger
logger = logging.getLogger(__name__)


def get_curr_date(spark):
    try:
        opDF = spark.sql(""" select current_date """)  # output will be in dataFrame
        logger.info("Validate the spark object by printing current date : " + str(opDF.collect()))  # convert the dataFrame into list using collect()

    except NameError as exp:
        logger.error("NameError in the method get_curr_date(). " + str(exp), exc_info=True)
        raise
    except Exception as exp:
        logger.error("Error in the method spark_curr_date(). " + str(exp), exc_info=True)
    else:
        logger.info("Spark object is validated and it is ready")

