from flask import Flask, render_template_string, request, session, redirect, url_for, render_template
from werkzeug.security import generate_password_hash, check_password_hash 

usrInput = input("Pass: ")