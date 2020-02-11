from __future__ import annotations

import typing

import pydantic

import events
from base import BaseModel

airdrop = 'airdrop'


class AbilityModel(BaseModel):
    description: str = None


class TriggeredEffects(AbilityModel):
    name: typing.Literal['triggered_effects']
    trigger: events.Event
    effects: typing.Optional[
        typing.Union[
            effect.Effect,
            typing.List[effect.Effect]
        ]
    ] = None
    cancel: bool = False


Ability = typing.Union[TriggeredEffects,
                       typing.Literal[airdrop]]

import effect

TriggeredEffects.update_forward_refs()
