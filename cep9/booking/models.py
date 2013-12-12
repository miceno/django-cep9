from django.db import models
import datetime

try:
    import organizations.models as organizations
except ImportError as e:
    print( "unable to load module organizations")
    raise e

# Create your models here.
class Booking(models.Model):
    """(Booking description)"""    
    organization = models.ForeignKey('organizations.Organization', null=True, blank=True)
    contact = models.EmailField()
    date = models.DateField(default=datetime.datetime.today)

    def __unicode__(self):
        return ", ".join( (str(self.date), self.organization.name) )
