print("Welcome to Quiz Game")

user_input = input("Do you want to play? ")
if user_input.lower() != "yes":
    quit()

print("welcome to my game")
score = 0
#while True:
Quiz = input("what does cpu stand for? ")
if Quiz.lower() == "central processing unit":
        print("correct")
        score += 1
else:
        print("incorect")

Quiz = input("what does gpu stand for? ")
if Quiz.lower() == "graphics processing unit":
        print("correct")
score = 0
else:
        print("incorect")

Quiz = input("what does ram stand for? ")
if Quiz.lower() == "random access memory":
        print("correct")
        score += 1
else:
        print("incorect")

Quiz = input("what does rom stand for? ")
if Quiz.lower() == "read only memory":
        print("correct")
        score += 1
else:
        print("incorect")

Quiz = input("""what does hd stand for? 
    a.) hellodog
    b.) hard drive
    c.) hard disk  """)
if Quiz.lower() == "c":
        print("correct")
        score += 1
else:
        print("incorect")
print(f"You got {str(score/5*100)} %.")
print(f"You got {str(score)} out of 5 questions correct")
    #continue