'''
class Student(object):
	name='Student'
	def __init__(self,name):
		self.name=name






s = Student('Bob')
s.score = 90

print(s.name)
print(Student.name)
'''

"""
class Student(object):

	def get_score(self):
		return self._score

	def set_score(self,value):
		if not isinstance(value,int):
			raise ValueError('score must be an integer!')

		if value<0 or value>100:
			raise ValueError('score must be between 0~100!')
		self._score=value

s=Student()
s.set_score(60)
print(s.get_score())
"""


# -*- coding: utf-8 -*-
class  Screen(object):
	"""docstring for  Screen"""
	@property
	def width(self):
	    return self._width

	@width.setter
	def width(self,width):
		self._width=width

	@property
	def height(self):
	    return self._height

	@height.setter
	def height(self,height):
		self._height=height

	@property
	def resolution(self):
	    return self._width*self._height

# test:
s = Screen()
s.width = 1024
s.height = 768
print(s.resolution)
assert s.resolution == 786432, '1024 * 768 = %d ?' % s.resolution
	













