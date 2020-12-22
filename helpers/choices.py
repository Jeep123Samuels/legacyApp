import enum


class ShopListsStatus(enum.Enum):
    active = 'ACTIVE'
    completed = 'COMPLETED'
    inactive = 'INACTIVE'
    incomplete = 'INCOMPLETE'


class UserProductStatus(enum.Enum):
    bought = 'BOUGHT'
    not_found = 'NOT_FOUND'
    searching = 'SEARCHING'
