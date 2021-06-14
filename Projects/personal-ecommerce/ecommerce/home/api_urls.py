from rest_framework import routers
from home.views import *
from django.urls import path,include

router=routers.DefaultRouters()
router.register('items',ItemViewSet)


urlpatterns=[
    path('',include(router.urls)),
]