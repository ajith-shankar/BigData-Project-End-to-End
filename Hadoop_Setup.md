---

# Hadoop Setup Instructions

This guide outlines the steps to set up Apache Hadoop for the BigData Project: End-to-End. Hadoop is a fundamental component for distributed storage and processing, and the following instructions will help you configure it for seamless integration into your project.

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

3. **Configure Hadoop Environment**

Edit the Hadoop configuration files to match your system settings. Key configuration files include:

- `hadoop-env.sh`: Configure Java Home and other environment variables.
- `core-site.xml`: Configure Hadoop core settings.
- `hdfs-site.xml`: Configure Hadoop Distributed File System (HDFS) settings.
- `mapred-site.xml`: Configure MapReduce settings.

Example:

```bash
# Set Java Home in hadoop-env.sh
export JAVA_HOME=/path/to/your/jdk

# Configure core-site.xml
<configuration>
    <property>
        <name>fs.defaultFS</name>
        <value>hdfs://localhost:9000</value>
    </property>
</configuration>

# Configure hdfs-site.xml
<configuration>
    <property>
        <name>dfs.replication</name>
        <value>1</value>
    </property>
</configuration>
```

### 4. Format HDFS

Format the Hadoop Distributed File System (HDFS) before starting Hadoop:

```bash
bin/hdfs namenode -format
```

### 5. Start Hadoop Services

Start the Hadoop services:

```bash
sbin/start-dfs.sh
sbin/start-yarn.sh
```

### 6. Access Hadoop Web UI

Access the Hadoop Web UI to verify successful setup:

- HDFS Namenode: [http://localhost:9870/](http://localhost:9870/)
- YARN ResourceManager: [http://localhost:8088/](http://localhost:8088/)

## Conclusion

Hadoop is now set up and ready for use in your BigData Project. Ensure that the services are running correctly before proceeding with data processing and analysis tasks.

For additional configuration options and advanced settings, refer to the official Hadoop documentation: [https://hadoop.apache.org/](https://hadoop.apache.org/)

```

Adjust the paths, version numbers, and configuration settings based on your specific requirements. Additionally, consider providing troubleshooting tips or additional resources if needed.


Conclusion

You have successfully set up Apache Hadoop for the BigData Project: End-to-End. Ensure that Hadoop services are running, and you can proceed with other components of your project that rely on distributed storage and processing.

For further configurations and advanced settings, refer to the official Hadoop documentation.

Happy data processing!
