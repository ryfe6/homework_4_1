import pytest
from src.keyboard import Keyboard

def test_class_keyboard():
    kb = Keyboard("Scorpion K6909", 2500, 1, "RU")
    assert str(kb) == "Scorpion K6909"
    assert kb.price == 2500
    assert str(kb.language) == "RU"
    kb.change_lang()
    assert str(kb.language) == "EN"
    with pytest.raises(AttributeError):
        kb.language = "AR"
