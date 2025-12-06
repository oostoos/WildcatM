'''
Docstring for testing.core.$.piece

Quick run:
python -c "import runpy; runpy.run_path(r'testing/m/d/t_piece.py', run_name='__main__')"
'''

from src.m.d.dollar import *
from testing.utils.perfUtils import perfTimer

def testMain():
    unitTests()
    perfTests()

def unitTests():
    unitTest_1()

def perfTests():
    perfTest_1()
    perfTest_2()

# Unit Testing #

def unitTest_1():
    # Validate none or empty string
    assert d_piece("") == ""
    assert d_piece(None) == ""
    # Validate none or empty delimiter
    assert d_piece("one,two,three") == ""
    assert d_piece("one,two,three", "") == ""
    assert d_piece("one,two,three", None) == ""
    # Validate none or empty index
    assert d_piece("one,two,three", ",") == "one"
    assert d_piece("one,two,three", ",", None) == "one"
    assert d_piece("one,two,three", ",", "") == "one"
    print("Test 1 PASS")

def unitTest_2():
    # Validate out of bounds index
    assert d_piece("one,two,three", ",", -1) == ""
    assert d_piece("one,two,three", ",", 0) == ""
    assert d_piece("one,two,three", ",", 4) == ""
    assert d_piece("one,two,three", ",", 100) == ""
    print("Test 2 PASS")

def unitTest_3():
    # Validate normal operation
    assert d_piece("one,two,three", ",") == "one"
    assert d_piece("one,two,three", ",", 1) == "one"
    assert d_piece("one,two,three", ",", 2) == "two"
    assert d_piece("one,two,three", ",", 3) == "three"
    print("Test 3 PASS")

# Performance Testing #

def perfTest_1():
    test_string = "one^two^three^four^five^six^seven^eight^nine^ten"
    lFxn = lambda: d_piece(test_string, "^", 5)
    perfTimer(lFxn, 100_000)

def perfTest_2():
    test_string = "one^two^three^four^five^six^seven^eight^nine^ten"
    lFxn = lambda: d_piece(test_string, "^", 10)
    perfTimer(lFxn, 100_000)

if __name__ == "__main__":
    testMain()
    