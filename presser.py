from itertools import combinations
import collections


def load_anagrams():
    anagrams = collections.defaultdict(list)
    lengths = set()
    with open('anadict.txt', 'r') as file_handle:
        for line in file_handle:
            words = line.split()
            anagrams[tuple(words[0])] = words[1:]
            lengths.add(len(words[0]))
    return (anagrams, max(lengths))


def find_words(board, anagrams, max_length):
    board = ''.join(sorted(board))
    target_words = []
    for word_length in range(3, max_length + 1):
        print(word_length)
        for combination in combinations(board, word_length):
            if combination in anagrams:
                target_words += anagrams[combination]
    return target_words

if __name__ == "__main__":
    import sys
    if len(sys.argv) == 2:
        rack = sys.argv[1].strip()
    else:
        exit()
    anagrams, max_length = load_anagrams()
    target_words = set(find_words(rack, anagrams, max_length))
    large_words = [word for word in target_words if len(word) > 14]
    print(large_words)
