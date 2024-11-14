class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0;
        self.following = 0
        self.seats = 5


    def follow(self, user):
        user.followers += 1
        self.following += 1



user1 = User('001','Johan')
user2 = User('002','Paula')

print (f'User1 Following : {user1.following}')
print (f'User1 Followers : {user1.followers}')

print (f'User2 Following : {user2.following}')
print (f'User2 Followers : {user2.followers}')

user1.follow(user2)
user2.follow(user1)
print (f'User1 Following : {user1.following}')
print (f'User1 Followers : {user1.followers}')

print (f'User2 Following : {user2.following}')
print (f'User2 Followers : {user2.followers}')
