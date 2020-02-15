lucky_numbers = [4, 8, 12, 14, 18, 21]
friends = ["John", "Jim", "Jim", "Sofia", "Oscar", "Mike"]

#friends.extend(lucky_numbers)  # append another list
friends.append("Korea")  # add element
friends.pop()  # remove the last element
friends.index("Jim")
friends.count("Jim")

friends.sort()
friends.reverse()
print(friends)

friends2 = friends.copy()