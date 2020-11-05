from rest_framework import serializers
from shoutitout.models import User, ListItem, List

class ListItemSerializer(serializers.ModelSerializer):
    
    class Meta:
        model= ListItem
        fields= ('id', 'name', 'description', 'parentList', 'createdAt', 'updatedAt')

class ListSerializer(serializers.ModelSerializer):
    
    items= serializers.SerializerMethodField()

    class Meta:
        model= List
        fields= ('id', 'name', 'subscribers', 'numberOfSubs', 'items', 
            'visibility', 'creator', 'createdAt', 'updatedAt'
        )

    def get_items(self, instance):
        items= ListItem.objects.filter(list= instance)
        return ListItemSerializer(items, many= True).data

class UserSerializer(serializers.ModelSerializer):
    
    listsCreated= serializers.SerializerMethodField()
    listsFollowed= serializers.SerializerMethodField()

    class Meta:
        model= User
        fields= ('id', 'email', 'password', 'name', 'listsCreated', 
            'numberOfListsCreated', 'listsFollowed', 'numberOfListsFollowed', 
            'createdAt', 'updatedAt',
        )

    def to_representation(self, instance):
        data= super().to_representation(instance)
        return data

    def get_listsCreated(self, instance):
        listsCreated= List.objects.filter(user= instance)
        return ListSerializer(listsCreated, many= true).data

    def get_listsFollowed(self, instance):
        listsFollowed= List.objects.filter(user= instance)
        return ListSerializer(listsFollowed, many= true).data