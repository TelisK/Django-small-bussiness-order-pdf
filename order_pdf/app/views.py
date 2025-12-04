from django.shortcuts import render, redirect, get_object_or_404
from .models import Content
from .forms import ContentForm
from xhtml2pdf import pisa
from django.template.loader import render_to_string
from io import BytesIO
from django.http import HttpResponse
from django.contrib import messages

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

    form = ContentForm()
    return redirect('generate_pdf', id=user_data.id)
    # return render(request,'app/index.html',{'form':form})

def history(request):
    content = Content.objects.all()

    return render(request,'app/history.html',{'content':content})

def history_details(request, id):
    content = Content.objects.get(pk=id)
    return render(request, 'app/history_details.html', {'content':content})

def generate_pdf(request, id):
    content = Content.objects.get(pk=id)
    html = render_to_string('app/pdf_template.html',{'content':content})
    buffer = BytesIO()

    pisa_status = pisa.CreatePDF(src=html, dest=buffer)
    return HttpResponse(buffer.getvalue(), content_type='application/pdf')

def delete(request, id):
    content = get_object_or_404(Content, pk=id)
    content.delete()
    messages.success(request, "Deleted successfully")
    return redirect('history')