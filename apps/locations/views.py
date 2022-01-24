from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import LocationModel
from .serializers import LocationSerializer
from rest_framework.pagination import LimitOffsetPagination
import django_auto_prefetching
from django_auto_prefetching import AutoPrefetchViewSetMixin



class LocationListView(APIView, LimitOffsetPagination, AutoPrefetchViewSetMixin):
    serializer_class = LocationSerializer

    # GET ALL
    def get(self, request):
        try:
            locations = LocationModel.objects.all()
            locations = locations.select_related()
            self.paginate_queryset(locations, request, view=self)
            results = django_auto_prefetching.prefetch(locations, self.serializer_class)
            serializer = LocationSerializer(results, many=True)
            return self.get_paginated_response(serializer.data)
        except Exception as error:
            datos = {'message': str(error)}
            return Response(datos, status=status.HTTP_204_NO_CONTENT)

    # CREATE
    def post(self, request):
        try:
            serializers = LocationSerializer(data=request.data)
            if serializers.is_valid():
                serializers.save()

                datos = {'message': "success created",
                         'result': serializers.data}
                return Response(datos, status=status.HTTP_201_CREATED)
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as error:
            datos = {'message':
                         str(error)}
            return Response(datos, status=status.HTTP_400_BAD_REQUEST)


class LocationDetailView(APIView, LimitOffsetPagination, AutoPrefetchViewSetMixin):
    serializer_class = LocationSerializer

    # GET filter ID
    def get(self, request, pk=None):
        try:
            location = LocationModel.objects.filter(id=pk)
            location = location.select_related()
            self.paginate_queryset(location, request, view=self)
            results = django_auto_prefetching.prefetch(location, self.serializer_class)
            serializer = LocationSerializer(results, many=True)
            return self.get_paginated_response(serializer.data)
        except Exception as error:
            return Response({'message': str(error)}, status=status.HTTP_204_NO_CONTENT)

    # UPDATE
    def put(self, request, pk=None):
        try:
            location = LocationModel.objects.get(id=pk)
            serializers = LocationSerializer(location, data=request.data, partial=True)
            if serializers.is_valid():
                serializers.save()
                datos = {'message': "update success",
                         'result': serializers.data}
                return Response(datos, status=status.HTTP_200_OK)
            else:
                return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as error:
            datos = {'error': str(error)}
            return Response(datos, status=status.HTTP_204_NO_CONTENT)

    # DELETE
    def delete(self, request, pk=None):
        try:
            location = LocationModel.objects.get(id=pk).delete()
            datos = {'message': "delete success"}
            return Response(datos, status=status.HTTP_200_OK)
        except Exception as error:
            datos = {'message':
                         ["no found!!!"]}
            return Response(datos, status=status.HTTP_204_NO_CONTENT)

