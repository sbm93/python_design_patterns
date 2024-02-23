class Singleton:
    __instance = None

    def __init__(self, name, age):
        self.set_data(name, age)

        if Singleton.__instance is not None:
            raise Exception("Single instance exist")
        else:
            Singleton.__instance = self

    @staticmethod
    def get_instance(name, age):
        if Singleton.__instance is None:
            Singleton(name, age)
        return Singleton.__instance

    def set_data(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return self.name + " : " + str(self.age)


if __name__ == '__main__':
    s1 = Singleton("A", 14)
    print(s1, id(s1))

    s2 = Singleton.get_instance("B", 15)
    s2.set_data("B", 16)
    print(s2, id(s2))
    print(s1, id(s1))
