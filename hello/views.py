from django.http import HttpResponse

def home(request):
    return HttpResponse("Disciplina: Cloud Computing & Site Reliability Engineering Aluno: Fabricio Coutinho de Araujo")