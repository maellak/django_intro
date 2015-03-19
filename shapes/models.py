from django.db import models

class Shape(models.Model):
    dimensions = models.CharField(max_length=200)
    area = models.IntegerField(max_length=200)
    perimeter = models.IntegerField(max_length=200)
    def calculateArea(self, dimensions):
        raise NotImplementedError("Please Implement this method")
    def calculatePerimeter(self, dimensions):
        raise NotImplementedError("Please Implement this method")

class Triangle(Shape):
    def calculateArea(self, dimensions):
        splitDimensions = dimensions.split('x')
        # Actually we need to calculate the height here,
        # but for the sake of the example lets assume splitDimensions[0] is the height
        return int(int(float(splitDimensions[0]))*int(float(splitDimensions[1]))/2)
    def calculatePerimeter(self, dimensions):
        splitDimensions = dimensions.split('x')
        return int(float(splitDimensions[0]))+int(float(splitDimensions[1]))+int(float(splitDimensions[2]))

class Parallelogram(Shape):
    def calculateArea(self, dimensions):
        splitDimensions = dimensions.split('x')
        # Actually we need to calculate the height here,
        # but for the sake of the example lets assume splitDimensions[0] is the height
        return int(float(splitDimensions[0]))*int(float(splitDimensions[1]))
    def calculatePerimeter(self, dimensions):
        splitDimensions = dimensions.split('x')
        return int(float(splitDimensions[0]))*2+int(float(splitDimensions[1]))*2
