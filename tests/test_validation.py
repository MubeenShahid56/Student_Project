from src.student_app.utils.validate_name import validate_name
from src.student_app.utils.validate_marks import validate_marks


def test_valid_name():
    assert validate_name("Ali") is True


def test_invalid_name():
    assert validate_name("") is False


def test_valid_marks():
    assert validate_marks(85) is True


def test_invalid_marks():
    assert validate_marks(105) is False


def test_marks_boundaries():
    assert validate_marks(0) is True
    assert validate_marks(100) is True