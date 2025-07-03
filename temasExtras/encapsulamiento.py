class Person:

    def __init__(self, name: str, age: int, mail: str):
        self.__name = name
        self.__age = age
        self.__mail = mail

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        if isinstance(name, str) and len(name) > 0:
            self.__name = name
        else:
            raise ValueError("Name must be a non-empty string.")

    @name.deleter
    def name(self):
        print("Deleting name...")
        del self.__name

def main():
    person = Person("Alice", 30, "jma@jma.com")
    print(person.name)  # Accessing the name property
    person.name = "Bob"  # Setting a new name
    print(person.name)  # Accessing the updated name
    del person.name  # Deleting the name property
    try:
        print(person.name)  # Attempting to access the deleted name
    except AttributeError as e:
        print(e)

if __name__ == "__main__":
    main()