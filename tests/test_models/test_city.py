import unittest
import os
from models.city import City
from models.engine.file_storage import FileStorage
from models import storage
from models.base_model import BaseModel

class TestCity(unittest.TestCase):

    # Set up and tear down methods
    def setUp(self):
        pass

    def tearDown(self):
        self.resetStorage()

    def resetStorage(self):
        FileStorage._FileStorage__objects = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    # Test cases for City class
    def test_instantiation(self):
        # Test instantiation of City class
        city_instance = City()
        self.assertEqual(str(type(city_instance)), "<class 'models.city.City'>")
        self.assertIsInstance(city_instance, City)
        self.assertTrue(issubclass(type(city_instance), BaseModel))

    # Other test methods...

    def test_attributes(self):
        # Test the attributes of City class
        attributes = storage.attributes()["City"]
        city_instance = City()
        for attribute_name, attribute_type in attributes.items():
            self.assertTrue(hasattr(city_instance, attribute_name))
            self.assertEqual(type(getattr(city_instance, attribute_name, None)), attribute_type)

if __name__ == "__main__":
    unittest.main()

