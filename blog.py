class Blog():
    def __init__(self,book,author):
        self.book = book
        self.author = author
        self.post = []

    #now tested all things
    def __repr__(self):
        return "{} is test by {}({} posts)".format(self.book,self.author,len(self.post))