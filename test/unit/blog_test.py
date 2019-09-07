#blog post
from unittest import TestCase
from blog import Blog

class BlogTest(TestCase):
    def test_blog(self):
        b = Blog('BookName','sem',[])

        self.assertEqual('BookName',b.book)
        self.assertEqual('sem',b.author)

    def test_createdPost(self):
        b = Blog('BookName1','sem',[])
        b1 = Blog('BookName2','kamlesh',[])

        self.assertEqual(b.__repr__(),"kamlesh is test by sem(0 posts)")
        self.assertEqual(b1.__repr__(),"kamlesh is test by sem(0 posts)")