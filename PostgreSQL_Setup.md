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

# print list of users
\du
```

5. **Create Databases and Users**


