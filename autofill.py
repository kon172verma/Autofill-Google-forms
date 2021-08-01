from selenium import webdriver
import time
import datetime
import random
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning) 

# User Data 
name = 'Konark Verma'
empId = 'TC1006'

def markAttendance(date, weekday):
	try:
		# Run chrome in the background
		options = webdriver.ChromeOptions()
		options.add_experimental_option('excludeSwitches', ['enable-logging'])
		# options.add_argument("--headless")
		web = webdriver.Chrome(chrome_options=options)
		web.get('https://forms.office.com/Pages/ResponsePage.aspx?id=IFlAaXO2fE-IReEk6dCK8n4oTiWA-MFEgkUpFqFzIiNUREI4TTMyUjgzOFBRMENKQlU2U0pYSjJPWC4u')
		time.sleep(1)
		# Adding name
		web.find_element_by_xpath('//*[@id="SelectId_0_placeholder"]/i').click()
		time.sleep(1)
		web.find_element_by_xpath('//*[@id="SelectId_0"]/div[2]/div[5]').click()
		# Adding date
		web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[3]/div[2]/div/div[2]/div/div[2]/div/div/div/input[1]').send_keys(date)
		# Marking attendance
		web.find_element_by_xpath('//*[@id="SelectId_1_placeholder"]/i').click()
		time.sleep(1)
		if(weekday==5 or weekday==6):
			web.find_element_by_xpath('//*[@id="SelectId_1"]/div[2]/div[8]/div/span').click()
		else:
			web.find_element_by_xpath('//*[@id="SelectId_1"]/div[2]/div[1]/div/span').click()
		# Submit
		time.sleep(1)
		web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[3]/div[3]/div[1]/button/div').click()
	except:		
		# Return Failure.
		return 0
	# Return success.
	return 1

def markHealthStatus(date, work):
	try:
		# Run chrome in the background
		options = webdriver.ChromeOptions()
		options.add_experimental_option('excludeSwitches', ['enable-logging'])

		# options.add_argument("--headless")
		web = webdriver.Chrome(chrome_options=options)
		web.get('https://forms.office.com/Pages/ResponsePage.aspx?id=IFlAaXO2fE-IReEk6dCK8n4oTiWA-MFEgkUpFqFzIiNUQlI1UTUxTEU2ODhSTU01QkNRMU40QUNRMC4u')
		time.sleep(1)
		# Name
		web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div/div[1]/div/div[2]/div/div/input').send_keys(name)
		# Employee Id
		web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div/div[2]/div/div[2]/div/div/input').send_keys(empId)
		# Date
		web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div/div[3]/div/div[2]/div/div/div/input[1]').send_keys(date)
		# Working Day Schedule
		if work == 'weekend':
			web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div/div[4]/div/div[2]/div/div[5]/div/label/input').click()
		elif work == 'home':
			web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div/div[4]/div/div[2]/div/div[1]/div/label/input').click()
		else:
			web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div/div[4]/div/div[2]/div/div[2]/div/label/input').click()
		# Temperature
		temp = str(98 + round(random.random()/2,1))	
		web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div/div[5]/div/div[2]/div/div/input').send_keys(temp)
		# Health Symptoms
		web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div/div[6]/div/div[2]/div/div[2]/div[3]/input').click()
		web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div/div[6]/div/div[2]/div/div[3]/div[3]/input').click()
		web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div/div[6]/div/div[2]/div/div[4]/div[3]/input').click()
		web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div/div[6]/div/div[2]/div/div[5]/div[3]/input').click()
		web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div/div[6]/div/div[2]/div/div[6]/div[3]/input').click()
		web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div/div[6]/div/div[2]/div/div[7]/div[3]/input').click()
		web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div/div[6]/div/div[2]/div/div[8]/div[3]/input').click()
		web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div/div[6]/div/div[2]/div/div[9]/div[3]/input').click()
		web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div/div[6]/div/div[2]/div/div[10]/div[3]/input').click()
		# Public Transport
		web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div/div[7]/div/div[2]/div/div[2]/div/label/input').click()
		# Aarogya Setu App
		web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div/div[8]/div/div[2]/div/div[1]/div/label/input').click()
		# COVID Patient nearby
		web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div/div[9]/div/div[2]/div/div[2]/div/label/input').click()
		# Social Gathering
		web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div/div[10]/div/div[2]/div/div[2]/div/label/input').click()
		# Submit
		time.sleep(1)		
		web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[3]/div[1]/button').click()
	except:		
		# Return Failure.
		return 0
	# Return success.
	return 1


# Get old data
file = open("data_autofill.txt",'r')
data = file.readlines()
file.close()

# Get last working day status
workLastMarked = ''
if data[-1].split(',')[0]!='5' and data[-1].split(',')[0]!='6':
	workLastMarked = data[-1].split(',')[2]
elif data[-1].split(',')[0]=='5':
	workLastMarked = data[-2].split(',')[2]
else:
	workLastMarked = data[-3].split(',')[2]

# Get last marked date
data = data[-1].split(',')[1]
dateLastMarked = datetime.datetime.strptime(data, '%m/%d/%Y')
dateToday = datetime.datetime.now()
date = dateLastMarked

# Append all the data.
data = []
while date.strftime('%m/%d/%Y') != dateToday.strftime('%m/%d/%Y'):
	temp = []
	date = date+datetime.timedelta(days=1)
	temp.append(date.strftime('%m/%d/%Y'))
	weekday = date.weekday()
	temp.append(weekday)
	if(weekday==5 or weekday==6):
		temp.append('weekend')
	elif(weekday==0):
		if workLastMarked=='home':
			workLastMarked='office'
		elif workLastMarked=='office':
			workLastMarked='home'
		temp.append(workLastMarked)
	else:
		temp.append(workLastMarked)
	data.append(temp)

# Marking the attendance and health status for all the dates.
for date, weekday, work in data:
	date = datetime.datetime.strptime(date, '%m/%d/%Y')
	date = str(int(date.strftime('%m')))+'/'+str(int(date.strftime('%d')))+'/'+str(int(date.strftime('%Y')))

	# Writing data to logs
	file = open("data_autofill.txt", "a")
	log = [weekday, date, work]

	resultAttendance, resultHealth1, resultHealth2 = 0,0,0

	# Mark Attendance.
	print('Marking Attendance for '+str(date)+' :')
	for i in range(1,4):
		print('try '+str(i)+'/3')
		resultAttendance = markAttendance(date, weekday)
		if resultAttendance == 1:
			print('Successfully marked attendance.!')
			break
		else:
			print('Some error occured.!')
	print()

	# Mark Health Status-1.
	print('Marking Health Status - 1  for '+str(date)+' :')
	for i in range(1,4):
		print('try '+str(i)+'/3')
		resultHealth1 = markHealthStatus(date, work)
		if resultHealth1 == 1:
			print('Successfully marked Health Status-1.!')

			break
		else:
			print('Some error occured.!')
	print()

	# Mark Health Status-2.
	print('Marking Health Status - 2  for '+str(date)+' :')
	for i in range(1,4):
		print('try '+str(i)+'/3')
		resultHealth2 = markHealthStatus(date, work)
		if resultHealth2 == 1:
			print('Successfully marked Health Status-2.!')
			break
		else:
			print('Some error occured.!')
	print()

	value = ''
	for i in log:
		value += str(i)+','
	value += str(resultAttendance)+','+str(resultHealth1)+','+str(resultHealth2)+'\n'
	file.write(value)
	file.close()