from sqlalchemy import create_engine
from google.cloud import bigquery
from google.oauth2google.oauth2 import service_account

# connection to postgresss database.
engine = create_engine('postgres://ibnzqkfl:rYgeprTJq6jD_eR0bxEXwAnYX7fM-yRD@rajje.db.elephantsql.com:5432/ibnzqkfl')
# google service account credentials.
credentials = service_account.Credentials.from_service_account_file('HackerNews-a13892bba4db.json')
# label the project.
project_id = 'SaltyNews-HackerNews'
# set the bigquery client.
client = bigquery.Client(credentials=credentials, project=project_id)
# set the referenced dataset and proect from bigquery.
data_project_ref = client.dataset('hacker_news', project='bigquery-public-data')
# set the referenced tabe 'comments' from the bigquery hacker news dataset.
table_ref = data_project_ref.table('comments')
# get the table from big query.
comments_table = client.get_table(table_ref)


