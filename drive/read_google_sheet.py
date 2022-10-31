import gspread
from oauth2client.service_account import ServiceAccountCredentials


SHEET_NAME=''
CRED_FILE=''

scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name(CRED_FILE, scope)


client = gspread.authorize(creds)

sheet = client.open(SHEET_NAME)

sheet_instance = sheet.get_worksheet(0)

records_data = sheet_instance.get_all_records()