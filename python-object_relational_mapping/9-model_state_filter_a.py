#!/usr/bin/python3
"""
This script connects to a MySQL database
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def main():
    usr = sys.argv[1]
    pwd = sys.argv[2]
    db_name = sys.argv[3]
    st_name = sys.argv[4]

    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(usr, pwd, db_name))

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    for state in session.query(State).filter(State.name == st_name).all():
        print(state.id)
        return
    print("Not found")


if __name__ == "__main__":
    main()
