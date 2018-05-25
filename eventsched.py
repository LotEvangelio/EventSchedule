import datetime
import time

class eventscheduler(object):
	
	def __init__(self, title, time_input, location, note):

		self.title = title
		self.time_input = time_input
		self.location = location
		self.note = note

	def save(self, title, time_input, location, note):

		with open("output.txt","a+") as f:
		    f.write(title + '\n' +  time_input +"\n" + location +'\n' + note +'\n' +'\n')
		    f.read()
		    f.close()

	def remove(self,title, time_input, location, note):

		with open("output.txt", "w") as f:
			f.write(title + '\n' +  time_input +"\n" + location +'\n' + note +'\n' +'\n')
			f.close()

if __name__ == "__main__":

		stop = False
		
		title = input('Event: ')
		time_input = input('Date/Time (Mon, 21 May 2018 01:01:01):  ')
		location = input('Location: ')
		note = input('Note: ')

		sc = eventscheduler(title, time_input, location, note)

		sc.save(title, time_input, location, note)
		sc.remove(title, time_input, location, note)

		print(time_input)
		while(stop != True):
			currenttime = time.strftime("%a, %d %b %Y %I:%M:%S")
			if time_input == currenttime:
				print("It's Game Day!")
				print("title: " + title)
				break
				print(currenttime)