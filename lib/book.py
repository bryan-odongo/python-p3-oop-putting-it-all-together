#!/usr/bin/env python3


class Book:
    def __init__(self, title, pages=0):
        self.title = title
        self._pages = pages

    def turn_page(self):
        print("Flipping the page...wow, you read fast!")

    @property
    def page_count(self):
        return self._pages

    @page_count.setter
    def page_count(self, value):
        if isinstance(value, int):
            self._pages = value
        else:
            print("page_count must be an integer")
