import os
from pathlib import Path


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
currentPath = Path.cwd()
staging_dim_path = str(currentPath.parents[1]) + '/staging/Dim'
staging_fact_path = str(currentPath.parents[1]) + '/staging/Fact'





