import unittest
import os
from models.review import Review
from models.engine.file_storage import FileStorage
from models import storage
from models.base_model import BaseModel

class TestReview(unittest.TestCase):

    # Set up and tear down methods
    def setUp(self):
        pass

    def tearDown(self):
        self.resetStorage()

    def resetStorage(self):
        FileStorage._FileStorage__objects = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    # Test cases for Review class
    def test_instantiation(self):
        # Test instantiation of Review class
        review_instance = Review()
        self.assertEqual(str(type(review_instance)), "<class 'models.review.Review'>")
        self.assertIsInstance(review_instance, Review)
        self.assertTrue(issubclass(type(review_instance), BaseModel))

    # Other test methods...

    def test_attributes(self):
        # Test the attributes of Review class
        attributes = storage.attributes()["Review"]
        review_instance = Review()
        for attribute_name, attribute_type in attributes.items():
            self.assertTrue(hasattr(review_instance, attribute_name))
            self.assertEqual(type(getattr(review_instance, attribute_name, None)), attribute_type)

if __name__ == "__main__":
    unittest.main()

