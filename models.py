from django.db import models

class CarInput(models.Model):
    hp = models.FloatField(verbose_name='Horsepower')
    wt = models.FloatField(verbose_name='Weight (1000 lbs)')
    cyl = models.IntegerField(verbose_name='Number of Cylinders')
    predicted_mpg = models.FloatField(verbose_name='Predicted MPG', null=True, blank=True)

    def __str__(self):
        return f'Car Input: {self.hp} HP, {self.wt} Weight, {self.cyl} Cylinders'


