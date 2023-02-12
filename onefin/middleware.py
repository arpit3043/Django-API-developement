# made a request counter function and import it for our purpose here to count
# the request from movie collection models
from movie_collection.models import RequestCounter

# made a class for getting request count from middleware
class RequestCounterMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    # One-time configuration and initialization.
    def __call__(self, request):
        # get the request count from the request counter object
        request_counter = RequestCounter.objects.all().first()
        if request_counter:
            request_counter.request_count = int(request_counter.request_count) + 1
            request_counter.save()
        # for creating the request and increase the counter by 1
        else:
            RequestCounter.objects.create(request_count=1)
        response = self.get_response(request)

        return response