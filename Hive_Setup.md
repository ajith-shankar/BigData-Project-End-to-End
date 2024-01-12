---

# Hive Setup Instructions

This guide outlines the steps to set up Apache Hive for the BigData Project: End-to-End. Hive is used for data warehousing and SQL-like queries, providing a higher-level abstraction for processing and analyzing large datasets.


## Prerequisites

Before starting the Hive setup process, ensure that you have the following prerequisites installed and configured:

- **Java Development Kit (JDK):** Hive relies on Java, so ensure you have the latest JDK installed on your system. Download and install it from the official Oracle website. or refer to the project's [hadoop_setup.md](./Hadoop_Setup.md) for Java setup instructions.

- **Hadoop:** Hive runs on top of Hadoop, so ensure you have a working Hadoop installation. Refer to the project's [hadoop_setup.md](./Hadoop_Setup.md) for Hadoop setup instructions.


### Steps for Hive Setup
1. **Download Hive**

Visit the official Apache Hive website (https://hive.apache.org/) to download the latest stable release. Choose the appropriate distribution package based on your operating system.

Swith to the user **hadoop**
```bash
sudo su – hadoop
```
```bash
wget https://downloads.apache.org/hive/hive-3.1.2/apache-hive-3.1.2-bin.tar.gz
```


2. **Extract Hive**

Extract the downloaded Hadoop file
```bash
tar xzf hadoop-3.3.6.tar.gz
```


3. **Set the environment variables and path**
```bash
sudo nano ~/.bashrc
```

```bash
# Append the following path to the end of the file.

export HIVE_HOME= /home/hdoop/apache-hive-3.1.2-bin
export PATH=$PATH:$HIVE_HOME/bin
```


4. **Enable the changes**
```bash
source ~/.bashrc
```

5. **Create Directories**

Create related directories in HDFS
```bash
hadoop fs -mkdir /tmp
hadoop fs -chmod g+w /tmp
hadoop fs -mkdir -p /user/hive/warehouse
hadoop fs -chmod g+w /user/hive/warehouse
```

6. **Remove conflicting jars**

Delete the conflicting JAR files from the Hive lib directory and transfer the appropriate JAR files from the HDFS lib to the Hive lib directory.
```bash
# remove guava-* jar from Hive lib
rm $HIVE_HOME/lib/guava-19.0.jar

# copy guava-* jar from HDFS lib to Hive lib
cp $HADOOP_HOME/share/hadoop/hdfs/lib/guava-27.0-jre.jar $HIVE_HOME/lib/
```

7. **Configure Hive Environment**

Edit the Hadoop configuration files to match your system settings. Key configuration files include:

- `hive-site.xml`: Configure hive settings.

`hive-site.xml`
```bash
# open in nano editor
sudo nano $HIVE_HOME/conf/hive-site.xml

# add the below properties
configuration>
    <property>
        <name>javax.jdo.option.ConnectionURL</name>
        <value>jdbc:postgresql://localhost:5432/metastore</value>
        <description>JDBC Driver Connection for PostgrSQL</description>
    </property>
    <property>
        <name>javax.jdo.option.ConnectionDriverName</name>
        <value>org.postgresql.Driver</value>
        <description>PostgreSQL metastore driver class name</description>
    </property>
    <property>
        <name>javax.jdo.option.ConnectionUserName</name>
        <value>hive</value>
        <description>Database User Name</description>
    </property>
    <property>
        <name>javax.jdo.option.ConnectionPassword</name>
        <value>hive@123</value>
        <description>Database User Password</description>
    </property>
    <property>
        <name>hive.metastore.schema.verification</name>
        <value>false</value>
    </property>
    <property>
        <name>hive.metastore.warehouse.dir</name>
        <value>/user/hive/warehouse </value>
        <description>location of the warehouse directory</description>
    </property>
</configuration>

```


8. **Configure Hive Metastore**

Hive uses a metastore to store metadata about tables. You can use an embedded Derby database for testing or set up a more robust external database like MySQL or PostgreSQL for production. We will be using PostgreSQL.
```bash
# download the PostgreSQL jar into hive lib folder
cd $HIVE_HOME/lib/
```
```bash
# download jar 
wget https://jdbc.postgresql.org/download/postgresql-42.7.1.jar
```

9. **Start Hive metastore**
```bash
schematool -dbType postgres -initSchema
```

10. **Start Hive CLI**
```bash
hive
```





