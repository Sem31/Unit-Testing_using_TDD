#blog post
from unittest import TestCase
from blog import Blog

class BlogTest(TestCase):
    def test_blog(self):
        b = Blog('BookName','sem',[])

        self.assertEqual('BookName',b.book)
        self.assertEqual('sem',b.author)