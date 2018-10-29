from django.shortcuts import render, redirect
import MySQLdb
from django import forms
import datetime
import json	

db = MySQLdb.connect(user='root', db='mars', passwd='Rohan333', host='localhost')
cursor = db.cursor(MySQLdb.cursors.DictCursor)

# Create your views here.

def docSignUp(request):

	cursor = db.cursor(MySQLdb.cursors.DictCursor)
		

	if request.method == "POST":
		fname = request.POST.get("firstname", None)
		lname = request.POST.get("lastname", None)
		contact = int(request.POST.get("Contact", None))
		email = request.POST.get("email", None)
		password = request.POST.get("password", None)
		age = request.POST.get("Age", None)
		username = request.POST.get("username", None)	

		name = fname + " " + lname

		print("\n\n\n\n\n")

		hospital = request.POST.get("hospital", None)
		speciality = request.POST.get("speciality", None)
		address = request.POST.get("address", None)
		working_hours = "9:00AM - 5:00PM"

		# insert into doctor table

		insert_doctor = cursor.execute("INSERT INTO doctor (doc_name, hospital, speciality, working_hours, email, phone, address, username) VALUES ( %s, %s, %s, %s, %s, %s, %s, %s)", [name, hospital, speciality, working_hours, email, contact, address, username])

		db.commit()

		print(hospital)
		print(speciality)
		return redirect('/login')
		



	return render(request, 'marsmdwebsite/signup.html')	

def signup(request):

	cursor = db.cursor(MySQLdb.cursors.DictCursor)
	

	if request.method == "POST":
		fname = request.POST.get("firstname", None)
		lname = request.POST.get("lastname", None)
		contact = int(request.POST.get("Contact", None))
		email = request.POST.get("email", None)
		password = request.POST.get("password", None)
		age = request.POST.get("Age", None)
		username = request.POST.get("username", None)
		sex = request.POST.get("gender", None)			

		name = fname + " " + lname

		print("\n\n\n\n\n")
		

		# insert into patient table

		
		insert_into_login = cursor.execute("INSERT INTO login (username, password) VALUES (%s, %s)", [username, password])
		db.commit()
		insert_patient = cursor.execute("INSERT INTO patient (name, age, sex, phone, email, username) VALUES (%s, %s, %s, %s, %s, %s)", [name, age, sex, contact, email, username])
		db.commit()

		print(sex)
		print(age)
		return redirect('/login')			


	return render(request, 'marsmdwebsite/signup.html')

def login(request):
	
	if request.method == 'POST': 
		username = request.POST.get('email', None)
		password = request.POST.get('password', None)

		print(username)
		print(password)

		password_db = cursor.execute('select l.username,l.password,p.patient_id from login l,patient p where l.username=p.username and l.username like %s and l.password like %s;', [username,password])
		print(password_db)
		l1=cursor.fetchall()
		print(l1)
		if (password_db > 0):
			request.session['user'] = l1[0]['username']
			request.session['user_id']=l1[0]['patient_id']
			print(str(l1[0]['username'])+"and "+str(l1[0]['patient_id']))
			return redirect('/admin_index')
			

	# cursor = db.cursor()
	# result = cursor.execute('INSERT INTO login VALUES ("John", "Doe")')
	# db.commit()
	# name = cursor.fetchall()


	# if(result):
	# 	print(name)
	# 	print ("SUCCESS!")

	return render(request, 'marsmdwebsite/login.html')


def forgot_password(request):

	if request.method == 'POST':
		email = request.POST.get('email', None)

		cursor = db.cursor()

		check_email = cursor.execute('')

	return render(request, 'marsmdwebsite/forgot_password.html')

def index(request):

	# if request.method == 'POST': 
	# 	username = request.POST.get('username', None)
	# 	password = request.POST.get('password', None)

	# 	print(username)
	# cursor = db.cursor()
	# password_db = cursor.execute('SELECT password FROM login WHERE username like ')
	# db.commit()
	# name = cursor.fetchall()


	return render(request, 'marsmdwebsite/home.html')

