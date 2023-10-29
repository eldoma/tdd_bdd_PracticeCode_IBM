"""
Test Cases TestAccountModel
"""
import json
from unittest import TestCase
from models import db
from models.account import Account

ACCOUNT_DATA = {}

class TestAccountModel(TestCase):
    """Test Account Model"""

    @classmethod
    def setUpClass(cls):
        """ Connect and Load data needed by tests """
        db.create_all()  # make our SQLAlchemy tables, part of Step 03.1: Initialize the Database
        global ACCOUNT_DATA
        with open('tests/fixtures/account_data.json') as json_data:
            ACCOUNT_DATA = json.load(json_data) # make our SQLAlchemy tables, part of Step 03.2: Load Test Data

    @classmethod
    def tearDownClass(cls):
        """Disconnect from database"""
        db.session.close() # close the database session, part of Step 03.1: Initialize the Database

    def setUp(self):
        """Truncate the tables"""
        db.session.query(Account).delete()
        db.session.commit() # Clear out the tables before each test part of Step 03.5

    def tearDown(self):
        """Remove the session"""
        db.session.remove() # Clear out the tables before each test part of Step 03.5

    ######################################################################
    #  T E S T   C A S E S
    ######################################################################
  
    def test_create_all_accounts(self):
        """ Test creating multiple Accounts """
        for data in ACCOUNT_DATA: # a Test Case to Create All Accounts, part of Step 03.3, 03.4
            account = Account(**data)
            account.create()
        self.assertEqual(len(Account.all()), len(ACCOUNT_DATA))