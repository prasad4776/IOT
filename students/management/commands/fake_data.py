from django.core.management.base import BaseCommand

from students.models import Student
from users.models import User


class Command(BaseCommand):
    help = "Loads Some data in the database"

    def handle(self, *args, **kwargs):
        first_name = ["Morgan", "Michael", "Dwight", "Jim", "Pam"]
        last_name = ["Tobey", "Scott", "Schrute", "Halpert", "Beesly"]
        subject = ["Maths", "Chemistry", "Physics", "Biology", "French"]
        marks = [90, 80, 70, 60, 85]

        for x in range(5):
            Student.objects.create(
                first_name=first_name[x],
                last_name=last_name[x],
                subject=subject[x],
                marks=marks[x],
            )

        User.objects.create_user(email="test@iot.com", password="SorI0t123")

        return "data loaded successfully"
