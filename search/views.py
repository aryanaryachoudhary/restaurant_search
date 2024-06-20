from django.shortcuts import render
from .models import Restaurant
from .forms import SearchForm

# Create your views here.

def search(request):
    form = SearchForm()
    results = []
    if request.method == 'GET' and 'query' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            results = Restaurant.objects.filter(items__icontains=query)
    return render(request, 'search/search.html', {'form': form, 'results': results})


