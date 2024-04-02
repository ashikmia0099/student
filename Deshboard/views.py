from django.shortcuts import render

# Create your views here.

def HomeView(request):
    return render(request, 'home.html')

def AllcoursePage(request):
    return render(request,'all_course_page.html')

def CategoryPage(request):
    return render(request, 'category_page.html')


def SeminerPage(request):
    return render(request, 'join_seminer.html')

def VideoPage(request):
    return render(request, 'video.html')
