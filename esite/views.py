import logging
logger = logging.getLogger(__name__)

from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404
from django.shortcuts import render, redirect

from store.models import Store

def index(request):
    logger.debug('index.html - calling esite.views.index()')
#     store = get_object_or_404(Store, code='10001')
    
    requestContext = RequestContext(request, {
        'page_title': 'Home',
#         'store': store
    })
        
    return render(request, 'index.html', requestContext)
#     return redirect('products')


def file_not_found_404(request):
    page_title = 'Page Not Found'
    return render_to_response("404.html", locals(), context_instance=RequestContext(request))

def server_error_500(request):
    return render_to_response('500.html')

def app_offline(request):
    page_title = 'Application is offline'
    return render_to_response('app_offline.html', locals(), context_instance=RequestContext(request))
