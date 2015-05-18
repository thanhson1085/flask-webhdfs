from flask import render_template
from app import app
from elasticsearch import Elasticsearch
from config import config as cfg
import json
from flask import request, redirect
from app import db
from app.module_search.models import User

es_url = "{}:{}".format(cfg.ELASTIC_HOST, cfg.ELASTIC_PORT)
es = Elasticsearch([es_url])

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Ngoc Cuong'}
    #es = Elasticsearch([{"hosts": cfg.ELASTIC_HOST, "port": cfg.ELASTIC_PORT}])
    res = es.search(index="test_feeder", body={"query": {"match_all": {}}})
    users = User.query.all()

    return render_template('module_search/index.html', title='Home page', user = user, data=users, autocomplete=res)

@app.route('/insert', methods=["POST"])
def insert_user():
    params = request.form
    user = User(username=params['username'], password=params['password'], email=params['email'], first_name=params['first_name'], last_name=params['last_name'])
    try:
        db.session.add(user)
        db.session.commit()

        new_user = User.query.order_by(User.id.desc()).first()
        es.index(index="test_feeder", doc_type="test_feeder_type", body={
                    "id": new_user.id,\
                    "username": new_user.username,\
                    "password": new_user.password,\
                    "first_name": new_user.first_name,\
                    "last_name": new_user.last_name,\
                    "email": new_user.email,\
                })
    except Exception as e:
        print(e)
    return redirect("/")

@app.route("/delete/<int:id>")
def delete_user(id):
    try:
        User.query.filter(User.id==id).delete()
        db.session.commit()
        es.delete_by_query(index='test_feeder', doc_type='test_feeder_type', body={
                              "query": {
                                           "match": {"id": id}
                                       }
                          })
    except Exception as e:
        print(e)
    return redirect("/")

@app.route("/get_user_by_name", methods=["POST"])
def get_user_by_name():
    params = request.data
    #print(params)
    username = params
    print(username)
    users = User.query.filter(User.username==username).all()
    results = []
    for u in users:
        dicts = {
            "id" : u.id,
            "username": u.username,
            "email": u.email,
            "password": u.password,
            "first_name": u.first_name,
            "last_name": u.last_name
        }
        results.append(dicts)
    data = json.dumps(results)
    return data

