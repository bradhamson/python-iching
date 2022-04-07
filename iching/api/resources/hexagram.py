from flask_restful import Resource

from .trigram import Trigram
from ..data import HEXAGRAMS

class Hexagram(Resource):

    def __init__(self) -> None:
        self.lower_trigram = Trigram()
        self.upper_trigram = Trigram()
        self.binary_lines = self.lower_trigram.binary_lines + self.upper_trigram.binary_lines
        self.binary_changes = self.lower_trigram.as_binary_str('changing') + self.upper_trigram.as_binary_str('changing')
        self.title = HEXAGRAMS[self.binary_lines]['title']
        self.symbol = HEXAGRAMS[self.binary_lines]['symbol']
        self.changing_lines = [index+1 for index,value in enumerate(self.binary_changes) if value == '1']

    def transform_hexagram(self) -> dict:
        if self.changing_lines:
            indexes = [line-1 for line in self.changing_lines]
            transformed_hexagram = list(self.binary_lines)
            for index in indexes:
                if transformed_hexagram[index] == '0':
                    transformed_hexagram[index] = '1'
                else:
                    transformed_hexagram[index] = '0'
            return HEXAGRAMS[''.join(transformed_hexagram)]

    def get(self) -> dict:
        if not self.changing_lines:
            self.changing_lines = None
        return{
            'title': self.title,
            'symbol': self.symbol,
            'upper_trigram': {
                'title': self.upper_trigram.title,
                'symbol': self.upper_trigram.symbol
            },
            'lower_trigram': {
                'title': self.lower_trigram.title,
                'symbol': self.lower_trigram.symbol
            },
            'changing_lines': self.changing_lines,
            'transformed_hexagram': self.transform_hexagram()
        }
