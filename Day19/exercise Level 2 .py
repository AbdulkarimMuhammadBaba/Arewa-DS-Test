import sys
sys.path.append("data")
import os
import re
from collections import Counter
import string
from stop_words import stop_words as sw
import math
import csv

def list_of_words(fname):
    output = []
    with open(fname, "r", encoding="UTF8") as file:
        for line in file:
            for word in line.split():
                output.append(word)
    return list(set(output))


def check_email(word):
    if re.fullmatch(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b", word):
        return True
    else:
        return False


def extract_emails(fname):
    words = list_of_words(fname)
    email_list = []

    for word in words:
        if check_email(word):
            email_list.append(word)

    return email_list

 print(extract_emails("data\email_exchanges_big.txt"))


def find_most_common_words(fname, value):
    text = open(fname).read()
    split_it = text.split()
    Cnter = [(sub[1], sub[0]) for sub in Counter(split_it).most_common()]

    return Cnter[:value]


print(find_most_common_words(r'data\romeo_and_juliet.txt', 10))
print(find_most_common_words(r'data\donald_speech.txt', 10))
print(find_most_common_words(r'data\melina_trump_speech.txt', 10))
print(find_most_common_words(r'data\michelle_obama_speech.txt', 10))
print(find_most_common_words(r'data\obama_speech.txt', 10))


def clean_text(text):
    text = text.lower()
    text = re.sub("\[.*?]", "", text)
    text = re.sub("https?://\S+|www\.\S+", "", text)
    text = re.sub("<.*?>+", "", text)
    text = re.sub("[%s]" % re.escape(string.punctuation), "", text)
    text = re.sub("\n", "", text)
    text = re.sub("\w*\d\w*", "", text)
    return text


def remove_support_words(text):
    return [word for word in text.split() if word not in sw]


def read_file(fname):
    try:
        with open(fname, "r", encoding="UTF8") as f:
            data = remove_support_words(clean_text(f.read()))
        return data
    except IOError:
        print("Error opening or reading input file: ", fname)
        sys.exit()


translation_table = str.maketrans(
    string.punctuation + string.ascii_uppercase,
    " " * len(string.punctuation) + string.ascii_lowercase,
)


def count_frequency(word_list):
    D = {}

    for new_word in word_list:

        if new_word in D:
            D[new_word] = D[new_word] + 1

        else:
            D[new_word] = 1

    return D


def word_frequencies_for_file(filename):
    word_list = read_file(filename)
    freq_mapping = count_frequency(word_list)

    print(
        "File",
        filename,
        ":",
    )
    print(len(freq_mapping), "distinct words")

    return freq_mapping



def dotProduct(D1, D2):
    Sum = 0.0

    for key in D1:

        if key in D2:
            Sum += D1[key] * D2[key]

    return Sum

def vector_angle(D1, D2):
    numerator = dotProduct(D1, D2)
    denominator = math.sqrt(dotProduct(D1, D1) * dotProduct(D2, D2))

    return math.acos(numerator / denominator)


def documentSimilarity(filename_1, filename_2):
    sorted_word_list_1 = word_frequencies_for_file(filename_1)
    sorted_word_list_2 = word_frequencies_for_file(filename_2)
    distance = (vector_angle(sorted_word_list_1, sorted_word_list_2) * 180) / math.pi

    print("The distance between the documents is: % 0.2f (degrees)" % distance)


 documentSimilarity("data\michelle_obama_speech.txt", "data\melina_trump_speech.txt")


def hacker_count(fname):
    csvFile = csv.reader(open(fname, mode="r"))
    count_a = 0
    count_b = 0
    count_c = 0
    for lines in csvFile:
        plain_text_line = " ".join(lines)
        if "python" in plain_text_line or "Python" in plain_text_line:
            count_a += 1
        if (
                "JavaScript" in plain_text_line
                or "Javascript" in plain_text_line
                or "javascript" in plain_text_line
        ):
            count_b += 1
        if not (not ("Java" in plain_text_line) or "Javascript" in plain_text_line):
            count_c += 1
    print(count_a, count_b, count_c)