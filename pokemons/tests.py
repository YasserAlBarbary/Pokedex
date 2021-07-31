from django.test import TestCase
from .models import Pokemon


class PokemonModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Pokemon.objects.create(
            name="pikachu",
            description='''When several of these POKéMON gather, their electricity could build and cause lightning storms.''',
            habitat="forest",
            is_legendary=False,
        )

    def test_description_content(self):
        pokemon = Pokemon.objects.get(name="pikachu")
        expected_object_name = f'{pokemon.description}'
        self.assertEqual(expected_object_name, '''When several of these POKéMON gather, their electricity could build and cause lightning storms.''')

    def test_name_content(self):
        pokemon = Pokemon.objects.get(name="pikachu")
        expected_object_name = pokemon.name
        self.assertEqual(expected_object_name, "pikachu")

    def test_body_content(self):
        pokemon = Pokemon.objects.get(name="pikachu")
        expected_object_name = pokemon.habitat
        self.assertEqual(expected_object_name, "forest")

    def test_is_legendary_content(self):
        pokemon = Pokemon.objects.get(name="pikachu")
        expected_object_name = f'{pokemon.is_legendary}'
        print("legend?",expected_object_name)
        self.assertTrue(expected_object_name, False)
