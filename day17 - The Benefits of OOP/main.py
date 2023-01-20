# we create a class in Python, we modelling instagram account
class User:
    pass;

class User:
    # we define __init__ as the constructor function
    def __init__(self, user_id:str, username:str):
        print("new user being created..");
        self.id = user_id;
        self.username = username;
        self.follower = 0;          # you could make the default value like this
        self.following = 0;
    
    # first method
    def follow(self, user:User):
        user.follower += 1;
        self.following += 1;
        
    # constructor function will called automaticall everytime you create an object from it(instance)

user_1 = User("001", "anggun");
# create another instagram account
user_2 = User("002", "faza");

# you create an object's attributes in multiple ways:
# user_1.id = "0001";
# user_1.username = "anggun";

# but this is not effective because we could go wrong in multiple object
# print(user_1.username);
# so we initialize the attributes inside the constructor

user_1.follow(user_2);
# follback the user_1
user_2.follow(user_1);

print(user_1.follower);
print(user_1.following);
print(user_2.follower);
print(user_2.following);