print("Welcome to THE QUIZ")

playing = input("Do you want to play? ")

if playing.lower() !="yes": 
    quit()

print("Okay get your brain ready! :D")
score = 0

answer = input("Who is the Father of computer? ") 
if answer.lower() == "charles babbage" :
    print ("Correct! ✅✅")
    score += 1
else: 
    print("Wrong ❌❌")
    
answer = input("What is the capital of Nepal? ") 
if answer.lower() == "kathmandu" :
    print ("Correct! ✅✅")
    score += 1
else: 
    print("Wrong ❌❌")

answer = input("What is the full form of CPU? ") 
if answer.lower() == "central processing unit" :
    print ("Correct! ✅✅")
    score += 1
else: 
    print("Wrong ❌❌")

answer = input("What are the tiny microscopic boxes on your computer/mobile screen? ") 
if answer.lower() == "pixels" :
    print ("Correct! ✅✅")
    score += 1
else: 
    print("Wrong ❌❌")

print("You got " + str(score) + " questions correct")
print("You got " + str((score/4) * 100 ) + "%")