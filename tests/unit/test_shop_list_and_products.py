
from helpers.choices import ShopListsStatus
from models import Products, ShopLists
from models.shop_items import shop_list_product
from app import db
from sqlalchemy import select, column


def test_return_correct_adding_of_objects():
    """Should return 200 return status with correct data posted."""
    #
    # a = dict(
    #     description="Testing this shit out 500g number 2",
    #     image_url="google.com",
    #     retailer="PnP",
    # )
    # b = dict(
    #     description="Testing this shit out 500g",
    #     image_url="google.com2",
    #     retailer="PnP1",
    # )
    # d = dict(
    #     description="Elizabeth lotion 500g",
    #     image_url="google.c",
    #     retailer="Shoprite",
    # )
    # for n in [ d]:
    #     product = Products(**n)
    #     product.save_instance()
    # for i in range(3):
    #     c = dict(
    #         name=f"default{i}",
    #         status=ShopListsStatus.inactive,
    #         owner_id=91,
    #     )
    #     shop_list = ShopLists(**c)
    #     shop_list.save_instance()
    print(dir(shop_list_product))
    print(shop_list_product.columns)
    shoplists_filter = select([ShopLists.products]).where(
        ShopLists.id == column('shop_list_product.shoplists_id'))
    print(products_filter)
    shop_list_1 = db.session.query(ShopLists).filter_by(id=1).first()
    shop_list_2 = db.session.query(ShopLists).filter_by(id=2).first()
    # product = db.session.query(Products).filter_by(id=5).first()
    # product.shoplists.append(shop_list_1)
    # product.shoplists.append(shop_list_2)
    # product.save_instance()
    products = db.session.query(Products).filter(Products.id.in_(products_filter)).all()
    print(products)
    print(dir(shop_list_1))
    print(shop_list_1.products[0])
    for product in shop_list_1.products:
        print(product.to_dict())
    # print(dir(shop_list_1))
    assert 2 == 1
