import pytest
@pytest.fixture
def inp_value():
    l = []
    for i in range(11):
        c = 0
        for j in range(1,1+i):
            if i%j== 0:
                c += 1
        if c == 2:
            l.append(i)
    return l