from django.shortcuts import render

import json
from django.http import JsonResponse
from django.views import View
from pets.models import Owner, Dog

# Create your views here.


class OwnerView(View):
    def post(self, request):
        data = json.loads(request.body)
        owner = Owner.objects.create(
            name=data['name'],
            email=data['email'],
            age=data['age']
        )
        return JsonResponse({'MESSAGE': 'SUCCESS'}, status=201)

    def get(self, request):
        owners = Owner.objects.all()
        results = []
        for owner in owners:
            dog_list = []
            dogs = owner.dog_set.all()

            for dog in dogs:
                dog_info = {
                    'dog_name': dog.name,
                    'dog_age': dog.age
                }
                dog_list.append(dog_info)

            owner_info = {
                'name': owner.name,
                'email': owner.email,
                'age': owner.age,
                'dog_list': dog_list
            }
            results.append(owner_info)
        return JsonResponse({'result': results}, status=200)


class DogsView(View):
    def post(self, request):
        data = json.loads(request.body)
        Dog.objects.create(
            name=data['name'],
            age=data['age'],
            owner=Owner.objects.get(id=data["owner_id"])
        )

        return JsonResponse({'MESSAGE': 'SUCCESS'}, status=201)

    def get(self, request):
        dogs = Dog.objects.all()
        results = []
        for dog in dogs:
            dog = (
                {
                    "owner": dog.owner.name,
                    "name": dog.name,
                    "age": dog.age
                }
            )
            results.append(dog)
        return JsonResponse({'results': results}, status=200)
