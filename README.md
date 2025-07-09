END TO END DATA SCIENCE PROJECT 

import dagshub
dagshub.init(repo_owner='vibhutisarode', repo_name='datascience', mlflow=True)

import mlflow
with mlflow.start_run():
  mlflow.log_param('parameter name', 'value')
  mlflow.log_metric('metric name', 1)