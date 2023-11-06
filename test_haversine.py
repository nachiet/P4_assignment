from myhaversine import myhaversine, mysqrt, mycos, myarcsin, mysin
import numpy as np

def test_myhaversine():
    pass


def test_mysqrt():
    assert mysqrt(-10) == 0
    assert -0.01 <= mysqrt(0) <= 0.01
    assert mysqrt(1) == 1
    assert 4.999 <= mysqrt(25) <= 5.001
    assert 54.771 <= mysqrt(3000) <= 54.773


def test_mycos():
    assert mycos(0) == 1
    assert mycos(90) == 0
    assert 0.706 <= mycos(45) <= 0.708
    assert -0.708 <= mycos(135) <= -0.706
    assert mycos(180) == -1
    assert -0.501 <= mycos(3000) <= -0.499

def test_myarcsin():
    assert myarcsin(-300) == -90
    assert myarcsin(-1) == -90
    assert myarcsin(0) == 0
    assert myarcsin(1) == 90
    assert myarcsin(300) == 90
    
def test_sin():
    assert mysin(90) == 1
    assert mysin(30) == 0.5
    assert mysin(180) == 0
    assert mysin(270) == -1

# test_myarcsin()

# test_sin()

