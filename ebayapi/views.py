from django.shortcuts import render
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
from django.core import urlresolvers
from django.http import HttpResponseRedirect
from . import requests

'''
sport - 95672
heels - 55793
boots - 53557
Oxfords- 45333
work - 53548
sandals - 62107
slippers - 11632
bags - 169291
'''

def home(request):
    return render(request, "home.html")


def show_category(request, page='1', category_id = '3034'):
        reply = requests.query_category(request, page, category_id)

        #if reply:
        return render_to_response("category.html", 
        {'imgs':reply['imgs'], 
        'category':reply['category'],
        'total_pages':reply['total_pages'], 
        'total_entries':reply['total_entries'],
        'minprice_selected':reply['minprice_selected'],
        'maxprice_selected':reply['maxprice_selected']},
        context_instance=RequestContext(request))
        # else:
        #     return HttpResponseRedirect("/")



def show_product(request, itemID):
    reply = requests.query_product(request, itemID)

    return render_to_response("product.html", 
    {'title':reply['title'], 
    'price':reply['price'], 
    'pics':reply['pics'], 
    'condition':reply['condition'], 
    'condition_desc':reply['condition_desc'],
    'shipping':reply['shipping'], 
    'size':reply['size'], 
    'width':reply['width'],
    'material':reply['material'], 
    'color':reply['color'], 
    'kabluk':reply['kabluk']},
    context_instance=RequestContext(request))