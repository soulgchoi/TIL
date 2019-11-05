from django.shortcuts import render

# Create your views here.


def info(request):
    Teacher = '유태영'
    Student = ['최솔지', '홍수경', '문다혜']
    return render(request, 'info.html', context={
        'Teacher': Teacher,
        'Student': Student,
    })