from sqlalchemy import * 
from sqlalchemy import create_engine


engine = create_engine('mysql+pymysql://root:@localhost:3306/blog?charset=utf8')
metadata = MetaData()
user_likes = Table('user_likes', metadata, Column('id', Integer, primary_key=True), mysql_engine='InnoDB')


def create_all_tables():
    metadata.create_all(engine)

def create_one_tables():
    user_likes.create(engine, checkfirst=True)

def drop_one_table():
    user_likes.drop(engine, checkfirst=False)

if __name__ == '__main__':
    drop_one_table()