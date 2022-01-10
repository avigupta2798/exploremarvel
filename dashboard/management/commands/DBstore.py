from django.core.management.base import BaseCommand
from django.db.models import Count

from datetime import timedelta, datetime
from django.utils.timezone import utc
  
  
def now():
    return datetime.utcnow().replace(tzinfo=utc)
  
  
class Command(BaseCommand):
    help = 'Displays stats related to Article and Comment models'
  
    def handle(self, *args, **kwargs):
        From = now() - timedelta(hours=5)
        To = now()
        print(From)