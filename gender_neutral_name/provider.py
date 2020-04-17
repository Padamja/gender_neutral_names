from faker.providers import BaseProvider
import json


class GenderNeutralNameProvider(BaseProvider):

    def __init__(self, generator):
        self.generator = generator
        self.adjectives = json.loads(open('data/adjective.json').read())
        self.names = json.loads(open('data/names.json').read())

    def name(self):
        return self.random_element(elements=self.adjectives) + ' ' + self.random_element(elements=self.names)