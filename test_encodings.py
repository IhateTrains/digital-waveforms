from manchester import manchester


def test_NRZ():
    assert manchester([0,1,1,1,1,0,0,1], 0, 1) == [0,1,1,0,1,0,1,0,1,0,0,1,0,1,1,0]
    assert manchester([1,0,1,0,1], 0, 1) == [1,0,0,1,1,0,0,1,1,0]

def test_manchester():
    assert manchester([0,1,1,1,1,0,0,1], 0, 1) == [0,1,1,0,1,0,1,0,1,0,0,1,0,1,1,0]
    assert manchester([1,0,1,0,1], 0, 1) == [1,0,0,1,1,0,0,1,1,0]