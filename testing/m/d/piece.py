'''
Docstring for testing.core.$.piece

Quick run:
python -c "import runpy; runpy.run_path(r'testing/m/d/piece.py', run_name='__main__')"
'''

from src.m.d import dollar as d
from testing.utils.perfUtils import perf_timer
import timeit

def test_main():
    unit_test_main()
    perf_test_main()

def unit_test_main():
    unit_test_1()

def perf_test_main():
    perf_test_1()
    perf_test_2()

# Unit Testing #

def unit_test_1():
    assert d.p("one,two,three", ",", -1) == ""
    assert d.p("one,two,three", ",", 0) == ""
    assert d.p("one,two,three", ",", 1) == "one"
    assert d.piece("a,b,c", ",", 2) == "b"
    assert d.P("a|b|c|d", "|", 3) == "c"
    assert d.PIECE("x y z", " ", 4) == ""
    print("Test 1 PASS")

# Performance Testing #

def perf_test_1():
    test_string = "one^two^three^four^five^six^seven^eight^nine^ten"
    lFxn = lambda: d.p(test_string, "^", 5)
    perf_timer(lFxn, 100_000)

def perf_test_2():
    test_string = "one^two^three^four^five^six^seven^eight^nine^ten"
    lFxn = lambda: d.piece(test_string, "^", 10)
    perf_timer(lFxn, 100_000)

if __name__ == "__main__":
    test_main()
    