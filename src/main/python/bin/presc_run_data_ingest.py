import logging
import logging.config

# load the logging configuration file
logging.config.fileConfig(fname='../utils/logging_to_file.conf')
# custom logger
logger = logging.getLogger(__name__)


def load_files(spark, file_dir, ing_file_format, header, inferSchema):
    try:
        logger.info("The load_files() is started ...")
        if ing_file_format == 'parquet':
            df = spark.read.format(ing_file_format).load(file_dir)

        elif ing_file_format == 'csv':
            df = spark.read.format(ing_file_format) \
                .options(header=header) \
                .options(inferSchema=inferSchema) \
                .load(file_dir)
    except Exception as exp:
        logger.error("Error in the method load_files(). " + str(exp))
        raise
    else:
        logger.info(f"The input file {file_dir} is loaded to the data frame")
        logger.info("The load_files() is completed ...")
    return df
