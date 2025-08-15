class Parent():
    def greet(self):
        print("hello")

class Child(Parent):
    pass

c = Child()
c.greet()