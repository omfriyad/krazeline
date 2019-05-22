import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'krazeline.settings')

import django
django.setup()

## Fake pop

import random
from blog.models import *
from faker import Faker

fakegen = Faker()

def populate(N=5):

    for entry in range(N):
        genre = random.choice(Genre.objects.all())



        print(genre)



populate(4)