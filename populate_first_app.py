"""This module populates data"""
import random
import os
from faker import Faker
import django

from first_app.models import AccessRecord, WebPage, Topic

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'first_project.settings')
django.setup()


# Fake pop script


FAKEGEN = Faker()
TOPICS = ['Search', 'Social', 'MarketPlace', 'News', 'Games']


def add_topic():
    """
    Gets or Creates a topic randomly from TOPICS
    Returns it
    """
    topic_created = Topic.objects.get_or_create(top_name=random.choice(TOPICS))[0]
    topic_created.save()
    return topic_created


def populate(amount_to_populate=5):
    """
    will populate the data with (amount_to_populate) entries
    """
    for entry in range(amount_to_populate):

        # get the topic for the entry
        top = add_topic()

        # Create the fake data for that entry
        fake_url = FAKEGEN.url()
        fake_date = FAKEGEN.date()
        fake_name = FAKEGEN.company()

        # Create the new webpage entry
        webpg = WebPage.objects.get_or_create(
            topic=top, url=fake_url, name=fake_name)[0]

        # create a fake access record for that webpage
        acc_rec = AccessRecord.objects.get_or_create(
            name=webpg, date=fake_date)[0]


if __name__ == '__main__':
    print("Populating script!")
    populate(20)
    print("Populating complete!")
