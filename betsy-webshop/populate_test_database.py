from models import *

def create_test_data():
    db.connect()

    # Create tables for our models as well as the through model
    db.create_tables([User, Tag, Products, Transaction, Product_Tag], safe=True)

    User.create(
        name= 'Jan Jansen',
        address_data = 'Stationstraat 19 5751 AC Deurne',
        billing_information= 'BH90 MFEN NPHZ KHMD VAA4 EK'
    )
    
    User.create(
        name= 'Astrix Whatley',
        address_data = 'Spoorlaan 139 2051 HF Arnhem',
        billing_information= 'CY86 0495 9199 M5DU G7ZT OWQ3 MVFK'
    )

    User.create(
        name= 'Dew Matula',
        address_data = 'Utrechtlaan 234 8071 FG Utrecht',
        billing_information= 'BE84 6243 5363 3648'
    )

    User.create(
        name= 'Amandie Cunliffe',
        address_data = 'Haarlemstraat 356 4325 RM Haarlem',
        billing_information= 'HR53 2858 6909 5502 0274 6'
    )

    User.create(
        name= 'Gualterio Percifull',
        address_data = 'Hoofdstraat 87 5432 WL Venlo',
        billing_information= 'SI34 7230 3721 0889 489'
    )

    tag_toys = Tag.create(name= 'tag_toys')

    tag_blue= Tag.create(name= 'tag_blue')

    tag_shoes = Tag.create(name= 'tag_shoes')

    tag_jeans = Tag.create(name= 'tag_jeans')

    tag_bike = Tag.create(name= 'tag_bike')


    jeans = Products.create(
        seller_id = 1,
        product_name = 'jeans',
        description = 'blue jeans',
        price_per_unit = 65,
        stock_quantity = 11,
    )
    jeans_id = Products.get(Products.id == jeans.id)
    jeans_id.descriptive_tags=[tag_blue, tag_jeans]
    jeans_id.save()
   

    bike1 = Products.create(
        seller_id = 1,
        product_name = 'bike for boys',
        description = 'beautiful blue bicycle with gears',
        price_per_unit = 175,
        stock_quantity = 3,
    )
    bike1_id = Products.get(Products.id == bike1.id)
    bike1_id.descriptive_tags=[tag_blue, tag_bike]
    bike1_id.save()

    bike2 = Products.create(
        seller_id = 3,
        product_name = 'bike for dolls',
        description = 'nice blue bike for a doll',
        price_per_unit = 23,
        stock_quantity = 9,
    )
    bike2_id = Products.get(Products.id == bike2.id)
    bike2_id.descriptive_tags=[tag_blue, tag_bike, tag_toys]
    bike2_id.save()

    pumps  = Products.create(
        seller_id = 5,
        product_name = 'pumps',
        description = 'nice blue pumps',
        price_per_unit = 37,
        stock_quantity = 6,
    )
    pumps_id = Products.get(Products.id == pumps.id)
    pumps_id.descriptive_tags=[tag_blue, tag_shoes]
    pumps_id.save()

    lego = Products.create(
        seller_id = 5,
        product_name = 'lego',
        description = 'blue lego for building',
        price_per_unit = 8,
        stock_quantity = 18,
    )
    lego_id = Products.get(Products.id == lego.id)
    lego_id.descriptive_tags=[tag_blue, tag_toys]
    lego_id.save()

    Transaction.create(
        buyer_id = 2,
        bought_product_id = 1,
        quantity_purchased_items = 2
    )

    Transaction.create(
        buyer_id = 2,
        bought_product_id = 5,
        quantity_purchased_items = 3
    )

    Transaction.create(
        buyer_id = 4,
        bought_product_id = 5,
        quantity_purchased_items = 2
    )

    db.close()
    print('database made')

if __name__ == "__main__":
    create_test_data()