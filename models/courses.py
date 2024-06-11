from .base import Base

class Course(Base, table=True):
    __tablename__ = "courses"

    name: str


    def __repr__(self):
        return f"<course {self.name!r}>"