from django.shortcuts import render
from .models import Teashop
from  django.views.generic import DetailView



def createProduct(request):

    auto_idno=0
    try:
        res=Teashop.objects.all()[::-1][0]
        auto_idno=int(res.idno)+1
    except IndexError:
        auto_idno=1000

    qs=Teashop.objects.all()

    return render(request,'index.html',{'data':auto_idno,'data1':qs})


def addProduct(request):
    p_id=request.POST.get("idno")
    p_name=request.POST.get("name")
    p_desc=request.POST.get("desc")
    p_price=request.POST.get("price")
    p_image=request.FILES["image"]
    res=Teashop(idno=p_id,name=p_name,description=p_desc,price=p_price,images=p_image)
    res.save()

    return createProduct(request)


class DisplayProduct(DetailView):

    model = Teashop
    template_name = "details.html"


def deleteProduct(request):
    d_id = request.GET.get("delete_idno")
    Teashop.objects.get(idno=d_id).delete()
    return createProduct(request)

