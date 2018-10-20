class Udacian:
    def __init__(self, name, city, enrollment, nandoegree, status):
        self.name = name
        self.city = city
        self.enrollment = enrollment
        self.nandoegree = nandoegree
        self.status = status


    def print_ud(self):
        return self.name + "; " + self.city + ", " + self.enrollment + ", " + self.nanodegree + ", " + self.status
