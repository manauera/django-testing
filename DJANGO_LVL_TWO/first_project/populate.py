import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'first_project.settings')

import django
django.setup()

import random
from first_app.models import AccessRecord, Topic, Webpage
from faker import Faker

fakegen = Faker()
topics = ['Search', 'Social', 'Marketplace', 'News', 'Games']

def add_topic():
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t
    
    
def populate(n=5):
    for entry in range(n):
        # get topic for the entry
        top = add_topic()
        
        # create fake data for that entry
        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()
        
        # create the new webpage entry
        webpg = Webpage.objects.get_or_create(topic=top, name=fake_name, url=fake_url)[0]
        
        # create a fake access record for that webpage
        acc_res = AccessRecord.objects.get_or_create(name=webpg, date=fake_date)[0]
        
if __name__ == '__main__':
    print("populating script running!")
    populate(20)
    print("populating complete!")
        
        