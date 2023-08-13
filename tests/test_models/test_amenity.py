import unittest
import os
from models.amenity import Amenity
from models.engine.file_storage import FileStorage
from models import storage
from models.base_model import BaseModel

class TestAmenity(unittest.TestCase):

    def setUp(self):
        # Set up any necessary resources for each test method
        self.resetStorage()

    def tearDown(self):
        # Clean up resources after each test method
        self.resetStorage()

    def resetStorage(self):
        # Reset FileStorage data and delete the storage file if it exists
        FileStorage._FileStorage__objects = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_instantiation(self):
        # Test the instantiation of Amenity class
        amenity_instance = Amenity()
        self.assertEqual(str(type(amenity_instance)), "<class 'models.amenity.Amenity'>")
        self.assertIsInstance(amenity_instance, Amenity)
        self.assertTrue(issubclass(type(amenity_instance), BaseModel))

    def test_attributes(self):
        # Test the attributes of the Amenity class
        attributes = storage.attributes()["Amenity"]
        amenity_instance = Amenity()
        for attribute_name, attribute_type in attributes.items():
            self.assertTrue(hasattr(amenity_instance, attribute_name))
            self.assertEqual(type(getattr(amenity_instance, attribute_name, None)), attribute_type)

if __name__ == "__main__":
    unittest.main()

