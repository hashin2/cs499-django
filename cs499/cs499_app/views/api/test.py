from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from helpers import rest_mux, jsonify, dejsonify


def hello_world(request):
    return rest_mux(
        request,
        {
            'GET': __hello_world
        })

def __hello_world(request, query_params=None, **kwargs):
	retVal = {
		'msg': 'Hello World!'
	};

	return HttpResponse(jsonify(retVal, query_params), mimetype="application/json")