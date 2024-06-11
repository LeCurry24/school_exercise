DATABASE_URL = 'postgresql://postgres@localhost/school_exercise'

from sqlmodel import create_engine, SQLModel, Session

engine = create_engine(DATABASE_URL, echo=True)

def init_db():
    SQLmodel.metadata.create_call(engine)

def get_session():
    with Session(engine) as session:
        yield session       