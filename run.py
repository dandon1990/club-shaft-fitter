import gspread
from google.oauth2.service_account import Credentials
from colorama import Fore, Back, Style
import pyfiglet


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

    while True:
        print(Fore.GREEN + " Please enter your name")
        user_name = input(
            Fore.YELLOW +
            " Enter your name here: \n " + Fore.CYAN).capitalize()

        if validate_name(user_name):
            break

    while True:

        print(Fore.GREEN + " Please enter your handicap")
        user_handicap = input(
            Fore.YELLOW + " Enter your handicap here: \n " + Fore.CYAN)

        if validate_handicap(user_handicap):
            break

    while True:

        print(Fore.GREEN + " Please enter how far you \n"
              " hit your Pitching Wedge (in yards)")
        pwedge_distance = input(
            Fore.YELLOW + " Enter PW distance here: \n " + Fore.CYAN)

        if validate_pwedge_distance(pwedge_distance):
            break

    while True:

        print(Fore.GREEN + " Please enter how far you"
              " hit your 6 iron(in yards)")
        six_distance = input(
            Fore.YELLOW + " Enter 6i distance here: \n " + Fore.CYAN)

        if validate_six_distance(six_distance):
            break

    while True:

        print(Fore.GREEN + " Please enter how far you"
              " hit your Driver(in yards)")
        driver_distance = input(
            Fore.YELLOW + " Enter Driver distance here: \n " + Fore.CYAN)

        if validate_driver_distance(driver_distance):
            break

    print(Fore.MAGENTA + f" The name you provided is: {Fore.CYAN + user_name}")
    print(Fore.MAGENTA +
          f" The handicap you provided is: {Fore.CYAN + user_handicap}")
    print(Fore.MAGENTA +
          f" Your PW distance is: {Fore.CYAN + pwedge_distance}")
    print(Fore.MAGENTA + f" Your 6i distance is: {Fore.CYAN + six_distance}")
    print(Fore.MAGENTA +
          f" Your Driver distance is: {Fore.CYAN + driver_distance}")

    result = [user_name, user_handicap, pwedge_distance,
              six_distance, driver_distance]

    return result


def validate_name(values):
    """
    Inside the try, checks to see if the string is
    only alphabetical characters. If not then raises
    a ValueError and the user has to enter a name that
    is only characters of the alphabet.
    """
    try:
        if not values.isalpha():
            raise ValueError(Fore.RED +
                             f" Your name cannot contain numbers\n"
                             f" or special characters, \n"
                             f" you entered {Fore.CYAN + values + Fore.RED}")
    except ValueError as e:
        print(f" Invalid data: {e}, Please try again.")
        return False

    return True


def validate_handicap(values):
    """
    Inside the try, converts string value to integer.
    Raises ValueError if string cannot be converted into integer,
    or if value is more than 54 (max golf handicap).
    """
    try:
        if int(values) > 54:
            raise ValueError(Fore.RED +
                             f" The max handicap is 54 \n"
                             f" as this is the legal limit,\n"
                             f" you provided {Fore.CYAN + values + Fore.RED}")
        elif int(values) < 1:
            raise ValueError(Fore.RED +
                             f" Your handicap is \n"
                             f" {Fore.CYAN + values + Fore.RED}\n"
                             f" maybe you should try and join The PGA Tour")
    except ValueError as e:
        print(f" Invalid data: {e}, Please try again.")
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
            raise ValueError(Fore.RED +
                             f" It seems you hit your PW rather far,\n"
                             f" your distance provided \n"
                             f" {Fore.CYAN + values + Fore.RED}"
                             )
        elif int(values) < 90:
            raise ValueError(Fore.RED +
                             f" Your PW doesn't go far, your distance\n"
                             f" provided {Fore.CYAN + values + Fore.RED}. \n"
                             f" Maybe a lesson is needed before \n"
                             f" getting fitted for clubs"
                             )
    except ValueError as e:
        print(f" Invalid data: {e}, Please try again.")
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
            raise ValueError(Fore.RED +
                             f" It seems you hit your 6iron rather far,\n"
                             f" your distance provided\n"
                             f" {Fore.CYAN + values + Fore.RED}"
                             )
        elif int(values) < 130:
            raise ValueError(Fore.RED +
                             f" Your 6 Iron doesn't go far,\n"
                             f" your distance provided \n"
                             f" {Fore.CYAN + values + Fore.RED}.\n"
                             f" Maybe a lesson is needed \n"
                             f" before getting fitted for clubs"
                             )
    except ValueError as e:
        print(f" Invalid data: {e}, Please try again.")
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
            raise ValueError(Fore.RED +
                             f" It seems you hit your Driver rather far,\n"
                             f" your distance provided \n"
                             f" {Fore.CYAN + values + Fore.RED}"
                             )
        elif int(values) < 190:
            raise ValueError(Fore.RED +
                             f" Your Driver doesn't go far, \n"
                             f" your distance provided \n"
                             f" {Fore.CYAN + values + Fore.RED}. \n"
                             f" Maybe a lesson is needed \n"
                             f" before getting fitted for clubs"
                             )
    except ValueError as e:
        print(f" Invalid data: {e}, Please try again.")
        return False

    return True


