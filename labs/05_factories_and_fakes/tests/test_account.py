"""
Test Cases TestAccountModel
"""
# import json, deleted, step 05.10
from factories import AccountFactory # Update the Test Cases, Step 05.03
# from random import randrange, deleted, step 05.10
from unittest import TestCase
from models import db
from models.account import Account, DataValidationError

# ACCOUNT_DATA = {}, deleted ACCOUNT_DATA, step 05.10

class TestAccountModel(TestCase):
    """Test Account Model"""

    @classmethod
    def setUpClass(cls):
        """ Load data needed by tests """
        db.create_all()  # make our sqlalchemy tables, Remove ACCOUNT_DATA references, step 05.10

    @classmethod
    def tearDownClass(cls):
        """Disconnext from database"""
        db.session.close()

    def setUp(self):
        """Truncate the tables"""
        db.session.query(Account).delete()
        db.session.commit() # Remove ACCOUNT_DATA references, step 05.10

    def tearDown(self):
        """Remove the session"""
        db.session.remove()

    ######################################################################
    #  T E S T   C A S E S
    ######################################################################

    def test_create_all_accounts(self):
        """ Test creating multiple Accounts """
        for _ in range(10):
            account = AccountFactory()
            account.create()
        self.assertEqual(len(Account.all()), 10) # Update the Test Cases, Step 05.03

    def test_create_an_account(self):
        """ Test Account creation using known data """
        account = AccountFactory()
        account.create()
        self.assertEqual(len(Account.all()), 1) # Update test_create_an_account(), Step 05.04

    def test_repr(self):
        """Test the representation of an account"""
        account = Account()
        account.name = "Foo"
        self.assertEqual(str(account), "<Account 'Foo'>")

    def test_to_dict(self):
        """ Test account to dict """
        account = AccountFactory()
        result = account.to_dict()
        self.assertEqual(account.name, result["name"])
        self.assertEqual(account.email, result["email"])
        self.assertEqual(account.phone_number, result["phone_number"])
        self.assertEqual(account.disabled, result["disabled"])
        self.assertEqual(account.date_joined, result["date_joined"]) # Update test_to_dict(), Step 05.05

    def test_from_dict(self):
        """ Test account from dict """
        data = AccountFactory().to_dict()
        account = Account()
        account.from_dict(data)
        self.assertEqual(account.name, data["name"])
        self.assertEqual(account.email, data["email"])
        self.assertEqual(account.phone_number, data["phone_number"])
        self.assertEqual(account.disabled, data["disabled"]) # Update test_from_dict(), Step 05.06

    def test_update_an_account(self):
        """ Test Account update using known data """
        account = AccountFactory()
        account.create()
        self.assertIsNotNone(account.id)
        account.name = "Rumpelstiltskin"
        account.update()
        found = Account.find(account.id)
        self.assertEqual(found.name, account.name) # Update test_an_account(), Step 05.07

    def test_invalid_id_on_update(self):
        """ Test invalid ID update """
        account = AccountFactory()
        account.id = None
        self.assertRaises(DataValidationError, account.update) # Update test_invalid_id_on_update(), Step 05.08

    def test_delete_an_account(self):
        """ Test Account update using known data """
        account = AccountFactory()
        account.create()
        self.assertEqual(len(Account.all()), 1)
        account.delete()
        self.assertEqual(len(Account.all()), 0) # Update test_delete_an_account(), Step 05.09

