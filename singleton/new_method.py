"""
" `__new__`: method is called to create a new instance of the class.
" We override it to ensure that only one instance of the is created
"
"""


class Singleton:
    __instance = None

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __str__(self):
        return self.name + " : " + str(self.age)


if __name__ == '__main__':
    s1 = Singleton("A", 12)
    print(s1, id(s1))

    s2 = Singleton('B', 24)
    print(s2, id(s2))
    print(s1, id(s1))