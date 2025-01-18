#write a program that contains a funciton game() that returns a score and open a file named hi-score.txt, compare the score with its contents and if the score is greater than the contents, write the score to the file

import random

# def game():
#     return random.randint(1, 6)

# score = str(game())
# print(score)


# with open("/home/dushyant_new/python/file_input_output/problems/hi-score.txt") as f:
#     contents = f.read()
#     print(contents)
    
#     if score > contents:
#         with open("/home/dushyant_new/python/file_input_output/problems/hi-score.txt", "w") as f:
#             f.write(score) 
            
            
#another way using only function

def game():
    print("you are playing a game..")
    score = random.randint(1, 10)
    
    with open("/home/dushyant_new/python/file_input_output/problems/hi-score.txt") as f:
        highscore = f.read()
        if(highscore != ""):
            highscore = int(highscore) #read() always returns a string, so we need to convert it to int to compare it with the score
        else:
            highscore = 0
    
    print(f"your score : {score}")
    if score > highscore:
        with open("/home/dushyant_new/python/file_input_output/problems/hi-score.txt", "w") as f:
            f.write(str(score)) # after comapring again convert the score to string to write it there
        
game()