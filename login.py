import configparser
from tkinter import messagebox
from unicodedata import name
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import  SlideTransition, Screen
from kivymd.toast import toast
from datetime import datetime
from matplotlib.pyplot import connect
import mysql.connector
import pymysql


class login(Screen):
    pass
    def connect(self):
        app = App.get_running_app()
        input_user = app.manager.get_screen('login').ids['input_user'].text
        input_password = app.manager.get_screen('login').ids['input_password'].text
        config = configparser.ConfigParser()
        config.read('config.ini')
        
        host = config['mysql']['host']
        user = config['mysql']['user']
        password = config['mysql']['password']
        dbname = config['mysql']['db']
        
        db = mysql.connector.Connect(host = str(host), user = str(user), password = str(password), database = str(dbname))
       # db = mysql.connector.connect(user='root', password='administrador', host='localhost', database = 'asistencia', port='3307')
        cursor = db.cursor()
        
        query = "SELECT count(*) FROM users where usuario= '" + str(input_user)+"' and password = '" +str(input_password)+ "'" 
        cursor.execute(query)
        data = cursor.fetchone()
        count = data[0]
        
        if count == 0:
            messagebox.showwarning("Cuidado",'Usuario y/o contraseña Invalido')
           # toast('Usuario y/o contraseña Invalido')
        else: 
           # toast('Datos Correctos')
            Builder.load_file('empresas.kv')
            now = datetime.now()
            query = "update users set last_login='" + str(input_user)+"' and password = '" +str(input_password)+ "'" 
            cursor.execute(query)
            db.commit()
        db.close()
        pass