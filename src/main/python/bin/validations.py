

def get_curr_date(spark):
    opDF = spark.sql(""" select current_date """) # output will be in dataFrame
    print("Validate the spark object by printing current date : " + str(opDF.collect())) # convert the dataFrame into list using collect()