try:
    count = int("hello")
except ValueError:
    print("Bad number given")


try:
    assert 1 ==2, "One does not equal 2"
except Exception as what:
    print("assert throws", type(what))