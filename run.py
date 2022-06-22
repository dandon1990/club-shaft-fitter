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
SHEET = GSPREAD_CLIENT.open('club_shaft_fitter')

def get_user_data():
    """
    Get user details and information
    """
    print("Please enter your name")
    user_name = input("Enter your name here: \n")

    print ("Please enter your handicap")
    user_handicap = input("Enter your handicap here: \n")

    print("Please enter how far you hit your Pitching Wedge (in yards)")
    pwedge_distance = input("Enter PW distance here: \n")

    print("Please enter how far you hit your 6 iron(in yards)")
    six_distance = input("Enter 6i distance here: \n")

    print("Please enter how far you hit your Driver(in yards)")
    driver_distance = input("Enter Driver distance here: \n")

    print(f"The name you provided is: {user_name}")
    print(f"The handicap you provided is: {user_handicap}")
    print(f"Your PW distance is: {pwedge_distance}")
    print(f"Your 6i distance is: {six_distance}")
    print(f"Your Driver distance is: {driver_distance}")

get_user_data()