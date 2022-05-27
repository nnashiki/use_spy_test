import chat
from chat import __version__, ChatClient
import unittest
from unittest.mock import Mock, MagicMock

def test_version():
    assert __version__ == '0.1.0'

def test_client_connection():
    with unittest.mock.patch('chat.external_method') as mock_method:
        client = ChatClient("User 1")
        client.send_message("Hello World")
    mock_method.assert_called()


def test_class_mocking():
    @unittest.mock.patch('module.ClassName2')
    @unittest.mock.patch('module.ClassName1')
    def test(MockClass1, MockClass2):
        module.ClassName1()
        module.ClassName2()
        assert MockClass1 is module.ClassName1
        assert MockClass2 is module.ClassName2
        assert MockClass1.called
        assert MockClass2.called


def test_method_mocking():
    class ProductionClass:

        def method(self):
            return 'hoge'

    with unittest.mock.patch.object(ProductionClass, 'method', return_value=None) as mock_method:
        thing = ProductionClass()
        assert thing.method(1, 2, 3) is None
        mock_method.assert_called_once_with(1, 2, 3)
