import logging
import logging.config

# load the logging configuration file
logging.config.fileConfig(fname="../utils/logging_to_file.conf")
# custom logger
logger = logging.getLogger(__name__)


def extract_files(df, fileFormat, filePath, split_no, headerReq, compressionType):
    try:
        logger.info("The Extraction - extract_files() is started ...")
        df.coalesce(split_no).write.format(fileFormat).save(
            filePath, header=headerReq, compression=compressionType
        )
    except Exception as exp:
        logger.error("Error in the method extract_files(). " + str(exp), exc_info=True)
        raise
    else:
        logger.info("The Extraction - extract_files() is completed")
