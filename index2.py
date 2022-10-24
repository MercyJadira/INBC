from locale import currency
from kivy.uix.screenmanager import ScreenManager , NoTransition, Screen
import configparser
from kivymd.app import MDApp
from kivy.app import App
from kivy.lang import Builder
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.properties import ObjectProperty
import kivy
from datetime import datetime
import os, sys
from login import login
from empresas import Empresas

kivy.require('1.0.8')
Window.size = (350,580)


class LoginApp(MDApp):
  def build(self):
    #global screen_manager
    #screen_manager = ScreenManager()
    self.manager = ScreenManager(transition = NoTransition())    
    self.manager.add_widget(Builder.load_file("pre-splash.kv"))
#    self.manager.add_widget(Builder.load_file("empresas.kv"))

   # self .theme_cls.theme_style = 'Dark'
    self.theme_cls.primary_palette='DeepOrange'
    self.manager.add_widget(login(name = "login"))
  #  self.manager.add_widget(Empresas(name = "empresas"))
    
    return self.manager
  
    
  def on_start(self):
      Clock.schedule_once(self.login, 3)
      
  def login(self, *args):
      self.manager.current = "login"
   #  self.manager.current = "empresas"

      
if __name__=='__main__':
  LoginApp().run()
    
    