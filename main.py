import requests
from render import save_graph
from threading import Thread

def get_dashboards(login, password, host, port=''):

    url = f'http://{login}:{password}@{host}:{port}/api/search/'
    response = requests.get(url)
    for dashboard in response.json():
        if dashboard['type'] == 'dash-db':
            dashboard_title = dashboard['title']
            dashboard_url = dashboard['url'].split('/d')[1]
            dashboard_uid = dashboard_url.split('/')[1]
            try:
                folder_title = dashboard['folderTitle']
            except KeyError:
                folder_title = 'General'

            print(f'FOLDER_TITLE: {folder_title}; DASHBOARD_TITLE: {dashboard_title}, URL: {dashboard_url}, UID: {dashboard_uid}')


def get_ids(login, password, host, port, dashboard_uid):

    url = f'http://{login}:{password}@{host}:{port}/api/dashboards/uid/{dashboard_uid}'
    response = requests.get(url)
    panels = []
    for row in response.json()['dashboard']['panels']:
        if row['type'] != 'row':
            panel_id = row['id']
            panel_title = row['title']
            panels.append(panel_id)
            print(f'PANEL_TITLE: {panel_title}; PANEL_ID: {panel_id}')
    return panels

# get_dashboards('admin', 'admin', '192.168.48.128', '3000')
panels = get_ids('admin', 'admin', '192.168.48.128', '3000', 'xkrINvrZz')

