from typing import Union, Literal

NumberOperator = Union[Literal['+'],
                       Literal['-'],
                       Literal['*'],
                       Literal['/']]
Operator = Union[NumberOperator]
