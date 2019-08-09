from django.shortcuts import render

def welcome(request):
    return render(request, 'index.html', {'msg':'Hello World!'})

def restaurant_list(request):

    context = {
    "my_list":[
    {"restaurant_name":"king burger" , "food_type":"burger"},
    {"restaurant_name":"dunkin donuts" , "food_type":"donuts"},
    {"restaurant_name":"Patchi" , "food_type":"chocolate"},
    ],
    }
    return render(request, 'list.html', context)


def restaurant_detail(request):

    context = {
    "my_object" : {"restaurant_name": "alromansiah", "food_type": "mandy"},

    }
    return render(request, 'detail.html', context)
