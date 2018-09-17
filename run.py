import os
import json
from flask import Flask, render_template, request, redirect

app = Flask(__name__)




#general write to file func
def write_to_file(filename, data):
    with open(filename, "a") as file:
        file.writelines(data)
    

# write guesses to the guesses.txt file to be used later
def store_guess(username, guess):
    write_to_file("data/guesses.txt", "({0}) - {1}\n".format(username, guess))
    

# load files and return the data to a variable
def load_file(filename):
    with open(filename, "r") as data:
        return [row for row in data if len(row.strip()) > 0]
            
        


# INDEX PAGE TO ENTER USERNAME

@app.route("/", methods=["GET", "POST"])
def index():
    """
    Index page with username input
    """
    
    #Username post request
    if request.method == "POST":
        write_to_file("data/users.txt", request.form["username"] + "\n")
        return redirect(request.form["username"])
        
    users = load_file("data/users.txt")
    
    
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
    if request.method == "POST":
        
        #get current question_id from the hidden form field
        question_id = int(request.form["question_id"])
        
        #gets current fail count from the hidden form field
        score = int(request.form["score"])
        
        
        #user_guess is equal to the input the user gives. Using .lower to remove any capitalisation (all answers are exclusively lower case)
        user_guess = request.form["answer"].lower() 
 
        #if users guess is correct +1 to question id and go to the next riddle
        if data[question_id]["answer"] == user_guess:
            question_id += 1
            score += 1
        else:
            store_guess(username, user_guess + "\n")
            score -= 1
            
         
    
            
            
    # if last question is answered correctly, return game over page
    if request.method == "POST":    
        
        if question_id > 8 and user_guess == "current":
            return render_template("game_over.html")
         
    
    # get_guesses has to be called after the post request otherwise it will show the previous answer. eg if you guess 'hello' and then guess 'world' on the second guess it will show 'hello'
    guesses = load_file("data/guesses.txt")   
    
    
    
    
    return render_template("maingame.html", riddle_data=data, question_id=question_id, guesses=guesses, score=score)
    



app.run(host=os.getenv('IP'), port=int(os.getenv('PORT')), debug=True)