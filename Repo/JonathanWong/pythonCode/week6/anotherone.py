class Person:
    def __init__(self , name: str, surname: str, passport: str) -> None:
        self.name = name
        self.surname = surname
        self.passport = passport
    def __str__(self) -> str:
        return self.name + ", " + self.surname + ", " + str(self.passport)

class Worker(Person):
    def __init__(self , name: str, surname: str, passport: str, job: str) -> None:
        Person.__init__(self , name , surname , passport)
        self.job = job
    def __str__(self) -> str:
        return Person.__str__(self) + ", " + str(self.job)

    def __eq__(self, other)->bool:
        return self.passport == other.passport

class Athlete(Person):
    def __init__(self , name: str, surname: str, passport: str, sport: str) -> None:
        Person.__init__(self , name , surname , passport)
        self.sport = sport
    def __str__(self) -> str:
        return Person.__str__(self) + ", " + str(self.sport)

class AthleteWorker(Worker, Athlete):
    def __init__(self, name:str, surname:str, passport: str, sport: str, job: str)-> None:
        Worker.__init__(self, name, surname, passport, job)
        Athlete.__init__(self,name,surname,passport,sport)
    def __str__(self) -> str:
        return Worker.__str__(self) + ", " + str(self.sport)

person1 = Worker("Juan","Tan","123","PoolMember")
str(person1)
person2 = AthleteWorker("Mary","Loke","123","Swimmer", "Chess")
print(str(person2))
print(person1==person2)

