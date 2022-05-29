class PoolMember:
    poolname: str = "FIT students community pool"
    name: str = ""
    age: int = 0
    gender: str = None
    
    def __init__(self , name: str, age: int, gender: str) -> None:
        self.name = name
        self.age = age
        self.gender = gender


admin = PoolMember("Juan", 18, "male")
PoolMember.poolname = 'Monash_pool'

supervisor = PoolMember("Emilia", 26, "female")
