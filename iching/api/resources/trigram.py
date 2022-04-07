from typing import List

from flask_restful import Resource

from .line import Line
from ..data import TRIGRAMS

class Trigram(Resource):

    def __init__(self) -> None:
        self.lines = self.cast_lines()
        self.binary_lines = self.as_binary_str()
        self.title = TRIGRAMS[self.binary_lines]['title']
        self.symbol = TRIGRAMS[self.binary_lines]['symbol']

    def cast_lines(self) -> List[Line]:
        lines = []
        for i in range(1, 4):
            line = Line()
            line.line_number = i
            line.cast()
            lines.append(line)
        return lines

    def as_binary_str(self, changing: bool = False) -> str:
        string_lines = []
        for line in self.lines:
            if changing:
                string_lines.append(str(line.changing))
            else:
                string_lines.append(str(line.broken))
        return ''.join(string_lines)

    def get(self) -> dict:
        return {
            'title': self.title,
            'symbol': self.symbol,
            'lines': [line.__dict__ for line in self.lines]
        }
