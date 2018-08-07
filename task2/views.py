from django.shortcuts import render
from rest_framework import views
from rest_framework.generics import ListCreateAPIView
from .forms import MyForm
from .serializer import MySerializer, MySerilizer1
from rest_framework.response import Response
import time
import datetime
from rest_framework import status
from rest_framework.renderers import TemplateHTMLRenderer


class MyView (views.APIView):

    def get(self, request):
        serializer = MySerializer(request)
        print(serializer.data)


        return Response(serializer.data)

    def post(self, request):
        form = MyForm
        return Response(template_name='form.html')
        pass


class MyView1(ListCreateAPIView):
    serializer_class = MySerilizer1
    context_object_name = 'me'
    renderer_classes = (TemplateHTMLRenderer,)

    def post(self, request, *args,**kwargs):
        db_start = time.time()
        request_time = datetime.datetime.now()
        serializer = MySerilizer1(data=request.data)
        if serializer.is_valid():
            result = serializer["input"].value.split(serializer["delimiter"].value)
            my_response = {
                    "id": 1,
                    "output": result,
                    "WordCount": len(result),
                    "InputString": serializer["input"].value,
                    "ProcessingDelay": time.time()-db_start,
                    "RequestTimeDate": request_time,
                    "ResponseTmeDate": datetime.datetime.now()
                }
            # request.data = my_response

            return Response(data=my_response, template_name='query1.html')
        else:
            return Response(status.HTTP_203_NON_AUTHORITATIVE_INFORMATION, template_name='query.html')

    def get(self, request, *args, **kwargs):
        return render(request, template_name='form.html')
        pass

# Create your views here.
