from __future__ import print_function
import httplib2
import os

from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage

try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None

# If modifying these scopes, delete your previously saved credentials
# at ~/.credentials/sheets.googleapis.com-python-quickstart.json
SCOPES = 'https://www.googleapis.com/auth/spreadsheets.readonly'
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'Google Sheets API Python Quickstart'


def get_credentials():
    """Gets valid user credentials from storage.

    If nothing has been stored, or if the stored credentials are invalid,
    the OAuth2 flow is completed to obtain the new credentials.

    Returns:
        Credentials, the obtained credential.
    """
    home_dir = os.path.expanduser('~')
    credential_dir = os.path.join(home_dir, '.credentials')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir,
                                   'sheets.googleapis.com-python-quickstart.json')

    store = Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        if flags:
            credentials = tools.run_flow(flow, store, flags)
        else: # Needed only for compatibility with Python 2.6
            credentials = tools.run(flow, store)
        print('Storing credentials to ' + credential_path)
    return credentials

#begin Spreadsheet Setup
credentials = get_credentials()
http = credentials.authorize(httplib2.Http())
discoveryUrl = ('https://sheets.googleapis.com/$discovery/rest?'
                'version=v4')
service = discovery.build('sheets', 'v4', http=http,
                          discoveryServiceUrl=discoveryUrl)

#spreadsheetId = '1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgvE2upms'
spreadsheetId = '19orie97IMYbHyZg0rd2FQy_joWmA9wqpFIHLq8u8clw'
rangeName = 'A2:ZZ'
result = service.spreadsheets().values().get(
    spreadsheetId=spreadsheetId, range=rangeName).execute()
values = result.get('values', [])
#end Spreadsheet Setup

class data():
    def __init__(self):
        return

    def value_length(self):
        return len(values)

    def get_cat_level_one(self):
        arr = []
        if not values:
            print('No data found.')
        else:
            for row in values:
                arr.append(row[1])
        return arr[0:4]

    def get_trivia_questions(self):
        arr = []
        if not values:
            print('No data found.')
        else:
            for row in values:
                arr.append(row[2])
        return arr

    def get_trivia_answers(self):
        arr = []
        if not values:
            print('No data found.')
        else:
            for row in values:
                arr.append(row[3])
        return arr

    def get_artistry(self):
        arr = []
        if not values:
            print('No data found.')
        else:
            for row in values:
                arr.append(row[4])
        return arr

    def get_chance(self):
        arr = []
        if not values:
            print('No data found.')
        else:
            for row in values:
                arr.append(row[5])
        return arr

    def get_puzzle(self):
        arr = []
        if not values:
            print('No data found.')
        else:
            for row in values:
                arr.append(row[6])
        return arr

    def get_body(self):
        arr = []
        if not values:
            print('No data found.')
        else:
            for row in values:
                arr.append(row[7])
        return arr

    def get_spirit(self):
        arr = []
        if not values:
            print('No data found.')
        else:
            for row in values:
                arr.append(row[8])
        return arr

    def get_classics(self):
        arr = []
        if not values:
            print('No data found.')
        else:
            for row in values:
                arr.append(row[9])
        return arr
