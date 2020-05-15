from tkinter import *

root = Tk()
root.title("resume builder")
root.geometry("900x900")


course = StringVar()
#course.set("")

#Defining functions
def func(value):
	course = value
#submit button function
def data():
	degree = course
	name = name_box.get()
	name_box.delete(0, END)

	year = year_box.get()
	year_box.delete(0, END)
	
	dateofbirth = dob_box.get()
	dob_box.delete(0, END)
	
	email = email_box.get()
	email_box.delete(0, END)
	
	enrollment = enrollment_box.get()
	enrollment_box.delete(0, END)
	
	department = department_box.get()
	department_box.delete(0, END)
	
	gender = gender_box.get()
	gender_box.delete(0, END)
	
	specialization = specialization_box.get()
	specialization_box.delete(0, END)
	
	mobile = mobile_box.get()
	mobile_box.delete(0, END)
	
	pg_completion = pg_year_box.get()
	pg_year_box.delete(0, END)
	
	pg_cgpa = pg_cgpa_box.get()
	pg_cgpa_box.delete(0, END)
	
	ug_completion = ug_year_box.get()
	ug_year_box.delete(0, END)
	
	ug_cgpa = ug_cgpa_box.get()
	ug_cgpa_box.delete(0, END)
	
	board_12 = board_12_box.get()
	board_12_box.delete(0, END)
	
	school_12 = school_12_box.get()
	school_12_box.delete(0, END)
	
	passing_year_12 = yop_12_box.get()
	yop_12_box.delete(0, END)
	
	percent_12 = percent_12_box.get()
	percent_12_box.delete(0, END)
	
	board_diploma = diploma_board_box.get()
	diploma_board_box.delete(0, END)
	
	school_12 = school_diploma_box.get()
	school_diploma_box.delete(0, END)
	
	passing_year_diploma = yop_diploma_box.get()
	yop_diploma_box.delete(0, END)
	
	percent_diploma = percent_diploma_box.get()
	percent_diploma_box.delete(0, END)
	
	board_10 = board_10_box.get()
	board_10_box.delete(0, END)
	
	school_10 = school_10_box.get()
	school_10_box.delete(0, END)
	
	passing_year_10 = yop_10_box.get()
	yop_10_box.delete(0, END)
	
	percent_10 = percent_10_box.get()
	percent_10_box.delete(0, END)
	
	scholastic_1 = scholastic_1_box.get()
	scholastic_1_box.delete(0, END)
	
	scholastic_1_year = scholastic_1_year_box.get()
	scholastic_1_year_box.delete(0, END)
	
	acad_project_title = acad_project_title_box.get()
	acad_project_title_box.delete(0, END)
	
	acad_faculty = acad_faculty_box.get()
	acad_faculty_box.delete(0, END)
	
	acad_project_desc = acad_project_desc_box.get()
	acad_project_desc_box.delete(0, END)
	
	acad_duration = acad_duration_box.get()
	acad_duration_box.delete(0, END)
	
	os = os_box.get()
	os_box.delete(0, END)

	print(os,acad_project_desc,acad_project_desc)

#Defining Labels
course_label = Label(root, text="Course")
course_label.grid(row=0,column=0,sticky=W,padx=10)

name_label = Label(root, text="Name")
name_label.grid(row=1,column=0,sticky=W,padx=10)

year_label = Label(root, text = "UG/PG year")
year_label.grid(row=2,column=0,sticky=W,padx=10)

dob_label = Label(root, text = "Date of Birth")
dob_label.grid(row=3,column=0,sticky=W,padx=10)

email_label = Label(root, text = "Email id")
email_label.grid(row=4,column=0,sticky=W,padx=10)

enrollment_label = Label(root, text = "Enrollment No.")
enrollment_label.grid(row=5,column=0,sticky=W,padx=10)

department_label = Label(root, text = "Department")
department_label.grid(row=6,column=0,sticky=W,padx=10)

gender_label = Label(root, text = "Gender")
gender_label.grid(row=7,column=0,sticky=W,padx=10)

specialization_label = Label(root, text = "Specialization")
specialization_label.grid(row=8,column=0,sticky=W,padx=10)

mobile_label = Label(root, text = "Mobile No.")
mobile_label.grid(row=9,column=0,sticky=W,padx=10)

##Educational Qualification
pg_year_label = Label(root, text = "PG completion year")
pg_year_label.grid(row=10,column=0,sticky=W,padx=10)

pg_cgpa_label = Label(root, text = "PG CGPA")
pg_cgpa_label.grid(row=11,column=0,sticky=W,padx=10)

ug_year_label = Label(root, text = "UG completion year")
ug_year_label.grid(row=12,column=0,sticky=W,padx=10)

ug_cgpa_label = Label(root, text = "UG CGPA")
ug_cgpa_label.grid(row=13,column=0,sticky=W,padx=10)

board_12_label = Label(root, text = "12 University/Board")
board_12_label.grid(row=14,column=0,sticky=W,padx=10) 

school_12_label = Label(root, text = "12 Institue/School Name")
school_12_label.grid(row=15,column=0,sticky=W,padx=10)

yop_12_label = Label(root, text = "Passing Year of 12")
yop_12_label.grid(row=16,column=0,sticky=W,padx=10)

percent_12_label = Label(root, text = "12 Percentage")
percent_12_label.grid(row=17,column=0,sticky=W,padx=10)

diploma_board_label = Label(root, text = "Diploma University/Board")
diploma_board_label.grid(row=18,column=0,sticky=W,padx=10)

school_diploma_label = Label(root, text = "Diploma Institue/School Name")
school_diploma_label.grid(row=19,column=0,sticky=W,padx=10)

