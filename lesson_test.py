from lesson import Lesson

# OK
lesson1 = Lesson("python", "messbah","mno-yrew",3)
print(lesson1.__dict__)

# ERROR
lesson2 = Lesson("ab", "hon","new-mia",4)
print(lesson2.__dict__)