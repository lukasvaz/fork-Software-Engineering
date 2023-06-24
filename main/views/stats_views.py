from django.http import   HttpRequest
from django.shortcuts import render
from main.models import  AccountStatus
from django.core.exceptions import ObjectDoesNotExist
from django.views.decorators.cache import cache_control
from django.shortcuts import render



@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def stats(request: HttpRequest):
    """Render the statistics page template with the associated info from user.Cache was disabled to ensure user's privacy 
    """
    ctx={'name':request.user.first_name}
    
    return render(request,"stats/stats.html",ctx)


