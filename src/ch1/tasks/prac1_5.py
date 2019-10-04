def test_assetion():
    something = [3, 5, 6]
    val_a = 34
    val_b = 55
    name = "kodama"

    assert 5 in something
    assert val_a < val_b
    assert name not in "takuyakodmatakuya"
