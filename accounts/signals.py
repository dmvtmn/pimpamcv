import stripe
from django.conf import settings

'''
try:
    from django.contrib.auth import get_user_model
    User = get_user_model()
except ImportError:
    from django.contrib.auth.models import User
'''

from django.contrib.auth.models import User

from django.contrib.auth.signals import user_logged_in
from django.db.models.signals import post_save

from .models import UserStripe, EmailConfirmed

stripe.api_key = settings.STRIPE_SECRET_KEY

'''
if we decide to change how we add stripe iden, this is where we set it for user
def get_or_create_stripe(sender, user, *args, **kwargs):
    try:
        user.userstripe.stripe_id
        print user.userstripe.stripe_id
    except UserStripe.DoesNotExist:
        customer = stripe.Customer.create(
        email = str(user.email)
        )
        new_user_stripe = UserStripe.objects.create(
            user = user,
            stripe_id = customer.id
            )
    except:
        pass

#user_logged_in.connect(get_or_create_stripe)# This sends the signal when someone logs in
'''

def get_create_stripe(user):

    new_user_stripe, created = UserStripe.objects.get_or_create(user=user)
    if created:
        customer = stripe.Customer.create(
        email = str(user.email)
        )
        new_user_stripe.stripe_id = customer.id
        new_user_stripe.save()


def user_created(sender, instance, created, *args, **kwargs):
    user = instance

    if created:
        get_create_stripe(user)# instance being user instance
        email_confirmed, email_is_created = EmailConfirmed.objects.get_or_create(user=user)
        if email_is_created:
            pass
            #send email
            #print user.emailconfirmed.email_user()

post_save.connect(user_created, sender=User)
