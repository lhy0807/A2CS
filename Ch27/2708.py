# Tianhe Zhang
# Chapter 27.08


class Course(object):

	def __init__(self, title, maxStudent):
		# maxStudent
		self.title = title
		self.maxStudent = maxStudent
		self.num_lesson = 0
		self.lessons = []
		self.assess = None # this should be class Assessment

	def addLesson(self, new_lesson):
		if len(self.lessons) >= 50:
			raise IndexError("Max lesson exceeded")
		else:
			self.lessons.append(new_lesson)

	def addAssess(self, new_assess):
		self.assess = new_assess

	# Sometimes this function raises Unicode Error ????
	def __str__(self):
		return "Course\nTitle: {}\nMax Student: {}\nLesson Number: {}\nLessons: {}\nAssessment: {}".format(self.title,\
			self.maxStudent, self.num_lesson, self.lessons, self.assess)

class Lesson(object):

	def __init__(self, title, duration, lab):
		self.title = title
		self.duration = duration
		self.lab = lab

	def __repr__(self):
		return "\nTitle: {}\nDuration: {}\nLab Requirement: {}\n".format(self.title, \
			self.duration, self.lab)

class Assessment(object):

	def __init__(self, title, maxMark):
		self.title = title
		self.maxMark = maxMark

	def __str__(self):
		return "\nAssessment Title: {}\nMax Mark: {}\n".format(self.title, self.maxMark)

def test():
	c = Course("Operating System", 100)
	c.addLesson(Lesson("Scheduling", 10, True))
	c.addLesson(Lesson("Virtual Memory", 8, True))
	c.addAssess(Assessment("OS Kernal Development", 100))
	print(c)

# test()
