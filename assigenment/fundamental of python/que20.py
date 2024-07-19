#Write a Python function that takes a list of words and returns the length
#of the longest one

def find_longest_word(word_list):
    longest_word = max(word_list, key=len)
    return len(longest_word)
