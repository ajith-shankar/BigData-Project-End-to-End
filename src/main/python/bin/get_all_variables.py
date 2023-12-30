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
#abs_path = os.path.dirname(__file__)
#rlt_path = "../staging/Dim"
#full_path = os.path.join(abs_path, rlt_path)
staging_dim_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../', 'staging/Dim'))
staging_fact_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../', 'staging/Fact'))
# print(currentPath)
# print(abs_path)
# print(rlt_path)
# print(full_path)
# print(staging_fact_path)





