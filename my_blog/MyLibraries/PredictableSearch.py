from django.core import serializers
from django.http import HttpResponse


def fetch_data_to_show_in_input_deployed(request, *data):
    """
    This function is for to show the result of a searching done by the user
    in a input on the font-end
    :param request: Data from the request
    :param data: We bring a model where we will search the writing by the user and the function for showing the result
    :return: We are returning the answer from the database server to the user
    """
    q = request.GET.get('q')
    info = ""
    if len(q.strip()) > 0:
        q = str(q).lower()
        info = serializers.serialize('json', data[0].objects.filter(slug__contains=q))

        return info
    else:
        info = serializers.serialize('json', info)
        return  info
