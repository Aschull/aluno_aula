from sqlalchemy import Column, Integer, String
from app.configs.db.sqlite import Base, session


class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    age = Column(Integer)
    classes = Column(String(255))

    class Config:
        orm_mode = True


    def crate_student(self, db: session):
        session.add(self)
        session.commit()
        session.close()

    def update_student(self, name, age, classes):
        self.name = name
        self.age = age
        self.classes = classes
        session.commit()