###########################
# Poor coding
# Tangle
###########################

import json
import requests
from django.http import HttpResponse


def external_view(request, *args, **kwargs):
    try:
        response = requests.post('http://api.cdn.com/method', {'id': request.POST['id']})
    except:
        return HttpResponse(json.dumps({
            "success": False
        }))

    return HttpResponse(json.dumps({
        "success": True,
        "id": response.json()['id']
    }))

###########################
# Improved coding
###########################

import json
import requests
from django.http import HttpResponse

def external_view(request, *args, **kwargs):

    urls = ['http://api.cdn.com/method']
    params = {'id': request.POST['id']}
    json_objs = []

    if args:
        urls = args

    if kwargs:
        params = kwargs

    for url in urls:
        obj = {
            "url": url,
            "success": False,
            "id": -1
        }

        print "Posting to URL '{}'".format(url)

        try:
            response = requests.post(url, data=params)

            # Consider any status other than 2xx an error
            if not response.status_code // 100 == 2:
                print "Error: Unexpected response {}".format(response)
            else:
                print "Success."
                obj["success"] = True
                obj["id"] = response.json()['id']

        except requests.exceptions.RequestException as e:
            # A serious problem happened, like an SSLError or InvalidURL
            print "Error: {}".format(e)

        json_objs.append(obj)

    return HttpResponse(json.dumps(json_objs))







