#!/usr/bin/python3
"""Add Louisiana to the states table."""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def main():
    """Add Louisiana and print its ID."""
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
        state = State(name="Louisiana")
        session.add(state)
        session.commit()
        print(state.id)
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()
        engine.dispose()


if __name__ == "__main__":
    main()
