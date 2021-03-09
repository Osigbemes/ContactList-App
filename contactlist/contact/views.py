from django.shortcuts import render, redirect
from .models import Contact

def index(request):
    contacts=Contact.objects.all()
    search_input = request.GET.get('search-area')
    if search_input:
        contacts = Contact.objects.filter(full_name__icontains = search_input)
    else:
        contacts = Contact.objects.all()
        search_input=''
    context={'contacts':contacts, 'search_input':search_input}
    return render(request, 'contact/index.html', context)

def addContact(request):
    if request.method == 'POST':
        new_contact = Contact(
            full_name = request.POST['fullname'],
            relationship = request.POST['relationship'],
            email = request.POST['email'],
            phone_number = request.POST['phone-number'],
            address = request.POST['address']
        )
        new_contact.save()
        return redirect('/')
    return render(request, 'contact/new.html', {})

def ContactProfile(request, pk):
    contacts = Contact.objects.get(id=pk)

    context = {'contacts':contacts}
    return render(request, 'contact/contact-profile.html', context)

def editContact(request, pk):
    contacts = Contact.objects.get(id=pk)

    if request.method == 'POST':
        contacts.full_name= request.POST['fullname']
        contacts.relationship= request.POST['relationship']
        contacts.email= request.POST['e-mail']
        contacts.address= request.POST['address']
        contacts.phone_number= request.POST['phone-number']

        contacts.save()
        return redirect('/profile/'+ str(contacts.id))
    context = {'contacts':contacts}
    return render(request, 'contact/edit.html', context)

def deleteContact(request, pk):
    contact = Contact.objects.get(id=pk)
    if request.method == 'POST':
        contact.delete()
        return redirect('/')
    context={'contact':contact}
    return render(request, 'contact/delete.html', context)
