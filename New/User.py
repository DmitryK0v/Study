class User(object):
    def __init__(self, name, age, user_type):
        self.name = name
        self.age = age
        self.user_type = user_type

    def access_database(self):
        if self.user_type.lower() == 'SuperUser'.lower():
            print('access granted')
        else:
            print('access denied')


class SuperUser(User):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def access_database(self):
        print('access granted')

pavl = User('Pavlo', 20, 'User')
pavl.access_database()
dima = User('Dmitry', 21, 'SuperUser')
dima.access_database()
Kate = SuperUser('Kate', 21)
Kate.access_database()
jar = User('janikk', 25, 'superuser')
jar.access_database()


