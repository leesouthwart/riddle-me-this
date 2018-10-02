import unittest
import riddles



class TestRiddles(unittest.TestCase):

    
    #test if write_username file writes the input to a file.
    def test_write_username(self):
        
        username = "Test Username1234"
        riddles.write_to_file("data/users.txt", username + "\n")
        content = open("data/users.txt").read()
        
        self.assertIn("Test Username1234", content)
        
        #delete test username after use.
        with open("data/users.txt", "r+") as users:
            user = users.readlines()
            users.seek(0)
            for line in user:
                if line != "Test Username1234" + "\n":
                    users.write(line)
                users.truncate()
                users.close()
        
        
        
    #test that score and username is stored properly when store_score is called
    def test_store_score(self):
        
        username = "Test Username"
        score = 5
        
        riddles.store_score(username, score)
        content = open("data/scores.txt").read()
        
        self.assertIn("{0}, {1}".format(username,score), content)
            
        #delete test username from scores.txt file after use
        with open("data/scores.txt", "r+") as user_data:
            users = user_data.readlines()
            user_data.seek(0)
            for line in users:
                if line != "Test Username, 5" + "\n":
                    user_data.write(line)
            user_data.truncate()
            user_data.close()
        
        
    
    #test that guess is stored properly when store_guess is called
    def test_store_guess(self):
        
        username = "Test Username"
        guess = "Test guess"
        
        riddles.store_guess(username, guess)
        content = open("data/guesses.txt").read()
        
        self.assertIn("{0} - {1}\n".format(username, guess), content)
        
        #delete test guesses from guesses.txt file after use
        with open("data/guesses.txt", "r+") as guess_data:
            guess = guess_data.readlines()
            guess_data.seek(0)
            for line in guess:
                if line != "Test Username - Test guess" + "\n":
                    guess_data.write(line)
            guess_data.truncate()
            guess_data.close()
    
    
    
    
    #test if the logic for checking if the answer is correct works
    def test_is_answer_right(self):

        question = {
            "riddle": "Question1",
            "answer": ["Answer1"],
            "hint": "The hint."
        }
        
        user_answer = "wrong answer"
        
        self.assertEqual(riddles.is_answer_right(question, user_answer), False)
        
        user_answer = "Answer1"
        
        self.assertEqual(riddles.is_answer_right(question, user_answer), True)
        
     
     
    #check that only top 10 scores are being displayed
    def test_get_scores(self):
        
        data = "data/scores.txt"
        scores = riddles.get_scores("data/scores.txt")
        
        print(scores)
        self.assertTrue(len(scores) <= 10)

    #check return_guesses function returns only 5 or less incorrect answers
    def test_return_guesses(self):
        
        
        spliced_guesses = riddles.return_guesses()
        
        
        self.assertTrue(len(spliced_guesses) <= 5)
        print("expected <= 5, got", len(spliced_guesses))



if __name__ == "__main__":
    unittest.main()