#!/usr/bin/python3
"""Delete states whose names contain the letter a."""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def main():
    """Delete all states with an a in their name."""
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
        session.query(State).filter(
            State.name.ilike("%a%")
        ).delete(synchronize_session=False)
        session.commit()
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()
        engine.dispose()


if __name__ == "__main__":
    main()
