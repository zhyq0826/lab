import realpath
from db.conn import DBSession
from models.blog import Entries 



def test_session_entries():
    assert isinstance(DBSession().query(Entries).all(), list)