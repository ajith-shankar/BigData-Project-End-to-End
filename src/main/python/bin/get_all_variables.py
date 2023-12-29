import os

# set environment variables
os.environ['envn'] = 'Test'
os.environ['header'] = 'True'
os.environ['inferSchema'] = 'True'

# Get environment variables
envn = os.environ['envn']
header = os.environ['header']
inferSchema = os.environ['inferSchema']

# Set other variables
appName = "USA Prescriber Report"
currentPath = os.getcwd()
staging_dim = currentPath + '/staging/dim'
staging_fact = currentPath + '/staging/fact'


