from .base import Base

class Enrollment(Base, table=True):
    __tablename__ = "enrollments"

    student: str
    course: str

    def __repr__(self):
        return f"<executive {self.name!r}>"