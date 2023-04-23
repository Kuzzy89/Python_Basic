print("Wellcome ot my game qiuz! ")

playing = input("Do you want to play?" )

print(playing)
if playing != "yes":
    quit()
print("Okay! Let's play :) ")

answer = input("What does CPU stand for? ")
if answer == "central processing unit":
    print("Correct!")