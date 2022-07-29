# Models go here
from peewee import *

db = SqliteDatabase('betsy_webshop.db')

class Basemodel(Model):
    class Meta:
        database = db

class User(Basemodel):
    name = CharField(primary_key=True)
    address_data = CharField()
    billing_information = CharField()

class Tag(Basemodel):
    name = CharField(primary_key=True)

class Products(Basemodel):
    seller_id = ForeignKeyField(User) 
    product_name = CharField()
    description = CharField()
    price_per_unit = DecimalField(auto_round =True)
    stock_quantity = IntegerField()
    descriptive_tags = ManyToManyField(Tag)

class Transaction(Basemodel):
    buyer_id = ForeignKeyField(User)
    bought_product_id = ForeignKeyField(Products)
    quantity_purchased_items = IntegerField()

# When creating tables for an application that uses ManyToManyField, you must create the through table expicitly.
Product_Tag = Products.descriptive_tags.get_through_model()
