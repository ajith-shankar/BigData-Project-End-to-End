# BigData-Project-End-to-End
This repo contains Big Data batch processing project 


# Practice 

A brief description of what this project does and who it's for


## Documentation

[Documentation](https://linktodocumentation)

Step 1) Install pip
sudo apt install python3-pip

Step2) Install Java
sudo apt-get install openjdk-8-jdk

to verify java –version

Step3) Set Up Local SSH
sudo apt install openssh-server openssh-client

Step4) Create a Non-Root user for hadoop
sudo addser hadoop

username=hadoop
password=hadoop

enable superuser privileges
sudo usermod -aG sudo hadoop

Step5) now switch to the non-root user
sudo su – hadoop

Step6) Now generate the public and privae keys
ssh-keygen -t rsa 

hit enter 
hit enter 
hit enter

cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys

chmod 640 ~/.ssh/authorized_keys

Step7) verify ssh
ssh localhost

yes
hit enter

Step8) download hadoop
wget https://downloads.apache.org/hadoop/common/hadoop-3.3.6/hadoop-3.3.6.tar.gz

Step9) extract tar file
tar xzf hadoop-3.3.6.tar.gz

step10) move the extracted file
sudo mv hadoop-3.3.6 /usr/local/hadoop

step11) change the ownership of the usrlocal/hadoop to the user hadoop
sudo chown -R hadoop:hadoop /usr/local/hadoop

Step12) set environment path
sudo nano ~/.bashrc

press ctrl+/ to goto the last line, and type
export HADOOP_HOME = usr/local/hadoop
export PATH=$PATH:$HADOOP_HOME/sbin:$HADOOP_HOME/bin
export JAVA_HOME=/usr/lib/jvm/java-1.8.0-openjdk-amd64

press ctrl+o to save
ctrl+x to exit

Now run .bashrc by source ~/.bashrc

Step13) sudo nano $HADOOP_HOME/etc/hadoop/core-site.xml

<configuration>
	<property>
		<name>fs.defaultFS</name>
		<value>hdfs://localhost:9000</value>
		<description>Where HDFS NameNode can be found on the network</description>
	</property>
	<property>
		<name>hadoop.tmp.dir</name>
		<value>/home/hdoop/tmpdata</value>
	</property>
</configuration>

Step14) sudo mkdir -p home/hadoop/dfs

sudo chown -R hadoop:hadoop home/hadoop/dfs

sudo nano $HADOOP_HOME/etc/hadoop/hdfs-site.xml

<configuration>
    <property>
	<name>dfs.namenode.name.dir</name>
	<value>file:/home/hadoop/dfs/namenode</value>
    </property>
    <property>
	<name>dfs.datanode.name.dir</name>
	<value>file:/home/hadoop/dfs/datanode</value>
    </property>
    <property>
	<name>dfs.namenode.checkpoint.dir</name>
	<value>file:/home/hadoop/dfs/secondaryname</value>
    </property>
    <property>
	<name>dfs.replication</name>
	<value>1</value>
    </property>
    <property>
	<name>dfs.blocksize</name>
	<value>134217728</value>
    </property>
</configuration>

