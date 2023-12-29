from pyspark.sql import SparkSession
import logging
import logging.config


# load the logging configuration file
logging.config.fileConfig(fname='../utils/logging_to_file.conf')
# custom logger
logger = logging.getLogger(__name__)


def get_spark_object(envn, appName):
    try:
        logger.info(f"get_spark_object() is started. The '{envn}' env is used.")
        if envn == 'Test':
            master = 'local'
        else:
            master = 'yarn'
        spark = SparkSession.builder.master(master).appName(appName).getOrCreate()

    except NameError as exp:
        logger.error("NameError in the method get_spark_object(). " + str(exp), exc_info=True)
    except Exception as exp:
        logger.error("Error in the method get_spark_object() " + str(exp), exc_info=True)
    else:
        logger.info("Spark Object is created")
    return spark

