from __future__ import annotations

import typing

import pydantic

import events
from base import BaseModel

airdrop = 'airdrop'


class AbilityModel(BaseModel):
    description: str = None


class TriggeredEffect(AbilityModel):
    name: typing.Literal['triggered_effect']
    trigger: events.Event
    effect: typing.Optional[effects.Effect] = None
    cancel: bool = False


Ability = typing.Union[TriggeredEffect,
                       typing.Literal[airdrop]]

import effects

TriggeredEffect.update_forward_refs()
