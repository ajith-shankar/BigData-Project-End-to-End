def get_curr_date(spark):
    try:
        opDF = spark.sql(""" select current_date """)  # output will be in dataFrame
        print("Validate the spark object by printing current date : " + str(opDF.collect()))  # convert the dataFrame into list using collect()

    except NameError as exp:
        print("NameError in the method spark_curr_date(). " + str(exp))
        raise
    except Exception as exp:
        print("Error in the method spark_curr_date(). " + str(exp))

