import configparser
from distutils.command.build import build
from unicodedata import name
from kivy.app import App
from  kivymd.app import MDApp 
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, SlideTransition
from kivymd.toast import toast
from datetime import datetime
import mysql.connector
import pymysql

class Empresas(Screen):
    def build(self):
        Builder.load_file("empresas.kv")

        sm = Screen()
        
        
    