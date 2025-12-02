from django.shortcuts import render
from .models import Content

# Create your views here.
def index(request):
    
    if request.method == 'POST':
        order_type = request.POST.get('order_type','')
        customer_name = request.POST.get('customer_name','')
        customer_address = request.POST.get('customer_address','')
        supplier_name = request.POST.get('supplier_name','')
        supplier_address = request.POST.get('supplier_address','')
        order_date = request.POST.get('order_date','')
        products = request.POST.get('products','')
        notes = request.POST.get('notes','')

        user_data = Content(order_type=order_type, customer_name=customer_name,customer_address=customer_address,supplier_name=supplier_name,
                            supplier_address=supplier_address,order_date=order_date,products=products,notes=notes)
        user_data.save()

    return render(request,'app/index.html',{'user_data':user_data})

# def history(request):
#     content = Content.objects.all()

#     return render(request,'app/index.html',{'content':content})