import pytest


test_param = [1, 2, 3, 4]


@pytest.mark.parametrize('value', test_param)
def test_type_int(value):
    assert type(value) is int

id_param = ['one', 'two', 'three', 'four']


@pytest.mark.parametrize('value', test_param, ids=id_param)
def test_type_int_2(value):
    assert type(value) is int

pytest_param = [
    pytest.param(1, id='one'),
    pytest.param(2, id='two'),
    pytest.param(3, id='three'),
    pytest.param(4, id='four')
]

@pytest.mark.parametrize('value', pytest_param)
def test_type_int_3(value):
    assert type(value) is int
