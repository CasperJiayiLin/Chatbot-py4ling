import os
import re

input_path = os.path.join('Gem of Poetry.txt')
output_path = os.path.join('questions.txt')
with open(input_path, 'r', encoding='UTF-8') as file:
    raw_text = file.read()
regex = r'\s[A-Za-z\s]*\?'
questions_raw = re.findall(regex, raw_text, re.DOTALL)
print(questions_raw)
questions = []
for question in questions_raw:
    questions.append(question)

# filtered = os.linesep.join([s for s in questions.strip().splitlines(True) if s.strip()])
# print(filtered) wanted to see if it worked on questions

wh_words = ['what','when', 'where', 'how', 'why']
auxiliaries = ['is', 'were', 'are', 'did', 'do', 'does', 'have', 'has', 'had'
               "isn't", "weren't", "aren't", "didn't", "don't", "doesn't", "haven't", "hasn't", "hadn't"]
def both(list1, list2):
    """Takes two lists and returns True if any element appears in both."""
    for element in list1:
        if element in list2:
            return True
    return False

with open(output_path, 'w', encoding='UTF-8') as output_file:
    for question in questions:
        if question.lower().split()[0] in wh_words:
            category = 'wh-fronted:\t'
        elif both(question.lower().split(), wh_words):
            category = 'wh-in-situ:\t'
        elif question.lower().split()[0] in auxiliaries:
            category = 'polar:\t'
        else:
            category = 'declarative:\t'
        output_file.write(category)
        output_file.write(question)
        output_file.write('\n')
