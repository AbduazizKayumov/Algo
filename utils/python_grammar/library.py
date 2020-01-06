import random

week_days = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]

def randomWeekday():
    return week_days[random.randint(0,6)]

def roll_dice(num):
    return random.randint(1,num)