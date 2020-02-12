import typing
import base
import objects

damage = 'damage'
DamageDealtProperty = typing.Union[
    typing.Literal[damage]
]


class GetVarNumber(base.BaseModel):
    name: typing.Literal['get_var_number']
    var: str
    initial: int = 1


attack = 'attack'  # A unit's attack value.
max_health = 'max_health'
cur_health = 'cur_health'
UnitProperty = typing.Union[
    typing.Literal[attack],
    typing.Literal[max_health],
    typing.Literal[cur_health]
]  # A trait something has, such as a minion's attack or a card's cost.

Property = typing.Union[UnitProperty, DamageDealtProperty]


class GetPropertyModel(base.BaseModel):
    """Modify a property of an object."""
    name: typing.Literal['change_property']
    property_owner: objects.Object = 'this'


class GetProperty(base.BaseModel):
    """Modify a property of an object."""
    property: Property


class GetUnitProperty(GetPropertyModel):
    """Modify a property of an object."""
    type: typing.Literal['unit'] = 'unit'
    # todo property owner must be a unit or unit selector
    property: UnitProperty


Number = typing.Union[GetProperty, GetUnitProperty, GetVarNumber, int]
