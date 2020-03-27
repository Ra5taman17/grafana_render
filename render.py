import requests
import os

def save_graph(login,password,host,port,dashboard_uid,dashboard_title,panel_id):
    url = f'http://{login}:{password}@{host}:{port}/render/d-solo/{dashboard_uid}/{dashboard_title}?panelId={panel_id}&orgId=1&refresh=1m&from=1585126462563&to=1585130062564&width=1000&height=500'
    response = requests.get(url)
    file_name = f'{dashboard_title}_{panel_id}'
    if not os.path.exists('temp'):
        os.mkdir('temp')
    with open(os.path.join('temp', f'{file_name}.jpg'), 'wb') as file:
        file.write(response.content)

# save_graph(url, 'test123')