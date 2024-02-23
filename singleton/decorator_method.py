def singleton(cls):
    __instance = {}

    def wrapper(*args, **kwargs):
        if cls not in __instance:
            __instance[cls] = cls(*args, **kwargs)
        return __instance[cls]

    return wrapper


@singleton
class Singleton:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return self.name + " : " + str(self.age)


if __name__ == '__main__':
    s1 = Singleton("A", 12)
    print(s1, id(s1))

    s2 = Singleton('B', 24)
    print(s2, id(s2))
    print(s1, id(s1))
