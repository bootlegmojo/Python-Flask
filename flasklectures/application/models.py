from application import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(id):
	return Users.query.get(int(id))

class Posts(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	first_name = db.Column(db.String(30), nullable=False)
	last_name = db.Column(db.String(30), nullable=False)
	title = db.Column(db.String(100), nullable=False, unique=True)
	content = db.Column(db.String(10000), nullable=False, unique=True)
	
	def __repr__(self):
		return ''.join([
			"User: ", self.first_name, " ", self.last_name, "\r\n",
			"Title: ", self.title, "\r\n", self.content
			])

class Users(db.Model, UserMixin):
	id = db.Column(db.Integer, primary_key=True)
	email = db.Column(db.String(150), nullable=False, unique=True)
	password = db.Column(db.String(50), nullable=False)

	def __repr__(self):
		return ''.join(['User ID: ', str(self.id), '\r\n', 'Email: ', self.email])