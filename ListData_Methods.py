#1 Python List append() Method
Countries = [ "France","Germany","Spain","Italy" ]
Countries.append("Argentina")
print(Countries)


#2 Python List clear() Method
Countries = [ "France","Germany","Spain","Italy" ]
Countries.clear()
print(Countries)


#3 Python List copy() Method
Countries = [ "France","Germany","Spain","Italy" ]
x = Countries.copy()
print(Countries)


#4 Python List count() Method
Countries = [ "France","Germany","Spain","Italy" ]
x = Countries.count("Germany")
print(Countries)


#5 Python List extend() Method
Countries = [ "France","Germany","Spain","Italy" ]

cars = ['Ford', 'BMW', 'Volvo']

Countries.extend(cars)
print(Countries)


#6 Python List index() Method
Countries = [ "France","Germany","Spain","Italy" ]

x = Countries.index("Spain")
print(Countries)


#7 Python List insert() Method
Countries = [ "France","Germany","Spain","Italy" ]

Countries.insert(1, "India") 
print(Countries)


#8 Python List pop() Method
Countries = [ "France","Germany","Spain","Italy" ]

Countries.pop(3) 
print(Countries)


#9 Python List remove() Method
Countries = [ "France","Germany","Spain","Italy" ]

Countries.remove("Italy") 
print(Countries)


#10 Python List reverse() Method
Countries = [ "France","Germany","Spain","Italy" ]

Countries.reverse()
print(Countries)


#11 Python List sort() Method
cars = ['Ford', 'BMW', 'Volvo']

cars.sort()
print(Countries)
