class Producer:
    surname = str()
    name = str()

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __str__(self):
        result = str()
        result += self.name + " " + self.surname
        return result

    def __eq__(self, other):
        return self.name == other.name and self.surname == other.surname

    def __hash__(self):
        string = self.name + self.surname
        return hash(string * len(string))