def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def test():
    assert add(1, 2) == 3
    assert subtract(5, 5) == 0
    print("✅ All tests passed.")

if __name__ == "__main__":  # <- Corrected line
    print("5 + 3 =", add(5, 3))
    print("10 - 7 =", subtract(10, 7))
    test()
