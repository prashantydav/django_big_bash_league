from django.shortcuts import render
from .models import match , Squad
from Squadinfo.mixins import value_stored
# Create your views here.
value_stored()
def home_view(requests):
    # if requests.method == 'post':
    #     code = requests.POST.get('match_id')

    mat = match.objects.all()
    con = {
        'mat': mat
    }
    return render(requests,'home.html',con)

def Squad_view(requests):

    mat = Squad.objects.all()
    con = {
        'mat': mat
    }
    return render(requests,'mat.html',con)