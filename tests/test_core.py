from saypy import say_hi
def test_dummy():
    assert 1 == 1

def test_say_hi():
    assert say_hi('Matt') == 'Hey, Matt! Whats Up?'