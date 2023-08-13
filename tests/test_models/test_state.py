import unittest
import os
from models.state import State
from models.engine.file_storage import FileStorage
from models import storage
from models.base_model import BaseModel

class TestState(unittest.TestCase):

    # Set up and tear down methods
    def setUp(self):
        pass

    def tearDown(self):
        self.resetStorage()

    def resetStorage(self):
        FileStorage._FileStorage__objects = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    # Test cases for State class
    def test_instantiation(self):
        # Test instantiation of State class
        state_instance = State()
        self.assertEqual(str(type(state_instance)), "<class 'models.state.State'>")
        self.assertIsInstance(state_instance, State)
        self.assertTrue(issubclass(type(state_instance), BaseModel))

    # Other test methods...

    def test_attributes(self):
        # Test the attributes of State class
        attributes = storage.attributes()["State"]
        state_instance = State()
        for attribute_name, attribute_type in attributes.items():
            self.assertTrue(hasattr(state_instance, attribute_name))
            self.assertEqual(type(getattr(state_instance, attribute_name, None)), attribute_type)

if __name__ == "__main__":
    unittest.main()

