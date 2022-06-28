# DEEDEE'S CLUB-SHAFT-FITTER

DEEDEE's fitting app is used for keen golfers to enter data that they know about their game and be able to get accurate results on what clubs (irons) and what flex of shaft they should be using.

[Here is a live link to the app](https://deedees-fitting-app.herokuapp.com/)

![App Title](/Assets/Documentation/deedee.png)

## How to use the app

The app is designed to take information from the user and then give a recommendation on what type of clubs the should be using anf what type of shaft the should use with the club. The app will ask the user a series of questions and then make some calculations based on the information given and the make recommendations based on the calculations.

## Features
* The app features a series of questions that include: 
    * User's Name
    * User's handicap
    * Distance of the user's pitching wedge
    * Distance of the user's 6 Iron
    * Distance of the user's Driver

* The app take's driver distance and can work out clubhead speed by dividing the data by (2.5). Based on the player's clubhead speed the app will recommend a shaft flex which is suited to them. The flex will be either Regular, Stiff or Extra-Stiff.

![Shaft Flex Calculating](/Assets/Documentation/flex_calcualtion.png)

* The app updates a google sheet with all the all of the User's inputs and the recommendations for club and shaft types.
![Google sheet of user input]()  


## Testing

I have manually yesyed this project by doing the following:
* Passed the code through a PEP8 linter and confirmed there are...


* Given invalid inputs when asked for user's name:
    * Entered nothing when name was reuested
    * Entered numbers when the name was requested e.g(12345678890)
    * Entered special characters when the name was requested e.g(,.<>/?\|;:@'[]{})
* Each time an invalid input was entered into the Name request I expected to see an Error message to say that name couldn't be entered and this is what I seen.

![Name Validation](/Assets/Documentation/name_valid.png)


* Given invalid inputs when asked for the User's Handicap:
    * Entered a value higher than 54
    * Entered a value lower than 1
* Both times I expected to see an Error messsage saying that it was an invalid data input:
    * Too high for values over 54
    * Too Low for values under 1

![Handicap Validation](/Assets/Documentation/handicap_valid.png)

* Invalid inputs were also given for Pitching Wedge distance:
    * Too high (any values over 170 yards)
    * Too low (any values under 90 yards)
* Both times I expected to see an Error messsage saying that it was an invalid data input:
    * Too high for values over 170
    * Too Low for values under 90

![Pitching Wedge Validation](/Assets/Documentation/pwedge_valid.png)

* Invalid inputs were also given for 6 Iron distance:
    * Too high (any values over 220 yards)
    * Too low (any values under 130 yards)
* Both times I expected to see an Error messsage saying that it was an invalid data input:
    * Too high for values over 220
    * Too Low for values under 130

![Six Iron Validation](/Assets/Documentation/six_iron_valid.png)

* Invalid inputs were also given for Driver distance:
    * Too high (any values over 350 yards)
    * Too low (any values under 190 yards)
* Both times I expected to see an Error messsage saying that it was an invalid data input:
    * Too high for values over 350
    * Too Low for values under 130

![Driver Distance Vaildation](/Assets/Documentation/driver_valid.png)

* I also done manual testing to make sure all the outcomes would be accurate for different combinations of inputs.

* I tested a difference of less than 56 yards between 6 iron and pitching wedge distances.
    * My expected result result was Cavity Backs

        ![Cavity test](/Assets/Documentation/cav_test.png)

* I tested a difference of more than 55 yards between 6 iron and pitching wedge distances but with the 6 iron distance less then 190.
    * My expected result was Combo Set

        ![Combo test](/Assets/Documentation/combo_test.png)

* I tested a difference of more than 55 yards between 6 iron and pitching wedge distances but with the 6 iron distance more then 190.
    * My expected result was Blades

        ![Blades test](/Assets/Documentation/blade_test.png)

* I done testing to make sure that there are different outcomes for shaft flex:

    * I tested with different Driver distances of:
        * Less than 213
        * Between 213 - 262
        * More then 262
    
    The reason these distances were tested is that they correspond to the different clubhead speeds in the function that chooses the flex of shaft for the user.
    
    * My expected result of distances less than 213 were Regular

        ![Regular test](/Assets/Documentation/reg_test.png) 

    * My expected result of distances between 213 and 262 was Stiff

        ![Stiff test](/Assets/Documentation/stiff_test.png)

    * My expected result of distances more than 262 was Extra-Stiff

        ![Extra test](/Assets/Documentation/extra_test.png)
    

