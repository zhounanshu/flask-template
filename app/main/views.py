#!/ustr/bin/env python
# -*- coding: utf-8 -*-
from ..models import *
from flask import request
from flask.ext.restful import Resource, reqparse
import time


def to_json(model):
    """ Returns a JSON representation of an SQLAlchemy-backed object. """
    json = {}
    for col in model._sa_class_manager.mapper.mapped_table.columns:
        json[col.name] = getattr(model, col.name)
    return json


def to_json_list(model_list):
    json_list = []
    for model in model_list:
        json_list.append(to_json(model))
    return json_list


class ExpResource(Resource):

    def get(self, id):
        record = Example.query.filter_by(id=id).first()
        return to_json(record), 200

    def put(self, id):
        parser = reqparse.RequestParser()
        parser.add_argument('time', type=str)
        parser.add_argument('field1', type=str)
        parser.add_argument('field2', type=str)
        parser.add_argument('field3', type=str)
        parser.add_argument('field4', type=str)
        args = parser.parse_args(strict=True)
        record = Example.query.filter_by(id=id).first()
        if record:
            record.time = args['time']
            record.field1 = args['field1']
            record.field1 = args['field2']
            record.field1 = args['field3']
            record.field1 = args['field4']
            db.session.commit()
            return {"status": "ok"}
        return {"status": "ok"}

    def delete(self, id):
        record = Example.query.filter_by(id=id).first()
        if record:
            db.session.delete(record)
            db.session.commit()
            return {"status": "deleted"}, 204
        return {"status": "not exit"}, 400


class ExpList(Resource):

    def get(self):
        try:
            field1 = request.args.get('field1')
            start_time = request.args.get('start_time')
            end_time = request.args.get('end_time')
            if (start_time is not None) and (end_time is not None):
                records = Example.query.filter(
                    Example.time >= start_time,
                    Example.time <= end_time,
                    field1 == field1
                ).order_by('time desc').limit(10)
            else:
                records = Example.query.order_by(
                    Example.time.desc()).limit(10).all()
                return to_json_list(records)
        except:
            return{"status": "error"}

    # post json data into database
    def post(self):
        paser = reqparse.RequestParser()
        paser.add_argument('time', type=str)
        paser.add_argument('field1', type=str)
        paser.add_argument('field2', type=str)
        paser.add_argument('field3', type=str)
        paser.add_argument('field4', type=str)
        args = paser.parse_args(strict=True)
        if time is None:
            return {"status": "no data"}
        new_record = Example(
            args['time'], args['field1'], args['field2'], args['field3'], args['field4'])
        try:
            db.session.add(new_record)
            db.session.commit()
        except:
            print "something wrong"
