# How to create a class

class User:      # -- Class name should always be PascalCase
# Attributes
    id = ""
    username = ""

# Methods
    def __init__(self, user_id, username):     # -- Constructor
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        self.followers += 1
        self.following += 1

user = User("001", "Eric")
user_2 = User("002", "Mumbles")
user.follow(user_2)


class Car:
    def enter_race_mode():
        self.seats = 2

my_car = Car()
my_car.enter_race_mode()
