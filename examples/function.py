def func1(a1, a2):
    print("func1: " + str(a1) + ", " + str(a2))

func1("this", "that")


def func2(a1, a2, a3="hello", a4=42):
    print("func2: " + str(a1) + ", " + str(a2) + ", " + str(a3) + ", " + str(a4))

func2("this", "that", "something", "else")

def func3(a1, a2, *, a3="hello", a4=42):
    print("func3: " + str(a1) + ", " + str(a2) + ", " + str(a3) + ", " + str(a4))

func3("this", "that", a3="something", a4="else")

