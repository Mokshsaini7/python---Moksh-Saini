# import the random module 
import random

# 2 - create subjects
subjects = [
    "Shahrukh khan ",
    "Virat kohli ",
    "Nirmala Sitaraman ",
    "A Group of Monkey ",
    "Prime Minister  Modi ",
    "Auto Rickshaw Driver from Delhi "
    "Goldy brar ",
    "Sidhu moose wala "
]

actions =[
    " launches ",
    " cancels ",
    " dances with ",
    " eats ",
    "  celebrates ",
    " order ",
    " declare war on ",
    " Took responsiblity of "
]

places_or_things =[
    " In Red Fort",
    " In Mumbai local train",
    " A plate of samsosa",
    " At ganga ghat",
    " in Banaras",
    " During IPL match",
    " Inside Parliament",
    " At India gate"
]

# Start the headline generation loop
while True:
    subject = random.choice(subjects)
    action = random.choice(actions)
    places_or_thing = random.choice(places_or_things)

    headline = (f"BREAKING NEWS: {subject} {action}{places_or_thing}")

    print("\n" + headline)

    user_input =input("\n Do you want another headline? (Yes/no)").strip().lower()
    if user_input == "no":
        break

    #print goodbye message
    print("\n Thanks  for using the Fake News Headlines Generator .have a fun day")

    