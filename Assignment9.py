#Q.1 area and circumference of circle usin function.
class Circle:
    def __init__(self,radius):
        self.radius=radius
    def getArea(self):
        print(3.14*self.radius*self.radius)
    def getCircumference(self):
        print(2*3.14*self.radius)
radius=int(input("enter the radius: "))
c=Circle(radius)
c.getArea()
c.getCircumference()
        
#Q.2.create a student class and initialize with name and roll no.
class Student:
    def __init__(self,roll,name):
        self.name=name
        self.roll=roll
    def show(self):
        print(self.name,self.roll)
roll=int(input("enter roll no"))
name=input("enter name")
s1=Student(roll,name)
s1.show()


#.Q.3.create a temp class and convert into the celsius and farehnite.
class Temperature:
    def __init__(self,celcius,farenhiet):
        self.farenhiet=farenhiet
        self.celsius=celcius
    def getfarenhiet(self):
        print("farenhiet is",(1.8*self.celsius)+32)
    def getcelsius(self):
        print("celsius",(self.farenhiet-32)*0.55)
farenhiet=float(input("enter farenhiet"))
celsius=float(input("enter celsius"))
t=Temperature(celsius,farenhiet)
t.getfarenhiet()
t.getcelsius()

#Q.4.print movie namea nd diapaly it and update it.
class moviedetails:
    def __init__(self,moviename,artistname,rating,year):
        self.moviename=moviename
        self.artistname=artistname
        self.year=year
        self.rating=rating
    def getdisplay(self):
        print(self.moviename,self.artistname,self.year,self.rating)
    def update(self,moviename,artistname,rating,year):
        self.moviename=moviename
        self.artistname=artistname
        self.year=year
        self.rating=rating
        
c=moviedetails("race 3","salman",2018,5)
c.getdisplay()
c.update("sanju","ranveer",2018,4)
c.getdisplay()
#Q.5.print expenditure,saving and total salary.
class expenditure:
    def __init__(self,expenditure,saving):
        self.expenditure=expenditure
        self.saving=saving
    def getdisplay(self):
        print("expend is",self.expenditure,"saving is",self.saving)
    def getcalculation(self):
        print("total salary=",self.expenditure+self.saving)
        
c=expenditure(40000,50000)
c.getdisplay()
c.getcalculation()
        
    

