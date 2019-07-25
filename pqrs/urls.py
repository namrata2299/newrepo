
from rest_framework import routers
from pqrs.views import *
router =routers.SimpleRouter()
router.register(r'books',BookOperations)

urlpatterns=router.urls
