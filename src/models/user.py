from src.common.database import Database
import uuid

class User(object):
    # user owns blogs
    def __init__(self, email, password, _id=None):
        self.email = email
        self.password = password
        self._id = uuid.uuid4().hex if _id is None else _id
    
    # when getting user by email, won't have user (current object)
    # interested in db and finding user
    @classmethod
    def get_by_email(cls, email):
        data = Database.find_one('users', {'email': email})
        if data is not None:
            return cls(**data)
    
    @classmethod
    def get_by_id(cls, _id):
        data = Database.find_one('users', {'_id': _id})
        if data is not None:
            return lcs(**data)
    
    # check user email and pass match
    # does not need self for anything
    # we can make it static
    @staticmethod
    def login_valid(email, password):
        # User.Login_valid("matt@schoolsucks.me", "1234")
        # this creates user object
        user = User.get_by_email(email)

        if user is not None:
            # check the password
            return user.password == password

    # we can use class method b/c we are in user class
    # if we change user class name, we don't have to change this method
    @classmethod
    def register(cls, email, password):
        user = cls.get_by_email(email)
        if user is None:
            # user doesn't exist, we can create it
            new_user = User(email, password)
            new_user.save_to_mongo()
            return True
        else:
            # user exists
            return False

    def login(self):
        pass
    
    def get_blogs(self):
        pass

    def json(self):
        pass

    def save_to_mongo(self):
        pass