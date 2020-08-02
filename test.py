class Hello:
    def __init__(self):
        a = type(self).__name__
        print(a)
        print(type(a))


a = Hello()
