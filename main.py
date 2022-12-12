score = 0

# Question 1
answer1 = input ("What is the best university for computer science in Canada?\n a. University of Alberta\n b. University of British Colombia\n c. University of Toronto\n d. McGill University \nAnswer: ") 
if answer1 == "c" or answer1 == "University of Toronto":
  score += 1 
  print("Correct!")
  print("Score: ", score)
  print("\n")
else:
  print("Incorrect! The answer is University of Toronto.")
  print("Score: ", score)
  print("\n")
  
# Question 2
answer2 = input ("What is the fourth colour in the rainbow?\n a. red \n b. blue \n c. purple \n d. green \nAnswer: ") 
if answer2 == "d" or answer2 == "green":
  score += 1 
  print("Correct!")
  print("Score: ", score)
  print("\n")
else:
  print("Incorrect! The answer is green.")
  print("Score: ", score)
  print("\n")

# Question 3
answer3 = input ("Who owns Tesla? \n a. Elon Musk \n b. Jim Watson \n c. Donald Trump \n d. Tim Cook \nAnswer: ") 
if answer3 == "a" or answer3 == "Elon Musk":
  score += 1 
  print("Correct!")
  print("Score: ", score)
  print("\n")
else:
  print("Incorrect! The answer is Elon Musk.")
  print("Score: ", score)
  print("\n")