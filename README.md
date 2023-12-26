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

## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`API_KEY`

`ANOTHER_API_KEY`




