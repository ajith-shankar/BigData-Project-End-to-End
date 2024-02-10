---

# Hadoop Setup Instructions

This guide outlines the steps to set up Apache Hadoop for the BigData Project: USA-Healthcare-Report. Hadoop is a fundamental component for distributed storage and processing, and the following instructions will help you configure it for seamless integration into your project.

## Prerequisites

Before starting the Hadoop setup process, ensure that you have the following prerequisites installed and configured:

- **Java Development Kit (JDK):** Hadoop is a Java-based framework, so you need to have Java installed on your system. Download and install the latest JDK from the official Oracle website. In a Linux environment, execute the command below in the terminal.
   ```bash
   sudo apt-get install openjdk-8-jdk
   ```
   
- **Python3:** As we will be using PySpark, it is necessary to have Python installed. You can install the latest version of Python by executing the following command in the Linux terminal.
   ```bash
   sudo apt install python3
   ```

- **SSH (Secure Shell):** As we plan to install various services on our local machine, establishing an SSH connection is essential for communication with them. Execute the following command to install SSH, and subsequently, we will configure passwordless communication over SSH.
    ```bash
   sudo apt install openssh-server openssh-client
   ```
   It is advisable to create a dedicated user for Hadoop, distinct from your root user. Let's create a new user by executing the following commands.
   ```bash
   sudo addser hadoop
   # username=hadoop
   # password=hadoop
   ```
   ```bash
   sudo usermod -aG sudo hadoop
   ```
   Now, swith to the user **hadoop**
   ```bash
   sudo su – hadoop
   ```
   Now, we will configure passwordless communication
   ```bash
   ssh-keygen -t rsa
   # hit enter 
   # hit enter 
   # hit enter
   ```
   ```bash
   cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys
   ```
   ```bash
   chmod 640 ~/.ssh/authorized_keys
   ```
   Verify SSH by
   ```bash
   ssh localhost
   # type yes 
   # hit enter
   ```


### Steps for Hadoop Setup
1. **Download Hadoop**

Visit the official Apache Hadoop website (https://hadoop.apache.org/) to download the latest stable release. Choose the appropriate distribution package based on your operating system.
```bash
wget https://downloads.apache.org/hadoop/common/hadoop-3.3.6/hadoop-3.3.6.tar.gz
```


2. **Extract Hadoop**

Extract the downloaded Hadoop file
```bash
tar xzf hadoop-3.3.6.tar.gz
```

3. **Move the extracted file**
```bash
sudo mv hadoop-3.3.6 /usr/local/hadoop
```

5. **Change the ownership of the directory '/usr/local/hadoop' to the user 'hadoop'**
```bash
sudo chown -R hadoop:hadoop /usr/local/hadoop
```

6. **Set the environment variables and path**
```bash
sudo nano ~/.bashrc
```

```bash
# Append the following path to the end of the file.

export HADOOP_HOME = /usr/local/hadoop
export PATH=$PATH:$HADOOP_HOME/sbin:$HADOOP_HOME/bin
export JAVA_HOME=/usr/lib/jvm/java-1.8.0-openjdk-amd64
```

7. **Enable the changes**
```bash
source ~/.bashrc
```
 
8. **Configure Hadoop Environment**

Edit the Hadoop configuration files to match your system settings. Key configuration files include:

- `core-site.xml`: Configure Hadoop core settings.
- `hdfs-site.xml`: Configure Hadoop Distributed File System (HDFS) settings.
- `mapred-site.xml`: Configure MapReduce settings.
- `hadoop-env.sh`: Configure Java Home and other environment variables.
- `yarn-site.xml`: Configure YARN settings.


`core-site.xml`
```bash
# open in nano editor
sudo nano $HADOOP_HOME/etc/hadoop/core-site.xml

# add the below properties
<configuration>
    <property>
        <name>fs.defaultFS</name>
        <value>hdfs://localhost:9000</value>
        <description>Where HDFS NameNode can be found on the network</descripti>
    </property>
    <property>
        <name>hadoop.tmp.dir</name>
        <value>/home/hadoop/tmp</value>
    </property>
</configuration>
```


`hdfs-site.xml`
```bash
# create a directory to store node metadata
sudo mkdir -p home/hadoop/dfs

# change the ownership of the directory to user 'hadoop'
sudo chown -R hadoop:hadoop home/hadoop/dfs

# open in nano editor
sudo nano $HADOOP_HOME/etc/hadoop/hdfs-site.xml

# add the below properties
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
```


`mapred-site.xml`
```bash
# open in nano editor
sudo nano $HADOOP_HOME/etc/hadoop/mapred-site.xml

# add the JAVA path and Hadoop OS type
export JAVA_HOME=/usr/lib/jvm/java-1.8.0-openjdk-amd64
export HADOOP_OS_TYPE=${HADOOP_OS_TYPE:-$(uname -s)}
```


`hadoop-env.sh`
```bash
# open in nano editor
sudo nano $HADOOP_HOME/etc/hadoop/hadoop-env.sh

# add the below properties
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
```

`yarn-site.xml`
```bash
# open in nano editor
sudo nano $HADOOP_HOME/etc/hadoop/yarn-site.xml

# add the below properties
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
```


9. **Format HDFS**

Format the Hadoop Distributed File System (HDFS) before starting Hadoop:
```bash
hdfs namenode -format
```

10. **Start Hadoop Services**

```bash
start-dfs.sh
start-yarn.sh
```

11. **Access Hadoop Web UI**

Access the Hadoop Web UI to verify successful setup:

- HDFS Namenode: [http://localhost:9870/](http://localhost:9870/)
- YARN ResourceManager: [http://localhost:8088/](http://localhost:8088/)

## Conclusion

You have successfully set up Apache Hadoop for the BigData Project: USA-Healthcare-Report. Ensure that Hadoop services are running, and you can proceed with other components of your project that rely on distributed storage and processing.

Adjust the paths, version numbers, and configuration settings based on your specific requirements. Additionally, consider providing troubleshooting tips or additional resources if needed.

For additional configuration options and advanced settings, refer to the official Hadoop [documentation](https://hadoop.apache.org/)

Happy data processing!
