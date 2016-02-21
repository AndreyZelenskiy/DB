class Film:
    def __init__(self, name, country):
        self.name = name
        self.country = country

    def __str__(self):
        return self.name + " " + self.country

    def __eq__(self, other):
        return self.name == other.name and self.country == other.country

    def __hash__(self):
        return hash(self.name + self.country * len(self.name + self.country))
