from django.db import models

# Create your models here.

class Organization(models.Model):
    """(Organization description)"""
    
    name = models.CharField(max_length=255, blank=True)
    address = models.TextField(blank=True)
    email = models.EmailField()

    # class Admin:
    #     list_display = ('',)
    #     search_fields = ('',)

    def __unicode__(self):
        return self.name
