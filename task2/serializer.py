from rest_framework import serializers
from drf_braces.serializers.form_serializer import FormSerializer
from .forms import MyForm
from django.db import models


class MySerializer(FormSerializer):
    class Meta:
        form = MyForm


class MySerilizer1(serializers.Serializer):
    # pass
    input = serializers.CharField(max_length=1000)
    delimiter = serializers.CharField(max_length=5)
    # class Meta:
    #     model = models.Model

        # pass