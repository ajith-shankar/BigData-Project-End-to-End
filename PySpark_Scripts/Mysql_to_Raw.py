# Move data from RDBMS (MySql) to Raw zone 

from pyspark.sql import SparkSession

# SparkSession is already created by the Pyspark shell 
spark = SparkSession.builder.appName("Testing Spark") \
    .master("yarn") \
    .getOrCreate()

# edit the variables
conn_url = "jdbc:mysql://localhost/3306/cars"
conn_driver = "com.mysql.cj.jdbc.driver"
db_table = "employees"
db_username = "root"
db_password = "test"

df = spark.read.format("jdbc") \
    .option("url", conn_url) \
    .option("driver", conn_driver) \
    .option("dbtable", db_table) \
    .option("user", db_username) \
    .option("password" , db_password) \
    .load()

df.printSchema()



