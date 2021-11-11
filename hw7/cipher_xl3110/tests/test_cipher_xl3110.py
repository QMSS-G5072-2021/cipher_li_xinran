from cipher_xl3110 import cipher_xl3110

import pytest

def test_single():
    actual = cipher_xl3110.cipher(text = "ivy", shift = 2)
    expected = "kxA"
    assert actual == expected, "Should give kxA"