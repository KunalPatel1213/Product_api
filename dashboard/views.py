from django.shortcuts import render, redirect
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import Details
from .serializers import DetailsSerializer
from .forms import DetailsForm


@api_view(['GET'])
def detail_list(request):
    details = Details.objects.all()
    serializer = DetailsSerializer(details, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def detail_detail(request, pk):
    detail = Details.objects.get(id=pk)
    serializer = DetailsSerializer(detail)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_detail(request):
    serializer = DetailsSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)


# Template-based views for Dashboard UI
def detail_list_page(request):
    details = Details.objects.all()
    return render(request, 'dashboard/detail_list.html', {'details': details})


def create_detail_page(request):
    success = False
    if request.method == 'POST':
        form = DetailsForm(request.POST)
        if form.is_valid():
            form.save()
            success = True
            form = DetailsForm()
    else:
        form = DetailsForm()
    return render(request, 'dashboard/create_detail.html', {'form': form, 'success': success})


