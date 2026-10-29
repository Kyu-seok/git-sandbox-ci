from wordcount import count_words


def test_single_spaces():
    assert count_words("hello world") == 2


def test_repeated_spaces():
    assert count_words("one  two three") == 3


def test_newlines():
    assert count_words("one\ntwo") == 2


def test_empty():
    assert count_words("") == 0
