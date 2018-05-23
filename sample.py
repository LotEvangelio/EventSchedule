import datetime
import time

class eventscheduler(object):
	
	def __init__(self, title, time_input, location, note):

		self.title = title
		self.time_input = time_input
		self.location = location
		self.note = note

	def save(self, title, time_input, location, note):

		with open("output.txt","a+" + "\n") as f:
		    f.write(title + '\n' +  time_input +"\n" + location +'\n' + note +'\n' +'\n')
		    f.read()
		    f.close()

if __name__ == "__main__":

		currenttime = time.strftime("%a, %d %b %Y %I:%M:%S")
		print(currenttime)
		
		title = raw_input('Event: ')
		time_input = raw_input('Date/Time (Wed, 23 May 2018 02:58:01):  ')
		location = raw_input('Location: ')
		note = raw_input('Note: ')

		sc = eventscheduler(title, time_input, location, note)

		sc.save(title, time_input, location, note)

		