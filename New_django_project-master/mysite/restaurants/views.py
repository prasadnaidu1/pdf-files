from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from  django.views.generic.detail import DetailView
from .forms import RestaurantCreateview
from .models import RestaurantLocation

def restaurants_createview(request):
    form=RestaurantCreateview(request.POST or None)
    errors=None
    if form.is_valid():
        obj=RestaurantLocation.objects.create(
            name=form.cleaned_data.get('name'),
            location=form.cleaned_data.get('location'),
            category=form.cleaned_data.get('category')
        )
        return HttpResponseRedirect("/restaurants/")
    if form.errors:
        errors=form.errors

    template_name  = 'restaurants/form.html'
    context        = {"form":form ,"errors":errors}
    return render(request, template_name, context)

def restaurant_listview(request):
    template_name  = 'restaurants/restaurants_list.html'
    queryset       = RestaurantLocation.objects.all()
    context        = { "object_list":queryset }
    return render(request, template_name, context)

def restaurant_detailview(request, pk):
    template_name  = 'restaurants/restaurantlocation_detail.html'
    obj       = RestaurantLocation.objects.get(pk = pk)
    context        = { "object":obj }
    return render(request, template_name, context)

class RestaurantListView(ListView):
    def get_queryset(self):
        print(self.kwargs)
        slug=self.kwargs.get("slug")
        if slug:
            queryset=RestaurantLocation.objects.filter(
            Q(category__iexact='slug')|
            Q(category__icontains='slug')
            )
        else:
            queryset=RestaurantLocation.objects.all()
        return queryset

class RestaurantDetailView(DetailView):
    queryset=RestaurantLocation.objects.all()#filter(category__iexact='asian')

    # def get_object(self, *args, **kwargs):
    #     rest_id=self.kwargs.get('rest_id')
    #     obj=get_object_or_404(RestaurantLocation, id=rest_id) #you can also do pk=rest_id
    #     return obj
