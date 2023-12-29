from pyspark.sql import SparkSession


def get_spark_object(envn, appName):
    try:
        if envn == 'TEST':
            master = 'local'
        else:
            master = 'yarn'
        spark = SparkSession.builder.master(master).appName(appName).getOrCreate()

    except NameError as exp:
        print("NameError in the method get_spark_object(). " + str(exp))
    except Exception as exp:
        print("Error in the method get_spark_object() " + str(exp))
    else:
        print("Spark Object is created")
    return spark

