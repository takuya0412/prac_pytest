import pytest

@pytest.fixture(name='lu')
def ultimate_answer_to_life_the_universe_and_enerything():
    return 42



def test_everything(lu):
    assert lu ==42
