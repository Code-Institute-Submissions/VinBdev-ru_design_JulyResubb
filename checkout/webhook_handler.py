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