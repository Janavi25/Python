# Person
#   - name
#   - talk()

class Person():
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f"hi There ,How are you {self.name}?")


Janavi = Person("Janavi Panchal")
Janavi.talk()

Jaimit = Person("Jaimit Panchal")
Jaimit.talk()
