from django.shortcuts import render
from django.utils import timezone
from .models import Form

# Create your views here.
def post_list(request):    
    forms = Form.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'forms/post_list.html', {'forms': forms})