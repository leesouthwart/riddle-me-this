import os
import json
from flask import Flask, render_template, request

app = Flask(__name__)

username = "lee"

#Writing the answers into the answer.json file

def write_to_file(filename, data):
    with open(filename, "a") as file:
        file.writelines(data)
    
def store_guess(username, guess):
    write_to_file("data/guesses.txt", "({0}) - {1}\n".format(username, guess))
    
def get_guesses():
    guesses = []
    with open("data/guesses.txt", "r") as guess_data:
        guesses = [row for row in guess_data if len(row.strip()) > 0]
    return guesses
        
        


@app.route("/", methods=["GET", "POST"])
def index():
    data = []
    with open("data/riddles.json", "r") as json_data:
        data = json.load(json_data)
    
    
    
    question_id = 0
   
    
    #Handle POST request
    if request.method == "POST":
        
        #get current question_id from the hidden form field
        question_id = int(request.form["question_id"])
        
        
        
        # user_guess is equal to the input the user gives. Using .lower to remove any capitalisation (all answers are exclusively lower case)
        user_guess = request.form["answer"].lower() 
 
        #if users guess is correct +1 to question id and go to the next riddle
        if data[question_id]["answer"] == user_guess:
            question_id += 1
        else:
            store_guess(username, user_guess + "\n")
            
    # if last question is answered correctly, return game over page
    if request.method == "POST":    
        
        if question_id > 8 and user_guess == "current":
            return render_template("game_over.html")
         
    
    # get_guesses has to be called after the post request otherwise it will show the previous answer. eg if you guess 'hello' and then guess 'world' on the second guess it will show 'hello'
    guesses = get_guesses()   
    
    
    return render_template("index.html", riddle_data=data, question_id=question_id, guesses=guesses)
    



app.run(host=os.getenv('IP'), port=int(os.getenv('PORT')), debug=True)