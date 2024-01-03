import os


# set environment variables
os.environ['envn'] = 'Prod'  # 'Test' if it local mode
os.environ['header'] = 'True'
os.environ['inferSchema'] = 'True'

# Get environment variables
envn = os.environ['envn']
header = os.environ['header']
inferSchema = os.environ['inferSchema']

# Set other variables
appName = "USA Prescriber Report"
currentPath = os.getcwd()
# local path
# staging_dim_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../', 'staging/Dim'))
# staging_fact_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../', 'staging/Fact'))

# # hdfs path
staging_dim_path = "/user/hadoop/Projects/PrescPipeline/staging/Dim"
staging_fact_path = "/user/hadoop/Projects/PrescPipeline/staging/Fact"


