import re
import string
import nltk.stem as Stemmer
from autocorrect import Speller

spell = Speller(lang='en')

STOPWORDS = set(['the', 'be', 'to', 'of', 'and', 'a', 'in', 'that', 'have',
                 'i', 'it', 'for', 'not', 'on', 'with', 'he', 'as', 'you',
                 'do', 'at', 'this', 'but', 'his', 'by', 'from'])
PUNCTUATION = re.compile('[%s]' % re.escape(string.punctuation))
STEMMER = Stemmer.SnowballStemmer("english")


def spellcheck(words):
    return [spell(word) for word in words]


def lowercase(words: str) -> list[str]:
    return [word.lower() for word in words]


def filter_punctuation(words: str) -> list[str]:
    return [PUNCTUATION.sub('', word) for word in words]


def filter_stopwords(words: str) -> list[str]:
    return [word for word in words if word not in STOPWORDS]


def filter_stem(words: str) -> list[str]:
    return [STEMMER.stem(word) for word in words]


def transform(text: str, spell_check: bool) -> list[str]:
    """
    Transform/filter text to lowercase, remove stop words, punctuations and stem words
    :param text: String to transform
    :param spell_check: use autocorrect
    :return: list of words
    """
    words = text.split()
    words = lowercase(words)
    words = filter_punctuation(words)
    words = filter_stopwords(words)
    words = filter_stem(words)
    if spell_check:
        words = spellcheck(words)
    # print(words)
    return [word for word in words if word]
