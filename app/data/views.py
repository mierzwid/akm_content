import random
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from data.models import Aktualnosc
from data.models import MenuPrawe
from data.models import MenuGorne
from data.models import Strona
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse

def save(request, wpis_id):
    p = get_object_or_404(Aktualnosc, pk=wpis_id)
    p.save()
    
    # Always return an HttpResponseRedirect after successfully dealing
    # with POST data. This prevents data from being posted twice if a
    # user hits the Back button.
    return HttpResponseRedirect(reverse('wpis_results', args=(p.id,)))
	
def load_menu():
	image = random.randint(1, 50)
	menu_prawe = MenuPrawe.objects.order_by('nazwa')[:15]
	menu_top = MenuGorne.objects.order_by('numer')[:4]
	return {'image' : image, 'menu_prawe' : menu_prawe, 'menu_top' : menu_top}

def glowna(request):
	data = load_menu()
	data['wpis_list'] = Aktualnosc.objects.order_by('-pub_date')[:5]
	return render_to_response('data/index.html', data, context_instance=RequestContext(request))
	
def strona(request, strona_id):
	data = load_menu()
	data['strona'] = get_object_or_404(Strona, pk=strona_id)
	return render_to_response('data/site.html', data, context_instance=RequestContext(request))
	
	
	