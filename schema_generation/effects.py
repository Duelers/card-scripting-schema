import typing
from typing import Union

import pydantic
from pydantic import BaseModel

from schema_generation import properties, operators, events


class InstantaneousEffect(BaseModel):
    """An effect cannot have a duration, such as killing a minion."""
    pass


class DurationEffectModel(BaseModel):
    """An continuous effect."""
    end_when_this_leaves_play: bool = False
    until: typing.Optional[events.Event] = None

    class Config:
        arbitrary_types_allowed = True


class ChangeProperty(DurationEffectModel):
    name: str = pydantic.Field('change_property', const=True)
    # property_owner: any = This()  # Todo set type
    property: properties.Property  # todo Only allow properties property_owner has? Or just ignore?
    operator: operators.NumberOperator
    by_value: int


DurationEffect = Union[ChangeProperty]
Effect = Union[InstantaneousEffect, DurationEffect]
