from evenorodd import check_evenorodd

def test_even_number():
    assert check_evenorodd(10) == "Even"

def test_odd_number():
    assert check_evenorodd(7) == "Odd"