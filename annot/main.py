# -*- coding: utf-8 -*-

from annot._utils import _annotations_to_init


def annots(cls):
    """
    A class decorator that adds class attribute annotations to __init__.

    Example ::

        @annots
        class Account:
            __tablename__ = 'account'

            username: str
            password: str

    Become to ::

        class Account:
            def __init__(self, username, password):
                self.username = str
                self.password = str

    """
    new_init = _annotations_to_init(cls)
    cls.__init__ = new_init
    return cls
