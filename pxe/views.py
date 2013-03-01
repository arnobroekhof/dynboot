from django.http import HttpResponse
from django.template import Context, loader

from pxe.models import Defaultboot
from pxe.models import Bootoption
from pxe.models import Serverboot

def index(request):
  defaultboot = Defaultboot.objects.get()
  template = loader.get_template('pxe/default.html')
  context = Context({ 'defaultboot': defaultboot, })

  return HttpResponse(template.render(context),content_type="text/plain")

def macfilter(request, macaddr):
  options = getmac(macaddr)
  if not options is None:
    template = loader.get_template('pxe/boot.html')
    context = Context({ 'boot': options, })
  else:
    defaultboot = Defaultboot.objects.get()
    template = loader.get_template('pxe/default.html')
    context = Context({ 'defaultboot': defaultboot, })

  return HttpResponse(template.render(context),content_type="text/plain")

def getmac(macaddr):
  try:
    bootoption = Serverboot.objects.get(macaddress=macaddr, enabled=True)
    Serverboot.objects.filter(macaddress=macaddr).update(enabled=False)
  except:
    bootoption = None

  return bootoption
  

