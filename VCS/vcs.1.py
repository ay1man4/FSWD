
class Udacian:

    def __init__(self, name, city, enrollment, nanodegree, status):
        self.name = name
        self.city = city
        self.enrollment = enrollment
        self.nanodegree = nanodegree
        self.status = status
    
    def udacian(self):
        return self.name + ", " + self.city + ", " + self.enrollment + ", " + self.nanodegree + ", " + self.status


udacian = Udacian('Ayman', 'Jeddah', 'Udacity', 'FSWD', 'active')
print (udacian.udacian())

       
    
