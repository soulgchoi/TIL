from django.shortcuts import render


def student(request, name):
    our_class = {
        '최솔지': 27,
        '홍수경': 26,
        '문다혜': 26,
    }
    
    return render(request, 'student.html', context={
        'name': name,
        'age': our_class[name]
    })