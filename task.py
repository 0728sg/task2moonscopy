from art import tprint
tprint("PYTHON")

class Hello:
    def tptint(self):
        print("Hello from the original class")
class NewClass(Hello):
    def tptint(self):
        print("Hello from the NewClass")
from class1 import NewClass
obj = NewClass()
obj.tptint()