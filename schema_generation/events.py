from typing import Union, Literal

import typing

import base
import pydantic

import objects
import players

summon = 'summon'  # TODO Clarify this. How to say "when this is played" vs "when a thing is played"?


class EndOfNTurns(base.BaseModel):
    name: typing.Literal['end_of_#_turns']
    num_turns: int = 0


class SpellCast(base.BaseModel):
    name: typing.Literal['spell_cast']
    target: typing.Optional[objects.Object] = None
    caster: typing.Optional[players.Player] = None


Event = Union[
    Literal[summon],
    EndOfNTurns,
    SpellCast,
]  # A thing that happens, such as a turn ending.
