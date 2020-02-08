from django.shortcuts import render
from django.conf import settings # new
from django.views.generic.base import TemplateView

# Create your views here.
class PaymentView(TemplateView):
    template_name = 'payment.html'

    def get_context_data(self, **kwargs): # new
        context = super().get_context_data(**kwargs)
        context['key'] = settings.STRIPE_PUBLISHABLE_KEY
        return context