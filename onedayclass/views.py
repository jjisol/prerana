from django.shortcuts import render, redirect, get_object_or_404
from .models import OnedayClass, OnedayClassReview
from .forms import OnedayClassReviewForm
from django.contrib import messages
from django.db.models import Count
# Create your views here.
def class_detail(request, id):
    onedayclass = get_object_or_404(OnedayClass, id=id)
    return render(request, 'class_detail.html', {'onedayclass':onedayclass})

def oneday_class_detail(request):
    onedayclass = OnedayClass.objects.annotate(num_of_review=Count('onedayclass_reviews'))
    newclasses = OnedayClass.objects.all().order_by('-id')
    endclasses = OnedayClass.objects.all().order_by('end_date')
    return render(request, 'oneday_class_detail.html',
     {'onedayclass':onedayclass, 'newclasses':newclasses, 'endclasses':endclasses})

def add_review_to_class(request, id):
    onedayclass = get_object_or_404(OnedayClass, id=id)
    if request.method == "POST":
        form = OnedayClassReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.onedayclass = onedayclass
            review.user = request.user
            review.save()
            return redirect('class_detail', id=onedayclass.id)
    else:
        form = OnedayClassReviewForm()
    return render(request, 'add_review_to_class.html', {'form':form, 'onedayclass':onedayclass})

def review_remove(request, id):
    review = get_object_or_404(OnedayClassReview, id=id)
    print(request.user==review.user)
    print(request.user, review.user)
    if request.user == review.user:
        review.delete()
    else:
        messages.warning(request, '권한 없음')
    return redirect('add_review_to_onedayclass', id=review.onedayclass.id)
