from faker.providers import BaseProvider
import json
from os.path import dirname, abspath, join


DIR = dirname(abspath(__file__))


class GenderNeutralNameProvider(BaseProvider):

    def __init__(self, generator):
        self.generator = generator
        self.adjectives = json.loads(open(join(DIR, 'data', 'adjective.json')).read())
        self.names = json.loads(open(join(DIR, 'data', 'names.json')).read())

    def name(self):
        return '{adjective} {name}'.format(
            adjective=self.random_element(elements=self.adjectives).capitalize(),
            name=self.random_element(elements=self.names).capitalize()
        )
