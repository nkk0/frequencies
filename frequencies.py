from collections import Counter

import json
import nltk
import numpy as np


def get_normalized_frequencies(raw_text):
    tokens = nltk.word_tokenize(raw_text)
    text = nltk.Text(tokens)
    freq_dist = nltk.FreqDist(text)

    words = list(zip(*freq_dist.most_common()))[0]
    arr = np.array(list(zip(*freq_dist.most_common()))[1])
    normalized = list(arr / len(tokens))

    words_normalized_dict = dict(list(zip(words, normalized)))
    return words_normalized_dict

def calculate_rmse(raw_corpus, raw_text):
    corpus = get_normalized_frequencies(raw_corpus)
    text = get_normalized_frequencies(raw_text)

    # Subtract the text values from the corpus values by key
    values = {key: corpus[key] - text.get(key, 0) for key in corpus.keys()}

    values = np.array(list(values.values()))
    values = np.square(values)
    mse = values.mean()
    rmse = np.sqrt(mse)
    import ipdb; ipdb.set_trace()

if __name__ == '__main__':
    with open('articles-1.json', 'r') as f:
        data = json.load(f)

    articles = ''
    for item in data:
        articles += item['text']
        articles += ' '
    articles = articles.lower()
    articles = articles.replace('\n', ' ')

    with open('test_set.txt', 'r') as f:
        test_text = f.read()
    test_text = test_text.replace('\n', ' ')

    calculate_rmse(articles, test_text)

