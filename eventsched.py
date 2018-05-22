from datetime import datetime
import time

class eventscheduler(object):
	
	def __init__(self, title, time_input, current_date, location, note):

		self.title = title
		self.time_input = time_input
		self.current_date = current_date
		self.location = location
		self.note = note

	def save(self, title, time_input, current_date, location, note):

		with open("output.txt","a+" + "\n") as f:
		    f.write(title + '\n' +  time_input +"\n" + date +'\n' + location +'\n' + note +'\n' +'\n')
		    f.read()
		    f.close()

if __name__ == "__main__":

		time.ctime()
		print(time.ctime())
		title = input('Event: ')
		time_input = input('Time: ')
		date = input('Date: ')
		location = input('Location: ')
		note = input('Note: ')

		sc = eventscheduler(title, time_input, current_date, location, note)

		sc.save(title, time_input, current_date, location, note)