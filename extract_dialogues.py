import os
import re

input_path = os.path.join('donkeys to bald pate.txt')
output_path = os.path.join('dialogues.txt')

with open(input_path, 'r', encoding='UTF-8') as file:
    raw_text = file.read()
regex = r'"(.*?)"'
dialogue_raw = re.findall(regex, raw_text, re.DOTALL)
#quotes[]
#"'[^']*'" didnt work nicely
filtered = os.linesep.join([s for s in raw_text.splitlines() if s]).replace('\n', ' ').replace('\r', ' ') # process the string to remove special characters \n, \t, \s
irrelevant = [(m.start(), m.end()) for m in re.finditer('\*\*\*', filtered)] # process the string to remove all irrelevant text: header and footer
filtered = filtered[irrelevant[1][1]:irrelevant[2][0]]
indexes = [(m.start(0), m.end(0)) for m in re.finditer(r'"(.*?)"', filtered)] # find all the quotes, apply a regex to extract all sentences between "...", also collect the index
phrases = [filtered[first:last] for first, last in indexes]

words_between = [len(filtered[back[1]:front[0]].split()) for back, front in zip(indexes, indexes[1:])] # get the number of words between each phrase. Simply count words between end of last sentence, and begining of next one
maximum_distance_words = 20
# we have the sentences and number of words between them
with open(output_path, 'w', encoding='UTF-8') as output_file:
    for index, phrase in enumerate(phrases[:-1]):
        output_file.write(phrase)
        output_file.write('|' if words_between[index] <= maximum_distance_words else'\n')
    output_file.write(phrases[-1])

# reference:
# https://stackoverflow.com/questions/1140958/whats-a-quick-one-liner-to-remove-empty-lines-from-a-python-string
# https://stackoverflow.com/questions/34774126/re-finditer-returning-same-value-for-start-and-end-methods and https://www.pythontutorial.net/python-regex/python-regex-finditer/
# https://www.golinuxcloud.com/python-argparse/

# filepath = 'donkeys to bald pate.txt'


# regex = "'[^']*'"
# fix the regex to accurately get all quotes from the text file, because it also extracts weird sentences

# quotes_raw = re.findall(regex, raw_text)
# print(raw_text)
# print(quotes_raw)

# dialogues = []          # this should become a list of lists (each inner list being 1 dialogue)

#for i in range(len(quotes_raw)):
   # dialogue = []       # this should become a list of quotes that form one dialogue
   # while (re.search(quotes_raw[i+1], raw_text).start() - re.search(quotes_raw[i], raw_text).end()) < 20: #aaaa this does not work!!
      #  dialogue.append(i)
   # else:
       # dialogues.append(dialogue)

#for dialogue in dialogues:
#    print(dialogue)
# this is just to test whether it accurately forms the dialogues
# idk how to fix it if it doesn't

# write all the dialogues to a new .txt file, similar to the analyze_questions
# while (re.search(quotes_raw[i+1], raw_text).start() - re.search(quotes_raw[i], raw_text).end()) < 20:
# if the start index of the second quote minus the end index of the first quote is less than 20, it appends the first quote to the dialogue
# .end() and .start()



# for i in range(len(quotes_raw)):
#     dialogue = []
#     dialogue.append(quotes_raw[i])
#     if quotes_raw(i + 1) not more than 20 characters away:
#         dialogue.append(quotes_raw[i + 1])


# print(quotes_raw)
# print(raw_text)

