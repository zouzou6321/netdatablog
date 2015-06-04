import datetime, string, json, functools
from django.shortcuts import render_to_response, HttpResponse
from blog.models import news
from django.db.models import Q
pagesize = 5


def obj_serialize(event, fields_list):
    e = {}
    for field in fields_list:
        e[field] = '%s' % getattr(event, field)

    return e

def http_response(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kwargs):
        ret = fn(*args, **kwargs)
        return HttpResponse(json.dumps(ret))
    return wrapper

@http_response
def index(req):
    page = string.atoi(req.REQUEST.get('page', '0'))
    news_objs = news.objects.exclude(Q(news_time="") | Q(news_time=None)).order_by('-news_time')[page * pagesize: page * pagesize + 5]
    return [obj_serialize(news_obj, getattr(news_obj, 'list_fields')) for news_obj in news_objs]
