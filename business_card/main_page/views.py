from django.shortcuts import render

# Create your views here.
def main_page_view(request):
    f_name = 'Ilia'
    l_name = 'Kruglov'
    return render(request, 'index.html', {'first_name': f_name, 'last_name': l_name})  # Context dictionary
