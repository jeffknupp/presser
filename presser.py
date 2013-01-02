from bisect import bisect_left
from itertools import combinations


def load_anagrams():
    with open('anadict.txt', 'r') as file_handle:
        anagrams = file_handle.read().split('\n')
    return anagrams


def score_word(word):
    return sum([scores[c] for c in word])


def find_words(board, anagrams):
    board = ''.join(sorted(board))
    target_words = []
    for word_length in range(5, len(board) + 1):
        print(word_length)
        for combination in combinations(board, word_length):
            anagram = ''.join(combination)
            j = bisect_left(anagrams, anagram)
            if j == len(anagram):
                continue
            words = anagrams[j].split()
            if words[0] == anagram:
                target_words.extend(words[1:])
    return target_words

if __name__ == "__main__":
    import sys
    if len(sys.argv) == 2:
        rack = sys.argv[1].strip()
    else:
        exit()
    anagrams = load_anagrams()
    target_words = set(find_words(rack, anagrams))
    large_words = [word for word in target_words if len(word) > 5]
    print(large_words)
