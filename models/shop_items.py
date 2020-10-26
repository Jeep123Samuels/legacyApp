from copy import deepcopy

from sqlalchemy import Column, Enum, ForeignKey, Integer, String, exc

from app import db
from helpers.choices import ShopListsStatus
from helpers.utils import HelperModel


class Retailers(db.Model, HelperModel):
    """Represents the Retailers table."""

    __tablename__ = 'retailers'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(225), nullable=False)
    location = Column(String(225), nullable=True)
    contact_no = Column(String(20), nullable=True)

    def __repr__(self):
        return f'<Retailers: {self.username} - {self.email}>'

    def to_dict(self):
        data = self.__dict__
        if '_sa_instance_state' in data:
            del data['_sa_instance_state']
        return data


shop_list_product = db.Table(
    'shop_list_product', db.Model.metadata,
    db.Column('products_id', db.Integer, db.ForeignKey('products.id')),
    db.Column('shoplists_id', db.Integer, db.ForeignKey('shoplists.id')),
)


class Products(db.Model, HelperModel):
    """Represents the Products table."""

    __tablename__ = 'products'

    id = Column(Integer, primary_key=True, autoincrement=True)
    description = Column(String(255), index=True, unique=True, nullable=False)
    image_url = Column(String(255), unique=True, nullable=True)
    retailer = Column(String(225), nullable=True)
    slug = Column(String(225), index=True, unique=True, nullable=False)

    shoplists = db.relationship('ShopLists', secondary=shop_list_product)

    REQUIRED_FIELDS = {'description'}

    def __repr__(self):
        return f'<Products: {self.slug} - {self.id}>'

    def to_dict(self):
        data = deepcopy(self.__dict__)
        if '_sa_instance_state' in data:
            del data['_sa_instance_state']
        return data

    def save_instance(self):
        try:
            self.slug = self.description.lower().replace(' ', '_')
            db.session.add(self)
            db.session.commit()
            return
        except exc.SQLAlchemyError as e:
            return e


class ShopLists(db.Model, HelperModel):
    """Represents the ShopLists table."""

    __tablename__ = 'shoplists'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(225), nullable=False)
    status = Column(
        Enum(ShopListsStatus),
        default=ShopListsStatus.inactive,
        nullable=False,
    )
    owner_id = Column(Integer, ForeignKey('users.id'), nullable=True)
    products = db.relationship('Products', secondary=shop_list_product)

    # user_id = db.relationship('Users', backref='user')

    def __repr__(self):
        return f'<ShopList: {self.name} - {self.owner_id}>'

    def to_dict(self):
        data = self.__dict__
        if '_sa_instance_state' in data:
            del data['_sa_instance_state']
        return data

# class UserShopItems(db.Model, HelperModel):
#     """Represents the UserShopItems table."""
#
#     __tablename__ = 'usershopitems'
#
#     id = Column(Integer, primary_key=True, autoincrement=True)
#     description = Column(String(255), index=True, unique=True, nullable=False)
#     retailer = Column(String(225), unique=True, nullable=False)
#     slug = Column(String(225), index=True, unique=True, nullable=False)
#
#     def __repr__(self):
#         return f'<ShopItems: {self.slug}>'
#
#     def to_dict(self):
#         return self.__dict__
