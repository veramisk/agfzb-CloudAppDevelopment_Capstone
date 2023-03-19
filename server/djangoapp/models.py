from django.db import models
from django.utils.timezone import now


# Create your models here.

# <HINT> Create a Car Make model `class CarMake(models.Model)`:
# - Name
# - Description
# - Any other fields you would like to include in car make model
# - __str__ method to print a car make object
class CarMake(models.Model):
    name = models.CharField(null=False, max_length=100, default='make')
    description = models.TextField()
    def __str__(self):
        return f"{self.name}"                    
# <HINT> Create a Car Model model `class CarModel(models.Model):`:
class CarModel(models.Model):
# - Many-To-One relationship to Car Make model (One Car Make has many Car Models, using ForeignKey field)
    make = models.ForeignKey('CarMake', on_delete=models.CASCADE)
# - Name
    name = models.CharField(null=False,max_length=100, default='Car')
    SEDAN = 'Sedan'
    SUV = 'SUV'
    WAGON = 'Wagon' 
# - Dealer id, used to refer a dealer created in cloudant database
    id = models.IntegerField(default=1,primary_key=True)
# - Type (CharField with a choices argument to provide limited choices such as Sedan, SUV, WAGON, etc.)
    CAR_TYPES = [
    (SEDAN,'Sedan'),
    (SUV, 'SUV'),
    (WAGON, 'Wagon')     
    ]
    type = models.CharField(
        null=False,
        max_length=50,
        choices=CAR_TYPES,
        default=SEDAN
    )
# - Year (DateField)
    year = models.DateField(default=now)
# - Any other fields you would like to include in car model
# - __str__ method to print a car make object

    def __str__(self):
        return f"{self.make} {self.name} ({self.year})"   



# <HINT> Create a plain Python class `CarDealer` to hold dealer data


# <HINT> Create a plain Python class `DealerReview` to hold review data
