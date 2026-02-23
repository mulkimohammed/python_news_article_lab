with open("news_article.txt", "r", encoding="utf-8") as file:
    article_text = file.read()


# Function1:Count specific word
def count_specific_word(text, word):
    if not text:
        return 0  #edge case if text is empty

    words = text.lower().split()  #convert to lowercase and split
    return words.count(word.lower())


# Ask user for word to search
search_word = input("Enter a word to count: ")

# Call the function & print result
print("Word count:", count_specific_word(article_text, search_word))

# Function2:Identify the most common word
def identify_most_common_word(text):
    if not text:
        return None  #edge case if text is empty

    words = text.lower().split()  #convert to lowercase and split
    word_count = {}  # dictionary to count words

    for word in words:
        word_count[word] = word_count.get(word, 0) + 1  # count @ word

    most_common = max(word_count, key=word_count.get)  #get the word with highest count
    return most_common
print("most common word:",
 identify_most_common_word(article_text))

 # Function3:Calculate Average Word Length
def calculate_average_word_length(text):
    if not text:
        return 0  # edge case if empty text

    # Remove punctuation
    import string
    words = text.translate(str.maketrans("", "", string.punctuation)).split()

    if len(words) == 0:
        return 0

    total_length = sum(len(word) for word in words)
    average_length = total_length / len(words)
    return average_length
print("Average word length:",
calculate_average_word_length(article_text))

# Function4: Count no of paragraphs
def count_paragraphs(text):
    if not text:
        return 1  # edge case: empty text returns 1

    # Split by empty lines (paragraphs separated by double newlines)
    paragraphs = text.split("\n\n")
    return len(paragraphs)
print("Number of paragraphs:", count_paragraphs(article_text))

# Function5: Count no of sntcs
def count_sentences(text):
    if not text:
        return 1  # edge case if empty text returns 1

    # Count sntcs based on ., !, ?
    import re
    sentences = re.split(r'[.!?]+', text)
    # Remove empty strings from split
    sentences = [s for s in sentences if s.strip()]
    return len(sentences)
print("Number of sentences:", count_sentences(article_text))