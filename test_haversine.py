from myhaversine import myhaversine, mysqrt, mycos, myarcsin, mysin
import numpy as np

def test_myhaversine():
    pass


def test_mysqrt():
    pass


def test_mycos():
    pass
    

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

test_myarcsin()

test_sin()

