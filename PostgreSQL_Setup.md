---

# PostgreSQL Setup Instructions

This guide provides step-by-step instructions for setting up PostgreSQL as part of the BigData Project: End-to-End. PostgreSQL is a powerful open-source relational database that can serve as a robust data storage solution for your project.

## Prerequisites

Before starting the PostgreSQL setup process, ensure the following prerequisites are met:

- **Access to a Server:** You should have access to a server where you plan to install and configure PostgreSQL.
- **Superuser Privileges:** Ensure that you have superuser privileges on the server to install and configure PostgreSQL.


### Steps for PostgreSQL Setup
1. **Download PostgreSQL**
```bash
# switch to root user 
sudo su - Ajith
```
```bash
# Create the file repository configuration
sudo sh -c 'echo "deb https://apt.postgresql.org/pub/repos/apt $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list'

# Import the repository signing key
wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -

# Update the package lists
sudo apt-get update
```

2. **Install PostgreSQL**
Install the latest version of PostgreSQL.
```bash
sudo apt-get install -y postgresql postgresql-contrib
```

3. **Verify**
```bash
sudo systemctl status postgresql
```

4. **Connect to Postgre Server**
```bash
sudo su – postgres

# access postgre shell by typing
psql

# to list the users
\du

# to list the databases
\l
```

5. **Create Databases and Users**
```sql
# Superuser i.e. 'postgres'

# change password of superuser 'postgres'
ALTER USER postgres WITH ENCRYPTED PASSWORD 'admin@123';

# create a user for Hive
CREATE USER hive WITH ENCRYPTED PASSWORD 'hive@123';

# create a user for Spark
CREATE USER spark WITH ENCRYPTED PASSWORD 'spark@123';

# create a Database for hive metastore 
CREATE DATABASE metastore;

# grant all access to the user 'hive'
GRANT ALL ON DATABASE metastore TO hive;
GRANT ALL ON SCHEMA public TO hive;
```

## Conclusion

You have successfully set up PostgreSQL for the BigData Project: End-to-End. Ensure that your PostgreSQL database is running, and you can proceed with configuring other components of your project that interact with relational databases.

For further configurations and advanced settings, refer to the official PostgreSQL [documentation](https://www.postgresql.org/docs/).


Happy data warehousing!




