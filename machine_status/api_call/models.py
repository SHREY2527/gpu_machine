from django.db import models

class Status(models.Model):
    S_id =models.IntegerField(blank=True, null=True)
    status = models.CharField(max_length = 20)

    def __str__(self):
        return self.S_id,self.status


# class users(models.Model):
#     first_name = models.CharField(max_length=30)
#     last_name = models.CharField(max_length=20)
#     email_id = models.EmailField()
