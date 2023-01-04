##nuttig voor mezelf om bij te leren, dingen vanuit de 95 vragen van huiswerk derde les
aa='hi'
print(a)
print(type(a))

x=20.5
print(type(x))
x = ["apple", "banana", "cherry"]
print(type(x))
x = ("apple", "banana", "cherry")
print(type(x))
x = {"name" : "John", "age" : 36}
print(type(x))

x=True
print(type(x))

fruits = ("apple", "banana", "cherry", "kiwi")
print(type(fruits))
print(fruits[1:3])
print(fruits[-1]) #geeft het einde, werk met negatieve waarden -2 geeft voorlaatste
print(fruits[-2])

fruits = {"apple", "banana", "cherry", "kiwi"}
print(type(fruits))

fruits.add("pear")
print(fruits)

more_fruits = ["orange", "mango", "grapes"]
fruits.update(more_fruits)
print(fruits)

fruits.remove("kiwi")
print(fruits)

fruits.discard("pear")
print(fruits)

##geen idee wat het verschil is t


car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(
car.get("model")
)

car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car["year"]
 = 
2020

a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:  #elif = elseif
  print("a and b are equal")

#op 1 lijn
print("Yes") if 5 > 2 else print("No")

#break: while stoppen bij een bepaalde conditie
i = 1
while i < 6:
  if i == 3:
    break
  i += 1


#continue: In the loop, when i is 3, jump directly to the next iteration.
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)
    #resultaat is dus 1 2 4 5 6

#bekijk later wat class juist is, ik weet niet wat dit is
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


persoon1 = Person("ella", 23)
print(persoon1)
print(type(persoon1))


