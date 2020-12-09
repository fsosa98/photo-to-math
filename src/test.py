from Solver import *

def test_plus_small():
    solver = Solver()
    assert 4 == solver.solve("2+2")

def test_simple():
    solver = Solver()
    assert -18 == solver.solve("2+2-7*4+4/2*3")

def test_simple2():
    solver = Solver()
    assert -4 == solver.solve("1-1-1-1-1-1")

def test_simple3():
    solver = Solver()
    assert -35 == solver.solve("-5*7")

def test_brackets():
    solver = Solver()
    assert 5 == solver.solve("(1+(1+(1+(1))+1))")

def test_complex1():
    solver = Solver()
    assert 20 == solver.solve("5*7/(1+2*3)-(1-2*(4*2))")

def test_complex2():
    solver = Solver()
    assert 4.5 - solver.solve("((7-2)/2)+(2/2/1/1/1+1)") < 10e-12

def test_complex3():
    solver = Solver()
    assert 3803 == solver.solve("174*56/4-78*2+1523")

def test_complex4():
    solver = Solver()
    assert -42 == solver.solve("(-5)*7+(-4*2+1)")