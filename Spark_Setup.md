---

# Apache Spark Setup Instructions

This guide outlines the steps to set up Apache Spark for the BigData Project: End-to-End. Apache Spark is a distributed data processing framework that provides fast in-memory data processing capabilities.

## Prerequisites

Before starting the Spark setup process, ensure that you have the following prerequisites installed and configured:

- **Java Development Kit (JDK):** Spark runs on Java, so ensure you have the latest JDK installed on your system. Download and install it from the official Oracle website, or refer to the project's [hadoop_setup.md](./Hadoop_Setup.md) for Java setup instructions.

- **Hadoop:** Although Spark doesn't require Hadoop to run, it is often used in conjunction with Hadoop Distributed File System (HDFS). Refer to the project's [hadoop_setup.md](./Hadoop_Setup.md) for Hadoop setup instructions.


### Steps for Spark Setup
1. **Download Spark**

Visit the official Apache Spark website (https://spark.apache.org/) to download the latest stable release. Choose the appropriate distribution package based on your operating system.

Swith to the user **hadoop**
```bash
sudo su – hadoop
```

```bash
wget https://downloads.apache.org/spark/spark-3.3.4/spark-3.3.4-bin-hadoop3.tgz
```


2. **Extract Spark**

Extract the downloaded Spark file
```bash
tar xzf spark-3.3.4-bin-hadoop3.tgz
```


3. **Set the environment variables and path**
```bash
sudo nano ~/.bashrc
```

```bash
# Append the following path to the end of the file
export PYSPARK_PYTHON=python3
export HADOOP_CONF_DIR=/usr/local/hadoop/etc/hadoop
export PATH=$PATH:/home/hadoop/spark-3.3.4-bin-hadoop3/bin
export SPARK_HOME=/home/hadoop/spark-3.3.4-bin-hadoop3
```


4. **Enable the changes**
```bash
source ~/.bashrc
```

5. **Create Directories**

Create related directories in HDFS
```bash
# to store spark logs
hdfs dfs -mkdir /spark-logs

# to store spark jars 
hdfs dfs -mkdir /spark-jars

# copy all the jars from local to hdfs spark folder
hdfs dfs -put /home/hadoop/spark-3.3.4-bin-hadoop3/jars/* /spark-jars
```

6. **Configure Spark Environment**

Edit the Spark configuration files to match your system settings. Key configuration files include:

- `spark-env.sh`: Configure spark environment variables.
- `spark-defaults.conf`: Configure spark defualt properties.

`spark-env.sh`
```bash
# open in nano editor
sudo nano $SPARK_HOME/conf/spark-env.sh

# add the below paths
export HADOOP_HOME="/usr/local/hadoop"
export HADOOP_CONF_DIR="/usr/local/hadoop/etc/hadoop"
```

`spark-defaults.conf`
```bash
# open in nano editor
sudo nano $SPARK_HOME/conf/spark-defaults.conf

spark.driver.extraJavaOptions     -Dderby.system.home=/tmp/derby/
spark.sql.repl.eagerEval.enabled  true
spark.master                      yarn
spark.eventLog.enabled            true
spark.eventLog.dir                hdfs:///spark-logs
spark.history.provider            org.apache.spark.deploy.history.FsHistoryProvider
spark.history.fs.logDirectory     hdfs:///spark-logs
spark.history.fs.update.interval  10s
spark.history.ui.port             18080
spark.yarn.historyServer.address  localhost:18080
spark.yarn.jars                   hdfs:///spark-jars/*.jar
```

7. **Interlink Spark with Hive**





