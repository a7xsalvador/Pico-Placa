import PicoPlaca as pp

a = pp.PicoPlaca('ABC111','31/05/2021','17:00')
b = pp.PicoPlaca('ABC333','31/05/2021','17:00')
c = pp.PicoPlaca('ABC111','asdfasd','17:00')
d = pp.PicoPlaca('ABC999','30/05/2021','17:00')


def test_a():
  assert a.isAllowed() == False

def test_b():
  assert b.isAllowed() == True

def test_c():
  assert c.isAllowed() == 'formato'

def test_d():
  assert d.isAllowed() == True
