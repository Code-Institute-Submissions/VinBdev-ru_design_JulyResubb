import django.http import HttpResponse

class StripeWH_Handler:
    """ Handling stripe webhooks """

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """ Handling generic/ unknown webhoo event """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_succeeded(self, event):
        """ Handling payment_intent_succeeded from stripe """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_failed(self, event):
        """ Handling payment_intent_failed from stripe """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)