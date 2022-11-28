

from flask_appbuilder import Model
from sqlalchemy import Column, Date, ForeignKey, Integer, String, Table, Text


class Employee(Model):
    id = Column(Integer, primary_key=True)
    full_name = Column(String(150), nullable=False)
    year = Column(Integer, nullable=False)

    def __repr__(self):
        return self.full_name
