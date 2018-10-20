class Udacian:
    def __init__(self, name, city, enrollment, nanodegree, status):
        self.name = name
        self.city = city
        self.enrollment = enrollment
        self.nanodegree = nanodegree
        self.status = status

    # by override __str__ we can use method str(udacian) to print Udacian object
    def __str__(self):
        return self.name + ": " + self.city + ", " + self.enrollment + ", " + self.nanodegree + ", " + self.status