#blog post
from unittest import TestCase
from blog import Blog

class BlogTest(TestCase):
    def test_blog(self):
        b = Blog('BookName','sem')

        self.assertEqual('BookName',b.book)
        self.assertEqual('sem',b.author)

    def test_TitleAndAuthors(self):
        b = Blog('BookName1','sem')
        b1 = Blog('BookName2','kamlesh')

        self.assertEqual(b.__repr__(),"BookName1 is test by sem(0 posts)")
        self.assertEqual(b1.__repr__(),"BookName2 is test by kamlesh(0 posts)")

    #this is TDD way testing 
    def test_createdPost(self):
        b = Blog('BookName1','sem')
        b1 = Blog('BookName2','kamlesh')
        b1.post = ['1_post']
        b2 = Blog('BookName3','aman')
        b2.post = ['1_post','2_post']

        self.assertEqual(b.__repr__(),"BookName1 is test by sem(0 posts)")
        self.assertEqual(b1.__repr__(),"BookName2 is test by kamlesh(1 posts)")
        self.assertEqual(b2.__repr__(),"BookName3 is test by aman(2 posts)")