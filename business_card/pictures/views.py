from django.http import HttpResponseRedirect
from django.shortcuts import render

from .models import Picture
from .forms import AddNewPicForm


# Create your views here.
def pictures_view(request):
    return render(request, 'pictures.html')


def pictures_model_view(request):
    pictures = Picture.objects.all()
    return render(request, 'pictures.html', {'objects': pictures})


def pictures_add_view(request):
    # 2 запроса get, post
    if request.method == 'POST':
        # передаем данные в форму
        form = AddNewPicForm(request.POST, files=request.FILES)  # Don't forget import your model
        # форма сама себя проверят на ошибки
        if form.is_valid():
            # сама себя умеет сохранять
            object_ = form.save(commit=False)
            # LifeHack!!! Сохраняем текущего пользователя в объект
            object_.user = request.user
            object_.save()
            return HttpResponseRedirect('/pictures/')
        # если форма не валидна
        context = {'form': form}
        return render(request, 'pictures_add.html', context)
    # Для отрисовки самой страницы при переходе на неё
    context = {'form': AddNewPicForm()}
    return render(request, 'pictures_add.html', context)
