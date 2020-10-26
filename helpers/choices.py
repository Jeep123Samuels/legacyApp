import enum


class ShopListsStatus(enum.Enum):
    active = 'ACTIVE'
    completed = 'COMPLETED'
    inactive = 'INACTIVE'
    incomplete = 'INCOMPLETE'