def news(request):
	# return redirect('marsmdwebsite/news.html')
	return render(request, 'marsmdwebsite/news.html')
	
def appointments(request):

	cursor = db.cursor(MySQLdb.cursors.DictCursor)
	doctors = cursor.execute('SELECT * FROM doctor')
	# appointments = cursor.execute('SELECT doctor_id, date, time FROM appointment')
	doctors_dictionary=cursor.fetchall()


	if request.method == 'POST': 
		speciality = request.POST.get('doctor_speciality', None)
		doctor_name = request.POST.get('doc_name', None)	
		appointment_time = request.POST.get('appointment_time', None)	
		appointment_date = request.POST.get('date', None)	
		patient_name = request.POST.get('patient-name', None)	
		email = request.POST.get('patient-email', None)
		address = request.POST.get('patient-address', None)			
		phone = request.POST.get('patient-phone', None)
		description = request.POST.get('patient-illness-description', None)

		# print(phone)
		# print(appointment_date)
		# print(email)
		# print(address)
		# print(patient_name)

		patient_id = cursor.execute('SELECT patient_id FROM patient WHERE name like %s', [patient_name])
		pat_id = cursor.fetchall()
		doctor_id = cursor.execute('SELECT doctor_id FROM doctor WHERE doc_name like %s', [doctor_name])
		doc_id = cursor.fetchall()

		print("\n \n \n \n \n\n\n\n\n\n\n\n\n")

		appointment = cursor.execute("INSERT INTO appointment (patient_id, doctor_id, reason, date, time) VALUES (%s, %s, %s, %s, %s)", [pat_id[0]["patient_id"], doc_id[0]["doctor_id"], description, appointment_date, appointment_time])
# appointment = cursor.execute("INSERT INTO 'appointment' ( `patient_id`, `doctor_id`, `reason`, `date`, `time`) VALUES ( '{}', '{}', '{}', '{}', '{}');".format(pat_id, doc_id, description, appointment_date, appointment_time))
		db.commit()

	# print(doctors_dictionary)	

	return render(request, 'marsmdwebsite/appointments.html', {'doctors_dictionary':doctors_dictionary})
	

def blog1(request):
	return render(request, 'marsmdwebsite/blog1.html')


def blog2(request):
	return render(request, 'marsmdwebsite/blog2.html')


def blog3(request):
	return render(request, 'marsmdwebsite/blog3.html')

def about(request):
	return render(request, 'marsmdwebsite/about.html')


def location(request):
	return render(request, 'marsmdwebsite/location.html')

#Sbamin

def sbadminIndex(request):
	return render(request, 'sbadmin/index.html')
def adminLogin(request):
	return render(request,'sbadmin/login.html')
def history(request):
	if request.method == 'POST':
		fastingsc= request.POST.get('fastingsc', None)
		postmealsc= request.POST.get('postmealsc', None)
		bonecalc= request.POST.get('bonecalc', None)
		bloodcalc= request.POST.get('bloodalc', None)
		bloodgluc= request.POST.get('bloodgluc', None)
		today=datetime.date.today()
		user1 = request.session['user_id']
		act = cursor.execute('Insert into history(patient_id,fasting_sugar_count,post_meal_sugar,bone_calcium,blood_alcohol_content,blood_glucose,date) values( %s,%s,%s,%s,%s,%s,%s)',[user1,fastingsc,postmealsc,bonecalc,bloodcalc,bloodgluc,today])
		db.commit()
	user1 = request.session['user_id']
	execute=cursor.execute('Select * from history where patient_id like %s',[user1])
	history=cursor.fetchall()
	print(history)
	return render(request,'sbadmin/history.html',{'history':history})

