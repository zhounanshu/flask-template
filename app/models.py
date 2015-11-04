#!/usr/bin/env python
# -*- coding: utf-8 -*-
from . import db


class Example(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    time = db.Column(db.String(255))
    field1 = db.Column(db.String(255))
    field2 = db.Column(db.String(255))
    field3 = db.Column(db.String(255))
    field4 = db.Column(db.String(255))

    def __init__(self, time, field1, field2, field3, field4):
        self.time = time
        self.field1 = field1
        self.field2 = field2
        self.field3 = field3
        self.field4 = field4
