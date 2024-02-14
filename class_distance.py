import math
class distance:
    def __init__(self,p1,p2):
        self.p1 = p1
        self.p2 = p2

    def __add__(self, other):
        x = self.x+other.x
        y = self.y+other.y
        return distance(x,y)

    def distance_between_points(self):
        dist = math.sqrt(((self.p1*dist1.x-self.p2*dist2.x)**2)+((self.p1*dist1.y-self.p2*dist2.y)**2))
        print('(%g %g)' %(dist1.x ,dist1.y))
        print('(%g %g)' %(dist2.x ,dist2.y))
        return dist
    
    # def __str__(self,x,y):
    #     return "{} {}".format(self.x,self.y)
    
dist1 = distance(5,6)
dist1.x = 3
dist1.y = 4
dist2 = distance(7,8)
dist2.x = 8
dist2.y = 9
print(dist1.distance_between_points())
print(dist2.distance_between_points())
print(dist1+dist2)