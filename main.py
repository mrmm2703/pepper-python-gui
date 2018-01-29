import time
import sys
import datetime
import socket
import functions
import Tkinter as tk
from naoqi import ALProxy
from naoqi import ALModule
from naoqi import ALBroker

'''
TO-DO LIST:
T_OUTPUT: learnFace
T_OUTPUT: sayFace
T_OUTPUT: getGender
T_OUTPUT: visionRecog
T_OUTPUT: follow
T_OUTPUT: endFollow
'''

ROBOT_IP = None
ROBOT_PORT = None

tts = None
statustext = None

import animations as anim

class MyModule():
	def takePicture(self):
		self.photoproxy.setResolution(2)
		self.photoproxy.setPictureFormat("jpg")
		self.photoproxy.takePicture("/home/nao/moimages/", "image", True)
		
	def topicOutput(self, strVarName, value):
		print("ALMemory: Activated subscribed event 'output'")
		print("topicOutput: strVarName = " + str(strVarName))
		print("topicOutput: value = " + str(value))
		if value == "sayHello":
			self.o_sayHello()
		elif value == "surprised":
			self.o_surprised()
		elif value == "sing":
			self.o_sing()
		elif value == "rap":
			self.o_rap()
		elif value == "dab":
			self.o_dab()
		elif value == "subEnglish":
			self.o_subEnglish()
		elif value == "subComputing":
			self.o_subComputing()
		elif value == "standUp":
			self.o_standUp()
		elif value == "volQuiet":
			self.o_volQuiet()
		elif value == "volLoud":
			self.o_volLoud()
		elif value == "fly":
			self.o_fly()
		elif value == "laugh":
			self.o_laugh()
		elif value == "whipNaeNae":
			self.o_whipNaeNae()
		elif value == "time":
			self.o_time()
		elif value == "date":
			self.o_date()
		elif value == "squat":
			self.o_squat()
		elif value == "walk":
			self.o_walk()
		elif value == "macarena":
			self.o_macarena()
		elif value == "getTemp":
			self.o_getTemp()
		elif value == "battery":
			self.o_battery()
		elif value == "record":
			self.o_record()
		elif value == "unlearn":
			self.o_unlearn()
		elif value == "endApp":
			self.o_endApp()
			
	def o_walk():
		print("T_OUPUT: walk")
		self.motion.move(0.5, 0, 0)
		result == self.posture.goToPosture("Stand", 1)
		if(result):
			self.animtts.say("^mode(contextual) There we go!")
		else:
			self.animtts.say("^mode(contextual) I can't stand up!")
	
	def o_endApp():
		print("T_OUTPUT: endApp")
		print("------------------------------")
		print("ENDING APPLICATION")
		print("------------------------------")
		sys.exit()
	
	def o_unlearn():
		print("T_OUPUT: unlearn")
		self.facedetection.clearDatabase()
		self.animtts.say("^mode(contextual) I've cleared all faces on my database")
	
	def o_record():
		print("T_OUPUT: record")
		filepath = "/home/nao/morecordings/recording.wav"
		print("ALAudioDevice: Starting recording")
		self.animtts.say("^mode(contextual) I'll start recording now.")
		self.audiodevice.post.startMicrophonesRecording(filepath)
		time.sleep(5)
		print("ALAudioDevice: Stopping recording")
		self.animtts.say("^mode(contextual) That's it")
		self.audiodevice.stopMicrophonesRecording()
		print("ALAudioDevice: Stopped recording")
		print("ALAudioDevice: Playing recording")
		self.audio.playFile("/home/nao/morecordings/recording.wav")
		print("ALAudioDevice: Finished playing recording")
	
	def o_battery(self):
		print("T_OUPUT: battery")
		if functions.batteryCheck() == True:
			self.animtts.say("^mode(contextual) I am low on battery!")
		else:
			self.animtts.say("^mode(contextual) I am not low on battery!")
	
	def o_getTemp():
		print("T_OUTPUT: temp")
		tempstr = "^mode(contextual) It is " + str(functions.getTemp()) + " degrees celcius."
		animtts.say(tempstr)
	
	def o_macarena(self):
		print("T_OUTPUT: macarena")
		anim.anim_macarena_post()
		time.sleep(0.3)
		self.audio.play(sound_macarena)
	
	def o_squat():
		print("T_OUTPUT: squat")
		anim.anim_squat()
		self.animtts.say("^mode(contextual) I feel nice and refreshed now!")
	
	def o_date():
		print("T_OUTPUT: date")
		self.animtts.say("^mode(contextual) " + functions.getDate())

	def o_time():
		print("T_OUTPUT: time")
		self.animtts.say("^mode(contextual) " + functions.getTime())

	def o_whipNaeNae():
		print("T_OUTPUT: whipNaeNae")
		anim.anim_whipNaeNae()
		self.animtts.say("^mode(contextual) If I move too fast, my arms will break!")

	def o_laugh():
		print("T_OUTPUT: laugh")
		anim.anim_laugh()
		self.animtts.say("^mode(contextual) That was hilarious!")

	def o_fly():
		print("T_OUTPUT: fly")
		anim.anim_fly()
		self.animtts.say("^mode(contextual) Yay! I can fly!")

	def o_volLoud():
		print("T_OUTPUT: volLoud")
		self.audiodevice.setOutputVolume(100)

	def o_volQuiet():
		print("T_OUTPUT: volQuiet")
		self.audiodevice.setOutputVolume(30)

	def o_standUp():
		print("T_OUTPUT: stand")
		result == self.posture.goToPosture("Stand", 1)
		if(result):
			self.animtts.say("^mode(contextual) There we go!")
		else:
			self.animtts.say("^mode(contextual) I can't stand up!")

	def o_subComputing():
		print("T_OUTPUT: subComputing")
		anim.anim_typing()
		self.animtts.say("^mode(contextual) I love computing! It is the best! Just curious, do you prefer I O S or Android?")

	def o_subEnglish():
		print("T_OUTPUT: subEnglish")
		anim.anim_subEnglish()
		self.animtts.say("^mode(contextual) I don't.")

	def o_dab():
		print("T_OUTPUT: dab")
		anim.anim_dab()
		self.animtts.say("^mode(contextual) The felt amazing!")
	
	def o_rap(self):
		print("T_OUTPUT: rap")
		anim.anim_rap_post()
		time.sleep(0.5)
		self.audio.play(sound_rap)
		self.animtts.say("^mode(contextual) That was good!")

	def o_sing(self):
		print("T_OUTPUT: sing")
		anim.anim_cough()
		self.audio.play(sound_clearingThroat)
		anim.anim_downFromCough()
		time.sleep(2)
		self.audio.post.play(sound_song)
		anim.anim_singingMovingHead()

	def o_sayHello(self):
		print("T_OUTPUT: sayHello")
		anim.anim_hello()

	def o_surprised(self):
		print("T_OUTPUT: surpised")
		anim.anim_handsOnHead()
		self.audio.play(sound_explosion)
		anim.anim_handsDownFromHead()
		self.animtts.say("^mode(contextual) Amazing, I know. Mind blown.")

	def disconnect(self):
		global statustext
		global connectbutton
		print("Disconnecting...")
		statustext = "Disconnecting"
		self.updatestatus()
		self.disableactionbuttons()
		print("TK: Disabled action buttons")
		connectbutton.config(state=tk.NORMAL)
		print("TK: Enable connect button")
		tempstr = str(computername) + " from " + str(localip) + " has disconnected."
		tts.say(tempstr)
		print("ALProxy: Sent disconnect message")	
		statustext = "Awaiting connection"
		self.updatestatus()

	def disableactionbuttons(self):
		global macarenabutton
		global wavebutton
		global rapbutton
		global disconnectbutton
		global squatbutton
		global surprisedbutton
		global singbutton
		global tempbutton
		global dabbutton
		global walkbutton
		global standbutton
		macarenabutton.config(state=tk.DISABLED)
		wavebutton.config(state=tk.DISABLED)
		rapbutton.config(state=tk.DISABLED)
		disconnectbutton.config(state=tk.DISABLED)
		squatbutton.config(state=tk.DISABLED)
		surprisedbutton.config(state=tk.DISABLED)
		singbutton.config(state=tk.DISABLED)
		tempbutton.config(state=tk.DISABLED)
		dabbutton.config(state=tk.DISABLED)
		walkbutton.config(state=tk.DISABLED)
		standbutton.config(state=tk.DISABLED)
		

	def enableactionbuttons(self):
		global macarenabutton
		global wavebutton
		global rapbutton
		global disconnectbutton
		global squatbutton
		global surprisedbutton
		global singbutton
		global tempbutton
		global dabbutton
		global walkbutton
		global standbutton
		macarenabutton.config(state=tk.NORMAL)
		wavebutton.config(state=tk.NORMAL)
		rapbutton.config(state=tk.NORMAL)
		disconnectbutton.config(state=tk.NORMAL)
		squatbutton.config(state=tk.NORMAL)
		surprisedbutton.config(state=tk.NORMAL)
		singbutton.config(state=tk.NORMAL)
		tempbutton.config(state=tk.NORMAL)
		dabbutton.config(state=tk.NORMAL)
		walkbutton.config(state=tk.NORMAL)
		standbutton.config(state=tk.NORMAL)

	def updatestatus(self):
		global statuslabel
		global statustext
		statuslabel.config(text=statustext)

	def connect(self):
		global ROBOT_IP
		global ROBOT_PORT
		global tts
		global memory
		global dialog
		global audio
		global statustext
		global connected
		global computername
		global localip
		global connectbutton
		global sound_macarena
		global sound_explosion
		global topic
		ROBOT_IP = str(ipentry.get())
		ROBOT_PORT = int(portentry.get())
		tts = ALProxy("ALTextToSpeech", ROBOT_IP, ROBOT_PORT)
		print("ALProxy: Successfully connected to ALTextToSpeech on " + str(ROBOT_IP) + ":" + str(ROBOT_PORT))
		memory = ALProxy("ALMemory", ROBOT_IP, ROBOT_PORT)
		print("ALProxy: Successfully connected to ALMemory on " + str(ROBOT_IP) + ":" + str(ROBOT_PORT))
		dialog = ALProxy("ALDialog", ROBOT_IP, ROBOT_PORT)
		print("ALProxy: Successfully connected to ALDialog on " + str(ROBOT_IP) + ":" + str(ROBOT_PORT))
		dialog.setLanguage("English")
		print("ALDialog: Set language to English")
		audio = ALProxy("ALAudioPlayer", ROBOT_IP, ROBOT_PORT)
		print("ALProxy: Successfully connected to ALAudioPlayer on " + str(ROBOT_IP) + ":" + str(ROBOT_PORT))
		animtts = ALProxy("ALAnimatedSpeech", ROBOT_IP, ROBOT_PORT)
		print("ALProxy: Successfully connected to ALAnimatedSpeech on " + str(ROBOT_IP) + ":" + str(ROBOT_PORT))
		posture = ALProxy("ALRobotPosture", ROBOT_IP, ROBOT_PORT)
		print("ALProxy: Successfully connected to ALRobotPosture on " + str(ROBOT_IP) + ":" + str(ROBOT_PORT))
		photoproxy = ALProxy("ALPhotoCapture", ROBOT_IP, ROBOT_PORT)
		print("ALProxy: Successfully connected to ALPhotoCapture on " + str(ROBOT_IP) + ":" + str(ROBOT_PORT))
		'''
		audiodevice = ALProxy("ALAudioDevice", ROBOT_IP, ROBOT_PORT)
		print("ALProxy: Successfully connected to ALAudioDevice on " + str(ROBOT_IP) + ":" + str(ROBOT_PORT))
		facedetection = ALProxy("ALFaceDetection", ROBOT_IP, ROBOT_PORT)
		print("ALProxy: Successfully connected to ALFaceDetection on " + str(ROBOT_IP) + ":" + str(ROBOT_PORT))
		facec = ALProxy("ALFaceCharacteristics", ROBOT_IP, ROBOT_PORT)
		print("ALProxy: Successfully connected to ALFaceCharacteristics on " + str(ROBOT_IP) + ":" + str(ROBOT_PORT))
		'''
		try:
			sound_macarena = audio.loadFile("/home/nao/Macarena.wav")
			print("ALAudioPlayer: Loaded macarena.wav")
		except:
			print("Could not load /home/nao/macarena.wav. Please use scp to transfer to robot")
			print("Ignore error if using a virtual robot")
		try:
			sound_explosion = audio.loadFile("/home/nao/explosion.wav")
			print("ALAudioPlayer: Loaded explosion.wav")
		except:
			print("Could not load /home/nao/explosion.wav. Please use scp to transfer to robot")
			print("Ignore error if using a virtual robot")
		try:
			sound_clearingThroat = audio.loadFile("/home/nao/clearingThroat.wav")
			print("ALAudioPlayer: Loaded clearingThroat.wav")
		except:
			print("Could not load /home/nao/clearingThroat.wav. Please use scp to transfer to robot")
			print("Ignore error if using a virtual robot")
		try:
			sound_song = audio.loadFile("/home/nao/songPartOne.wav")
			print("ALAudioPlayer: Loaded song.wav")
		except:
			print("Could not load /home/nao/song.wav. Please use scp to transfer to robot")
			print("Ignore error if using a virtual robot")
		try:
			sound_rap = audio.loadFile("/home/nao/rap.wav")
			print("ALAudioPlayer: Loaded rap.wav")
		except:
			print("Could not load /home/nao/rap.wav. Please use scp to transfer to robot")
			print("Ignore error if using a virtual robot")
		try:
			topic = dialog.loadTopic("/home/nao/TopicOne_enu.top")
			print("ALDialog: Found topic")
		except:
			print("Could not load topic")
		try:
			dialog.activateTopic(topic)
			print("AlDialog: Activated topic")
		except:
			print("Could not activate topic")
		try:
			memory.subscribeToEvent("output", self.name, "topicOutput")
			print("ALMemory: Subscribed to event 'ouput'")
		except:
			print("Could not subscribe to event")
		statustext = "Connected to " + str(ROBOT_IP) + ":" + str(ROBOT_PORT)
		anim.anim_storevar(ROBOT_IP, ROBOT_PORT)
		print("ANIM: Successfully completed anim_storevar")
		self.updatestatus()
		try:
			functions.func_connect(ROBOT_IP, ROBOT_PORT)
			print("FUNCTIONS: Connected to ALMemory on " + str(ROBOT_IP) + ":" + str(ROBOT_PORT))
		except:
			print("ERR - FUNCTIONS: Could not connect to ALMemory on " + str(ROBOT_IP) + ":" + str(ROBOT_PORT))
		computername = str(socket.gethostname())
		localip = str(socket.gethostbyname(computername))
		tempstr = str(computername) + " has connected to me from " + str(localip)
		# tts.say(tempstr)
		self.enableactionbuttons()
		print("TK: Action buttons have been enabled")
		connectbutton.config(state=tk.DISABLED)
		print("TK: Connect button has been disabled")
		connected = True
		print("Set connected variable to true")

	
