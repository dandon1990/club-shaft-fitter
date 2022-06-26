import gspread
from google.oauth2.service_account import Credentials
from pprint import pprint

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
    Get user details and information. Run while loops to collect valid 
    strings of data from the user via the terminal, which must be 
    strings of 54 or less for handicap, 170 or less for Pitching
    Wedge distance, 220 or less for 6 iron distance and 350 or less 
    for Driver distace. The loops will repeatedly request data, until
    it is valid.
    """
    print("Please enter your name")
    user_name = input("Enter your name here: \n")
    
    
    while True:

        print ("Please enter your handicap")
        user_handicap = input("Enter your handicap here: \n")

        if validate_handicap(user_handicap):
            print("Data is valid")
            break

    while True:

        print("Please enter how far you hit your Pitching Wedge (in yards)")
        pwedge_distance = input("Enter PW distance here: \n")

        if validate_pwedge_distance(pwedge_distance):
            print("PW is valid")
            break


    while True:


        print("Please enter how far you hit your 6 iron(in yards)")
        six_distance = input("Enter 6i distance here: \n")

        if validate_six_distance(six_distance):
            print("6iron is valid")
            break

    while True:


        print("Please enter how far you hit your Driver(in yards)")
        driver_distance = input("Enter Driver distance here: \n")


        if validate_driver_distance(driver_distance):
            print("Driver is vaild")
            break

    print(f"The name you provided is: {user_name}")
    print(f"The handicap you provided is: {user_handicap}")
    print(f"Your PW distance is: {pwedge_distance}")
    print(f"Your 6i distance is: {six_distance}")
    print(f"Your Driver distance is: {driver_distance}")

    
    return user_name, user_handicap, pwedge_distance, six_distance, driver_distance
    

    

def validate_handicap(values):
    """
    Inside the try, converts string value to integer.
    Raises ValueError if string cannot be converted into integer,
    or if value is more than 54 (max golf handicap).
    """
    try:
        if int(values) > 54:
            raise ValueError(
                f"The max handicap is 54 as this is the legal limit, you provided {values}"
            )
    except ValueError as e:
        print(f"Invalid data: {e}, Please try again")
        return False

    return True

def validate_pwedge_distance(values):
    """
    Inside the try, converts string value to integer.
    Raises ValueError if string cannot be converted into integer,
    or if value is more than 170 yards.
    """
    try:
        if int(values) > 170:
            raise ValueError(
                f"It seems you hit your PW rather far, your distance provided {values}"
            )
    except ValueError as e:
        print(f"Invalid data: {e}, Please try again.")
        return False

    return True


def validate_six_distance(values):
    """
    Inside the try, converts string value to integer.
    Raises ValueError if string cannot be converted into integer,
    or if value is more than 220 yards.
    """
    try:
        if int(values) > 220:
            raise ValueError(
                f"It seems you hit your 6iron rather far, your distance provided {values}"
            )
    except ValueError as e:
        print(f"Invalid data: {e}, Please try again.")
        return False

    return True

def validate_driver_distance(values):
    """
    Inside the try, converts string value to integer.
    Raises ValueError if string cannot be converted into integer,
    or if value is more than 350 yards.
    """
    try:
        if int(values) > 350:
            raise ValueError(
                f"It seems you hit your Driver rather far, your distance provided {values}"
            )
    except ValueError as e:
        print(f"Invalid data: {e}, Please try again.")
        return False

    return True

def update_profile_worksheet(data):
    """
    Update player profile worksheet,
    """
    print("Updating profile worksheet...\n")

    profile_worksheet = SHEET.worksheet('Player Data')
    profile_worksheet.append_row(data)
    print("Profile worksheet updated succesfully. \n")

def calculate_shaft_flex(player_data_row):
    """
    Calculate the recommended shaft flex for player based on
    clubhead speed. This is calculate by taking total driver 
    distance and dividing it by 2.5.
    """
    print("Calculating shaft flex recomendation... \n")
    player_stats = SHEET.worksheet("Player Data").get_all_values()
    last_player_stats = player_stats[-1]
    





def main():
    """
    Run all program functions
    """
    user_data = get_user_data()
    user_name = user_data[0]
    profile_data = [int(num) for num in user_data if num.isnumeric()]
    profile_data.insert(0, user_name)
    print([type(data) for data in profile_data])
    update_profile_worksheet(profile_data)
    calculate_shaft_flex(profile_data)

    


main()
