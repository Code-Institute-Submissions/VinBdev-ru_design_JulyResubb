from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from .models import UserProfile
from products.models import Favourite
from .forms import UserProfileForm

from checkout.models import Order


@login_required
def profile(request):
    """Displaying users profile """
    user = User.objects.get(username=request.user.username)
    profile = get_object_or_404(UserProfile, user=user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile has been updated!')
        else:
            messages.success(request, 'Update has failed, please check \
                your form.')
    else:
        form = UserProfileForm(instance=profile)
    orders = profile.orders.all()
    favourites = Favourite.objects.filter(user_profile=profile)


    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
        'on_profile_page': True,
        'favourites': favourites 
    }
    return render(request, template, context)


def order_history(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'This is a previous confirmation number {order_number}.'
        'An email was sent on the day it was ordered.'
    ))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)
