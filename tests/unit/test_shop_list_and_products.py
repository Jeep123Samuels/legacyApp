
import pytest

from helpers.choices import ShopListsStatus, UserProductStatus
from models import Products, ShopLists, ShopListsXProducts, Users
from app import db


@pytest.fixture
def create_products(request):
    db.session.query(ShopListsXProducts).delete()
    db.session.query(Products).delete()
    db.session.commit()

    product_a = dict(
        description="Pasta 500g",
        image_url="google.com",
        retailer="PnP",
    )
    product_b = dict(
        description="Salad 500g",
        image_url="google.com2",
        retailer="PnP1",
    )
    product_c = dict(
        description="Elizabeth lotion 500g",
        image_url="google.c",
        retailer="Shoprite",
    )
    for n in [product_a, product_b, product_c]:
        product = Products(**n)
        product.save_instance()

    def teardown():
        # clear table after each test.
        db.session.query(ShopListsXProducts).delete()
        db.session.query(Products).delete()
        db.session.commit()

    request.addfinalizer(teardown)
    yield


@pytest.fixture
def create_shop_lists(request):
    db.session.query(ShopListsXProducts).delete()
    db.session.query(ShopLists).delete()
    db.session.commit()

    # Create Shop lists with Test user
    user = db.session.query(Users).filter_by(username='username').first()

    # given ... 3 ShopLists
    for i in range(3):
        c = dict(
            name=f"default{i}",
            status=ShopListsStatus.inactive,
            owner_id=user.id,
        )
        shop_list = ShopLists(**c)
        shop_list.save_instance()

    def teardown():
        # clear table after each test.
        db.session.query(ShopListsXProducts).delete()
        db.session.query(ShopLists).delete()
        db.session.commit()

    request.addfinalizer(teardown)
    yield


def test_correct_object_hierarchy_for_products_and_shopping_lists(
    client,
    create_products,
    create_shop_lists,
):
    """Should correctly create and pull objects with desired linkage."""
    # given
    # ... 3 products and 3 shop lists for an user
    user = db.session.query(Users).filter_by(username='username').first()
    shopping_lists = db.session.query(ShopLists).filter_by(owner_id=user.id).all()
    products = db.session.query(Products).all()

    # when ... user add two products to shop list one
    shop_list_1 = shopping_lists[0]
    product_1 = products[0]
    product_2 = products[1]

    # add product 1
    add_product: dict = dict(
        products_id=product_1.id,
        shoplists_id=shop_list_1.id,
        status=UserProductStatus.searching,
    )
    add_product = ShopListsXProducts(**add_product)
    add_product.save_instance()

    # add product 2
    add_product: dict = dict(
        products_id=product_2.id,
        shoplists_id=shop_list_1.id,
        status=UserProductStatus.searching,
    )
    add_product = ShopListsXProducts(**add_product)
    add_product.save_instance()

    # then ... we expect these to products to be linked to the shopping list
    shopping_list_items = db.session.query(
        ShopListsXProducts).filter_by(shoplists_id=shop_list_1.id).all()
    for item in shopping_list_items:
        assert item.products_id in [product_2.id, product_1.id]
    assert len(shopping_list_items) == 2
