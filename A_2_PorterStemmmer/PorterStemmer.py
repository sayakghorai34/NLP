from nltk.stem import PorterStemmer
import pandas as pd

class ExtPorterStem:
    def __init__(self):
        self.porter_stemmer = PorterStemmer()

    def AdditionalRules(self, word):
        if word.endswith("li"):
            return word[:-2]
        elif word.endswith("ral"):
            return word[:-2]+"e "
        elif word.endswith("ges"):
            return word[:-2]+"e "
        elif word.endswith("ine"):
            return word+" "
        elif word.endswith("ines"):
            return word[:-1]+" "
        return word

    def stem(self, word):
        # Apply additional rules + porter stemmer
        updated = self.AdditionalRules(word)
        res = self.porter_stemmer.stem(updated)
        
        #only porter stemmer
        nltkStems = self.porter_stemmer.stem(word)
        
        return [nltkStems,res]

# Example usage:
obj = ExtPorterStem()
inputTxt = open("/Users/sayakghorai/Desktop/Sem_Vi/NLP_TA/A_2_PorterStemmmer/Input.txt", "r").read()
wrds = inputTxt.split()

wrds = [w.strip(".,!?;:-'\"()[]{\}") for w in wrds]
wrds = list(set(wrds))
originalPorter = []
extendedPorter = []

for word in wrds:
    stem = obj.stem(word)
    originalPorter.append(stem[0].strip())
    extendedPorter.append(stem[1].strip())
dataframe = pd.DataFrame({
    "Original Words": wrds,
    "Original Porter Stemmer": originalPorter,
    "Extended Porter Stemmer": extendedPorter
})
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
print(dataframe)
with open('/Users/sayakghorai/Desktop/Sem_Vi/NLP_TA/A_2_PorterStemmmer/output.txt', 'w') as file:
    file.write(dataframe.to_string(index=False))



