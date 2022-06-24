from django.shortcuts import render

# Created views 

def view_bag(request):
    """ View that renders the bag page contents """

    return render(request, 'bag/bag.html')