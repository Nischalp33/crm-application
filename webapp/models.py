from django.db import models



class Record(models.Model):

    creation_date = models.DateTimeField(auto_now_add=True)

    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    email = models.CharField(max_length = 50)
    phone = models.CharField(max_length = 50)
    address = models.CharField(max_length = 50)
    city = models.CharField(max_length = 50)
    country = models.CharField(max_length = 50)



    def __str__(self):
        return self.first_name + " " + self.last_name