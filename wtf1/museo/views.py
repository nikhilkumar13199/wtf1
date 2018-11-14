# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.db import connection

# Create your views here.

def index(request):
	cursor=connection.cursor()
	args={}
	cursor.execute('''select * from movies_list''')
	row=cursor.fetchall()
	print('ROW:',row)
	args['row']=row
	return render(request,'museo/index.html',args)