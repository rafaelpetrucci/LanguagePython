import pandas as pd
import requests
from datetime import datetime

# Aplicação com possibilidade de jobs com alto tempo de execução.

# variáveis
print('\n--Aplicação com possibilidade de jobs com alto tempo de execução--\n')
username = input('Username: ').strip()
password = input('Senha: ').strip()
environment = input('Environment(Sem Porta): ').strip()
porta = input('Porta: ').strip().replace(':', '')
qnt_jobs = int(input('Limite máximo de jobs: '))
environment += ':' + porta
date_atual = datetime.now()
auxiliar_data_hoje = datetime.today().date()

print('Informativos:')
print(f'Environment com porta: {environment}')
print(f'Limite de jobs: {qnt_jobs}')
print(f'Data Atual: {auxiliar_data_hoje}\n\n')


# login
def login():
    users = {"username": username,
             "password": password}

    login_url = requests.post(f'https://{environment}/automation-api/session/login', json=users,
                              verify=False)
    login_dict = login_url.json()
    return {'Authorization': 'Bearer ' + login_dict['token']}


# Buscar jobs anormais
authorization = login()
response = requests.get(
    f'https://{environment}/automation-api/run/jobs/status?limit={qnt_jobs}&status=executing',
    headers=authorization, verify=False)
response_dict = response.json()['statuses']

# tratando os dados

# transformando os dados dict em dataframe
response_df = pd.DataFrame.from_dict(response_dict)

# transformando o estimatedEndTime em um unico valor para cada célula
response_df.loc[:, ['estimatedEndTime']] = response_df['estimatedEndTime'].transform(lambda x: x[0])

# transformando startTime em tipo de Datetime
response_df.loc[:, ['startTime']] = pd.to_datetime(response_df['startTime'], format='%Y%m%d%H%M%S')

# NO_TIME
executing_no_time = response_df[response_df['estimatedEndTime'].str.contains('NO_TIME')]

# retirando informações desnecessárias e atribuindo a um novo df
response_df = response_df[~response_df['estimatedEndTime'].str.contains('NO_TIME')]

# transformando as colunas date, em Datetime
response_df.loc[:, ['estimatedEndTime']] = pd.to_datetime(response_df['estimatedEndTime'], format='%Y%m%d%H%M%S')

# Separando
response_df = response_df[response_df['estimatedEndTime'] <= date_atual]

response_df.loc[:, ['difference']] = response_df['estimatedEndTime'] - response_df['startTime']
response_df = response_df[(response_df['difference'].dt.days > 0) |
                          (response_df['difference'].dt.components['hours'] > 0)]

if response_df.empty:
    print('Sem anormal')

executing_no_time = executing_no_time.set_index(executing_no_time['name'])
response_df = response_df.set_index(response_df['name'])
print('\nJobs sem tempo estimado de finalização:\n')
print(executing_no_time[['ctm', 'startTime', 'estimatedEndTime']])
print('---------------------------------------------------------')
print('\nJobs com possível anormal:\n')
print(response_df[['ctm', 'startTime', 'estimatedEndTime', 'difference']])
