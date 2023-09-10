# Read 
# In SQL called "SELECT"

from model import User
from model import app, db

def read_all_user():
    return User.query.all()

# By id (id of User table) or by name ... 
def read_user_by_id(id):
    # Or from userlist get by index
    user = User.query.get(id)
    return '%r' % user + "\n" + \
            'ID: %r' % user.id + "\n" + \
            'Name: %r' % user.username + "\n" + \
            'Email: %r' % user.email

with app.app_context():
    # print(read_user_by_id(1))
    pass