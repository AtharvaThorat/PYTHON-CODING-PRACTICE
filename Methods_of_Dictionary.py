#clear() method
Team = {
  "Name": "Liverpool",
  "Captain": "Henderson",
  "Established": 1996
}

Team.clear()

print(Team)

#copy() method
bike = {
  "brand": "Royal Enfield",
  "model": "Classic",
  "year": 2015
}

x = bike.copy()

print(x)

#Fromkey() method
x = ('key1', 'key2', 'key3')
y = 3

thisdict = dict.fromkeys(x, y)

print(thisdict)

#get() method
Mobile = {
  "brand": "Apple",
  "model": "13 pro max",
  "year": 2021
}

x = Mobile.get("model")

print(x)

#item() method
Tesla = {
  "Founder": "Elon Musk",
  "Business": "Cars",
  "year": 2003
}

x = Tesla.items()

print(x)

#keys() method
Amazon = {
  "Founder": "Jeff Bezoz",
  "CEO": "Andy Jassy",
  "year": 1994
}

x = Amazon.keys()

print(x)

#pop() method
car = {
  "brand": "Tata",
  "model": "Indica",
  "year": 1999
}

car.pop("model")

print(car)

#popitem() method
App = {
  "name": "Instagram",
  "Usage": "Social media",
  "Followers": 893
}

App.popitem()

print(App)

#setdefault() method

Language = {
  "Name": "Python",
  "Os": "Windows",
  "year": 1991
}

x = Language.setdefault("File extension", ".py")

print(x)

#update() method
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

car.update({"color": "White"})

print(car)

#values() method
Place = {
  "Country": "Spain",
  "Capital": "Madrid",
  "World Cup": 2012
}

x = Place.values()

print(x) 
