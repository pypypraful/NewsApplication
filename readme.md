NewsApplication with Technology FLASK, REACTJS, SQLite

commands for setting up:

-> Clone or download and unzip it
-> Inside project, run command: "python -m venv venv" without inverted commas
-> pip3 install flask, flask-bootstrap, flask-sqlalchemy, flask-login
-> Install Sqlite3
-> Run command in python3 shell in virtual environment itself
	-> from app import db
	-> db.create_all()
-> Exit the python shell
-> run command "flask run"

API's
	-> /login
		-> For login using email and password.
	-> /signup
		-> For User signup using email, password
		-> Table created for user_public_id, email(unique), password(hashed)
	-> /dashboard
		-> Logged in user can only log in
	-> /index
		-> Anyone can view this
