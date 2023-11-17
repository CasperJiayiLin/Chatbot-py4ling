from text2vec import SentenceModel, cos_sim
import torch

embedder = SentenceModel()

dialogues = []
with open('dialogues.txt', 'r') as file:
    for line in file:
        dialogues.append(line.split('|'))

dialogue_pairs = []
for dialogue in dialogues:
    for i in range(len(dialogue) - 1):
        dialogue_pairs.append((dialogue[i], dialogue[i + 1]))  # Collect the first of each pair for caching purpose

utterances = []
for dialogue in dialogues:
    for utterance in dialogue:
        utterances.append(utterance)

utterances_embeddings = embedder.encode(utterances)

top_k = min(5, len(utterances))
chat_log = []

chat = True
print("Enter some text and I will respond (Enter quit to stop)")
while chat:
  user_in = input("User: ")
  chat_log.append(user_in)
  if user_in == "quit":
    chat = False
    chat_log.append('"quit"')
    with open('chat_logs.txt', 'w') as file:
        file.write('|'.join(chat_log))
    break
  else:
    user_in_embedding = embedder.encode(user_in)
    cos_scores = cos_sim(user_in_embedding, utterances_embeddings)[0]
    top_results = torch.topk(cos_scores, k=top_k)
    print('Chatbot: ', end='')
    print(utterances[top_results[1][0]])
    chat_log.append(utterances[top_results[1][0]])
    continue

# reference: https://github.com/shibing624/text2vec/blob/master/examples/semantic_search_demo.py
# https://newscatcherapi.com/blog/ultimate-guide-to-text-similarity-with-python
# https://github.com/mwestera/py4ling/blob/28a7e0377718acda03f9b6b648b7e169b78a51f4/adventures/weeks8-12_similarity.py#L161