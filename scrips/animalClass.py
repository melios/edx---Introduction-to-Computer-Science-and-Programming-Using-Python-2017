import random

class Animal(object):

    def __init__(self, age):
        self.age = age
        self.name = None

    def get_age(self):
        return self.age

    def get_name(self):
        return self.name

    def set_age(self, newage):
        self.age = newage

    def set_name(self, newname = ''):
        self.name = newname

    def __str__(self):
        return ("Animal's name is '{0}' and its ages is '{1}'").format(self.get_name(), self.get_age())


class Cat(Animal):
    def speak(self):
        print('meow')

    def __str__(self):
        return ("Cats's name is '{0}' and its ages is '{1}'").format(self.get_name(), self.get_age())


# class Rabbit(Animal):
#     def speak(self):
#         print('meep')
#
#     def __str__(self):
#         return ("Rabbit's name is '{0}' and its ages is '{1}'").format(self.get_name(), self.get_age())

class Rabbit(Animal):

    # a class variable, tag, shared across all instances
    tag = 1
    def __init__(self, age, parent1=None, parent2=None):
        Animal.__init__(self, age)
        self.parent1 = parent1
        self.parent2 = parent2
        self.rid = Rabbit.tag
        Rabbit.tag += 1
    def get_rid(self):
        # zfill used to add leading zeroes 001 instead of 1
        return str(self.rid).zfill(3)
    def get_parent1(self):
        return self.parent1
    def get_parent2(self):
        return self.parent2
    def __add__(self, other):
        # returning object of same type as this class
        return Rabbit(0, self, other)
    def __eq__(self, other):
        # compare the ids of self and other's parents
        # don't care about the order of the parents
        # the backslash tells python I want to break up my line
        parents_same = self.parent1.rid == other.parent1.rid \
                       and self.parent2.rid == other.parent2.rid
        parents_opposite = self.parent2.rid == other.parent1.rid \
                           and self.parent1.rid == other.parent2.rid
        return parents_same or parents_opposite
    def __str__(self):
        return "rabbit:"+ self.get_rid()

    def get_parrents(self):
        return ("Rabbit's name is '{0}', its father name is '{1}' and its mother name is '{2}' and its id is '{3}' ").format(self.get_name(), self.get_parent1(), self.get_parent2(), self.get_rid())

    def set_parent1(self, parent1):
        self.parent1 = parent1
    #
    def set_parent2(self, parent2):
        self.parent2 = parent2
    #

    def speak(self):
        print('meep')

    def __str__(self):
       return ("Rabbit's name is '{0}' and its ages is '{1}'").format(self.get_name(), self.get_age())
        #return "rabbit:"+ self.get_rid()

class Person(Animal):
    def __init__(self, age, name):
        Animal.__init__(self, age)
        Animal.set_name(self, name)
        self.friend = []

    def get_friend(self):
        return self.friend

    def add_friend(self, fname):
        if fname not in self.friend:
            self.friend.append(fname)

    def speak(self):
        print('Hello!')

    def age_difference(self, other):
        #diff = self.get_age() - other.get_age()
        diff = self.age - other.age
        if self.age > other.age:
            print (("'{0}' is {1} years older than '{2}'").format(self.get_name(), diff, other.get_name()))
        else:
            print( ("'{0}' is {1} years younger than '{2}'").format(self.get_name(), diff, other.get_name()))

    def __str__(self):
        return ("Person's name is '{0}' and its ages is '{1}'").format(self.get_name(), self.get_age())


class Student(Person):
    def __init__(self, age, name, major = None):
        Person.__init__(self, age, name)
        self.major = major

    def change_major(self, major):
        self.major = major

    def speak(self):
        r = random.random()
        if r < 0.25:
            print('I have homework')
        elif 0.25 <= r < 0.5:
            print('I need sleep')
        elif 0.5 <= r < 0.75:
            print('I should eat')
        else:
            print('I am watching TV')

    def __str__(self):
        return ("Student's name is '{0}', ages is '{1}', major is '{2}'").format(self.get_name(), self.get_age(), self.major)

if __name__ == "__main__":
    print('===start===')
    myAnimal = Animal(3)
    print(myAnimal)
    print('===Import name===')
    myAnimal.set_name('Melios')
    print(myAnimal)
    print('===Change Age===')
    myAnimal.set_age(6)
    print(myAnimal)
    print('====Import a Cat===')
    jelly = Cat(1)
    jelly.speak()
    jelly.get_name()
    print("====Import a Cat's name ===")
    jelly.set_name('Jelly Belly')
    print(jelly)
    print('====Cats take Animals print=====')
    print(Animal.__str__(jelly))

    print('====Import a rabbit===')
    petter = Rabbit(5)
    jelly.speak()
    petter.speak()
    #
    print('====Import pesrons===')

    eric = Person(45, 'eric')
    john = Person(55, 'John')
    tania = Person(37, 'Tania')
    eric.age_difference(tania)
    Person.age_difference(john, eric)

    print('====Import Rabits===')
    melios = Rabbit(4)
    melios.set_name('Melios')
    eleutheria = Rabbit(3)
    eleutheria.set_name('Eleutheria')

    xristos = melios + eleutheria

    xristos.set_parent2(eleutheria)
    xristos.set_parent1(melios)
    print(xristos.get_parent1())
    print(xristos.get_parent2())
    print(xristos.get_rid(), melios.get_rid(), eleutheria.get_rid())
    theodoti = Rabbit(5, melios, eleutheria)
    theodoti.set_name('Theodoti')
    print(theodoti.get_parent1())
    print(theodoti.get_parent2())
    print(xristos.get_parrents())
    print(theodoti.get_parrents())
    print(theodoti.get_rid())
    eleni = melios + eleutheria

    print(xristos.parent1.rid)
    print(theodoti.parent1.rid)
    print(eleni == xristos)


