# nltk.download('stopwords')
# nltk.download('wordnet')
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, SnowballStemmer, WordNetLemmatizer
import re

example_string = """
Muad'Dib learned rapidly because his first training was in how to learn.
 And the first lesson of all was the basic trust that he could learn.
 it's shocking to find how many people do not believe they can learn,
 and how many more believe learning to be difficult."""
# region Tokenize

# Tokenize sentences
print(sent_tokenize(example_string))
# Tokenize words
print(word_tokenize(example_string))

words_in_string = word_tokenize(example_string)

# To focus on stop words in English
stop_words = set(stopwords.words('english'))

# endregion

# region Filtering stop words
# 1st way
filtered_list = []
for word in words_in_string:
    if word.casefold() not in stop_words:
        filtered_list.append(word)

print(filtered_list)

# Alternative way using list comprehension that is more pythonic
filtered_list = [
    word for word in words_in_string if word.casefold() not in stop_words
]
print(filtered_list)
# endregion

# region Stemming
# Snowball stemmer (Porter2) is better than Porter
stemmer = PorterStemmer()
stemmer2 = SnowballStemmer("english")
# using list comprehension
stemmed_words = [stemmer.stem(word) for word in words_in_string]
stemmed_words2 = [stemmer2.stem(word) for word in words_in_string]

print(stemmed_words)
print(stemmed_words2)
# endregion

# region Lemmatizing
lemmatizer = WordNetLemmatizer()

lemmatized_words = [lemmatizer.lemmatize(word) for word in words_in_string]

# Specify if the word is noun or adjective
lemmatizer.lemmatize('worst', pos='a')

print(lemmatized_words)

# endregion

# region Regular expression
path = r"D:\Files\College\nLP\Labs"  # raw string
print(path)

# Match a word at the begging of a string
result = re.match('Analytics', r'Analytics Vidhya is the largest data science community of India')
print(result)
print(result.group())
result_2 = re.match('largest', r'Analytics Vidhya is the largest data science community of India')
print(result_2)

# Search for the pattern "founded" in a given string
result = re.search('founded', r'Andrew NG founded Coursera. He also founded deeplearning.ai')
print(result.group())

result_2 = re.findall('founded', r'Andrew NG founded Coursera. He also founded deeplearning.ai')
print(result_2)

# Special sequences
string = r'Analytics Vidhya is the largest data science community of India'
# Check if there is any word that ends with 'est'
x = re.findall(r'est\b', string)
print(x)

string = "2 million monthly visits in Jan'19."
# Check if the string contains any digits (0 -> 9)
# Adding '+' after '\d' will continue to extract digits till encounters a space

x = re.findall("\d+", string)
print(x)

if x:
    print(f"yes, there is {len(x)} digit/s")
else:
    print("No numbers in the string")

# '\D' is inverse of '\d'

# Check if the word character NOT contain any digits
x = re.findall("\D+", string)
print(x)
if (x):
    print("Yes, there is at least one word with no digits")
else:
    print("No, all words contain digits")

# '\w' extract alphanumeric characters only ( a -> Z || 0 -> 9 || _ )
x = re.findall("\w+", string)
print(x)

# '\W' inverse of '\w'
x = re.findall("\W+", string)
print(x)

'''Metacharacters'''
# ( . ) matches any char
str = "rohan and rohit recently published a research paper!"

# Search for a string that starts with 'ro', followed by any number of characters

x = re.findall('ro.', str)  # searches one char after ro
x2 = re.findall('ro...', str)  # searches three chars after ro

print(x)
print(x2)

# ( ^ ) starts with

# check if the string starts with 'rohan'
x = re.findall('^rohan', str)
print(x)

if x:
    print("String starts with 'rohan' ")
else:
    print("String doesn't start with 'rohan' ")

# ( $ ) ends with
x = re.findall('paper!$', str)
print(x)

# ( * ) zero or more occurrences of the pattern to the left of it
str = "easy easssy eay ey"
x = re.findall('eas*y', str)
print(x)

# ( + ) one or more occurrences of the pattern to the left of it
x = re.findall('eas+y', str)
print(x)

# ( ? ) zero or one occurrences of the pattern left to it
x = re.findall('eas?y', str)
print(x)

# ( | ) either or
x = re.findall('easy|eassy', str)
print(x)
# endregion


# region HANDS ON
sentence = "Think and wonder, wonder and think."
x = re.findall(r'\w+', sentence)    # List of each alphanumeric chars word
x = ' '.join(x)     # Join all words in one string
print(x)
# endregion


