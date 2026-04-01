# HOMEWORK 1: DIFFERENCE BETWEEN FUNCTIONS AND METHODS

"""
1. A function is a block of code that is defined independently and 
   exists outside of any class structure.
2. A method is a function that is defined within a class and is 
   specifically associated with an instance of that class.

-------------------------------------------------------------------------------------------------
| FEATURE           | FUNCTION                                  | METHOD                        |
|-------------------|-------------------------------------------|-------------------------------|
| DEFINITION        | A function is defined outside of a class. | A method is defined inside.   |
| DEPENDENCY        | It is entirely independent of objects.    | It is tied to a specific class. |
| HOW TO CALL       | It is called simply by its name.          | It is called on an object.    |
| DATA ACCESS       | It only uses the data you pass to it.     | It can access internal data.  |
| FIRST PARAMETER   | It does not require any special parameter.| It usually requires 'self'.   |
-------------------------------------------------------------------------------------------------
"""

# HOMEWORK 2: 5 ClASSES

# Class 1: Cooler
class Cooler:
    def __init__(self, size, color):
        self.size = size
        self.color = color
    def display(self):
        print(f'The size of cooler is {self.size} and color is {self.color}.')

cool1 = Cooler(35.12, 'Silver')
cool1.display()

# Class 2: Fan
class Fan:
    def __init__(self, blades, speed):
        self.blades = blades
        self.speed = speed
    def show(self):
        print(f'Number of blades fan have {self.blades} and Fan speed is {self.speed}.')

fan1 = Fan(4, 50)
fan1.show()

# Class 3: Washing Machine
class W_Machine:
    def __init__(self, kg, warentee):
        self.kg = kg
        self.warentee = warentee
    def see(self):
        print(f'Washing Machine can wash {self.kg} cloths at time. It has {self.warentee} Warranty.')

wm1 = W_Machine('8 KG', '1 Year')
wm1.see()

# Class 4: Shoes
class Shoes:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price
    def detail(self):
        print(f'Shoe is manufactured by {self.brand} Company. Its price is {self.price}.')

shoe1 = Shoes('Adidas', 5000)
shoe1.detail()

# Class 5: Bed
class Bed:
    def __init__(self, height, width):
        self.height = height
        self.width = width
    def size_of_bed(self):
        print(f'The height & width of bed is {self.height} and {self.width}.')

bed1 = Bed(6, 5)
bed1.size_of_bed()


# HOMEWORK 3: 

class Players:
    def __init__(self, j_no, p_name, runs, t_name):
        self.jersey_no = j_no
        self.name = p_name
        self.run = runs
        self.team = t_name

    def display(self):
        print(f' Jersey no : {self.jersey_no}, Name : {self.name}, Runs : {self.run}, Team : {self.team}')
p1 = Players(20, 'Axar Patel', 1916, 'DC')
p2 = Players(1, 'KL Rahul', 4683, 'DC')
p3 = Players(23, 'Kuldeep Yadav', 201, 'DC')
p4 = Players(30, 'Tristan Stubbs', 655, 'DC')
p5 = Players(56, 'Mitchell Starc', 125, 'DC')
p6 = Players(44, 'T. Natarajan', 15, 'DC')
p7 = Players(10, 'David Miller', 2812, 'DC')
p8 = Players(27, 'Nitish Rana', 2636, 'DC')
p9 = Players(24, 'Abishek Porel', 550, 'DC')
p10 = Players(100, 'Prithvi Shaw', 1988, 'DC')
p11 = Players(49, 'Mukesh Kumar', 10, 'DC')

dc_squad = []

dc_squad.append(p1)
dc_squad.append(p2)
dc_squad.append(p3)
dc_squad.append(p4)
dc_squad.append(p5)
dc_squad.append(p6)
dc_squad.append(p7)
dc_squad.append(p8)
dc_squad.append(p9)
dc_squad.append(p10)
dc_squad.append(p11)

print("--- FULL DELHI CAPITALS 2026 SQUAD ---")
for player in dc_squad:
    player.display()