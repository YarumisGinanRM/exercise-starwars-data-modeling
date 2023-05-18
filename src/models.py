import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_name = Column(String(250), nullable=False)
    nombre = Column(String(250), nullable=False)
    apellido = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)
    fecha_suscripcion = Column(String(250), nullable=False)

class Planetas(Base):
    __tablename__ = 'planetas'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    descripcion = Column(String(250), nullable=False)

class Personajes(Base):
    __tablename__ = 'personajes'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    descripcion = Column(String(250), nullable=False)

class Favoritos(Base):
    __tablename__ = 'favoritos'
    id = Column(Integer, primary_key=True)
    planetas_id = Column(Integer, ForeignKey("planetas.id"), nullable=True)
    personajes_id = Column(Integer, ForeignKey("personajes.id"), nullable=True)
    user_id = Column(Integer, ForeignKey("user.id"))
    planeta = relationship(Planetas)
    personaje = relationship(Personajes)
    user = relationship(User)



# class Address(Base):
#     __tablename__ = 'address'
#     # Here we define columns for the table address.
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     street_name = Column(String(250))
#     street_number = Column(String(250))
#     post_code = Column(String(250), nullable=False)
#     person_id = Column(Integer, ForeignKey('user.id'))
#     person = relationship(User)

    # def to_dict(self):
    #     return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
