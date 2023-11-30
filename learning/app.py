from database import Database
from user import User

Database.initialise(database="learning", host="localhost", user="postgres", password="1234")

user = User('rustix260685@gmail.com', 'Rustam', 'Ismailov', None)

user.save_to_db()

user_from_db = User.load_from_db_by_email('rustix260685@gmail.com')

print(user_from_db)