import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'exercise.settings')

import django
django.setup()

import random
from social.models import User
from faker import Faker

fakegen = Faker()

def populate(n=5):
    for entry in range(n):

        # create fake data for that entry
        fake_name = fakegen.name()
        fake_fname = fake_name.split(' ')[0]
        fake_lname = fake_name.split(' ')[1]
        fake_email = fakegen.email()

        # create the new webpage entry
        user = User.objects.get_or_create(fname=fake_fname, lname=fake_lname, email=fake_email)[0]

if __name__ == '__main__':
    print("populating script running!")
    populate(20)
    print("populating complete!")
