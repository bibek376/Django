#python program
from django.htpp import HtppResponse
def index(requests):
    return HtppResponse("Hello")