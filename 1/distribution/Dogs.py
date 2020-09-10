class Dog():
	def __init__(self, name):
		self.name = name
		self.age = 0
		self.sticks_fetched = 0
	
	def grow(self):
		self.age += 1

	def fetch_sticks(self, sticks):
		self.sticks_fetched += sticks

	# Define __str__ method

class LazyDog(Dog):
    def fetch_sticks(self, sticks):
        if sticks > 5:
            return
        self.sticks_fetched += sticks

    def sleep(self):
        print("zzzzzzzzzz")

		