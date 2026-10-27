#!/usr/bin/python3
"""List all cities with their corresponding states."""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City


def main():
    """Print cities and state names ordered by city ID."""
    if len(sys.argv) != 4:
        return

    username, password, database = sys.argv[1:4]
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            username, password, database
        )
    )

    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        results = session.query(
            State.name, City.id, City.name
        ).join(
            City, State.id == City.state_id
        ).order_by(City.id).all()

        for state_name, city_id, city_name in results:
            print("{}: ({}) {}".format(
                state_name, city_id, city_name
            ))
    finally:
        session.close()
        engine.dispose()


if __name__ == "__main__":
    main()
