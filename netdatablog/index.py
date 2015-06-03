import datetime, string, json, functools
from django.shortcuts import render_to_response, HttpResponse
from blog.models import news

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
    s2 = datetime.datetime.now().strftime("\n        %Y-%m-%d")
    page = string.atoi(req.REQUEST.get('page', '0'))
    news_objs = news.objects.filter(news_time__gte=s2)[page * pagesize: page * pagesize + 5]
    for news_obj in news_objs:
        if news_obj.news_time > s2:
            print(news_obj.news_time)
            print(s2)
            print('aaaa')
        else:
            print(news_obj.news_time)
            print(s2)
            print('bbbb')
    return [obj_serialize(news_obj, getattr(news_obj, 'list_fields')) for news_obj in news_objs]
