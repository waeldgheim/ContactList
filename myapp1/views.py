from django.shortcuts import render, redirect
from .form import CreateContact
from .models import Contact
from django.http import HttpResponseRedirect



# Create your views here.
def list(request):
    context = Contact.objects.all()
    return render(request, "contact_list.html", {"context":context})


def create(request):
    if request.method == 'POST':
        form = CreateContact(request.POST)
        if form.is_valid():
         formdata = form.cleaned_data
         name=formdata['name']
         address = formdata['address']
         profession = formdata['profession']
         telephone = formdata['telephone']
         email = formdata['email']
         Contact.objects.create(name=name,address=address,profession=profession,telephone=telephone,email=email)
         return redirect('list')
    else:
        form = CreateContact()
        return render(request, 'contact.html', {'form': form})


def delete(request, contact_id):
    contact_id = int(contact_id)
    try:
        to_delete = Contact.objects.get(id = contact_id)
    except Contact.DoesNotExist:
        return redirect('list')
    to_delete.delete()
    return redirect('list')


def update(request, contact_id):
    contact_id = int(contact_id)
    try:
        to_update = Contact.objects.get(id = contact_id)
    except Contact.DoesNotExist:
        return redirect('list')
    
    if request.method == 'POST':
        form = CreateContact(request.POST, instance=to_update)
        if form.is_valid():
            form.save()
            return redirect('list')
    else:
        form = CreateContact(instance=to_update)
    return render(request, 'contact.html', {'form': form})



