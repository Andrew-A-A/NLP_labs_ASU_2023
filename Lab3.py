from nltk.tag import pos_tag
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from nltk.corpus import wordnet as wn
from nltk.corpus import stopwords
from collections import Counter
import string
from IPython.display import display, HTML

# region Pos Tagging
text = "the worst scarves has been  splitted"
token = word_tokenize(text)
print(token)
tags = pos_tag(token)
print(tags)
# endregion

# region Treebank
# WordNet POS tags are: NOUN = 'n', ADJ = 's', VERB = 'v' ADV = 'r' ADJ_SAT = 'a'
tag_map = {
    "CC": None,  # coordin. conjunction (Cand, but, or)
    "CD": wn.NOUN,  # cardinal number (Cone, two)
    "DT": None,  # determiner (a, the)
    "EX": wn.ADV,  # existential ‘there' (there)
    'FW': None,  # foreign word (mea culpa)
    'IN': wn.ADV,  # preposition/sub-conj (of, in, by)
    'JJ': wn.ADJ,  # adjective (yellow)
    'JJR': wn.ADJ,  # adj., comparative (bigger)
    'JJS': wn.ADJ,  # adj-., superlative (wildest)
    "LS": None,  # List item marker (1, 2, One)
    "MD": None,  # modal (can, should)
    "NN": wn.NOUN,  # noun, sing. or mass (llama)
    "NNS": wn.NOUN,  # noun, plural (llamas)
    'NNP': wn.NOUN,  # proper noun, stng. (TBM)
    'NNPS': wn.NOUN,  # proper noun, plural (Carolinas)
    'PDT': wn.ADJ,  # predeterminer (all, both)
    "POS": None,  # possessive ending ('s )
    'PRP': None,  # personal pronoun (I, you, he)
    'PRP$': None,  # possessive pronoun (your, one's)
    'RB': wn.ADV,  # adverb (quickly, never)
    'RBR': wn.ADV,  # adverb, comparative (faster)
    "RBS": wn.ADV,  # adverb, superlative (fastest)
    "RP": wn.ADJ,  # particle (up, off)
    "SYM": None,  # symbol (+,%, &)
    "TO": None,  # "to" (to)
    "UH": None,  # interjection (ah, oops)
    'VB': wn.VERB,  # verb base form (eat)
    "VBD": wn.VERB,  # verb past tense (ate)
    'VBG': wn.VERB,  # verb gerund (eating)
    'VBN': wn.VERB,  # verb past participle (eaten)
    'VBP': wn.VERB,  # verb non-3sg pres (eat)
    'VBZ': wn.VERB  # verb 3sg pres (eats)
}

# lemmatizing with benefiting of POS
lemmatizer = WordNetLemmatizer()
text = "worst scarves has been  cut"
token = word_tokenize(text)
tags = pos_tag(token)
w_net_lemma = []
for tag in tags:
    X = tag[1]
    w_net_lemma.append(lemmatizer.lemmatize(tag[0], pos=tag_map[X]))
print(w_net_lemma)

# endregion

# region Word Cloud
# 1. Read Text
f = open('Martin Luther King, Jr. - I Have a Dream.txt', 'r')
speech = f.read()

# 2. Word Tokenization
speech_words = word_tokenize(speech)

# 3. Filtering Stop Words
stop_words = set(stopwords.words("english"))
filtered_speech_words = [word for word in speech_words if word.casefold() not in stop_words]

# 4. Remove Punctuation Strings
no_punct_filtered_speech_words = [''.join(char for char in word if char not in string.punctuation)
                                  for word in filtered_speech_words
                                  ]
no_punct_filtered_speech_words = [word for word in no_punct_filtered_speech_words if word]
print(no_punct_filtered_speech_words)

# 5. Count words
words_counter = Counter(no_punct_filtered_speech_words)
# 6. Display words occurrences by changing font size using HTML
html_str = ''
for word in words_counter.keys():
    font_size = 20 + words_counter[word]
    html_str += '<span style="font-size:{}px">{}</span>'.format(font_size, word)
# display(HTML(html_str))
with open("data.html", "w") as file:
    file.write(html_str)
# endregion
