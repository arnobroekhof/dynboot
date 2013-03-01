from django.contrib import admin
from pxe.models import Bootoption
from pxe.models import Defaultboot
from pxe.models import Serverboot

admin.site.register(Bootoption)
admin.site.register(Defaultboot)
admin.site.register(Serverboot)
