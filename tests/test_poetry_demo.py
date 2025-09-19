from poetry_demo import greet, days_ahead

def test_greet():
    result = greet()
    assert "Hello!" in result
    assert "current time" in result

def test_days_ahead():
    result = days_ahead(3)
    assert "In 3 days" in result
    assert "will be" in result

