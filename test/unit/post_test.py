# create the unit test for the post.py file
from unittest import TestCase
from post import Post

class PostTest(TestCase):
	def test_post(self):
		p = Post('postTitle','postContent')

		self.assertEqual('postTitle',p.title)
		self.assertEqual('postContent',p.content)

	def test_json(self):
		p = Post('sem','sem Content')

		expected = {'title' : 'sem','content' : 'sem Content'}
		self.assertDictEqual(expected,p.json())











