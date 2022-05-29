class Phone:
    year: int = 2012
    memory: int = 3
    network: str = '2G'

    def __init__(self , model: str, colour: str) -> None:
        self.model = model
        self.colour = colour

    def set_memory(self , memory: int) -> None:
        self.memory = memory

    def set_network(self , network: str) -> None:
        Phone.network = network

phone1 = Phone('Pony', 'Magenta')
phone2 = Phone('Tomato', 'Green')

phone2.set_network('4G')
phone2.network = '3G'

phone1.set_memory(8)
phone1.year = 2018

print(phone1.colour)
print(phone1.memory)
print(phone1.network)

print(phone2.year)
print(phone2.memory)
print(phone2.network)

print(Phone.year)
print(Phone.model)