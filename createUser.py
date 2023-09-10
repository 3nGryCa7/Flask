# Create 
# In SQL called 'INSERT'

from model import User
from model import app, db

def create_user():
    admin = User('admin', 'admin@example.com')
    db.session.add(admin)

    user_amount = 10

    for i in range(1, user_amount+1):
        username = f'user{str(i)}'
        email = f'{username}@example.com'
        user = User(username, email)
        print(f"User:{user}")
        print(f"ID:{user.id}")
        print(f"Name:{user.username}")
        print(f"Email:{user.email}")
        print('----------------')
        db.session.add(user)
        db.session.commit()

# with app.app_context():
#     create_user()
