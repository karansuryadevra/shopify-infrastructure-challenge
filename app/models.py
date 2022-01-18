#! bin/python3

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class InventoryModel(db.Model):
    __tablename__ = "inventory"

    # Declare a primary key for SQLite DB
    id = db.Column(db.Integer, primary_key=True)

    # declare the columns in the DB SQLite DB
    inventory_id = db.Column(db.Integer(), unique=True)
    name = db.Column(db.String(), unique=True)
    description = db.Column(db.String())
    count = db.Column(db.Integer())

    def __init__(self, inventory_id, name, description, count):
        self.inventory_id = inventory_id
        self.name = name
        self.description = description
        self.count = count
    
    def __repr__(self):
        return f"{self.inventory_id}, {self.name}, {self.description}, {self.count}"