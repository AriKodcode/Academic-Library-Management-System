class Book:

    def __init__(self, title: str, author: str, ison: str, is_available=True):
        self.title = title
        self.author = author
        self.ison = ison
        self.is_available = is_available

    def get_details(self):
        return f"title: {self.title}, author: {self.author}, ison: {self.ison}, is available?: {self.is_available}"
