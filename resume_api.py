#import resume_builder
from flask import *
from flask import request

app = Flask(__name__)

@app.route('/', methods = ['POST'])
data = request.get_json()
def personal():
	f_name = data['first_name']
	l_name = data['last_name']
	year = data['year_of_study']
	dob =data['dob'] 
	email = data['email_id']
	enrollment = data['enrollment_no']
	department = data['branch']
	gender = "Male" if data['gender'] == "M" else "Female"
	specialization = "None"
	mobile = data['phone_no']
	
	name = f_name + " " + l_name
	resume_builder.personalInformation(name,year,dob,email,enrollment,department,gender,specialization,mobile)
	
	print(name,year, dob, email,enrollment,department, gender,specialization, mobile)
	
	return "OK"

def academic():
	grad_year = data['grad_year']
	grad_cgpa = data['grad_cgpa']
	
	high_school = data['high_school']
	high_school_year = data['high_school_year']
	high_school_board = data['high_school_board']
	high_school_institute = data['high_school_institute']
	high_school_cgpa = data['high_school_cgpa']

	secondary_school_year = data['secondary_school_year']
	secondary_school_board = data['secondary_school_board']
	secondary_school_cgpa = data['secondary_school_cgpa']
	secondary_school_institute = data['secondary_school_institute']

	resume_builder.academic(grad_year, grad_cgpa, high_school, high_school_year, high_school_board, high_school_institute, high_school_cgpa, secondary_school_year, secondary_school_board, secondary_school_institute, secondary_school_cgpa)
	return "academic OK"

def scholastic_achievements():
	scholastic_achievements = dict(data['scholastic_achievements'])

	resume_builder.scholastic_achievements(scholastic_achievements)
	return "scholastic_achievements OK"

def project():
	projects = dict(data['projects'])

	resume_builder.project(projects)
	return "project OK"

def work_ex():
	work_exp = dict(data['work_experience'])

	resume_builder.work_ex(work_exp)
	return "work_exp OK"

def platform_worked():
	operating_skills = data['platforms_os']
	programming_skills = data['platforms_ps']
	software_skills = data['platforms_ss']
	core_subject = data['courses_core']
	depth_subject = data['courses_depth']

	resume_builder.platform_worked(operating_skills, programming_skills, software_skills,core_subject, depth_subject)
	return 'platform_worked OK'

def extra_curricular():
	position_of_responsibility = dict(data['positions'])
	extra_curricular = dict(data['extracurricular'])

	resume_builder.extra_curricular(position_of_responsibility, extra_curricular)
	return "extracurricular OK"
	

if __name__ == '__main__':
	app.run()