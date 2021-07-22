USER = ["bob", "ann", "mike", "liz"]
PASSWORD = ["123", "pass123", "password123", "pass123"]
separator = "=" * 55
separator_1 = "-" * 55
separator_3 = "_._" * 9
total = []
cleared_words = []
words_length = dict()
cleared_words_1 = []
occurrence = []

users = dict(zip(USER, PASSWORD))

username = input("Enter your username: ")
password = input("Enter your password: ")

if users.get(username) == password:
    print(separator, "Welcome to the APP!".center(len(separator)),
          separator, sep="\n")
    print(f"{username.title()} we have 3 texts to be analyzed."
          .center(len(separator)), separator_1, sep="\n")
else:
    print(separator_1, "INCORRECT USERNAME OR PASSWORD!"
          .center(len(separator)), separator_1, sep="\n")
    quit()

TEXTS = ['''
Situated about 10 miles west of Kemmerer, 
Fossil Butte is a ruggedly impressive 
topographic feature that rises sharply 
some 1000 feet above Twin Creek Valley 
to an elevation of more than 7500 feet 
above sea level. The butte is located just 
north of US 30N and the Union Pacific Railroad, 
which traverse the valley. ''',
         '''
At the base of Fossil Butte are the bright 
red, purple, yellow and gray beds of the Wasatch 
Formation. Eroded portions of these horizontal 
beds slope gradually upward from the valley floor 
and steepen abruptly. Overlying them and extending 
to the top of the butte are the much steeper 
buff-to-white beds of the Green River Formation, 
which are about 300 feet thick.''',
         '''
The monument contains 8198 acres and protects 
a portion of the largest deposit of freshwater fish 
fossils in the world. The richest fossil fish deposits 
are found in multiple limestone layers, which lie some 
100 feet below the top of the butte. The fossils 
represent several varieties of perch, as well as 
other freshwater genera and herring similar to those 
in modern oceans. Other fish such as paddlefish, 
garpike and stingray are also present.''']

choice = input("Enter a number btw. 1 and 3 to select: ")
assignment = {"words": 0, "title": 0, "big": 0, "small": 0, "number": 0}

if "1" in choice or "2" in choice or "3" in choice:
    new_choice_1 = int(choice)
    new_choice = TEXTS[new_choice_1 - 1]
else:
    print(separator_1, "INCORRECT CHOICE!"
          .center(len(separator)), separator_1, sep="\n")
    quit()

for word in new_choice.split():
    without = word.strip(",.:;_-")
    cleared_words.append(without)
    cleared_words_1.append(len(without))
    cleared_words_1.sort(reverse=False)

for word in cleared_words:
    if not word.isspace():
        assignment["words"] += 1
    if word.istitle():
        assignment["title"] += 1
    if word.isupper() and word.isalpha():
        assignment["big"] += 1
    if not word.istitle():
        if word.islower():
            assignment["small"] += 1
    if word.isnumeric():
        assignment["number"] += 1
    if word.isnumeric():
        total.append(int(word))

print(separator_1, f"Your choice is number: {choice}.", separator_1, sep="\n")
print(f"There are {str(assignment['words'])} words in the selected text.")
print(f"There are {str(assignment['title'])} titlecase words.")
print(f"There are {str(assignment['big'])} uppercase words.")
print(f"There are {str(assignment['small'])} lowercase words.")
print(f"There are {int(assignment['number'])} numeric strings.")
print(f"The sum of all numbers {sum(total)}.")
print(separator_1, separator_3, sep="\n")
print(f"|LEN|    OCCURENCES     |NR|")
print(separator_3)

for word in cleared_words_1:
    if word not in words_length:
        words_length[word] = 1
    else:
        words_length[word] = words_length[word] + 1
sorted_occurrence = words_length.values()

for word in words_length:
    if words_length[word] in sorted_occurrence:
        occurrence.append((words_length[word], word))

for index, result in enumerate(occurrence, 1):
    print(f"|{result[1]: ^2}.|{'#' * result[0]: <18} |{result[0]: ^2}|",
          separator_3, sep="\n")