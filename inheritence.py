#single inheritence
print('"single inheritence"')
class dada():
    def mouse(self):
        print("Use mouse")
class daughter(dada):# for Interlink the both classes use, class name of 1st within the 2nd class brackets
    def keyboard(self):
        print("Use keyboard")
gopi=daughter()
gopi.mouse()

print("_*__*__*__*__*__*__")

#Multiple inheritence
print('"Multiple inheritence"')
class father():
    def water(self):
        print("Drink water ")
class mother():
    def soda(self):
        print("Drink soda ")
class boy_son(father,mother):# for Interlink the two classes with one, use class name of 1st and 2nd within the 3rd class brackets
    def chilly(self):
        print("i eat chilly")
ram=boy_son()
ram.soda()
ram.water()
print("_*__*__*__*__*__*__")

#Multiple level inheritence
#Here class 1 is linked with class 2 is linked with the  class 3,So each is inherites with each
print('"Multiple level inheritence"')
class dady():   #class 1
    def money(self):
        print("money ")
class mummy(dady): #class 2#class 2,here class 2 needs the class 1 so it using class 1
    def scooty(self):
        print("keys ")
class boy_baby(mummy): #class 3,here class 3 needs the class 2 so it using class 2 (boy_baby(mummy))
    def ride(self):
        print("ride")
abi= boy_baby()
abi.ride()
abi.scooty()
abi.money()


m1=mummy()
m1.money()

print("_*__*__*__*__*__*__")
#Hierarchical Inheritance
print("Hierarchical Inheritance")
#base class is one if one base class is dervied for two pt more is known as Hierarchical Inheritance
class dad():#base class
    def mokeys(self):
        print("money phone")


class son1 (dad):#class1
    pass
class son2 (dad):#class2
    pass
class son3 (dad):#class3
    pass
s3=son3()
s3.mokeys()

#Hierarchical Inheritance
#the all inheritence are coupled
print("Hybrid Inheritance")
class grandpa():
    def sell(self):
        print("land sell")
class land():
    def important(self):
        print("land important")
class sons1 (grandpa,land):#class1
    pass
class sons2 (grandpa):#class2
    pass
class sons3 (grandpa):#class3
    pass
s1=son1()
