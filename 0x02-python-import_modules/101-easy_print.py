#!/usr/bin/python3
(lambda f: f(f))(lambda f: __import__("sys").stdout.write("#pythoniscool\n"))

