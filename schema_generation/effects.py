import typing
from typing import Union

import pydantic
from pydantic import BaseModel

import properties
import operators
import events

InstantaneousEffect = Union[typing.Literal["UNIMPLEMENTED"]]
# An effect cannot have a duration, such as killing a minion.


class DurationEffectModel(BaseModel):
    """An continuous effect."""
    end_when_this_leaves_play: bool = False
    until: typing.Optional[events.Event] = None


class ChangeProperty(DurationEffectModel):
    name: str = pydantic.Field('change_property', const=True)
    # property_owner: any = This()  # Todo set type
    property: properties.Property  # todo Only allow properties property_owner has? Or just ignore?
    operator: operators.NumberOperator
    by_value: int


DurationEffect = Union[ChangeProperty]
Effect = Union[InstantaneousEffect, DurationEffect]


class TriggeredEffect(BaseModel):
    trigger: events.Event
    effect: Effect
