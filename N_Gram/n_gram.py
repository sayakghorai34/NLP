from nltk.util import ngrams
from nltk.tokenize import word_tokenize, sent_tokenize
from collections import Counter
import numpy as np
from scipy.sparse import lil_matrix

def tokenize_text(text):
    tokens = word_tokenize(text)
    punctuations_to_remove = ",;:-'\"()[]{\\}"
    tokens_without_punctuation = [token for token in tokens if token not in punctuations_to_remove]
    tokens_with_special_tokens = [token.lower() if token not in ['.', '!', '?'] else token for token in tokens_without_punctuation]
    return tokens_with_special_tokens

def preprocess_text(text):
    sentences = sent_tokenize(text)
    preprocessed_sentences = []
    for sentence in sentences:
        tokens = tokenize_text(sentence)
        preprocessed_sentences.append(tokens)
    return preprocessed_sentences

def extract_ngram_frequencies(corpus):
    unigram_freq = Counter()
    bigram_freq = Counter()

    for sentence in corpus:
        unigram_freq.update(sentence)
        bigram_freq.update(ngrams(sentence, 2))

    return unigram_freq, bigram_freq

def calculate_probabilities(unigram_freq, bigram_freq, total_unigrams, total_bigrams):
    unigram_probabilities = {word: (count / total_unigrams) for word, count in unigram_freq.items()}
    bigram_probabilities = {bigram: (count / unigram_freq[bigram[0]]) for bigram, count in bigram_freq.items()}

    return unigram_probabilities, bigram_probabilities

train_sentence = "Hello There! How are You? I am fine. How about you? I am also fine. Thank you!"
test_sentence = "How are you doing today?"

preprocessed_train_corpus = preprocess_text(train_sentence)
preprocessed_test_tokens = tokenize_text(test_sentence)

train_unigram_freq, train_bigram_freq = extract_ngram_frequencies(preprocessed_train_corpus)

train_total_unigrams = sum(train_unigram_freq.values())
train_total_bigrams = sum(train_bigram_freq.values())

train_unigram_probabilities, train_bigram_probabilities = calculate_probabilities(train_unigram_freq, train_bigram_freq, train_total_unigrams, train_total_bigrams)

print("Train Unigram Probabilities:")
print("Word\t\tCount\t\tProbability")
for word, count in sorted(train_unigram_freq.items(), key=lambda x: x[1], reverse=True):
    print(f"{word}\t\t{count}\t\t{train_unigram_probabilities[word]:.4f}")

print("\nTrain Bigram Probabilities:")
print("Bigram\t\tCount\t\tProbability")
for bigram, count in sorted(train_bigram_freq.items(), key=lambda x: x[1], reverse=True):
    bigram_str = ' '.join(bigram)
    print(f"{bigram_str}\t\t{count}\t\t{train_bigram_probabilities[bigram]:.4f}")

# Represent counts and probabilities as sparse matrices
vocab_size = len(train_unigram_freq)
train_unigram_count_matrix = lil_matrix((1, vocab_size), dtype=np.int32)
train_unigram_prob_matrix = lil_matrix((1, vocab_size), dtype=np.float64)

for word, count in train_unigram_freq.items():
    idx = list(train_unigram_freq.keys()).index(word)
    train_unigram_count_matrix[0, idx] = count
    train_unigram_prob_matrix[0, idx] = train_unigram_probabilities[word]

print("\nSparse Train Unigram Count Matrix:")
print(train_unigram_count_matrix)

print("\nSparse Train Unigram Probability Matrix:")
print(train_unigram_prob_matrix)

# Calculate bigram probabilities for test sentence
test_bigrams = list(ngrams(preprocessed_test_tokens, 2))
test_bigram_probabilities = {}
for bigram in test_bigrams:
    bigram_str = ' '.join(bigram)
    if bigram in train_bigram_probabilities:
        test_bigram_probabilities[bigram_str] = train_bigram_probabilities[bigram]
    else:
        test_bigram_probabilities[bigram_str] = 0.0

print("\nTest Bigram Probabilities:")
print("Bigram\t\tProbability")
for bigram, prob in test_bigram_probabilities.items():
    print(f"{bigram}\t\t{prob:.4f}")
