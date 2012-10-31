from django.contrib import admin

from data.models import Aktualnosc
from data.models import MenuGorne
from data.models import MenuPrawe
from data.models import PodMenuPrawe
from data.models import Strona

admin.site.register(Aktualnosc)
admin.site.register(MenuGorne)
admin.site.register(MenuPrawe)
admin.site.register(PodMenuPrawe)
admin.site.register(Strona)

