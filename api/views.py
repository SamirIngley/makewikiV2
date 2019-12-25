from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.generics import ListCreateAPIView, RetrieveDestroyAPIView

from wiki.models import Page
from api.serializers import PageSerializer

class PageList(APIView):
    def get(self, request):
        page = Page.objects.all()[:20]
        data = PageSerializer(page, many=True).data
        return Response(data)
