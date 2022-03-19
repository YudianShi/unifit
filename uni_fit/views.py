from django.urls import reverse
from django.shortcuts import render, redirect
from django.http import HttpResponse
from uni_fit.forms import UserForm, UserProfileForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import profile
from stat import FILE_ATTRIBUTE_SPARSE_FILE
from .models import Review
from django.contrib.contenttypes.models import ContentType
from django.http import JsonResponse


def index(request):
    return render(request, 'uni_fit/index.html', )


def home(request):
    return render(request, 'uni_fit/home.html', )


def profile(request):
    return render(request, 'uni_fit/profile.html', )


def review(request):
    return render(request, 'uni_fit/results.html', )

def update_comment(request):
    referer = request.META.get('HTTP_REFERER', reverse('home'))

    # user data check
    if not request.user.is_authenticated:
        return render(request, 'login.html')
    text = request.POST.get('text', '').strip()
    if text == '':
        return render(request, 'login.html')
    try:
        content_type = request.POST.get('content_type', '')
        object_id = int(request.POST.get('object_id', ''))
        model_class = ContentType.objects.get(model=content_type).model_class()
        model_obj = model_class.objects.get(pk=object_id)
    except Exception as e:
        return render(request, 'results.html', {'message': 'object error', 'redirect_to': referer})

    # save data
    comment = Review()
    comment.user = request.user
    comment.text = text
    comment.content_object = model_obj
    comment.save()
    return redirect(referer)

def rate_image(request):
    if request.method == 'POST':
        el_id = request.POST.get('el_id')
        val = request.POST.get('val')
        print(val)
        obj = Rating.objects.get(id=el_id)
        obj.score = val
        obj.save()
        return JsonResponse({'success':'true', 'score': val}, safe=False)
    return JsonResponse({'success':'false'})