import argparse
from didactar import create_app
from didactar.database import db
from didactar.config import DevelopmentConfig, TestConfig
from didactar.utils.populate import populate_database


def parse_commandline_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('--resetdb', dest='reset_db', action='store_true', default=False)
    parser.add_argument('--populate', dest='populate_db', action='store_true', default=False)
    parser.add_argument('--testserver', dest='test_server', action='store_true', default=False)
    parser.add_argument('--devserver', dest='dev_server', action='store_true', default=False)
    return parser.parse_args()


def reset_database(app):
    with app.app_context():
        db.reflect()
        db.drop_all()
        db.create_all()


if __name__ == '__main__':

    args = parse_commandline_arguments()
    
    if args.reset_db:
        app = create_app(DevelopmentConfig)
        reset_database(app)
        exit()

    if args.populate_db:
        populate_database()
        exit()

    if args.test_server:
        app = create_app(TestConfig)
        reset_database(app)
        app.run(threaded=True)

    if args.dev_server:
        app = create_app(DevelopmentConfig)
        app.run(threaded=True)
