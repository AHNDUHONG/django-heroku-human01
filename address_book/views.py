from ast import Add
from email import message
from django.shortcuts import render, redirect

from django.shortcuts import render, redirect
from .models import Address
from .forms import AddressForm
from django.contrib import messages

# Create your views here.
def home(request):
    all_addresses = Address.objects.all
    return render(request, 'home.html', {'all_addresses' : all_addresses})

def add_address(request):
    if request.method == 'POST':
        form = AddressForm(request.POST or None) 
        if form.is_valid():
            form.save()
            messages.success(request, ('Address Has Been Added!'))
            return redirect('home')
        else: 
            messages.success(request, ('Error'))
            return render(request, 'add_address.html', {})
    return render(request, 'add_address.html', {})

def edit(request, list_id):
    if request.method == 'POST':
        current_address = Address.objects.get(pk=list_id)
        form = AddressForm(request.POST or None, instance=current_address)
        if form.is_valid():
            form.save()
            messages.success(request, ('Address Has Been Edited!'))
            return redirect('home')
        else: 
            messages.success(request, ('Error'))
            return render(request, 'edit.html', {})
    else:
        get_address = Address.objects.get(pk=list_id)
        return render(request, 'edit.html', {'get_address' : get_address})

def delete(request, list_id):
    if request.method == 'POST':
        current_address = Address.objects.get(pk=list_id)
        current_address.delete()
        messages.success(request, ('Address Has Been Deleted..!'))
        return redirect('home')
    else:
        messages.success(request, ('Nothing To See Here...'))
        return redirect('home')