import time
import sys
from pydub import AudioSegment
from pydub.playback import play

class pymodoro:

	def __init__(self):
		self.ticks = 0
		self.lifecycle()

	def start_timer(self, total):
		while total >= 0:
			total -= 1
			sys.stdout.write("\r")
			sys.stdout.flush()
			time.sleep(1)
			sys.stdout.write("time left to " + self.current_task + ": " + str(total)+ "           ") #TODO - make a utility that flushes and adds a space buffer
			sys.stdout.flush()
		return True
	def lifecycle(self, work = True):
		if self.ticks > 3:
			input("you deserve a big break.. you have 25 minutes. Press enter to start")
			self.current_task = "take a big break"
			self.start_timer(25 * 60)
			self.alarm()
			self.ticks = 0
			self.lifecycle()
			return
		elif work:
			self.setCurrentTask()
			self.start_timer(25 * 60)
			self.alarm()
			self.ticks += 1
			self.lifecycle(False)
			return
		else:
			input("press enter to start break")
			self.current_task = "take a break"
			self.start_timer(5 * 60)
			self.alarm()
			self.lifecycle()
			return
			
	def alarm(self, num=10):
		sound = AudioSegment.from_ogg("./sonar.ogg")
		for i in range(num):
			play(sound)
			time.sleep(1)
		return
        
	def setCurrentTask(self):
		self.current_task = input("What's your current task?")



pymodoro()