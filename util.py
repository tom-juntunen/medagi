
from faker import Faker
import random
from datetime import datetime, timedelta
import pytz
from icalendar import Event
from icalendar import Event, vCalAddress, vText

class RandomSentenceGenerator:
    def __init__(self):
        self.subjects = ['Meeting', 'Appointment', 'Event', 'Task']
        self.actions = ['Scheduled', 'Planned', 'Upcoming', 'Important']
        self.objects = ['with Clients', 'with Team', 'for Project', 'for Presentation']

    def generate_sentence(self):
        subject = random.choice(self.subjects)
        action = random.choice(self.actions)
        object_ = random.choice(self.objects)

        return f"{subject} {action} {object_}"

def get_random_event():
    # Create a new Event object
    event = Event()

    # Example usage
    generator = RandomSentenceGenerator()

    # Generate a random start date within the next 30 days
    start_time = datetime.now(pytz.utc) + timedelta(days=random.randint(1, 30))

    # Generate a random duration for the event (between 1 and 3 hours)
    duration_hours = random.randint(1, 3)
    end_time = start_time + timedelta(hours=duration_hours)

    # Generate a random name for the attendee
    fake = Faker()
    attendee_name = fake.name()
    attendee_email = f'{attendee_name.replace(" ", "").lower()}@example.com'

    # Set the event properties
    summary = generator.generate_sentence()
    event.add('summary', summary)
    event.add('uid', 'unique-string-identifier')
    event.add('dtstart', start_time)
    event.add('dtend', end_time)

    # Add an attendee
    attendee = vCalAddress(f'MAILTO:{attendee_email}')

    # adding attendee specific parameters
    attendee.params['cn'] = vText(attendee_name)
    attendee.params['ROLE'] = vText('REQ-PARTICIPANT')

    event.add('attendee', attendee, encode=0)

    # Print the event details
    print(f"Event Summary: {summary}")
    print(f"Start Time: {start_time}")
    print(f"End Time: {end_time}")
    print(f"Attendee: {attendee_name} ({attendee_email})")

    return event


if __name__ == '__main__':
    print(get_random_event())