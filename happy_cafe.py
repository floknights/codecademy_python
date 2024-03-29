class Business:
  def __init__(self, name, franchises):
    self.name = name
    self.franchises = franchises

class Franchise:
  def __init__(self, address, menus):
    self.address = address
    self.menus = menus

  def __repr__(self):
    return self.address

  def available_menus(self, time):
    available = []
    for menu in self.menus:
      if menu.start_time <= time <= menu.end_time:
        available.append(menu)
    return available

class Menu:
  def __init__(self, name, items, start_time, end_time):
    self.name = name
    self.items = items
    self.start_time = start_time
    self.end_time = end_time

  def __repr__(self):
    return "{} menu available from {}:00 to {}:00".format(self.name, self.start_time, self.end_time)

  def calculate_bill(self, purchased_items):
    total = 0
    for purchased_item in purchased_items:
      if purchased_item in self.items:
        total += self.items[purchased_item]
    return total

#Brunch Menu
brunch_items = {
  'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50,
  'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50
  }
brunch = Menu("Brunch", brunch_items, 11, 16)

#Early Bird Menu
early_bird_items = {
  'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00
  }
early_bird = Menu("Early Bird", early_bird_items, 15, 18)

#Dinner Menu
dinner_items = {
  'crostini with eggplant caponata': 13.00, 'caesar salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00
  }
dinner = Menu("Dinner", dinner_items, 17, 23)

#Kids Menu
kids_items = {
  'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00
  }
kids = Menu("Kids", kids_items, 11, 21)

#Arepas Menu
arepas_items = {
  'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50
  }
arepas_menu = Menu("Arepas", arepas_items, 10, 20)

#print(brunch)
#print(brunch.calculate_bill(["pancakes", "home fries", "coffee"]))
#print(brunch.calculate_bill(["waffles", "orange juice"]))

#print(early_bird)
#print(early_bird.calculate_bill(["salumeria plate", "mushroom ravioli (vegan)"]))
    
menus = [brunch, early_bird, dinner, kids]

flagship_store = Franchise("1232 West End Road", [brunch, early_bird, dinner, kids])

new_installment = Franchise("12 East Mulberry Street", [brunch, early_bird, dinner, kids])

arepas_place = Franchise("189 Fitzgerald Aveune", [arepas_menu])

#print(flagship_store)
#print(flagship_store.available_menus(17))

happy_cafe = Business("Happy Cafe", [flagship_store, new_installment])

happy_arepa = Business("Happy Arepa", [arepas_place])

#print("Welcome to " + happy_arepa.name)
#print(happy_arepa.franchises[0].menus[0])