yop_diploma_label = Label(root, text = "Passing Year of diploma")
yop_diploma_label.grid(row=20,column=0,sticky=W,padx=10)

percent_diploma_label = Label(root, text = "diploma Percentage/CGPA")
percent_diploma_label.grid(row=21,column=0,sticky=W,padx=10)

board_10_label = Label(root, text = "10 University/Board")
board_10_label.grid(row=22,column=0,sticky=W,padx=10)

school_10_label = Label(root, text = "10 Institue/School Name")
school_10_label.grid(row=23,column=0,sticky=W,padx=10)

yop_10_label = Label(root, text = "Passing Year of 10")
yop_10_label.grid(row=24,column=0,sticky=W,padx=10)

percent_10_label = Label(root, text = "10 Percentage/CGPA")
percent_10_label.grid(row=25,column=0,sticky=W,padx=10)

##Scholastic Achievements
schol_label = Label(root, text="Scholastic Achievement")
schol_label.grid(row=26,column=0,columnspan=2)

scholastic_1_label = Label(root, text="Describe Scholastic Achievements")
scholastic_1_label.grid(row=27,column=0,sticky=W,padx=10)

scholastic_1_year_label = Label(root, text="Achievement Year")
scholastic_1_year_label.grid(row=28,column=0,sticky=W,padx=10)
'''
scholastic_2_label = Label(root, text="Describe Scholastic Achievements")
scholastic_2_label.grid(row=29,column=0,sticky=W,padx=10)

scholastic_2_year_label = Label(root, text="Achievement Year")
scholastic_2_year_label.grid(row=30,column=0,sticky=W,padx=10)
'''
##Academic Project
acad_label = Label(root, text="Academic Projects")
acad_label.grid(row=31,column=0,columnspan=2)

acad_project_title_label = Label(root,text="Project title")
acad_project_title_label.grid(row=32,column=0,sticky=W,padx=10)

acad_faculty_label = Label(root,text="Project Mentor")
acad_faculty_label.grid(row=33,column=0,sticky=W,padx=10)

acad_project_desc_label = Label(root,text="Project Description")
acad_project_desc_label.grid(row=34,column=0,sticky=W,padx=10)

acad_duration_label = Label(root,text="Project Duration")
acad_duration_label.grid(row=35,column=0,sticky=W,padx=10)
##platforms worked
plat_label = Label(root, text="Platforms worked")
plat_label.grid(row=36,column=0,columnspan=2, sticky=W,padx=10)

os_label = Label(root, text="Operating Systems")
os_label.grid(row=37,column=0,sticky=W,padx=10)

#prog_label = Label(root, text="Programming Skills")
#prog_label.grid(row=38,column=0,sticky=W,padx=10)




#Defining Input Boxes....
course_drop = OptionMenu(root, course, "UG","PG", command=func)
course_drop.grid(row=0,column=1)

name_box = Entry(root)
name_box.grid(row=1,column=1)

year_box = Entry(root)
year_box.grid(row=2,column=1)

dob_box = Entry(root)
dob_box.grid(row=3,column=1)

email_box = Entry(root)
email_box.grid(row=4,column=1)

enrollment_box = Entry(root)
enrollment_box.grid(row=5,column=1)

department_box = Entry(root)
department_box.grid(row=6,column=1)

gender_box = Entry(root)
gender_box.grid(row=7,column=1)

specialization_box = Entry(root)
specialization_box.grid(row=8,column=1)

mobile_box = Entry(root)
mobile_box.grid(row=9,column=1)


pg_year_box = Entry(root)
pg_year_box.grid(row=10,column=1)

pg_cgpa_box = Entry(root)
pg_cgpa_box.grid(row=11,column=1)

ug_year_box = Entry(root)
ug_year_box.grid(row=12,column=1)
	
ug_cgpa_box = Entry(root)
ug_cgpa_box.grid(row=13,column=1)

board_12_box = Entry(root)
board_12_box.grid(row=14,column=1) 

school_12_box = Entry(root)
school_12_box.grid(row=15,column=1)

yop_12_box = Entry(root)
yop_12_box.grid(row=16,column=1)

percent_12_box = Entry(root)
percent_12_box.grid(row=17,column=1)

diploma_board_box = Entry(root)
diploma_board_box.grid(row=18,column=1)

school_diploma_box = Entry(root)
school_diploma_box.grid(row=19,column=1)

yop_diploma_box = Entry(root)
yop_diploma_box.grid(row=20,column=1)

percent_diploma_box = Entry(root)
percent_diploma_box.grid(row=21,column=1)

board_10_box = Entry(root)
board_10_box.grid(row=22,column=1)

school_10_box = Entry(root)
school_10_box.grid(row=23,column=1)

yop_10_box = Entry(root)
yop_10_box.grid(row=24,column=1)

percent_10_box = Entry(root)
percent_10_box.grid(row=25,column=1)

scholastic_1_box = Entry(root)
scholastic_1_box.grid(row=27,column=1)

scholastic_1_year_box = Entry(root)
scholastic_1_year_box.grid(row=28,column=1)

acad_project_title_box = Entry(root)
acad_project_title_box.grid(row=32,column=1)

acad_faculty_box = Entry(root)
acad_faculty_box.grid(row=33,column=1)

acad_project_desc_box = Entry(root)
acad_project_desc_box.grid(row=34,column=1)

acad_duration_box = Entry(root)
acad_duration_box.grid(row=35,column=1)

os_box = Entry(root)
os_box.grid(row=37,column=1)

#prog_box = Entry(root)
#prog_box.grid(row=38,column=1)

submit_button = Button(root, text="Submit", command=data)
submit_button.grid(row=38,column=0,columnspan=2)


root.mainloop()