from flask import Flask, render_template, request, jsonify
from database.db import connectionSQL, add_user, consult_user
from controllers.admin_s3 import *
from server import app

def func_home_page():
    return render_template("home.html")

def func_register_page():
    return render_template("register.html")

def func_register_user():
    data_user = request.form
    data_photo = request.files
    id = data_user["id"]
    name = data_user["name"]
    lastname = data_user["lastname"]
    birthday = data_user["birthday"]
    photo = data_photo["photo"]
    confirm = add_user(id, name, lastname, birthday)
    if confirm:
        photo_path, photo_name = save_file(photo, id)
        upload_file(photo_path, photo_name)
        return "<h1> User added </h1>"
    else:
        return "<h1> Error creating the user </h1>"

def func_consult_page():
    return render_template("consult.html")

def func_consult_user():
    id = request.get_json()
    result_data = consult_user(id)
    obj_data = {
        'name':result_data[0][1],
        'lastname':result_data[0][2],
        'birthday':result_data[0][3]
    }
    return jsonify(obj_data)