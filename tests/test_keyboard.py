import pytest

from src.keyboard import Keyboard


def test_class_keyboard():
    kb = Keyboard("Scorpion K6909", 2500, 1)
    assert str(kb) == "Scorpion K6909"
    assert kb.price == 2500
    assert str(kb.language) == "EN"
    kb.change_lang()
    assert str(kb.language) == "RU"
    with pytest.raises(AttributeError):
        kb.language = "AR"
