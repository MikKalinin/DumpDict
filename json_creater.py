import json

t = [i.replace('\n', '') for i in open('words.txt', 'r', encoding='utf-8').readlines()]

string = {'words': []}

for i in range(1, len(t)+1):
    data = t[i-1]
    string['words'].append({'index': i, 'word': data})

print(string)

with open('word_dict.json', 'w', encoding='utf-8') as f:
    json.dump(string, f, ensure_ascii=False)

