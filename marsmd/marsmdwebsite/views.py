from django.shortcuts import render, redirect
import MySQLdb

# Create your views here.
def login(request):
	
	db = MySQLdb.connect(user='root', db='mars', passwd='Rohan333', host='localhost')
	cursor = db.cursor()
	result = cursor.execute('SELECT * FROM LOGIN')
	name = cursor.fetchall()

	if(result):
		print(name)
		print ("SUCCESS!")

	return render(request, 'marsmdwebsite/login.html')

def index(request):
	return render(request, 'marsmdwebsite/home.html')

def news(request):
	# return redirect('marsmdwebsite/news.html')
	return render(request, 'marsmdwebsite/news.html')
	
def appointments(request):
	# return redirect('marsmdwebsite/news.html')
	return render(request, 'marsmdwebsite/appointments.html')
	