#! /usr/bin/python3

import cgi
import subprocess

print("content-type: text/html")
print()

mydata = cgi.FieldStorage()

myx = mydata.getvalue("c")


o = subprocess.getoutput("sudo " + myx)

print("\n Hello User Wellcome to the output Screen")
print("<br />"
print("<br />")

print("Your Command is : ",myx)

print("<br />")
print("<br />")

print("output is:",o)
