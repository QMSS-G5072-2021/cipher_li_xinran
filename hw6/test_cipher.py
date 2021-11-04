#!/usr/bin/env python
# coding: utf-8

# In[ ]:

import pytest

def cipher(text, shift, encrypt=True):
    assert isinstance(shift, int), "Shift should be entered as a int"
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    new_text = ''
    for c in text:
        index = alphabet.find(c)
        if index == -1:
            new_text += c
        else:
            new_index = index + shift if encrypt == True else index - shift
            new_index %= len(alphabet)
            new_text += alphabet[new_index:new_index+1]
    return new_text


def test_single():
    actual = cipher(text = "ivy", shift = 2)
    expected = "kxA"
    assert actual == expected, "Should give kxA"


def test_negative():
    actual = cipher(text = "ivy", shift = -3)
    expected = "fsv"
    assert actual == expected, "Should give fsv"



def test_symbol():
    actual = cipher(text = "1vy", shift = 4)
    expected = "1zC"
    assert actual == expected, "Should give 1zC"


def test_assertion():
    with pytest.raises(AssertionError):
        cipher(text = "ivy", shift = "one")



