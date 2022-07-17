import logging
from support_example import comunity_courses
import time

logging.basicConfig(filename="challenge.log", level=logging.DEBUG, format="%(levelname)s %(asctime)s %(message)s")


logging.info(123)


class ineuron:
    """ welcome to ineuron here e have multiple courses"""

    def __init__(self, new_student, course_purchased):
        self.__instructors = []
        self.__students = []

    def get_instructors_name(self):
        """extract instructors name"""
        try:
            logging.info("extracting instructors for the courses")
            logging.info(self.__instructors)
            return self.__instructors
        except Exception as e:
            logging.exception(e)

    def get_students_name(self):
        """extract students name"""
        try:
            logging.info("extracting students name enrolled for different courses")
            logging.info(self.__students)
            return self.__students
        except Exception as e:
            logging.exception(e)


# inheritance
class instructors(ineuron):
    """ this class consists instructors expertise as per their knowledge and  experience"""

    def __domain(self):
        self.domains = {
            'instructor_name1': ['area of expertise', 'experience', 'knowledge', 'languages and technologies']}
        return self.domains

    def your_instructor(self, instructor_name):
        print(instructors.__domain(self)[instructor_name])


obj1 = instructors('a', 'b')
obj1.your_instructor('instructor_name1')


# class courses(comunity_courses):
#
#     def FSDS(self):
#         try:
#             logging.info("Full stack  data science  boot camp")
#             self.topics = {'topic1': ['subtopics', 'f', 'u', 'n']}
#         except Exception as e:
#             logging.exception(e)


# multiple inheritance + multilevel inheritance
# class students(ineuron, courses):
#
#     def students_id(self):
#         try:
#             logging.info()
#         except Exception as e:
#             logging.exception(e)


# multiple inheritance + multilevel inheritance
class hackathon(instructors):

    def __init__(self):
        self.__time = time.asctime()

    def set_time(self):
        """ setting up timing for next hackathon"""
        self.hackathon_start_time = self.__time[:8] + str(int(self.__time[8:10]) + 5)
        return self.hackathon_start_time


# calling hackathon
obj = hackathon()
print(obj.set_time())
