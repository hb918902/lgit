"""
class Student(object):
	@property
	def score(self):
	    return self._score


	@score.setter
	def score(self,value):
		if not isinstance(value,int):
			raise ValueError('score must be an integer')
		if value<0 or value >100:
			raise ValueError('score must between 0~100!')
		self._score=value
		
s=Student()
s.score=60
print(s.score)
#s.score=300
#print(s.score)	
"""


"""
class Screen(object):

    def __init__(self, height):
        self.__height = height

    @property
    def width(self):
        print('through getter: ')
        return self.__width

    @width.setter
    def width(self, width):
        # add some checks...
        print('through setter: %s' % width)
        self.__width = width

    @property
    def resolution(self):
        return self.__width**2

s = Screen(80)
s.width = 60  # 转化为setter操作
print(s.width)  # 转化为getter操作

# 尽管定义时采用了双下划线,但是仍然可以直接访问???
s.__width= 50  # 不经过setter
print(s.__width)  # 不经过get ter
print(s.width)  # 经过getter，而且没有受到上两行的影响？？

# 这里地__height就不可以访问了. 
# print(s.__height)
"""
'''
class Student(object):
	"""docstring for Student"""
	def __init__(self, name):
		self.name = name
	def __str__(self):
		return 'Student  object(name : %s)' % self.name
print(Student('Micheal'))
'''

"""
class Fib(object):
	def __init__(self):
		self.a,self.b=0,1	

	def __iter__(self):
		return self

	def __next__ (self):
		self.a,self.b=self.b,self.a+self.b
		if self.a>1000:
			raise StopIteration();
		return self.a

for n in Fib():
	print(n)
"""


#from enum import Enum 
#Month=Enum('Month',('jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'))

'''
class FooError(ValueError):
	"""docstring for FooError"""
	pass

def foo(s):
	n=int(s)
	if n==0:
		raise FooError('invalid value:%s'%s)
	return 10/n

foo('0')
'''



def foo(s):
    n = int(s)
    if n==0:
        raise ValueError('invalid value: %s' % s)
    return 10 / n

def bar():
    try:
        foo('0')
    except ValueError as e:
        print('ValueError!')
        raise

bar()
