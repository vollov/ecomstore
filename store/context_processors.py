from esite import settings
# from django.conf import settings
from models import Category, Store

def ecomstore(request):
    """ context processor for the site templates """
    return {
            'site_name': settings.SITE_NAME,
            'active_store': Store.objects.get(code=settings.STORE_CODE),
            'meta_keywords': settings.META_KEYWORDS,
            'meta_description': settings.META_DESCRIPTION,
#             'analytics_tracking_id': settings.ANALYTICS_TRACKING_ID,
            'request': request
            }
