from copy import deepcopy

from sqlalchemy import Column, Enum, ForeignKey, Integer, String, exc
from sqlalchemy.ext.declarative import declared_attr

from app import db
from helpers.choices import ShopListsStatus, UserProductStatus
from helpers.utils import HelperModel


class Retailers(db.Model, HelperModel):
    """Represents the Retailers table."""

    __tablename__ = 'retailers'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(225), nullable=False)
    location = Column(String(225), nullable=True)
    contact_no = Column(String(20), nullable=True)

    def __repr__(self):
        return f'<Retailers: {self.name} - {self.location}>'

    def to_dict(self):
        data = self.__dict__
        if '_sa_instance_state' in data:
            del data['_sa_instance_state']
        return data


class ShopListsXProducts(db.Model, HelperModel):
    """Represents the ShopListsXProducts table."""

    __tablename__ = 'shop_lists_products'

    id = Column(Integer, primary_key=True, autoincrement=True)
    status = Column(Enum(UserProductStatus), default=UserProductStatus.not_found, nullable=False)

    @declared_attr
    def products_id(cls):
        return Column(Integer, ForeignKey('products.id'))

    @declared_attr
    def shoplists_id(cls):
        return Column(Integer, ForeignKey('shoplists.id'))

    def __repr__(self):
        return f'<ShopListsXProducts: {self.products_id} - {self.shoplists_id}>'

    def to_dict(self):
        data = self.__dict__
        if '_sa_instance_state' in data:
            del data['_sa_instance_state']
        return data


class Products(db.Model, HelperModel):
    """Represents the Products table."""

    __tablename__ = 'products'

    id = Column(Integer, primary_key=True, autoincrement=True)
    description = Column(String(255), index=True, unique=True, nullable=False)
    image_url = Column(String(255), unique=True, nullable=True)
    retailer = Column(String(225), nullable=True)
    slug = Column(String(225), index=True, unique=True, nullable=False)

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

    @declared_attr
    def owner_id(cls):
        return Column(Integer, ForeignKey('users.id'), nullable=True)

    def __repr__(self):
        return f'<ShopLists: {self.name} - {self.owner_id}>'

    def to_dict(self):
        data = self.__dict__
        if '_sa_instance_state' in data:
            del data['_sa_instance_state']
        return data
