__winc_id__ = "d7b474e9b3a54d23bca54879a4f1855b"
__human_name__ = "Betsy Webshop"

from peewee import *
from models import *

def search(term):
    results=[]
    lower_term = term.lower()
    for found_products in Products.select().where(Products.product_name.contains(lower_term)):
        results.append(found_products.product_name)
    return results


def list_user_products(user_id):
    list_products=[]
    for user_products in Products.select().where(Products.seller_id == user_id):
        list_products.append(user_products.product_name)
    return list_products


def list_products_per_tag(tag_name):
    list_products=[]
    products_per_tag = (Product_Tag
                        .select(Product_Tag, Products)
                        .join(Products)
                        .where(Product_Tag.tag == tag_name))
    for product in products_per_tag:
        list_products.append(product.products.product_name)
    return list_products


def add_product_to_catalog(user_id, product, description, tags, price, quantity):
    add_product = Products.create(seller_id = user_id, product_name = product, description = description, price_per_unit = price, stock_quantity= quantity)
    product_id = Products.get(Products.id == add_product.id)
    product_id.descriptive_tags = [tags]
    product_id.save()
    return add_product


def remove_product(product):
    for product_delete in Products.select().where(Products.product_name == product):
        product_delete.delete_instance()


def overvieuw_products_catalog():
    catalog_products = Products.select()
    for overview in catalog_products:
        print(overview.product_name)


def update_stock(product, new_quantity):
    for update_product in Products.select().where(Products.product_name == product):
        old_quantity = update_product.stock_quantity
        update_product.stock_quantity = new_quantity
        update_product.save()
    print('Quantity from', product, 'is changed from:', old_quantity, 'to', new_quantity)


def purchase_product(buyer_id, product_id, quantity):
    Transaction.create(buyer_id=buyer_id, bought_product_id = product_id, quantity_purchased_items= quantity)

def last_transaction():
    purchased_products = Transaction.select()
    print(vars(purchased_products[-1]))

if __name__ == "__main__":
    print('Search results term "Bike":', search('Bike'))
    print('Products from seller_id "5":', list_user_products(5))
    print('Products with "tag_bike":', list_products_per_tag('tag_bike'))
    print('Ad product to webshop'), add_product_to_catalog(user_id=1, product='doll house', description= 'nice blue dollhouse', tags= ['tag_blue', 'tag_toys'], price=50, quantity=8)
    print('overvieuw_products_catalog after adding:'), overvieuw_products_catalog()
    print('Remove product from webshop'), remove_product('doll house')
    print('overvieuw_products_catalog after removing:'), overvieuw_products_catalog()
    update_stock('pumps', 31)
    purchase_product(3,5,27)
    last_transaction()
