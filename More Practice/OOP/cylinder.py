class Cylinder:

    def __init__(self,height=1,radius=1):

        self.height = height
        self.radius = radius

    def volume(self):
        return self.height * 3.14 * (self.radius)**2

