from flask import *

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])

def personal():
	if request.method == 'POST':
		name = request.args.get('name', type=str)
		year = request.args.get('year', type=str)
		dob = request.args.get('dob', type=str)
		email = request.args.get('email', type=str)
		enrollment = request.args.get('enrollment', type=str)
		department = request.args.get('department', type=str)
		gender = request.args.get('gender', type=str)
		specialization = request.args.get('specialization', type=str)
		mobile = request.args.get('mobile', type=str)

	return {'name' : name,
			'year' : year,
			'dob'  : dob,
			'email': email,
			'enrollment' : enrollment,
			'department' : department,
			'gender' : gender,
			'specialization' : specialization,
			'mobile' : mobile
			}


if __name__ == '__main__':
	app.run(debug=True)