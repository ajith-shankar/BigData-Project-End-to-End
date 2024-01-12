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
