from flask import Flask, flash, jsonify, redirect, render_template, request, session
from flask_session import Session
import sqlite3
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash
from defs import sql_connection, sql_table, login_required, apology
import sqlite3
from sqlite3 import Error
app = Flask(__name__)

con = sql_connection()

sql_table(con)

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        pass
    else:
        return render_template("login.html")