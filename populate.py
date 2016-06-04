from database import db
from config import DevelopConfig
from factory import create_app

from didactar.users.populate import populate_users
from didactar.channels.populate import populate_channels
from didactar.topics.populate import populate_topics
from didactar.events.populate import populate_events
from didactar.markings.populate import populate_markings
from didactar.participations.populate import populate_participations
from didactar.hostings.populate import populate_hostings



def populate_db():
    print('populating users...')
    users = populate_users()
    print('populating topics...')
    topics = populate_topics()
    print('populating channels...')
    channels = populate_channels()
    for channel in channels:
        print('  populating events...')
        events = populate_events(channel)
        for event in events:
            print('    populating markings...')
            populate_markings(event, topics, 5)
            print('    populating hostings...')
            populate_hostings(event, users, 5)
            print('    populating participations...')
            populate_participations(event, users, 5)



def reset_db():
    db.reflect()
    db.drop_all()
    db.create_all()


if __name__ == '__main__':
    config_object = DevelopConfig()
    app = create_app(config_object)
    with app.app_context():
        reset_db()
        populate_db()
