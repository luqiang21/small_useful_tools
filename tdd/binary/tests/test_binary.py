
from binary.binary import Binary

def test_binary_init_int():
    binary = Binary(6)
    assert int(binary) == 6

def test_binary_init_bitstr():
    binary = Binary('110')
    assert int(binary) == 6

def test_binary_init_binstr():
    binary = Binary('0b110')
    assert int(binary) == 6

def test_binary_init_hexstr():
    binary = Binary('0x6')
    assert int(binary) == 6

def test_binary_init_hex():
    binary = Binary(0x6)
    assert int(binary) == 6

def test_binary_init_inseq():
    binary = Binary([1,1,0])
    assert int(binary) == 6

def test_binary_init_strseq():
    binary = Binary(['1', '1', '0'])
    assert int(binary) == 6

import pytest
def test_binary_init_negative():
    with pytest.raises(ValueError):
        binary = Binary(-4)

def test_binary_int():
    binary = Binary(6)
    assert int(binary) == 6

def test_binary_str():
    binary = Binary(6)
    assert str(binary) == 6
