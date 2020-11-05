from django.db import models
from django.contrib.postgres.fields import ArrayField

class User(models.Model):
    id= models.IntegerField(primary_key=True)
    email= models.EmailField()
    password= models.CharField(max_length=20)
    name= models.CharField(max_length=20)
    listsCreated= models.Manytomanyfield(List, related_name= 'creator', null= True) 
    numberOfListsCreated= models.IntegerField(null= True) #update when list created
    listsFollowed= models.ManyToManyField(List, related_name= 'subscriber', null= True) 
    numberOfListsFollowed= models.IntegerField(null= True) #update when list followed
    createdAt= models.DateTimeField(auto_now_add= True)
    updatedAt= models.DateTimeField(auto_now= True, null= True) # call Model.save() to implement

    def __init__(self, **kwargs):
        self.email= kwargs['email'] 
        self.password= kwargs['password']
        self.name= kwargs['name']
        self.numberOfListsCreated= 0
        self.numberOfListsFollowed= 0

    def id(self, id= None):
        if id: self.id= id
        return self.id

    def password(self, password= None):
        if password: self.password= password
        return self.password

    def email(self, email=None):
        if email: self.email= email
        return self.email

    def name(self, name= None):
        if name: self.name= name
        return self.name

    def listsCreated(self, listsCreated= None):#needs work
        if listsCreated:
            self.listsCreated[numberOfListsCreated]= listsCreated
            numberOfListsCreated+= 1
        return self.listsCreated

    def getListsFollowed(self, listsFollowed= None): #needs work
        if listsFollowed:
            self.listsFollowed[numberOfListsFollowed]= listsFollowed
            numberOfListsFollowed+= 1
        return listsFollowed

    def deleteList(self, id):
        del listsCreated[]
        #add code

    def renameList(self, name):
        #add code

    def setItem(self, name):
        #add code

    def deleteItem(self,name):
        #add code

    def subscribeList(self, name):
        #add code

    def unsubscribeList(self, name):
        #add code

    def searchList(self, name): 
        #add code
    
    def getCreatedAt(self):
        return self.createdAt

    def updatedAt(self, updatedAt= None):#check this code
        if updatedAt: self.updatedAt= updatedAt
        return self.updatedAt

    
class List(models.Model):
    id= models.IntegerField(primary_key= True) 
    name= models.CharField(max_length=20)
    subscribers= models.ManyToManyField(User, null= True)
    numberOfSubs= models.IntegerField(null= True)
    items= models.ForeignKey(ListItem)
    visibility= models.CharField(max_length=20)
    creator= models.User() #Manytomany
    createdAt= models.DateTimeField(auto_now_add= True)
    updatedAt= models.DateTimeField(auto_now= True,null= True) # add code for calling updatedAt in each setter block

    def __init__(self, **kwargs):
        self.name= kwargs['name']
        self.numberOfSubs= 1
        self.visibility= kwargs['visibility']
        self.creator= kwargs['creator']
            
    def id(self, id= None):
        if id: self.id= id
        return self.id

    def name(self, name= None):
        if name: self.name= name
        return self.name


    def numberOfSubs(self): 
        #add code


    def subscribers(self):
        #add code User[ ]


    def items(self):
        #add code ListItem[ ]


    def deleteItem(self, name):
        #add code

    def visibility(self, visibility= None):
        if visibility: self.visibility= visibility
        return self.visibility


    def getCreator(self):
        return self.creator

    def getCreatedAt(self):
        return self.createdAt

    def updatedAt(self, updatedAt= None):
        if updatedAt: self.updatedAt= updatedAt
        return updatedAt

class ListItem(models.Model):
    id= models.IntegerField(primary_key= True)
    name= models.CharField(max_length= 20)
    description= models.TextField()
    parentList= models.List()
    createdAt= models.DateTimeField(auto_now_add= True)
    updatedAt= models.DateTimeField(auto_now= True, null= True) 

    def __init__(self, **kwargs):
        self.name= kwargs['name']
        self.description= kwargs['description']
        self.parentList= kwargs['parentList']

    def id(self, id= None):
        if id: self.id= id
        return self.id

    def name(self, name= None):
        if name: self.name= name
        return self.name

    def description(self, description= None):
        if description: self.description= description
        return description

    def getParentList(self): 
        return self.parentList

    def getCreatedAt(self): 
        return self.createdAt

    def updatedAt(self, updatedAt= None):
        if updatedAt: self.updatedAt= updatedAt
        return self.updatedAt


class Restaurant(ListItem):
    address= models.TextField()

    def __init__(self, **kwargs):
        self.address= kwargs['address']
        super().__init__(**kwargs)

    def location(self, address= None):
        if address: self.address= address
        return self.address        

class Place(ListItem):
    city= models.CharField(max_length=20)
    country= models.CharField(max_length=20)

    def __init__(self, **kwargs):
        self.city= kwargs['city']
        self.country= kwargs['country']
        super().__init__(**kwargs)

    def city(self, city= None):
        if city: self.city= city
        return self.city        

    def country(self, country= None):
        if country: self.country= country
        return self.country

class Music(ListItem):
    artist= models.CharField(max_length=20)

    def __init__(self, **kwargs):
        self.artist= kwargs['artist']
        super().__init__(**kwargs)

    def artist(self, artist= None):
        if artist: self.artist= artist
        return self.artist

class Book(ListItem):
    author= models.CharField(max_length= 20)

    def __init__(self, **kwargs):
        self.author= kwargs['author']
        super().__init__(**kwargs)

    def author(self, author= None):
        if author: self.author= author
        return self.author