def hearts(request):
	if request.method == 'POST':
		bloodpress= request.POST.get('bloodpress', None)
		walkingheartrate= request.POST.get('walkingheartrate', None)
		restingheartrate= request.POST.get('restingheartrate', None)
		variability= request.POST.get('variability', None)
		today=datetime.date.today()
		user1 = request.session['user_id']
		act = cursor.execute('Insert into heart(patient_id,blood_pressure,walking_heart_rate,resting_heart_rate,variability,date) values( %s,%s,%s,%s,%s,%s)',[user1,bloodpress,walkingheartrate,restingheartrate,variability,today])
		db.commit()
	user1 = request.session['user_id']
	execute=cursor.execute('Select * from heart where patient_id like %s',[user1])
	heart=cursor.fetchall()
	return render(request,'sbadmin/hearts.html',{'heart':heart})

def nutrition(request):
	if request.method == 'POST':
		caffeine= request.POST.get('caffeine', None)
		carbs= request.POST.get('carbs', None)
		cholestrol= request.POST.get('dietarychol', None)
		fibres= request.POST.get('fibres', None)
		proteins= request.POST.get('proteins', None)
		water= request.POST.get('water', None)
		iron= request.POST.get('iron', None)
		print("Hey babu")
		print(caffeine)
		print(water)
		print(iron)
		today=datetime.date.today()
		user1 = request.session['user_id']
		act = cursor.execute('Insert into nutrition(patient_id,caffeine,carbohydrates,cholestrol,fibre,protien,water,iron,date) values( %s,%s,%s,%s,%s,%s,%s,%s,%s)',[user1,caffeine,carbs,cholestrol,fibres,proteins,water,iron,today])
		db.commit()
	user1 = request.session['user_id']
	execute=cursor.execute('Select * from nutrition where patient_id like %s',[user1])
	nutrition=cursor.fetchall()
	return render(request,'sbadmin/nutrition.html',{'nutrition':nutrition})

def familyadded(request):
	cursor = db.cursor(MySQLdb.cursors.DictCursor)
	if request.method == 'POST':
		user2 = request.session['user_name']
		user1 = request.session['user']
		relation = request.POST.get('relation', None)
		print(user2)
		print(user1)
		print(relation)
		exec1 =cursor.execute('Select patient_id from patient where username like %s',[user1])
		userid_1=cursor.fetchone()
		exec2 =cursor.execute('Select patient_id from patient where username like %s',[user2])
		userid_2=cursor.fetchone()
		act = cursor.execute('Insert into family(user1,user2,status,relation) values( %s,%s,%s,%s)',[userid_1['patient_id'],userid_2['patient_id'],'pending',relation])
		db.commit()

	return render(request,'sbadmin/familyadded.html')

def activity(request):
	cursor = db.cursor(MySQLdb.cursors.DictCursor)
	if request.method == 'POST':
		cyclingdist= request.POST.get('cyclingdist', None)
		walkingdist= request.POST.get('walkingdist', None)
		stepsclimb= request.POST.get('stepsclimb', None)
		excercisemin= request.POST.get('exercisemin', None)
		standinghrs= request.POST.get('standinghrs', None)
		caloriesburnt= request.POST.get('caloriesburnt', None)
		restinghrs= request.POST.get('restinghrs', None)
		today=datetime.date.today()
		user1 = request.session['user_id']
		act = cursor.execute('Insert into activity(activity_id,Cycling_Distance,walking_distance,steps_climbed,Excercise_minutes,standing_hours,calories_burnt,resting_hours,datetime) values( %s,%s,%s,%s,%s,%s,%s,%s,%s)',[user1,cyclingdist,walkingdist,stepsclimb,excercisemin,standinghrs,caloriesburnt,restinghrs,today])
		db.commit()
	user_name1=request.session['user']
	act = cursor.execute('SELECT patient_id FROM patient where username like %s',[user_name1])
	patient_id=cursor.fetchone()
	print(patient_id)
	act = cursor.execute('SELECT * FROM activity where activity_id like %s',[patient_id['patient_id']])
	activity_db=cursor.fetchall()
	print("Hey")
	print("Hollla ",activity_db)
	print ("NAna",json.dumps(activity_db))
	return render(request,'sbadmin/activity.html',{'activity_db':activity_db})

