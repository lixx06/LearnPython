
class Animal(object):
	__slots__ = ("weight", "age", "_birth")
	@property
	def birth(self):
		return self._birth
	@birth.setter
	def birth(self, value):
		self._birth = value
	@property
	def age(slef):
		return 2014 - slef._birth
	def eat(self):
		print "Animal is eatting"
	def __str__(slef):
		return "Animal object"
	__repr__ = __str__


class FlyableMixin(object):
	def fly(self):
		print "flying"

class RunableMixin(object):
	def run(self):
		print "running"

class Dog(Animal, RunableMixin):
	def eat(self):
		print "Dog is eatting"

class Fish(Animal):
	pass

def eat_twice(animal):
	animal.eat()
	animal.eat()

eat_twice(Animal())

eat_twice(Dog())

eat_twice(Fish())

#eat_twice(int())

a = Animal()
a.weight = 10
a.birth = 2012
print a.weight, a.age
print a,";",a,";",a
a
a

#a.sex = "male"

b = Dog()
b.run()

