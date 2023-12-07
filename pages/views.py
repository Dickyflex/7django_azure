from django.http import HttpResponse

def home_page_view(request):
    return HttpResponse("Hello World! from CEI 202310 Cohort.")
