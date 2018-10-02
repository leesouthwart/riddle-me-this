import os
import json
from flask import Flask, render_template, request, redirect
from collections import deque
import riddles

app = Flask(__name__)


            
        


# INDEX PAGE TO ENTER USERNAME

@app.route("/", methods=["GET", "POST"])
def index():
 
    
    #Username post request
    if request.method == "POST":
        riddles.write_to_file("data/users.txt", request.form["username"] + "\n")
        return redirect(request.form["username"])
        
    users = riddles.load_file("data/users.txt")
    
    
    return render_template("index.html", users=users)



# MAIN GAME PAGE

@app.route("/<username>", methods=["GET", "POST"])
def user(username):
    data = []
    with open("data/riddles.json", "r") as json_data:
        data = json.load(json_data)
    
    
    #initial question_id
    question_id = 0
    
    #initial fail_count
    score = 0
    
    
    
    #Handle POST request
    
    # handles home button request. Deletes users from current users and incorrect answers and redirects to the homepage
    if request.method == "POST":
        if request.form["button"] == "home":
                riddles.delete_user(username)
                return redirect("/")   
    
    
            
    #handles submit button request and logic for adding/removing score and storing incorrect guesses.
    if request.method == "POST":
        if request.form["button"] == "submit":
                #get current question_id from the hidden form field
                question_id = int(request.form["question_id"])
        
                #gets current fail count from the hidden form field
                score = int(request.form["score"])
        
        
                #user_guess is equal to the input the user gives. Using .lower to remove any capitalisation (all answers are exclusively lower case)
                user_guess = request.form["answer"].lower() 
 
                if riddles.is_answer_right(data[question_id], user_guess):
                    question_id += 1
                    score += 1
                else:
                    riddles.store_guess(username, user_guess + "\n")
                    score -= 1
                  
    
    # Handles skip button request. -1 from score and giving user the next riddle.
    if request.method == "POST":
        if request.form["button"] == "skip":
            #get current question_id from the hidden form field
            question_id = int(request.form["question_id"])
        
            #gets current fail count from the hidden form field
            
            
            score = int(request.form["score"])
            
            question_id += 1
            score -= 1
            
            #if last question is skipped
            if question_id > 9:
                 #stores score for use in highscores page
                riddles.store_score(username, score)
                #deletes user from active users and deletes their incorrect answers
                riddles.delete_user(username)
                return redirect ("/game_over")
            
    
    # Handles highscores button request
    if request.method == "POST":
        if request.form["button"] == "highscores":
               
                #deletes user from active users and deletes their incorrect answers to 
                #avoid people quitting early and still being logged as active
                riddles.delete_user(username)
                return redirect ("/game_over")        
     
    # if last question is answered correctly, return game over page
    if request.method == "POST":    
        if request.form["button"] == "submit":
            
            if question_id > 8 and user_guess == "current":
                
                #stores score for use in highscores page
                riddles.store_score(username, score)
                #deletes user from active users and deletes their incorrect answers
                riddles.delete_user(username)
                return redirect ("/game_over")
           
                 
          
    spliced_guesses = riddles.return_guesses()

    return render_template("maingame.html", riddle_data=data, question_id=question_id, guesses=spliced_guesses, score=score, username=username)
    

# GAME OVER PAGE
@app.route("/game_over")
def game_over():
    
    top_10_scores = riddles.get_scores("data/scores.txt")
    
    return render_template("game_over.html", scores=top_10_scores)



app.run(host=os.getenv('IP'), port=int(os.getenv('PORT')), debug=True)