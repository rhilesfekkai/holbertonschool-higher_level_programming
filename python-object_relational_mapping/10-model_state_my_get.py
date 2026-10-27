#!/usr/bin/python3
"""Print the ID of a state matching a name in the database."""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def main():
    """Search for a state by name and print its ID."""
    if len(sys.argv) != 5:
        return

    username, password, database, state_name = sys.argv[1:5]
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            username, password, database
        )
    )

    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        state = session.query(State).filter(
            State.name == state_name
        ).order_by(State.id).first()

        if state is None:
            print("Not found")
        else:
            print(state.id)
    finally:
        session.close()
        engine.dispose()


if __name__ == "__main__":
    main()
