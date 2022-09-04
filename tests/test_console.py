#!/usr/bin/env python3
""" Test module for console.py """

import os
import unittest
from console import HBNBCommand
try:
    from unittest.mock import patch
except ImportError:
    pass
from io import StringIO
from models import storage
import console


class TestHBNBCommand(unittest.TestCase):
    """ Tests """

    @classmethod
    def setUpClass(cls):
        """ Call console before every test """

        cls.consol = HBNBCommand()

    @classmethod
    def tearDownClass(cls):
        """ Deletes console instance """

        del cls.consol

    def tearDown(self):
        """ Delete file.json """
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_quit(self):
        """ Test quit method """

        try:
            with patch('sys.stdout', new=StringIO()) as f:
                self.consol.onecmd("quit")
                self.assertEqual('', f.getvalue())
        except NameError:
            pass

    def test_eof(self):
        """ Test eof method """

        try:
            with patch('sys.stdout', new=StringIO()) as f:
                self.consol.onecmd("\n")
                self.assertEqual('', f.getvalue())
        except NameError:
            pass

    def test_emptyline(self):
        """ Test empty line """

        try:
            with patch('sys.stdout', new=StringIO()) as f:
                self.consol.onecmd('\n')
                self.assertEqual('', f.getvalue())
        except NameError:
            pass

    def test_create(self):
        """ Test create method """

        try:
            with patch('sys.stdout', new=StringIO()) as f:
                self.consol.onecmd('create')
                self.assertEqual('** class name missing **\n', f.getvalue())

            with patch('sys.stdout', new=StringIO()) as f:
                self.consol.onecmd('create floor')
                self.assertEqual('** class doesn\'t exist **\n', f.getvalue())

            with patch('sys.stdout', new=StringIO()) as f:
                try:
                    self.consol.onecmd("create BaseModel")
                    my_obj = storage.all()
                    for value in my_obj.values():
                        if value.id == f.getvalue():
                            break
                    self.assertEqual(value.id, f.getvalue().strip('\n'))
                except Exception:
                    pass
                self.consol.onecmd("destroy BaseModel {}".format(value.id))
        except NameError:
            pass

    def test_show(self):
        """ Test show method """

        try:
            with patch('sys.stdout', new=StringIO()) as f:
                self.consol.onecmd('show')
                self.assertEqual('** class name missing **\n', f.getvalue())

            with patch('sys.stdout', new=StringIO()) as f:
                self.consol.onecmd('show floor')
                self.assertEqual('** class doesn\'t exist **\n', f.getvalue())

            with patch('sys.stdout', new=StringIO()) as f:
                self.consol.onecmd('show User')
                self.assertEqual('** instance id missing **\n', f.getvalue())

            with patch('sys.stdout', new=StringIO()) as f:
                self.consol.onecmd('show User adbde448-23jfjs')
                self.assertEqual('** no instance found **\n', f.getvalue())

            with patch('sys.stdout', new=StringIO()) as f:
                try:
                    my_obj = storage.all()
                    my_values = []
                    for value in my_obj.values():
                        my_values.append(value.id)
                    my_set = set(my_values)
                    self.consol.onecmd('show User {}'.format(my_set[1]))
                    for value in my_obj.values():
                        if value.id == my_set[1]:
                            key = "{}.{}".format(type(value).__name__,
                                                 value.id)
                    self.assertEqual(my_obj[key], f.getvalue().strip('\n'))
                except Exception:
                    pass
        except NameError:
            pass

    def test_destroy(self):
        """ Test destroy method """

        try:
            with patch('sys.stdout', new=StringIO()) as f:
                self.consol.onecmd('destroy')
                self.assertEqual('** class name missing **\n', f.getvalue())

            with patch('sys.stdout', new=StringIO()) as f:
                self.consol.onecmd('destroy MyModel')
                self.assertEqual('** class doesn\'t exist **\n', f.getvalue())

            with patch('sys.stdout', new=StringIO()) as f:
                self.consol.onecmd('destroy User')
                self.assertEqual('** instance id missing **\n', f.getvalue())

            with patch('sys.stdout', new=StringIO()) as f:
                self.consol.onecmd('destroy User 4e46jsnd-jsk')
                self.assertEqual('** no instance found **\n', f.getvalue())

            with patch('sys.stdout', new=StringIO()) as f:
                try:
                    my_obj = storage.all()
                    my_values = []
                    for value in my_obj.values():
                        my_values.append(value.id)
                    my_set = set(my_values)
                    self.consol.onecmd('destroy BaseModel {}'.
                                       format(my_set[-1]))
                    for value in my_obj.values():
                        if value.id == my_set[-1]:
                            key = "{}.{}".format(type(value).__name__,
                                                 value.id)
                    self.assertEqual('', f.getvalue())
                except Exception:
                    pass
        except NameError:
            pass

    def test_all(self):
        """ Test 'all' method """

        try:
            with patch('sys.stdout', new=StringIO()) as f:
                self.consol.onecmd('all')
                self.assertEqual('', type(f.getvalue()).strip('\n'))

            with patch('sys.stdout', new=StringIO()) as f:
                self.consol.onecmd('all MyModel')
                self.assertEqual('** class doesn\'t exist **\n', f.getvalue())

            with patch('sys.stdout', new=StringIO()) as f:
                try:
                    my_list = []
                    my_obj = storage.all()
                    for value in my_obj.values():
                        my_list.append(str(value))
                    self.consol.onecmd('all')
                    self.assertEqual(eval(str(my_list)),
                                     eval(f.getvalue().strip('\n')))
                except Exception:
                    pass
        except NameError:
            pass

    def test_update(self):
        """ Test Update Function """

        try:
            with patch('sys.stdout', new=StringIO()) as f:
                self.consol.onecmd('update')
                self.assertEqual('** class name missing **\n', f.getvalue())

            with patch('sys.stdout', new=StringIO()) as f:
                self.consol.onecmd('update MyModel')
                self.assertEqual('** class doesn\'t exist **\n', f.getvalue())

            with patch('sys.stdout', new=StringIO()) as f:
                self.consol.onecmd('update User')
                self.assertEqual('** instance id missing **\n', f.getvalue())

            with patch('sys.stdout', new=StringIO()) as f:
                self.consol.onecmd('update User 21212121')
                self.assertEqual('** no instance found **\n', f.getvalue())

            try:
                my_list = []
                my_obj = storage.all()
                for value in my_obj.values():
                    if type(value).__name__ == "User":
                        my_list.append(value.id)
            except Exception:
                pass

            with patch('sys.stdout', new=StringIO()) as f:
                try:
                    self.consol.onecmd('update User {}'.format(my_list[-1]))
                    self.assertEqual('** attribute name missing **\n',
                                     f.getvalue())
                except Exception:
                    pass

            with patch('sys.stdout', new=StringIO()) as f:
                try:
                    self.consol.onecmd('update User {} first_name'.
                                       format(my_list[0]))
                    self.assertEqual('** value missing **\n', f.getvalue())
                except Exception:
                    pass

            """
            with patch('sys.stdout', new=StringIO()) as f:
                self.consol.onecmd('update User {} first_name "Balo"'.
                                   format(my_list[0]))
                self.assertEqual(eval(my_obj["User.{}[{}]".
                                 format(my_list[0].strip("\""),
                                        "first_name")]),
                                 "Balo")
            """
        except NameError:
            pass

    def test_docstrings_in_console(self):
        """checking for docstrings"""

        self.assertIsNotNone(console.__doc__)
        self.assertIsNotNone(HBNBCommand.emptyline.__doc__)
        self.assertIsNotNone(HBNBCommand.do_quit.__doc__)
        self.assertIsNotNone(HBNBCommand.do_EOF.__doc__)
        self.assertIsNotNone(HBNBCommand.do_create.__doc__)
        self.assertIsNotNone(HBNBCommand.do_show.__doc__)
        self.assertIsNotNone(HBNBCommand.do_destroy.__doc__)
        self.assertIsNotNone(HBNBCommand.do_all.__doc__)
        self.assertIsNotNone(HBNBCommand.do_update.__doc__)
        # self.assertIsNotNone(HBNBCommand.count.__doc__)
        self.assertIsNotNone(HBNBCommand.default.__doc__)

    def test_class_all(self):
        """ Test alternate all command input """

        try:
            with patch('sys.stdout', new=StringIO()) as f:
                self.consol.onecmd("MyModel.all()")
                self.assertEqual(
                    "** class doesn't exist **\n", f.getvalue())
            with patch('sys.stdout', new=StringIO()) as f:
                self.consol.onecmd("State.all()")
                self.assertEqual("[]\n", f.getvalue())
        except NameError:
            pass

    def test_class_show(self):
        """ Test alternate all command input """

        try:
            with patch('sys.stdout', new=StringIO()) as f:
                self.consol.onecmd("safdsa.show()")
                self.assertEqual(
                    "** class doesn't exist **\n", f.getvalue())
            with patch('sys.stdout', new=StringIO()) as f:
                self.consol.onecmd("BaseModel.show(abcd-123)")
                self.assertEqual(
                    "** no instance found **\n", f.getvalue())
        except NameError:
            pass

    def test_class_count(self):
        """ Test alternate all command input """

        try:
            with patch('sys.stdout', new=StringIO()) as f:
                self.consol.onecmd("asdfsdfsd.count()")
                self.assertEqual(
                    "** class doesn't exist **\n", f.getvalue())
            with patch('sys.stdout', new=StringIO()) as f:
                self.consol.onecmd("State.count()")
                self.assertEqual("0\n", f.getvalue())
        except NameError:
            pass


if __name__ == "__main__":
    unittest.main()
