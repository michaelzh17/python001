# -*- coding: utf-8 -*-


def greet_user(username):
	"""Display a simple greeting."""
	print("Hello " + username.title() + "!")

greet_user('Jessie')

greet_user('Joven')

greet_user('Victor')


def display_message():
	"""Display a message."""
	print("In this chapter, I learn function which is designed to do one specific job.")

display_message()


def favorite_book(title):
	"""Display my favorite book"""
	print("One of my favorite books is " + title.title() + ".")

favorite_book("the old man and the sea")
