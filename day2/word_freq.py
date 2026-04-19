import argparse
import re
from collections import Counter
import jieba

parser = argparse.ArgumentParser()
parser.add_argument('--lang', default='en', choices=['en', 'zh'])
args = parser.parse_args()

with open('sample.txt', 'r', encoding='utf-8') as f:
    text = f.read()

if args.lang == 'en':
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text)
    words = text.split()
else:
    words = jieba.lcut(text)
    words = [w.strip() for w in words if w.strip() and not re.match(r'[^\w]', w)]

counter = Counter(words)
top10 = counter.most_common(10)

print(f"Top 10 词频 ({args.lang}):\n")
for word, count in top10:
    print(f"{word}: {count}")
