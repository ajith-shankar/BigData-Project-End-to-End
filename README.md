---

# BigData Project: US-Prescribers-Report

![BigData Project](https://img.shields.io/badge/BigData-US--Prescribers--Report-blue)

## Overview

Welcome to the BigData Project: US-Prescribers-Report repository! This project is a comprehensive solution for handling large-scale data processing using various Big Data technologies. Whether you're a data engineer, data scientist, or anyone interested in working with big data, this repository provides a versatile platform for end-to-end data processing.

![DataFlow](./images/DataFlow_1.png?raw=true "DataFlow")


## Features

- **Data Ingestion:** Efficiently ingest large volumes of data from various sources.
- **Data Processing:** Perform complex data transformations and processing tasks.
- **Storage:** Store processed data in scalable and fault-tolerant storage systems.
- **Analytics:** Conduct analytics and gain insights from the processed data.
- **Visualization:** Visualize the results to make data-driven decisions.

## Technologies Used

- **Hadoop Distributed File System (HDFS):** For distributed storage.
- **Apache Spark:** For distributed data processing.
- **Apache Hive:** For data warehousing and SQL-like queries.
- **PostgreSQL:** For organizes data into tables with rows and columns.
- **Azure Blob Storage:** For object storage.

## Project Structure

The repository is organized as follows:

```img
US-Prescribers-Report/
└── src/
    └── main/
        ├── Staging/
        │   ├── Dim/
        │   │   └── USA_City.json
        │   └── Fact/
        │       └── USA_Prescriber.csv
        ├── Python/
        │   ├── bin/
        │   │   ├── run_pipeline.ksh
        │   │   └── .....*.py 
        │   ├── lib/
        │   │   └── PostgreSQL.jar
        │   ├── logs/
        │   │   ├── run_pipeline.log
        │   │   └── ....._current_date.log
        │   └── utils/
        │       └── logging_to_file.conf
        ├── sql/
        │   └── create_table.sql
        └── Output/
            ├── Dim
            └── Fact
```

- **[Hadoop Installation](./Hadoop_Setup.md):** Contains code for ingesting data from various sources.
- **[PostgreSQL Installation](./PostgreSQL_Setup.md):** Includes code for processing and transforming data using Apache Spark and Apache Flink.
- **[Hive Installation](./Hive_Setup.md):** Contains configurations and scripts for setting up storage systems like HDFS, Hive, and HBase.
- **[Spark Installation](./Spark_Setup.md):** Includes code for performing analytics on the processed data.

## Getting Started

Follow these steps to get started with the BigData Project:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/ajith-shankar/US-Prescribers-Report.git
   ```
2. **Navigate to the project directory:**
   ```bash
   cd US-Prescribers-Report
   ```
   
3. **Run the Pipeline:**
   ```bash
   # goto the corresponding directory
   cd src/main/python/bin
   ```
   ```bash
   ./run_pipeline.ksh
   ```   
3. **Explore the specific directories based on your interest (data_ingestion, data_processing, storage, analytics, visualization).**
4. **Refer to the README files in each directory for detailed instructions.**

## Contributors

- [Ajith Shankar](https://github.com/ajith-shankar)

Feel free to contribute by opening issues, submitting pull requests, or suggesting improvements. Your feedback and collaboration are highly appreciated!

## License

This project is licensed under the [MIT License](LICENSE).

---


