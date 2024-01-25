from django.shortcuts import render



def main(request):
    return render(request,'zadacha.html',)


def direct (request):
    return render(request,'ssilka.html')

