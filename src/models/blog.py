import uuid
import datetime
from post import Post
from src.common.database import Database


class Blog(object):
    def __init__(self, author, title, description, _id=None):
        self.author = author
        self.title = title
        self.description = description
        self._id = uuid.uuid4().hex if _id is None else _id

    def new_post(self):
        title = input('Enter post title: ')
        content = input('Enter post content: ')
        date = input('Enter post date, or leave blank for today in format DDMMYYYY: ')
        if date == "":
            date = datetime.datetime.utcnow()
        else:
            date = datetime.datetime.strptime(date, "%d%m%Y")
        print(date)
        post = Post(blog_id=self._id,
                    title=title,
                    content=content,
                    author=self.author,
                    # the "%" sign means we're expecting 2 digits for day and month
                    # 4 digits for year
                    created_date=date)
        post.save_to_mongo()

    def get_posts(self):
        return Post.from_blog(self._id)

    def save_to_mongo(self):
        Database.insert(collection='blogs',
                        data=self.json())

    def json(self):
        # python dictionary
        return {
            'author': self.author,
            'title': self.title,
            'description': self.description,
            '_id': self._id
        }

    # @staticmethod
    # def get_from_mongo(self):
    #     blog_data = Database.find_one(collection='blogs',
    #                                   query={'id': id})
    #     # create a blog with this blog data...
    #     # return an object of type blog
    #     return Blog(author=blog_data['author'],
    #                 title=blog_data['title'],
    #                 description=blog_data['description'],
    #                 id=blog_data['id'])

    # instead of static we can use classmethod
    # instead of data we can now return an object
    @classmethod
    def from_mongo(cls, id):
        blog_data = Database.find_one(collection='blogs', query={'_id': id})
        # create a blog with this blog data...
        # return an object of type blog
        print('BLOG DATA:', blog_data)
        
        # # can simplify this as well
        # return cls(author=blog_data['author'],
        #             title=blog_data['title'],
        #             description=blog_data['description'],
        #             _id=blog_data['_id'])

        return cls(**blog_data)