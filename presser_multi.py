from itertools import combinations
import collections
import concurrent.futures
import itertools

def load_anagrams():
    anagrams = collections.defaultdict(list)
    lengths = set()
    with open('anadict.txt', 'r') as file_handle:
        for line in file_handle:
            words = line.split()
            anagrams[tuple(words[0])] = words[1:]
            lengths.add(len(words[0]))
    return (anagrams, max(lengths))

def find_words_of_length(anagrams, board, length):
    target_words = []
    for combination in combinations(board, length):
        if combination in anagrams:
            target_words += anagrams[combination]
    print(length)
    return target_words


def find_words(board, anagrams, max_length):

    target_words = []
    board = ''.join(sorted(board))
    word_lengths = list(range(3, max_length + 1))
    board_argument = itertools.repeat(board)
    anagrams_argument = itertools.repeat(anagrams)
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        futures = [executor.submit(find_words_of_length, anagrams, board, length) for length in word_lengths]
        for future in concurrent.futures.as_completed(futures):
            target_words += future.result()

    return target_words


def is_corner(position):
    return position in [0, 4, 20, 24]

def is_vowel(character):
    return character in ['a', 'e', 'i', 'o', 'u', 'y']

def score_board(board, colors, player):
    protected = player[0]
    owned = protected.lower()
    score = 0

    if '.' not in colors:
        # End of game. Calculate winner.
        player_score = sum([1 for position in colors if position == protected or position == owned])

        if player_score > 12:
            return (-1, True)
        else:
            return (-1, False)

    for index, color in enumerate(colors):
        if color == owned:
            if is_vowel(board[index]):
                score += 3
            elif is_corner(index):
                score += 2
            else:
                score += 1

        if color == protected:
            if is_vowel(board[index]):
                score += 10
            if is_corner(index):
                score += 7
            else:
                score += 5

    return (score, False)

if __name__ == "__main__":
    import sys
    if len(sys.argv) == 2:
        rack = sys.argv[1].strip()
    else:
        exit()
    anagrams, max_length = load_anagrams()
    target_words = set(find_words(rack, anagrams, max_length))
    print(len(target_words))

