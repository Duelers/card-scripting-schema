from typing import Union, Literal

import pydantic

summon = 'summon'  # TODO Clarify this. How to say "when this is played" vs "when a thing is played"?


class EndOfNTurns(pydantic.BaseModel):
    name: str = pydantic.Field('end_of_#_turns', const=True)
    num_turns: int = 0


Event = Union[
    Literal[summon],
    EndOfNTurns
]  # A thing that happens, such as a turn ending.
