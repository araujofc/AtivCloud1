from django.http import HttpResponse

def home(request):
    return HttpResponse("<b>Disciplina:</b> Cloud Computing & Site Reliability Engineering <br><b>Aluno</b>: Fabricio Coutinho de Araujo")