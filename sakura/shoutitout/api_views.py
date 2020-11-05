from rest_framework import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
from shoutitout.serializer import UserSerializer
from shoutitout.models import User
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.exceptions import ValidationError

class UsersPagination(LimitOffsetPagination):
    default_limit= 10
    max_limit= 100

class UserCreate(CreateAPIView):
    serializer_class= UserSerializer

    def create(self, request, *args, **kwargs):
        #add code to check some field for validation
        return super().create(request, *args, **kwargs)

class UserRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset= User.objects.all()
    lookup_field= 'id'
    serializer_class= UserSerializer

    def delete(self, request, *args, **kwargs):
        user_id= request.data.get('id')
        response= super().delete(request, *args, **kwargs)
        if response.status_code== 204:
            from django.core.cache import cache
            cache.delete('user_data_{}'.format(user_id))
        return response

    def update(self, request, *args, **kwargs):
        response= super().update(request, *args, **kwargs)
        if response.status_code== 200:
            from django.core.cache import cache
            user= response.data
            cache.set('user_data_{}'.format(user['id']), {
                'email': user['email'],
                'password': user['password'],
                'name': user['name'],
                'listsCreated': user['listsCreated'],
                'numberOfListsCreated': user['numberOfListsCreated'],
                'listsFollowed': user['listsFollowed'],
                'numberOfListsFollowed': user['numberOfListsFollowed'],
                'createdAt': user['createdAt'],
                'updatedAt': user['updatedAt']
            })
        return response

class UserList(ListAPIView):
    queryset= User.objects.all()
    serializer_class= UserSerializer
    filter_backends= (DjangoFilterBackend, SearchFilter)
    filter_fields= ('id')
    search_fields= ('name', 'email')
    pagination_class= UsersPagination