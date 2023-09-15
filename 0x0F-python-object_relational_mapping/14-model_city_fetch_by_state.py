#!/usr/bin/python3
"""List all City objects from the database"""
from sys import argv
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(argv[1], argv[2], argv[3]))

    Session = sessionmaker(bind=engine)
    session = Session()

    cities = session.query(State.name, City.id, City.name)\
        .filter(State.id == City.state_id)
    for city in cities:
        print("{}: ({}) {}".format(city[0], city[1], city[2]))

    session.close()
