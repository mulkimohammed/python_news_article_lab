
import re

def count_specific_word(text, search_word):
    if not text or not search_word:
        return 0

    words = text.lower().split()
    search_word = search_word.lower()

    count = 0

    for word in words:  
        clean_word = re.sub(r'[^\w]', '', word)
        if clean_word == search_word:  
            count += 1

    return count

def identify_most_common_word(text):
    if not text:
        return None

    words = re.findall(r'\b\w+\b', text.lower())

    word_count = {}

    for word in words:  
        if word in word_count: 
            word_count[word] += 1
        else:
            word_count[word] = 1

    most_common = None
    max_count = 0

    for word in word_count:
        if word_count[word] > max_count:
            max_count = word_count[word]
            most_common = word

    return most_common



def calculate_average_word_length(text):
    if not text:
        return 0

    words = re.findall(r'\b\w+\b', text)

    if len(words) == 0:
        return 0

    total_length = 0

    for word in words:  
        total_length += len(word)

    return float(total_length / len(words))



def count_paragraphs(text):
    if text == "":
        return 1

    paragraphs = text.strip().split("\n\n")

    count = 0
    i = 0

    while i < len(paragraphs): 
        if paragraphs[i].strip() != "":
            count += 1
        i += 1

    return count



def count_sentences(text):
    if text == "":
        return 1

    sentences = re.findall(r'[.!?]+', text)

    if len(sentences) == 0:
        return 1
    else:  
        return len(sentences)


if __name__ == "__main__":

    print("Enter your news article (Press Enter twice to finish):")

    lines = []

    while True:  
        line = input()
        if line == "":
            break
        lines.append(line)

    article = "\n".join(lines)

    search_word = input("Enter the word you want to count: ")

    print("\nResults:")
    print("Specific Word Count:", count_specific_word(article, search_word))
    print("Most Common Word:", identify_most_common_word(article))
    print("Average Word Length:", calculate_average_word_length(article))
    print("Paragraph Count:", count_paragraphs(article))
    print("Sentence Count:", count_sentences(article))
