t1, t2=None, 10

def test(t1,t2):
    if t1 and t2:
        return t1+t2
    else:
        return t1 or t2

print(test(t1,t2))