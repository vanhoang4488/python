class A():

	__last_name = "hoang"

	def __init__(self, first_name, last_name):
		self.__first_name = first_name
		self.__last_name = last_name

	def get_first_name(self):
		return self.__last_name;

a = A("nguyen", "hoang")
print(a.get_first_name())

