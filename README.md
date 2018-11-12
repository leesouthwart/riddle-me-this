# Riddle Me This

Riddle Me This is a text based riddle game, developed in python using the Flask microframework.
Users select a username, and are then shown a riddle. If the riddle is answered correctly they are 
moved on to the next riddle, until all 10 have been answered. Their score is tracked and displayed on a highscores page.
Users also have the ability to get hints for the riddle, and can skip the question entirely if needed. The design is simple
to match the simplicity of the game. I felt no need for anything other than a simple style for the page, so I used a bootstrap theme from startbootstrap.com. The attention is drawn straight
to the riddles which is ideal. The design is mobile responsive.

Multiple users can play the game at the same time in different browsers with no problems.

The game can be found deployed at : https://riddle-me-this-app.herokuapp.com/

## UX

This application has been created for people who want to play a simple, basic riddle game on their computer or phone.

## Features

* Username Input - Allows the user to pick the name they will use throughout the game. This name is also what will be stored alongside the users score on the highscores table.
* Riddle Display - The maingame.html pulls the riddle from riddles.json and displays it using flask templating for the user to read.
* User guess box - Text box for users to input their guesses. When submitted, whatever text is in the textbox will be saved to a variable "user_guess" and checked against the answer that is saved in the riddles.json file.
* Incorrect Answers - If the user_guess variable doesnt match one of the answers to the riddle, it is saved in a text file "guesses.txt" and displayed on the page using flask templating by running a for loop over all lines in the file. It is also flashed under the submit box.
* Highscores - After a user has answered all 10 riddles their score is saved and displayed on the top 10 highscores


## Technologies Used

* Python/flask - The project is coded in python using the flask microframework
* HTML5
* CSS - For the basic styling. 
* Bootstrap library - Used for the default styles and the responsive grid system. [Bootstrap link](https://getbootstrap.com/)
* Heroku - For application deployment

## Testing

The application has several automated tests found in the test_riddles.py file. They test that the main components of the project work
as intended

* test_write_username - Tests that the username inputted is being written to the "users.txt" file when called.
* test_store_score - Tests that the users username and score is stored in the "scores.txt" file when called.
* test_store_guess - Tests that a users input is stored in the "guesses.txt" file when the function is called.
* test_is_answer_right - Tests that the main logic for comparing user input to the stored answer works.
* test_get_scores - Tests that the get_scores function only returns 10 scores. This function is used for the highscores page so checking that it only returns 10 scores is essential.
* test_return_guesses - Tests that the return_guesses function only returns 5 incorrect answers to display on the page as intended. 

I also performed manual tests on certain functionality of the site to make sure it performed as expected. This includes having several (5+) people
play the game at the same time.

##### Game button testing

* Home button - Created a user and inputted some fake guesses, and then ensured that clicking the home button removed both the user and the incorrect guesses from the relevant files.
* Highscores - Created a user, and tested that clicking the highscores button deleted the user and redirected to the highscores page as intended.
* Hint button - Tests that the button hides/unhides the hint as intended, and that the hint shown is the correct hint.
* Skip button - Tested that the skip button sends the user to the next riddle and decreases their score by 1. Also tested if the last riddle is skipped, the user is redirected to the highscores.
* Submit button - Tested that the post request is sent properly which calls all the functions to check the answer and add/decrease score.


## Credit

* The bootstrap theme used for the styling of this application can be found at https://startbootstrap.com/template-overviews/freelancer/

## Deployment

This project was deployed on heroku. The heroku config vars are ;

* IP: 0.0.0.0
* PORT: 5000

The deployed heroku version differs from the version stored on github in only 1 way, the debug mode is turned off
in the run.py of the deployed version. Debug mode is turned on in the development mode. To run locally, install the requirements found in 
requirements.txt and run the run.py by inputting "python3 run.py" into  the ide terminal.


