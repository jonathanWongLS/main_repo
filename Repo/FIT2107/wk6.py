class Person:
    def __init__(self, age, gender, givenName, familyName, givenFirst=True):
        self.age = age
        self.gender = gender
        self.givenName = givenName
        self.familyName = familyName
        self.givenFirst = givenFirst

    def greet(self, salutation="Hello"):
        '''a demonstration of why titles, full names and salutations
        should be stored explicitly not inferred'''

        if (self.gender == "Male"):
            if (self.age < 18):
                title="Master"
            else:
                title="Mr"
        elif (self.gender == "Female"):
            if (self.age < 18):
                title = "Miss"
            else:
                title = "Ms"
        else:
            title = "Mx"

        name = self.familyName + " " + self.givenName

        if (self.givenFirst is True):
            name = self.givenName + " " + self.familyName

        return salutation + ", " + title + " " + name


p1 = Person(age = 18, gender = "Male" , givenName = "Richard" , familyName = "Richardson", givenFirst = True )
# p2 = Person()
print(p1.greet("Sup"))