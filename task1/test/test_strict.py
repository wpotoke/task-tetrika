import pytest
from task1.solution.strict_deco import strict

# ----------- Примеры функций -----------

@strict
def add(a: int, b: int) -> int:
    return a + b

@strict
def repeat(word: str, times: int) -> str:
    return word * times

@strict
def combine(*args: str) -> str:
    return "-".join(args)

@strict
def config(**kwargs: bool) -> dict:
    return kwargs

@strict
def mix(x: int, *args: float, **kwargs: str) -> str:
    return f"{x} - {args} - {kwargs}"

# ----------- Успешные вызовы -----------

def test_add_valid():
    assert add(1, 2) == 3

def test_repeat_valid():
    assert repeat("a", 3) == "aaa"

def test_combine_valid():
    assert combine("one", "two", "three") == "one-two-three"

def test_config_valid():
    assert config(debug=True, verbose=False) == {"debug": True, "verbose": False}

def test_mix_valid():
    result = mix(1, 1.1, 2.2, key1="yes", key2="no")
    assert "1.1" in result and "key1" in result

# ----------- Ошибки -----------

def test_add_type_error():
    with pytest.raises(TypeError):
        add(1, "2")  # str вместо int

def test_repeat_wrong_word_type():
    with pytest.raises(TypeError):
        repeat(123, 3)

def test_combine_wrong_args_type():
    with pytest.raises(TypeError):
        combine("ok", 2, "bad")  # int среди str

def test_config_wrong_value_type():
    with pytest.raises(TypeError):
        config(debug="yes")  # str вместо bool

def test_mix_args_fail():
    with pytest.raises(TypeError):
        mix(5, 3.0, "oops")  # str не float

def test_mix_kwargs_fail():
    with pytest.raises(TypeError):
        mix(5, 1.0, val=123)  # 123 не str
