from flask import Blueprint, render_template, redirect

website = Blueprint('website', __name__)

@website.route('/', methods=['GET', 'POST'])
def index():
    return "123"