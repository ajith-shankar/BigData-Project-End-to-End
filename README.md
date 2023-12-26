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

## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`API_KEY`

`ANOTHER_API_KEY`




