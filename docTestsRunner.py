def test():
    import doctest
    doctest.testfile("refactoringDocTest.txt", verbose=1)


if __name__ == "__main__":
    test()
