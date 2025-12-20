import math
import re
import os
from collections import Counter

POSTS_DIR = "../_posts"
TOP_K = 5

STOPWORDS = {
    "the", "and", "to", "of", "a", "in", "for", "on", "with",
    "is", "it", "this", "that", "as", "by", "an", "i", "no", "awesome", "web", "would", "new"
}

def tokenize(text):
  text = text.lower()
  text = re.sub(r"[^a-z0-9\s]", " ", text)
  return [t for t in text.split() if t not in STOPWORDS]

def parse_post(path):
    with open(path, "r", encoding="utf-8") as f:
        raw = f.read()

    if not raw.startswith("---"):
        return ""

    _, fm, body = raw.split("---", 2)

    # Extract title manually (no YAML lib)
    title_match = re.search(r"title:\s*(.+)", fm)
    title = title_match.group(1) if title_match else ""

    return title, body

documents = []
paths = []

for file in os.listdir(POSTS_DIR):
    if not file.endswith(".md"):
        continue

    parsed = parse_post(os.path.join(POSTS_DIR, file))
    if not parsed:
        continue

    title, body = parsed

    # Weight title higher
    tokens = tokenize(title) * 3 + tokenize(body)

    documents.append(tokens)
    paths.append(file)

N = len(documents)

# -----------------------
# Build vocabulary
# -----------------------

vocab = sorted(set(word for doc in documents for word in doc))

# -----------------------
# Compute IDF
# -----------------------

idf = {}
for word in vocab:
    df = sum(1 for doc in documents if word in doc)
    idf[word] = math.log((N + 1) / (df + 1)) + 1

# -----------------------
# Extract tags per post
# -----------------------

for tokens, filename in zip(documents, paths):
    tf = Counter(tokens)
    total = len(tokens)

    scores = {}
    for word, count in tf.items():
        scores[word] = (count / total) * idf[word]

    top = sorted(scores.items(), key=lambda x: x[1], reverse=True)[:TOP_K]

    print(f"\n{filename}")
    print("Suggested tags:")
    for word, score in top:
        print(f"  {word}")