def update_worksheet(data, worksheet):
    """
    Updates the relevant worksheet
    """
    print(Fore.YELLOW + f" Updating {worksheet} worksheet...\n")
    profile_worksheet = SHEET.worksheet(worksheet)
    profile_worksheet.append_row(data)
    print(Fore.GREEN + f" {worksheet} worksheet updated succesfully. \n")


def calculate_shaft_flex(data):
    """
    Calculate the recommended shaft flex for player based on
    clubhead speed. This is calculate by taking total driver
    distance and dividing it by 2.5.
    """
    print(Fore.CYAN + " Calculating shaft flex recomendation... \n")
    player_stats = SHEET.worksheet("Player Data").get_all_values()
    last_player_stats = player_stats[-1]
    driver = last_player_stats[4]
    driver_speed = int(driver) / 2.5
    if driver_speed < 85:
        flex = " Regular"
    elif driver_speed < 105:
        flex = " Stiff"
    else:
        flex = " Extra-Stiff"

    return flex


def calculate_iron_type(data):
    """
    Calculate the recommended iron type for player based on
    distance between pitching wedge and 6 iron.
    This is calculated by subtracting the pitching wedge
    distance form the 6 iron distance.
    """
    print(Fore.CYAN + " Calculating Iron recomendation... \n")
    player_stats = SHEET.worksheet("Player Data").get_all_values()
    most_recent = player_stats[-1]
    six_iron = most_recent[3]
    p_wedge = most_recent[2]
    iron_difference = int(six_iron) - int(p_wedge)
    if int(iron_difference) > 55 and int(six_iron) > 190:
        iron_type = " Blades"
    elif iron_difference <= 55:
        iron_type = " Cavity Backs"
    else:
        iron_type = " Combo Set"

    return iron_type


def main():
    """
    Run all program functions
    """
    user_data = get_user_data()
    user_name = user_data[0]
    profile_data = [int(num) for num in user_data if num.isnumeric()]
    profile_data.insert(0, user_name)
    update_worksheet(profile_data, "Player Data")
    flex = calculate_shaft_flex(profile_data)
    print(Fore.RED + flex)
    iron_type = calculate_iron_type(profile_data)
    print(Fore.RED + iron_type)
    profile_data.append(iron_type)
    profile_data.append(flex)
    update_worksheet(profile_data, "Recommendations")


title_top = pyfiglet.figlet_format(" Welcome    to")
title_middle = pyfiglet.figlet_format(" DEEDEE's")
title_bottom = pyfiglet.figlet_format(" Fitting    APP")
print(title_top)
print(Fore.YELLOW + title_middle + Style.RESET_ALL)
print(title_bottom)
main()