Step15) sudo nano $HADOOP_HOME/etc/hadoop/mapred-site.xml
<configuration>
   <property>
      <name>mapreduce.framework.name</name>
      <value>yarn</value>
   </property>
   <property>
      <name>mapreduce.application.classpath</name>
      <value>$HADOOP_MAPRED_HOME/share/hadoop/mapreduce/*:$HADOOP_MAPRED_HOME/share/hadoop/mapreduce/lib/*</value>
   </property>
</configuration>

Step16) sudo nano $HADOOP_HOME/etc/hadoop/hadoop-env.sh
export JAVA_HOME=/usr/lib/jvm/java-1.8.0-openjdk-amd64
export HADOOP_OS_TYPE=${HADOOP_OS_TYPE:-$(uname -s)}
Step17) sudo nano $HADOOP_HOME/etc/hadoop/yarn-site.xml
<configuration>
   <property>
      <name>yarn.nodemanager.aux-services</name>
      <value>mapreduce_shuffle</value>
   </property>
   <property>
      <name>yarn.nodemanager.env-whitelist</name>
      <value>HADOOP_COMMON_HOME,HADOOP_HDFS_HOME,JAVA_HOME,HADOOP_CONF_DIR,CLASSPATH_PREPEND_DISTCACHE,HADOOP_YARN_HOME,HADOOP_MAPRED_HOME</value>
   </property>
</configuration>
Step18) hdfs webui
http://server_ip:9870
http://192.168.1.36:9870

HIVE Installation
Postgres installation
Step1) In root user, run the below commands

sudo sh -c 'echo "deb https://apt.postgresql.org/pub/repos/apt $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list'
wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -
sudo apt-get update
Step2) Install postgresql-16 
sudo apt-get install -y postgresql-16 postgresql-contrib-16
Step3) Now verify
sudo systemctl status postgresql
Step4) Now connet to the postgresql server
sudo su – postgres
psql
to print list of users
\du
Step5) Give password for the superuser i.e. postgres
ALTER USER postgres WITH PASSWORD 'admin@123';
CREATE USER hive WITH PASSWORD 'hive@123';
make hive user as a superuser
Step6)to list the databases
\l
CREATE DATABASE testDB;
CREATE DATABASE metastore;
GRANT ALL ON DATABASE metastore TO hive;
GRANT ALL ON SCHEMA public TO hive;
Step7) to switch database
\c testdb
CREATE TABLE sample(id INT, name VARCHAR(20));
Step8) to quit psql
\q
to stop postgresql server
sudo systemctl stop postgresql
to start again
sudo systemctl start postgresql
or
sudo service postgresql restart
Step9) to install pgadmin
sudo apt install curl
curl -fsS https://www.pgadmin.org/static/packages_pgadmin_org.pub | sudo gpg --dearmor -o /usr/share/keyrings/packages-pgadmin-org.gpg
sudo sh -c 'echo "deb [signed-by=/usr/share/keyrings/packages-pgadmin-org.gpg] https://ftp.postgresql.org/pub/pgadmin/pgadmin4/apt/$(lsb_release -cs) pgadmin4 main" > /etc/apt/sources.list.d/pgadmin4.list && apt update'
sudo apt install pgadmin4

Hive Installation
Step1) sudo su – hadoop
wget https://downloads.apache.org/hive/hive-3.1.2/apache-hive-3.1.2-bin.tar.gz
Untar the file
tar xzf apache-hive-3.1.2-bin.tar.gz
Step2) now edit env variables
sudo nano .bashrc
export HIVE_HOME= /home/hdoop/apache-hive-3.1.2-bin
export PATH=$PATH:$HIVE_HOME/bin
source ~/.bashrc
Step3) sudo nano $HIVE_HOME/bin/hive-config.sh

export HADOOP_HOME = usr/local/hadoop
Step4) Now create hive related directories in hdfs
hadoop fs -mkdir /tmp
hadoop fs -chmod g+w /tmp
hadoop fs -mkdir -p /user/hive/warehouse
hadoop fs -chmod g+w /user/hive/warehouse
Step5) remove guava jar for hive
cd apache-hive-3.1.2-bin/bin
ls $HIVE_HOME/lib
rm $HIVE_HOME/lib/guava-19.0.jar
cp $HADOOP_HOME/share/hadoop/hdfs/lib/guava-27.0-jre.jar $HIVE_HOME/lib/
Step6) 
cd apache-hive-3.1.2-bin
cd conf
sudo nano hive-site.xml

<configuration>
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
</configuration>

Step7) download postgres jar into hive/lib
cd apache-hive-3.1.2-bin
cd lib
wget https://jdbc.postgresql.org/download/postgresql-42.7.1.jar
step8) schematool -dbType postgres -initSchema


## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`API_KEY`

`ANOTHER_API_KEY`




