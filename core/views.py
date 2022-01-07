from rest_framework.response import Response
from rest_framework.decorators import api_view, renderer_classes, permission_classes
from rest_framework import permissions

import datetime
from .models import APIDATA
from .serializers import APIDATASerializer
from datetime import datetime


@api_view(("GET",))
@permission_classes((permissions.AllowAny,))
def endpoint(request):
    if request.method == "GET":

        print("hii")
        format_data = "%Y-%m-%d %H:%M:%S"
        data = None
        if "date1" in request.GET and "date2" in request.GET:
            first = request.GET["date1"] + " 00:00:00"
            second = request.GET["date2"] + " 23:59:59"
            try:
                date_1 = datetime.strptime(first, format_data)
            except:
                return Response({"error": "Incorrect Date format provided"})

            try:
                date_2 = datetime.strptime(second, format_data)
            except:
                return Response({"error": "Incorrect Date format provided"})

            queryset = APIDATA.objects.filter(
                timestamp__gte=date_1, timestamp__lte=date_2
            )
            data = APIDATASerializer(queryset, many=True)

        elif "date1" not in request.GET and "date2" not in request.GET:
            queryset = APIDATA.objects.all()
            data = APIDATASerializer(queryset, many=True)

        return Response(data.data)
