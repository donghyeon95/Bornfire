from flask import Blueprint, render_template, jsonify, request, redirect
import pymongo

mypage = Blueprint("mypage", __name__)

@mypage.route("/my-page")
def get_myPage():
    return render_template('my-page.html')


