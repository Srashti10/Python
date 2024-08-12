# Exercise 3 (Kaun Banega Crorepati)
# Create a program capable of displaying questions to the user like KBC.
# Use list data type to store questions and their correct answers.
# Display the final amount the person is taking home after playing the game.
# My Solution
print("Welcome to Kaun Banega Crorepati")
question = [" What comes after 50?"]
answers = [51,52,53,54]
print(question)
print("Your options are:","\n",answers[0] ,"\n",answers[1],"\n",answers[2],"\n",answers[3])
print("Entter your answer:")
yourAns = int(input())
if yourAns == answers[0]:
    print("Correct Answer! You win Rs.1000")
else:
    print("Sorry, Wrong Answer.")

# I will complete this after some time.



        
