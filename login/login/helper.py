## Helper functions for testing.

from .models import RandIds, Parent, Child

def delete_all():
    RandIds.objects.all().delete()
    Parent.objects.all().delete()
    Child.objects.all().delete()
