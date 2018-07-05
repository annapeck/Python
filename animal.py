class Animal:

	def __init__(self, name, health):
		self.name=name
		self.health=health
	def walk(self):
		self.health=self.health - 1
		return self
	def run(self):
		self.health=self.health - 5
		return self
	def displayHealth(self):
		print(self.health)
		return self

cat=Animal("pup", 10)
cat.walk().walk().walk().run().run().displayHealth()

class Dog(Animal):
	def __init__(self, name):
		super().__init__(name, 150)

	def pet(self):
		self.health=self.health + 5
		return self

dog=Dog("Snickers")

dog.walk().walk().walk().run().run().pet().fly().displayHealth()

class Dragon(Animal):
	def __init__(self, name):
		super().__init__(name, 170)

	def fly(self):
		self.health=self.health+10
		return self

	def displayHealth(self):
		print("I am a Dragon")
		super().displayHealth()
		return self
dragon=Dragon("Fire")
dragon.fly().displayHealth()

class Lizard(Animal):
	def __init__(self,name):
		super().__init__(name, 30)

lizard=Lizard("Green")
lizard.fly().pet().displayHealth()

