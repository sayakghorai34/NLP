
#Words stripping out punctuations
def CountWordsPunctuations(text):
    # Dictionaries to Store individual words and punctuation
    wordDict = {}
    punctuationDict = {}
    wordArr = text.split()
    # Look into each word and remove the trailing punctuation (ex: Hello, -> Hello)
    for w in wordArr:
        # get rid of punctuations from leading and trailing
        w = w.strip(".,!?;:-'\"()[]{\}").lower()
        # Update word frequency dictionary
        wordDict[w] = wordDict.get(w, 0) + 1

    # Now look into each character and count the punctuations
    for char in text:
        # Check for punctuation character
        if char in ".,!?;:-'\"()[]{\}":
            # Update punctuation frequency dictionary
            punctuationDict[char] = punctuationDict.get(char, 0) + 1

    return wordDict, punctuationDict



#words with punctuations. in that case, same words with different punctuations will be counted as different words
#ex: Hello, Hello! Hello? Hello. Hello; Hello: Hello' Hello" Hello( Hello) Hello[ Hello] Hello{ Hello}
def CountWordsNoPunctuations(text):
    # Dictionaries to Store individual words and punctuations
    wordDict = {}
    punctuationDict = {}
    wordArr = text.split()
    # Look into each word and remove the trailing punctuation (ex: Hello, -> Hello)
    for w in wordArr:
        # get rid of punctuations from leading and trailing
        w = w.lower()
        # Update word frequency dictionary
        wordDict[w] = wordDict.get(w, 0) + 1

    # Now look into each character and count the punctuations
    for char in text:
        # Check for punctuation character
        if char in ".,!?;:-'\"()[]{\}":
            # Update punctuation frequency dictionary
            punctuationDict[char] = punctuationDict.get(char, 0) + 1

    return wordDict, punctuationDict

#Test the code

input_text = open('input.txt', 'r').read()

#stripping out punctuations. Ex: 'Hello', 'Hello!' both will be 'hello' and count as same word
wordDict1, punctuationDict1 = CountWordsPunctuations(input_text)
wordDict1 = {k:v for k, v in sorted(wordDict1.items(), key=lambda x: x[1], reverse=True)}
punctuationDict1 = {k:v for k, v in sorted(punctuationDict1.items(), key=lambda x: x[1], reverse=True)}


#with punctuation. Ex: 'Hello', 'Hello!' both will be counted as different words
wordDict2, punctuationDict2 = CountWordsNoPunctuations(input_text)
wordDict2 = {k:v for k, v in sorted(wordDict2.items(), key=lambda x: x[1], reverse=True)}
punctuationDict2 = {k:v for k, v in sorted(punctuationDict2.items(), key=lambda x: x[1], reverse=True)}
print("Without punctuation:")
print("Word  ==»  Freq:")
for w, c in wordDict1.items():
    print(f" {w}  ==»  {c}")

print("\nPunctuation ==» Freq:")
for p, c in punctuationDict1.items():
    print(f" {p}  ==»   {c}")
    
print("\n\n\n\nWith puctuation:")
print("Word  ==»  Freq:")
for w, c in wordDict2.items():
    print(f" {w}  ==»  {c}")

print("\nPunctuation ==» Freq:")
for p, c in punctuationDict2.items():
    print(f" {p}  ==»   {c}")
