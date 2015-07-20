from sqlalchemy import Column, DateTime, String, Integer, ForeignKey, func, \
    create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref, sessionmaker
import json, time, logging, os, sys


sys.settrace
 
Base = declarative_base()

directory_name = os.path.join(os.getcwd())

# set up logging to file - see previous section for more details
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                    datefmt='%m-%d %H:%M',
                    filename='myapp.log',
                    filemode='w')
# define a Handler which writes INFO messages or higher to the sys.stderr
console = logging.StreamHandler()
console.setLevel(logging.INFO)
# set a format which is simpler for console use
formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
# tell the handler to use this format
console.setFormatter(formatter)
# add the handler to the root logger
logging.getLogger('').addHandler(console)

# create logger
logger = logging.getLogger('it-ebook')
logger.setLevel(logging.DEBUG)
# create file handler which logs even debug messages
fh = logging.FileHandler('itebook.log')
fh.setLevel(logging.DEBUG)
# create console handler with a higher log level
ch = logging.StreamHandler()
ch.setLevel(logging.ERROR)
# create formatter and add it to the handlers
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
fh.setFormatter(formatter)
# add the handlers to logger
logger.addHandler(ch)
logger.addHandler(fh)

class Book(Base):
    """A Book class is an entity having database table."""
    
    __tablename__ = 'book'
    id = Column(Integer, primary_key=True, autoincrement=True)
    bookName = Column('book_name', String(46), nullable=False)  # Title
    subTitle = Column('sub_title', String)  # Title
    isbn_10 = Column(String)  # isbn_10
    isbn_13 = Column(String)  # isbn_13
    series = Column(String)  # series
    dimension = Column(String)  # dimension
    customerReview = Column('customer_review', String)  # customerReview
    bookDescription = Column('book_description', String)  # bookDescription
    editionNo = Column('edition_no', String)  # editionNo
    publisher = Column(String)  # publisher
    bookFormat = Column("book_format", String)  # bookFormat
    fileSize = Column('file_size', String)  # fileSize
    numberOfPages = Column('number_of_pages', String)  # numberOfPages
    inLanguage = Column('in_language', String)  # inLanguage
    publishedOn = Column('published_on', DateTime, default=func.now())
    hasCover = Column('has_cover', String)  # hasCover
    hasCode = Column('has_code', String)  # hasCode
    bookPath = Column('book_path', String)  # bookPath
    rating = Column('rating', String)  # rating
    uuid = Column('uuid', String)  # uuid
    createdOn = Column('created_on', DateTime, default=func.now())
    authors = relationship(
        'Author',
        secondary='author_book_link', lazy='joined'
    )
    
#     def __repr__(self):
#         rep=''
#         print self.__dict__
#         return  ''
# 
#     def __str__(self):
#         return ''
    
class Author(Base):
    """A Author class is an entity having database table."""
    
    __tablename__ = 'author'
    id = Column(Integer, primary_key=True)
    authorName = Column('author_name', String(46), nullable=False, autoincrement=True)
    aboutAuthor = Column('about_author', String)
    email = Column(String, unique=True)
    created_on = Column(DateTime, default=func.now())
    
    books = relationship(
        Book,
        secondary='author_book_link'
    )
 
 
class AuthorBookLink(Base):
    """A AuthorBookLink class is an entity having database table. This class is for many to many association between Author and Book."""
    
    __tablename__ = 'author_book_link'
    id = Column(Integer, primary_key=True)
    authorId = Column('book_id', Integer, ForeignKey('author.id'))
    bookId = Column('author_id', Integer, ForeignKey('book.id'))
    extra_data = Column(String(256))
    author = relationship(Author, backref=backref("book_assoc"))
    book = relationship(Book, backref=backref("dauthor_assoc"))

class CreateDatabase:
    
    def creatingDatabase(self):
        directory_name = os.path.join(os.getcwd(), 'books')
        if not os.path.exists(directory_name):
            os.makedirs(directory_name, 777)
        os.chdir(directory_name)
        # engine = create_engine('sqlite:///calibre.sqlite', echo=True)
        engine = create_engine('sqlite:///calibre.sqlite', echo=True)
        session = sessionmaker()
        
        
        session.configure(bind=engine)
        Base.metadata.drop_all(engine)
        
        Base.metadata.create_all(engine)

        return session
    
def main():
    global books, frame
    session = CreateDatabase().creatingDatabase()
    

if __name__ == '__main__':
    main()
