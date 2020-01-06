def translate(word):
    translation = ""
    for letter in word:
        if letter.upper() in "AEIOU":
            if letter.isupper():
                translation += "G"
            else:
                translation += "g"
        else:
            translation += letter
    return translation


word = input("Enter a phrase: ")
print(translate(word))
