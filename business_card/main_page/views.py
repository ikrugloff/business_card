from django.shortcuts import render

# Create your views here.
def main_page_view(request):
    f_name = 'ilia'
    l_name = 'kruglov'
    print('Current user: ', request.user)
    print('Request type: ', request.method)



    return render(request, 'index.html', {'first_name': f_name,
                                          'last_name': l_name,
                                          'request_type': request.method
                                          })  # Context dictionary
