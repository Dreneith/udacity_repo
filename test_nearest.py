from nearest import nearest_square

def test_nearest_square_27():
    assert(nearest_square(27) == 25)

def test_nearest_square_n12():
    assert(nearest_square(12) == 9)
def test_nearest_square_not_int():
    assert(nearest_square(-12) == 0)
def test_nearest_square_9():
    assert(nearest_square(9) == 9)
