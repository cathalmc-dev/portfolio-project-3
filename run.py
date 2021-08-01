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


def identify_store():
    store = input("Enter your store name: ").lower()
    workbook = GSPREAD_CLIENT.open(store)
    print(workbook)
    print(dir(workbook))
    import pdb; pdb.set_trace()
    if store != "dundrum":
        print("Invalid")
        identify_store()
    else:
        identify_user()


def identify_user():
    user = input("Enter your user name: ").lower()
    print(user)
    # if validate_user(user):
    #     sheet = workbook.worksheet(user)
    #     data = sheet.get_all_values()
    #     print(data)


# def validate_user():
#     try:


def main():
    identify_store()

print("Welcome to Mobile Commission Tracker")
main()
