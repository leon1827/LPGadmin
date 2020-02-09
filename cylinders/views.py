from django.http import Http404
from django.shortcuts import get_object_or_404, get_list_or_404,render
# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from . import models
from .templates import cylinders


def lookupBygp(request, gp_code):
    contents = {}
    try: 
        gpinfo = get_list_or_404(models.Gp, gp_code=gp_code)[-1] # 获取最新的一条
        contents.update({'gpinfo':gpinfo})
        czinfo = get_list_or_404(models.Filling, gp_code=gp_code)[-1]
        contents.update({'czinfo':czinfo})
        psinfo = get_list_or_404(models.Record, gp_code=gp_code)[-1]
        contents.update({'psinfo':psinfo})
    except:
        pass
    finally:
        return render(request, 'cylinders/gpinfo.html', contents)

def index(request):
    # try:
    #     gpinfo = models.Gps.objects.get(pk=1)
    # except models.Gps.DoesNotExist:
    #     raise Http404("Gps does not exist")
    # 还可以使用如下函数，不错
    try:
        gpinfo = get_object_or_404(models.Gp, pk=1)
    except:
        pass
    return render(request, 'cylinders/index.html', {'gpinfo': gpinfo})

def page1_gp(request):
    return render(request, 'cylinders/page1_gp.html')

def addGp(request):
    if request.method == 'POST':
        jf_code = request.POST['jf_code']
        gp_code = request.POST['gp_code']
        zn_code = request.POST['zn_code']
        sc_date = request.POST['sc_date']
        jc_date = request.POST['jc_date']
        manufacturer = request.POST['manufacturer']
        specification = request.POST['specification']
        company = request.POST['company']
        xj_date = request.POST['xj_date']
        bf_date = request.POST['bf_date']
        gp = models.Gp(jf_code=jf_code, gp_code=gp_code, zn_code=zn_code, 
                        sc_date=sc_date, jc_date=jc_date, 
                        manufacturer=manufacturer, specification=specification, 
                        company=company, xj_date=xj_date, bf_date=bf_date)
        gp.save()
    return HttpResponseRedirect(reverse('cylinders:page1_gp'))