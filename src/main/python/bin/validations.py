import logging
import logging.config
import pandas

# load the logging configuration file
logging.config.fileConfig(fname='../utils/logging_to_file.conf')
# custom logger
logger = logging.getLogger(__name__)


def get_curr_date(spark):
    try:
        opDF = spark.sql(""" select current_date """)  # output will be in dataFrame
        logger.info("Validate the spark object by printing current date : " + str(
            opDF.collect()))  # convert the dataFrame into list using collect()

    except NameError as exp:
        logger.error("NameError in the method get_curr_date(). " + str(exp), exc_info=True)
        raise
    except Exception as exp:
        logger.error("Error in the method spark_curr_date(). " + str(exp), exc_info=True)
    else:
        logger.info("Spark object is validated and it is ready")


def df_count(df, dfName):
    try:
        logger.info(f"The DataFrame validation by count df_count() is started for the dataframe {dfName} ...")
        dfcount = df.count()
        logger.info(f"The dataframe count is {dfcount}.")
    except Exception as exp:
        logger.error("Error in the method df_count(). " + str(exp))
        raise
    else:
        logger.info(f"The DataFrame validation by count df_count() is completed.")


def df_top10_rec(df, dfName):
    try:
        logger.info(f"The DataFrame validation by top 10 record df_top10_rec() is started for DataFrame {dfName} ..")
        logger.info(f"The DataFrame top 10 records are: ...")
        df_pandas = df.limit(10).toPandas()
        logger.info('\n \t' + df_pandas.to_string(index=False))
    except Exception as exp:
        logger.error("Error in the method df_top10_rec. " + str(exp))
        raise
    else:
        logger.info("The DataFrame validation by to 10 record df_top10_rec() is completed.")


def df_print_schema(df, dfName):
    try:
        logger.info(f"The DataFrame Schema validation for dataframe {dfName} ...")
        sch = df.schema.fields
        logger.info(f"The Dataframe {dfName} schema is: ")
        for i in sch:
            logger.info(f"\t{i}")
    except Exception as exp:
        logger.error("Error in the method df_print_schema(). " + str(exp))
        raise
    else:
        logger.info("The DataFrame schema validation is completed.")
