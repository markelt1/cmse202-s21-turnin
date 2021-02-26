# The Student class (you'll edit and expand on this)
class Student():
    '''
    This class is designed to include information about individual students.
    Currently this class has the following attributes:
    
    name : this is the student's name
    gpa : this is the student's curret gpa
    '''
    
    def __init__(self, name='', gpa=0.0, year= 0):
        self.name = name
        self.gpa = gpa
        self.year = year
        
    def get_name(self):
        '''
        This function prints the name of the student
        '''
        print("My name is", self.name)
    
    def enroll(self, courses):
        self.courses = courses
        
    def display_courses(self):
        print( 'I am enrolled in:', self.courses)
        return
        
    def years_until_graduation(self):
        print('I will graduate in', (4 - self.year), 'years')
        return
    

class Spartan(Student):
    
    def set_motto(self, motto= ''):
        self.motto = motto
      
    def school_spirit(self):
        print(self.get_name())
        print('I am a Spartan. My motto is', self.motto)
    