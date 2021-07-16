import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)

def identify_user():
    store = input("Enter your store name: ").lower()
    workbook = GSPREAD_CLIENT.open(store)
    user = input("Enter your user name: ").lower()
    sheet = workbook.worksheet(user)
    data = sheet.get_all_values()
    print(data)

def main():
    identify_user()

print("Welcome to Mobile Commission Tracker")
main()