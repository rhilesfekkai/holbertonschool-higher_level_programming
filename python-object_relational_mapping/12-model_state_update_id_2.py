#!/usr/bin/python3
"""Change the name of the state with ID 2 to New Mexico."""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def main():
    """Update the state name for ID 2."""
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
        state = session.query(State).filter(State.id == 2).first()
        if state is not None:
            state.name = "New Mexico"
            session.commit()
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()
        engine.dispose()


if __name__ == "__main__":
    main()