def tables(request):
	cursor = db.cursor(MySQLdb.cursors.DictCursor)
	if request.method == 'POST':
		user_name = request.POST.get('search', None)
		request.session['user_name'] = user_name
		print(user_name)
		if user_name:
			act = cursor.execute('SELECT * FROM patient where username like %s OR name like %s',[user_name,user_name])
			user_details=cursor.fetchall()
			if (act>0) :
				print("Successful")
				print(user_details)
				return render(request,'sbadmin/tables.html',{'sr':user_details})
			else:
				print("Error")	
	return render(request,'sbadmin/tables.html')


def charts(request):
	user_name1=request.session['user']
	cursor = db.cursor(MySQLdb.cursors.DictCursor)
	act = cursor.execute('SELECT patient_id FROM patient where username like %s',[user_name1])
	patient_id=cursor.fetchone()
	print("Yo",patient_id)
	act = cursor.execute('SELECT datetime FROM activity where activity_id like %s',[patient_id['patient_id']])
	x_axis=cursor.fetchall()
	print(x_axis)
	label=[]
	j=0
	#print("Gand mara",str(x_axis[0]['datetime']))
	for i in x_axis:
	  	label.append(str(x_axis[j]['datetime']))
	  	j=j+1
	print(label)
	month=json.dumps(label)

	act1 = cursor.execute('SELECT Cycling_Distance FROM activity where activity_id like %s',[patient_id['patient_id']])
	y_axis=cursor.fetchall()
	print(y_axis)
	data=[]
	j=0
	#print("Gand mara",str(y_axis[0]['Cycling_Distance']))
	for i in y_axis:
	  	data.append(str(y_axis[j]['Cycling_Distance']))
	  	j=j+1
	print(data)
	data1=json.dumps(data)
	act2 = cursor.execute('SELECT carbohydrates,cholestrol,water,iron,protien FROM nutrition where patient_id like %s order by(nutrition_id) desc ',[patient_id['patient_id']])
	pie=cursor.fetchall()
	print(pie)
	pie_chart=[]
	j=0
	#print("Gand mara",str(y_axis[0]['Cycling_Distance']))
	pie_chart.append(str(pie[0]['carbohydrates']))
	pie_chart.append(str(pie[0]['cholestrol']))
	pie_chart.append(str(pie[0]['water']))
	pie_chart.append(str(pie[0]['iron']))
	pie_chart.append(str(pie[0]['protien']))
	print(pie_chart)
	pie_chart_java=json.dumps(pie_chart)
	act = cursor.execute('SELECT date FROM history where patient_id like %s',[patient_id['patient_id']])
	date_history=cursor.fetchall()
	print(date_history)
	history=[]
	j=0
	#print("Gand mara",str(x_axis[0]['datetime']))
	for i in date_history:
	  	history.append(str(date_history[j]['date']))
	  	j=j+1
	print(history)
	history_xaxis=json.dumps(history)

	act1 = cursor.execute('SELECT post_meal_sugar FROM history where patient_id like %s',[patient_id['patient_id']])
	count_history=cursor.fetchall()
	print(count_history)
	count=[]
	j=0
	#print("Gand mara",str(y_axis[0]['Cycling_Distance']))
	for i in count_history:
	  	count.append(str(count_history[j]['post_meal_sugar']))
	  	j=j+1
	print(count)
	history_yaxis=json.dumps(count)


	return render(request,'sbadmin/charts.html',{'label':label,'month':month,'data1':data1,'pie_chart_java':pie_chart_java,'history_xaxis':history_xaxis,'history_yaxis':history_yaxis})

def register(request):
	return render(request,'sbadmin/register.html')

def appointment_display(request):
	
	user1 = request.session['user_id']
	appointment_cur = cursor.execute("SELECT a.appointment_id,d.doc_name,d.speciality,a.date,a.time,a.reason from appointment a,doctor d where a.doctor_id=d.doctor_id and patient_id like %s", [user1])
	db.commit()
	return render(request,'sbadmin/appointment_display.html')