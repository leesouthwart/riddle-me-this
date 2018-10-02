from collections import deque


#general write to file func
def write_to_file(filename, data):
    with open(filename, "a") as file:
        file.writelines(data)
           
        
        
# write guesses to the guesses.txt file
def store_guess(username, guess):
    write_to_file("data/guesses.txt", "{0} - {1}\n".format(username, guess))
    
# write scores to the scores.txt file
def store_score(username, score):
    write_to_file("data/scores.txt", "{0}, {1}\n".format(username, score))        



# load files and return the data to a variable
def load_file(filename):
    with open(filename, "r") as data:
        return [row for row in data if len(row.strip()) > 0]


#deletes user from users.txt and deletes their incorrect guesses from guesses.txt
def delete_user(username):
    with open("data/users.txt", "r+") as user_data:
        users = user_data.readlines()
        user_data.seek(0)
        for line in users:
            if line != username + "\n":
                user_data.write(line)
        user_data.truncate()
        user_data.close()
    
    with open("data/guesses.txt", "r+") as data:
        f = data.readlines()
        data.seek(0)
        for line in f:
            if username not in line:
                data.write(line)
        data.truncate()
        data.close()



#open guesses file and return 5 most recent incorrect guesses to display on page
def return_guesses():
    
    # loading the guesses file has to be called after the post request otherwise it will show the previous answer. eg if you guess 'hello' and then guess 'world' on the second guess it will show 'hello'
    guesses = load_file("data/guesses.txt")
    # uses deque to return the last 5 guesses
    spliced_guesses = deque(guesses, 5)
    return spliced_guesses


#logic for checking answer
def is_answer_right(question, user_guess):
    #if users guess is correct +1 to question id and go to the next riddle
    if user_guess in question["answer"]:
        return True
    else:
        return False
        

# open scores.txt and get the 10 highest scores
def get_scores(data):
    scores = []
    with open(data) as f:
        for line in f:
            name, score = line.split(',')
            score = int(score)
            scores.append((name, score))
    
    #sorts the scores by numerical value, highest first
    scores.sort(key=lambda s: s[1], reverse=True) 
    
    #return the top 10 scores in order
    top_10_scores = scores[:10]
    return top_10_scores