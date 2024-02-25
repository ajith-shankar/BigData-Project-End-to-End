import datetime as date
from pyspark.sql.functions import lit
import logging
import logging.config

# load the logging configuration file
logging.config.fileConfig(fname='../utils/logging_to_file.conf')
# custom logger
logger = logging.getLogger(__name__)


def data_persist_hive(spark, df, dfName, partitionBy, mode):
    try:
        logger.info("Data Persist - data_persist_hive() is started ... ")
        # add a static column with current date
        df = df.withColumn("Created_Date", lit(date.datetime.now().strftime("%Y-%m-%d")))
        #database = 'US_Prescribers_Report'
        spark.sql("""CREATE DATABASE IF NOT EXISTS us_prescribers_report location 
        'hdfs://localhost:9000/user/hive/warehouse/ """)
        spark.sql(""" USE US_Prescribers_Report """)
        df.write.saveAsTable(dfName, partitionBy='Created_Date', mode=mode)
    except Exception as exp:
        logger.error("Error in the method data_persist_hive(). " + str(exp), exc_info=True)
        raise
    else:
        logger.info(f"Data Persist - data_persist_hive() is completed. Saving dataframe {dfName} into Hive table...")


def data_persist_postgres(spark, df, dfName, url, driver, dbtable, mode, user, password):
    try:
        logger.info("Data Persist - data_persist_postgres() is started ... ")
        df.write.format("jdbc") \
                .option("url", url) \
                .option("driver", driver) \
                .option("dbtable", dbtable) \
                .mode(mode) \
                .option("user", user) \
                .option("password", password) \
                .save()
    except Exception as exp:
        logger.error("Error in the method data_persist_postgres(). " + str(exp), exc_info=True)
        raise
    else:
        logger.info(f"Data Persist - data_persist_postgres() is completed. Saving dataframe {dfName} into Postgres table...")






