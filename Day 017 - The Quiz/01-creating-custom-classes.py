class User:

    # Constructor
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0  # default value
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1


user_1 = User("001", "angela")
# print(user_1.id)
user_2 = User("002", "jack")

user_1.follow(user_2)
print("User 1 following: {} and followers: {}.".format(user_1.following, user_1.followers))
print("User 2 following: {} and followers: {}.".format(user_2.following, user_2.followers))