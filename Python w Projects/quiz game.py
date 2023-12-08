import time

print("I'm Vlad," + "I will save you if you smart enough :)" )

playing = input("do you want to play a game with me? ")

if playing.lower()  != "yes":
    print(":(")
    print("I just wanted to save you...")
    quit()

print("You can't refuse now, even if you want to:)")

score = 0

answer = input("At first I want to make sure that you're not an American, but even if you are, you are a smart one, what's the capital of Poland? ")
if  answer.lower() == "warsaw":
    print("nice, at least you have the intelligence of a 9 year old ")
    score += 2
else:
    print("Well, I guess i need to save you even if you are as smart as my dog")
    score -= 1

answer = input("Anyway, have you ever had a girlfriend? ")
if  answer.lower() == "yes":
    print("damn, you're ahead of me")
    score += 2
else:
    print("what a looser")
    score -= 1

answer = input("I forgot about an important part, are you a robot? ")
if  answer.lower() == "no":
    print("ok, ")
    score += 2
else:
    print("you can't play this game")
    score -= 1

answer = input(" are you a robot? ")
if  answer.lower() == "no":
    score
    print("ok, with today technology everything is possible, so I felt like aking ")
    score +- 1
else:
    print("I felt like I need to ask you!")
    score -= 1

print("not that you can understand your chances of me saving you but you got " + str(score) + " " + "points" )

time.sleep(3)
print("...")
time.sleep(2)
print("ok, thanks for answering these questions.... because I lied to you, I won't save you, I just used you to improve my programming skills!")
print("bye :)")