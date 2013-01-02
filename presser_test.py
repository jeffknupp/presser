import presser

def test_corners():
    TEST_BOARD_COLORS = '\
B...B\
.....\
.....\
.....\
....B'


    TEST_BOARD_LETTERS = '\
xxxxx\
xxxxx\
xxxxx\
xxxxx\
xxxxx'
    assert presser.score_board(TEST_BOARD_LETTERS, TEST_BOARD_COLORS, 'Blue') == (21, False)

def test_light_colors():
    TEST_BOARD_COLORS = '\
.bbb.\
.bbb.\
.bbb.\
.bbb.\
.bbb.'

    TEST_BOARD_LETTERS = '\
xxxxx\
xxxxx\
xxxxx\
xxxxx\
xxxxx'

    assert presser.score_board(TEST_BOARD_LETTERS, TEST_BOARD_COLORS, 'Blue') == (15, False)

def test_protected_non_vowel_non_corners():
    TEST_BOARD_COLORS = '\
.BBB.\
.BBB.\
.BBB.\
.BBB.\
.BBB.'
    TEST_BOARD_LETTERS = '\
xxxxx\
xxxxx\
xxxxx\
xxxxx\
xxxxx'

    assert presser.score_board(TEST_BOARD_LETTERS, TEST_BOARD_COLORS, 'Blue') == (75, False)

def test_protected_vowel_non_corners():
    TEST_BOARD_COLORS = '\
.BBB.\
.BBB.\
.BBB.\
.BBB.\
.BBB.'
    TEST_BOARD_LETTERS = '\
xaaax\
xaaax\
xaaax\
xaaax\
xaaax'

    assert presser.score_board(TEST_BOARD_LETTERS, TEST_BOARD_COLORS, 'Blue') == (225, False)


def test_win():
    TEST_BOARD_COLORS = '\
rBBBr\
rBBBr\
rBBBr\
rBBBr\
rBBBr'
    TEST_BOARD_LETTERS = '\
xaaax\
xaaax\
xaaax\
xaaax\
xaaax'

    assert presser.score_board(TEST_BOARD_LETTERS, TEST_BOARD_COLORS, 'Blue') == (-1, True)


def test_lose():
    TEST_BOARD_COLORS = '\
rrBBr\
rrBBr\
rrBBr\
rrBBr\
rrBBr'
    TEST_BOARD_LETTERS = '\
xaaax\
xaaax\
xaaax\
xaaax\
xaaax'

    assert presser.score_board(TEST_BOARD_LETTERS, TEST_BOARD_COLORS, 'Blue') == (-1, False)
