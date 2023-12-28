print("Start ...")
  
from pyspark.sql import SparkSession
spark = SparkSession \
       .builder \
       .master('yarn') \
       .appName("Python Spark SQL basic example") \
       .getOrCreate()

spark.sparkContext.setLogLevel('OFF')
print("Spark Object is created")
print("Spark Version used is :" + spark.sparkContext.version)

print("... End")
