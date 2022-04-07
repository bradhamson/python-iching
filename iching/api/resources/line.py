from random import randrange
from dataclasses import dataclass, field

from flask_restful import Resource

@dataclass
class Line(Resource):

    line_number: int = field(default=None)
    title: str = field(default='yang')
    broken: int = field(default=0)
    changing: int = field(default=0)
    raw: int = field(default_factory=lambda : randrange(6, 10))

    def cast(self) -> None:
        if self.raw % 2 == 0:
            self.title = 'yin'
            self.broken = 1
        if self.raw % 3 == 0:
            self.changing = 1

    def get(self) -> dict:
        self.cast()
        return self.__dict__
