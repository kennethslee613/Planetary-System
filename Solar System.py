import turtle
import math
import random

def randomColor():
    """Code is not used here but you may find it usefull"""
    return [random.random() for i in range(3)]
def randomnumber(num):
	return [random.random() for i in range(num)]
def randomint():
	return random.randrange(2,5)

class Sun:
	def __init__(self, center, size, color):
		self.center = center
		self.size = size
		self.color = color
		self.selection = 0

	def draw(self):
		turtle.penup()
		turtle.goto(self.center)
		turtle.dot(self.size,self.color)

	def getCenter(self):
		return self.center

	def setColor(self, color):
		self.color = color

	def inside(self, location):
		if location[0] ** 2 + location[1] ** 2 < (self.size / 2) ** 2:
			return True
		else:
			return False

	def onClick(self, location):
		if self.inside(location):
			self.color = randomColor()
			self.selection = 1
		else:
			self.selection = 0


class Planet(Sun):
	def __init__(self, orbitAround, orbitRadius, size, color, speed):
		self.orbitAround = orbitAround
		self.orbitRadius = orbitRadius
		self.size = size
		self.color = color
		self.speed = speed
		self.angle = 0
		self.selection = 0
		super().__init__(self.getCenter(), size, color)

	def getCenter(self):
		return [x+self.orbitRadius*f(self.angle)
					for x,f in zip(self.orbitAround.getCenter(), (math.sin,math.cos))]

	def move(self):
		self.angle += self.speed
		self.center = self.getCenter()


class SolarSystem:
	def __init__(self):
		self.sun = Sun((0, 0), 100, "yellow")
		self.planet = []
		self.moon = []
		for i in randomnumber(randomint()):
			self.planet.append(Planet(self.sun, randomint()*80, randomint()*15, randomColor(), randomint()*0.0009))
		for i in randomnumber(randomint()):
				self.moon.append(Planet(random.choice(self.planet), randomint()*30, randomint()*7, randomColor(), randomint()*0.0005))

	def draw(self):
		turtle.clear()
		#turtle.tracer(0, 0)
		self.sun.draw()
		for i in range(len(self.planet)):
			self.planet[i].move()
			self.planet[i].draw()
		for i in range(len(self.moon)):
			self.moon[i].move()
			self.moon[i].draw()
		screen.ontimer(self.draw, 0)

	def onClick(self, location):
		for i in self.planet:
			if (location[0] - i.getCenter()[0]) ** 2 + (location[1] - i.getCenter()[1]) ** 2 < (i.size / 2) ** 2:
				i.color = randomColor()
				i.selection = 1
			else:
				i.selection = 0
		for i in self.moon:
			if (location[0] - i.getCenter()[0]) ** 2 + (location[1] - i.getCenter()[1]) ** 2 < (i.size / 2) ** 2:
				i.color = randomColor()
				i.selection = 1
			else:
				i.selection = 0
		self.sun.onClick(location)


s = SolarSystem()

def onClick(x, y):
	s.onClick((x, y))

def keyRight():
	for i in s.planet:
		if i.selection == 1:
			i.orbitRadius += 5
		else:
			for j in s.moon:
				if j.selection == 1:
					j.orbitRadius += 2
				else:
					None

def keyLeft():
	for i in s.planet:
		if i.selection == 1:
			i.orbitRadius -= 5
		else:
			for j in s.moon:
				if j.selection == 1:
					j.orbitRadius -= 2
				else:
					None

def keyUp():
	for i in s.planet:
		if i.selection == 1:
			i.size += 2
		else:
			for j in s.moon:
				if j.selection == 1:
					j.size += 1
				else:
					if s.sun.selection == 1:
						s.sun.size += 0.75
					else:
						None

def keyDown():
	for i in s.planet:
		if i.selection == 1:
			i.size -= 2
		else:
			for j in s.moon:
				if j.selection == 1:
					j.size -= 1
				else:
					if s.sun.selection == 1:
						s.sun.size -= 0.75
					else:
						None

def keySpace():
	for i in s.planet:
		if i.selection == 1:
			i.color = randomColor()
		else:
			for j in s.moon:
				if j.selection == 1:
					j.color = randomColor()
				else:
					if s.sun.selection == 1:
						s.sun.color = randomColor()
					else:
						None

def keyN():
	for i in s.planet:
		if i.selection == 1:
			s.moon.append(Planet(i, randomint()*30, randomint()*7, randomColor(), randomint()*0.0005))
		else:
			None
	if s.sun.selection == 1:
		s.planet.append(Planet(s.sun, randomint()*80, randomint()*15, randomColor(), randomint()*0.0009))
	else:
		None




turtle.tracer(0, 0)
turtle.ht()
screen = turtle.Screen() #Needed for the following
screen.onkey(turtle.bye, "q") #quits if you press q
screen.ontimer(s.draw, 0) #Tells the system to call draw. Don’t call it directly
screen.onclick(onClick)
screen.onkey(keyRight, "Right")
screen.onkey(keyLeft, "Left")
screen.onkey(keyUp, "Up")
screen.onkey(keyDown, "Down")
screen.onkey(keySpace, "space")
screen.onkey(keyN, "n")
screen.listen()
screen.mainloop()