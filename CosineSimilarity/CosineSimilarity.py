import math
from nltk.stem import PorterStemmer

# Porter Stemmer
def PortStem(text):
    stemmer = PorterStemmer()
    return ' '.join([stemmer.stem(word) for word in text.split()])

# Tokenization
def tokenize(text):
    return [word.lower().strip(".,!?;:-'\"()[]{\}") for word in text.split()]

# Remove Stop Words
def stopRemoval(tokens, stop_words):
    return [word for word in tokens if word not in stop_words]

# Cosine Similarity Calculation
def cosine_similarity(freq_dict1, freq_dict2):
    common_words = set(freq_dict1.keys()) & set(freq_dict2.keys())
    dot_prod = sum(freq_dict1[word] * freq_dict2[word] for word in common_words)
    mag_1 = math.sqrt(sum(freq_dict1[word] ** 2 for word in freq_dict1))
    mag_2 = math.sqrt(sum(freq_dict2[word] ** 2 for word in freq_dict2))
    if mag_1 == 0 or mag_2 == 0:
        return 0
    return dot_prod / (mag_1 * mag_2)

def print_decorated(title, content):
    print("\n" + "-"*50)
    print(title)
    print("-"*50)
    print(content)

#````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````
#Input Files
Paragraph_1 = "In the heart of beauty, bustling urban landscapes, modern cities are emblematic of human progress and innovation.Skyscrapers pierce the skyline, reflecting the ambition and dynamism of contemporary society. The constant hum of traffic and the glow of neon lights create an atmosphere that never sleeps, as people navigate through a labyrinth of streets and alleys. Technology intertwines seamlessly with daily life, from smartphones in the palms of hands to automated systems streamlining various processes. The metropolis becomes a melting pot of diverse cultures, fostering an environment where individuals from different backgrounds coexist and contribute to the vibrant tapestry of urban living."
Paragraph_2 = "Nature, with its tranquil beauty, innovative offers a stark contrast to the bustling energy of city life. In serene landscapes, lush greenery stretches as far as the eye can see, providing a refuge from the concrete jungles of urban environments. The whispering winds through trees and the gentle babble of streams create a soothing symphony that resonates with those seeking solace. Biodiversity flourishes, with flora and fauna harmonizing to form delicate ecosystems. Unlike the constant motion of city streets, the rhythm of nature follows a more leisurely pace, inviting individuals to pause, reflect, and appreciate the simplicity and balance inherent in the natural world. Amidst the peaceful surroundings, people find a sanctuary to escape the rapid pace of modern life and reconnect with the timeless beauty of the earth."
# Stop Words
stop_words = set(['in', 'of', 'and', 'the', 'a', 'to', 'is', 'with', 'from', 'its', 'that', 'are', 'for', 'as', 'on', 'by', 'an', 'has', 'it', 'at', 'be', 'or', 'not'])
#````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````


#Case1: Without Porter Stemmer and without Stop Words removal
#````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````
case1_tokens_1 = tokenize(Paragraph_1)
case1_tokens_2 = tokenize(Paragraph_2)
case1_freq_dict_1 = {word: case1_tokens_1.count(word) for word in set(case1_tokens_1)}
case1_freq_dict_2 = {word: case1_tokens_2.count(word) for word in set(case1_tokens_2)}
similarity1 = cosine_similarity(case1_freq_dict_1, case1_freq_dict_2)
#````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````

#Case2: Without Porter Stemmer and with Stop Words removal
#````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````
case2_tokens_1 = tokenize(Paragraph_1)
case2_tokens_2 = tokenize(Paragraph_2)
case2_filtered_t1 = stopRemoval(case2_tokens_1, stop_words)
case2_filtered_t2 = stopRemoval(case2_tokens_2, stop_words)
case2_freq_dict_1 = {word: case2_filtered_t1.count(word) for word in set(case2_filtered_t1)}
case2_freq_dict_2 = {word: case2_filtered_t2.count(word) for word in set(case2_filtered_t2)}
similarity2 = cosine_similarity(case2_freq_dict_1, case2_freq_dict_2)
#````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````

#Case3: With Porter Stemmer and without Stop Words removal
#````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````
case3_Stemmed_1 = PortStem(Paragraph_1)
case3_Stemmed_2 = PortStem(Paragraph_2)
case3_tokens_1 = tokenize(case3_Stemmed_1)
case3_tokens_2 = tokenize(case3_Stemmed_2)
case3_freq_dict_1 = {word: case3_tokens_1.count(word) for word in set(case3_tokens_1)}
case3_freq_dict_2 = {word: case3_tokens_2.count(word) for word in set(case3_tokens_2)}
similarity3 = cosine_similarity(case3_freq_dict_1, case3_freq_dict_2)
#````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````

#Case4: With Porter Stemmer and with Stop Words removal
#````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````
case4_Stemmed_1 = PortStem(Paragraph_1)
case4_Stemmed_2 = PortStem(Paragraph_2)
case4_tokens_1 = tokenize(case4_Stemmed_1)
case4_tokens_2 = tokenize(case4_Stemmed_2)
case4_filtered_t1 = stopRemoval(case4_tokens_1, stop_words)
case4_filtered_t2 = stopRemoval(case4_tokens_2, stop_words)
case4_freq_dict_1 = {word: case4_filtered_t1.count(word) for word in set(case4_filtered_t1)}
case4_freq_dict_2 = {word: case4_filtered_t2.count(word) for word in set(case4_filtered_t2)}
similarity4 = cosine_similarity(case4_freq_dict_1, case4_freq_dict_2)
#````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````


print_decorated("Case 1: Without Porter Stemmer and without Stop Words removal", f"Cosine Similarity: {similarity1}")
print_decorated("Case 2: Without Porter Stemmer and with Stop Words removal", f"Cosine Similarity: {similarity2}")
print_decorated("Case 3: With Porter Stemmer and without Stop Words removal", f"Cosine Similarity: {similarity3}")
print_decorated("Case 4: With Porter Stemmer and with Stop Words removal", f"Cosine Similarity: {similarity4}")


with open('output_file.txt', "w") as file:
    file.write("Case 1: Without Porter Stemmer and without Stop Words removal\n")
    file.write(f"Paragraph1 Token: {case1_tokens_1}\n")
    file.write(f"Paragraph2 Token: {case1_tokens_2}\n")
    file.write(f"Cosine Similarity: {similarity1}\n\n")

    file.write("Case 2: Without Porter Stemmer and with Stop Words removal\n")
    file.write(f"Paragraph1 Token: {case2_filtered_t1}\n")
    file.write(f"Paragraph2 Token: {case2_filtered_t2}\n")
    file.write(f"Cosine Similarity: {similarity2}\n\n")

    file.write("Case 3: With Porter Stemmer and without Stop Words removal\n")
    file.write(f"Paragraph1 Token: {case3_tokens_1}\n")
    file.write(f"Paragraph2 Token: {case3_tokens_2}\n")
    file.write(f"Cosine Similarity: {similarity3}\n\n")

    file.write("Case 4: With Porter Stemmer and with Stop Words removal\n")
    file.write(f"Paragraph1 Token: {case4_filtered_t1}\n")
    file.write(f"Paragraph2 Token: {case4_filtered_t2}\n")
    file.write(f"Cosine Similarity: {similarity4}\n\n")

print("\nResults have been written to output_file.txt")