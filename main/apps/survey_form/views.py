# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

# Create your views here.
def index(req):
    if 'sNumber' not in req.session:
        req.session['sNumber'] = 0
    context = {
        'sNumber': req.session['sNumber'],
    }
    return render(req, 'survey_form/index.html', context)

def surveysProcess(req):
    req.session['sNumber'] +=1
    
    form = req.POST
    req.session['name'] = form.get('name')
    req.session['location'] = form.get('location')
    req.session['language'] = form.get('language')
    req.session['comment'] = form.get('comment')

    return redirect('/result')

def result(req):
    context = {
        'sNumber': req.session['sNumber'],
        'name': req.session['name'],
        'location': req.session['location'],
        'language': req.session['language'],
        'comment': req.session['comment'],
    }
    return render(req, 'survey_form/result.html', context)

def goBack(req):
    return render(req, 'survey_form/index.html')