classname = MyModule()
global root
root = tk.Tk()
root.title("Connect to Pepper")
iplabel = tk.Label(root, text="IP:")
iplabel.grid(row=0, column=0)
ipentry = tk.Entry(root, width=30)
ipentry.grid(row=0, column=1)
ipentry.delete(0, tk.END)
ipentry.insert(0, "localhost")
portlabel = tk.Label(root, text="Port:")
portlabel.grid(row=1, column=0)
portentry = tk.Entry(root, width=30)
portentry.grid(row=1, column=1)
portentry.delete(0, tk.END)
portentry.insert(0, "33487")
connectionframe = tk.Frame(root)
connectionframe.grid(row=2, columnspan=2)
connectbutton = tk.Button(connectionframe, text="Connect", command=classname.connect)
connectbutton.grid(row=0, column=0)
disconnectbutton = tk.Button(connectionframe, text="Disconnect", command=classname.disconnect, state=tk.DISABLED)
disconnectbutton.grid(row=0, column=1)
statuslabel = tk.Label(root, text="Awaiting connection")
statuslabel.grid(row=3, columnspan=2)
actionslabel = tk.Label(root, text="Actions:")
actionslabel.grid(row=4, columnspan=2)
actionframe = tk.Frame(root)
actionframe.grid(row=5, columnspan=2)
actionframe1 = tk.Frame(actionframe)
actionframe1.grid(row=0, column=0)
actionframe2 = tk.Frame(actionframe)
actionframe2.grid(row=1, column=0)
actionframe3 = tk.Frame(actionframe)
actionframe3.grid(row=2, column=0)
macarenabutton = tk.Button(actionframe1, text="Macarena", command=classname.o_macarena, state=tk.DISABLED)
macarenabutton.pack(side=tk.LEFT)
wavebutton = tk.Button(actionframe1, text="Wave", command=anim.anim_hello, state=tk.DISABLED)
wavebutton.pack(side=tk.LEFT)
rapbutton = tk.Button(actionframe1, text="Rap", command=anim.anim_rap, state=tk.DISABLED)
rapbutton.pack(side=tk.LEFT)
squatbutton = tk.Button(actionframe1, text="Squat", command=anim.anim_squat, state=tk.DISABLED)
squatbutton.pack(side=tk.LEFT)
surprisedbutton = tk.Button(actionframe2, text="Surprised?", command=classname.o_surprised, state=tk.DISABLED)
surprisedbutton.pack(side=tk.LEFT)
singbutton = tk.Button(actionframe2, text="Sing", command=classname.o_sing, state=tk.DISABLED)
singbutton.pack(side=tk.LEFT)
tempbutton = tk.Button(actionframe2, text="Temperature", command=classname.o_getTemp, state=tk.DISABLED)
tempbutton.pack(side=tk.LEFT)
dabbutton = tk.Button(actionframe3, text="Dab", command=anim.anim_dab, state=tk.DISABLED)
dabbutton.pack(side=tk.LEFT)
walkbutton = tk.Button(actionframe3, text="Walk", command=classname.o_walk, state=tk.DISABLED)
walkbutton.pack(side=tk.LEFT)
standbutton = tk.Button(actionframe3, text="Stand", command=classname.o_standUp, state=tk.DISABLED)
standbutton.pack(side=tk.LEFT)
root.mainloop()