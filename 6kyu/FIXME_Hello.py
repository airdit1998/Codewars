"""
The code provided has a method hello which is supposed to show only those attributes
which have been explicitly set. Furthermore,
it is supposed to say them in the same order they were set.

But it's not working properly.

Notes

There are 3 attributes

name
age
sex ('M' or 'F')
When the same attribute is assigned multiple times the hello method shows it only once.
If this happens the order depends on the first assignment of that attribute,
but the value is from the last assignment.
"""


class Dinglemouse(object):

    def __init__(self):
        self.output_string = "Hello."
        self.call_list = []

        self.age_string = ''
        self.sex_string = ''
        self.name_string = ''

    def setAge(self, age):
        self.age_string = f" I am {age}." if age else ""
        #self.call_list.append(self.age_string) if self
        return self

    def setSex(self, sex):
        self.sex_string = f" I am {'male' if sex == 'M' else 'female'}." if sex else ""
        return self

    def setName(self, name):
        self.name_string = f" My name is {name}." if name else ""
        return self

    def hello(self):
        return self.output_string


a = Dinglemouse().setAge(27).setSex('M').setName('Dick').setAge(37)
print(a.hello())
