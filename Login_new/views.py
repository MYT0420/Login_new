# -*- encoding=UTF-8 -*-

from Login_new import app, db
from flask import render_template, redirect, request
from Login_new.models import User


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = User.query.filter_by(username=username, password=password).first()
        user_name = User.query.filter_by(username=username).first()
        user_pass = User.query.filter_by(password=password).first()
        if user:
            return 'Hello ' + str(username) + ' !'
        if not user_name:
            db.session.add(User(username, password))
            db.session.commit()
            return render_template('login.html')
        if user_name and not user_pass:
            return 'Wrong password!'
    if request.method == 'GET':
        return render_template('login.html')
    return 'Bad login!'
