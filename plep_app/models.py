from django.db import models


class Client(models.Model):
    fullname = models.CharField(max_length=200, blank=True)
    supervisor_name = models.CharField(max_length=200, blank=True)
    project_catg = models.CharField(max_length=200, blank=True)
    others = models.CharField(max_length=200, blank=True)
    project_name = models.CharField(max_length=200, blank=True)
    project_description = models.TextField()
    program_lang = models.CharField(max_length=200, blank=True)
    email = models.CharField(max_length=200, blank=True)
    phone = models.CharField(max_length=200, blank=True)
    project_mode = models.CharField(max_length=200, blank=True)
    no_of_member = models.CharField(max_length=2, blank=True)

    uid = models.CharField(max_length=50, blank=True, primary_key=True)
    is_verify = models.BooleanField(default=False)


    def __str__(self):
        return str(self.fullname.title()) + " -- " + str(self.uid)
