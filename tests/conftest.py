import pytest
import random
import string
@pytest.fixture
def rand_int():
    return random.randint(1, 10)


@pytest.fixture
def rand_str():
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(30))
