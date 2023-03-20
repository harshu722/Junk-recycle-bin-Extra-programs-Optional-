class user:
    def __init__(self,name,mobile, age):
        self.name = name
        self.mobile = mobile
        self.age = age

    def __eq__(self,other):
        return self.name == other.name \
               and self.mobile == other.mobile \
               and self.age == other.age

    def __lt__(self, other):
        return self.age < other.age

    def __gt__(self,other):
        return self.age > other.age

    def __str__(self):
        return f"name:{self.name},"\
               f"age={self.age}," \
               f"mobile={self.mobile}"

user_1 = User(name="jon", mobile="1111", age=20)
user_2 = User(name="jack", mobile="1111", age=23)

print(user_1 == user_2)
print(user_2 > user_1)

user_1 = User(name="jon", mobile="1111", age=20)
user_2 = User(name="jon", mobile="1111", age=20)

print(user_1 == user_2)
print(user_1)              
              
             
