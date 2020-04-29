import pytest
from src.stack import Stack

def test_exercise():
    s = Stack()
    assert s.is_empty()
    s.add("Value")
    assert not s.is_empty()
    assert s.values() == ["Value"]
    s.take()
    assert s.is_empty()
