from django.db import models

# Create your models here.

class Query(models.Model):
    age = models.IntegerField(default=25)
    stage = models.IntegerField(default=5)

    HIGH = 'High'
    MED = 'Medium'
    LOW = 'Low'
    EPIDEMIC_PREVALENCE = (
        (HIGH, 'High'),
        (MED, 'Medium'),
        (LOW, 'Low'),
    )
    epidemic_Prevalence = models.CharField(max_length=10, choices=EPIDEMIC_PREVALENCE, default=LOW)


    def __str__(self):
        return "age="+str(self.age) +", stg="+ str(self.stage)