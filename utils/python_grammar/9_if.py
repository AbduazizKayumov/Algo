is_male = False
is_tall = True

if is_male or is_tall:
    print("You are a male")
else:
    print("You are a female")

if is_male and is_tall:
    print("You are a tall male")
elif is_male:
    print("You are a male")
elif is_tall:
    print("You are a tall female")
else:
    print("You are e female")