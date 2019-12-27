from django.shortcuts import render, redirect, get_object_or_404
from .models import Center, CenterReview
from instructor.models import Instructor
from .forms import CenterReviewForm
from django.contrib import messages

# Create your views here.
def center_detail(request, id):
    center = get_object_or_404(Center, id=id)
    instructors = Instructor.objects.filter(center=center.id)
    return render(request, 'center_detail.html', {'center':center, 'instructors':instructors})

def add_review_to_center(request, id):
    center = get_object_or_404(Center, id=id)
    if request.method == "POST":
        form = CenterReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.center = center
            review.user = request.user
            review.save()
            return redirect('center_detail', id=center.id)
    else:
        form = CenterReviewForm()
    return render(request, 'add_review_to_center.html', {'form':form, 'center':center})

def review_remove(request, id):
    review = get_object_or_404(CenterReview, id=id)
    print(request.user==review.user)
    print(request.user, review.user)
    if request.user == review.user:
        review.delete()
    else:
        messages.warning(request, '권한 없음')
    return redirect('add_review_to_center', id=review.center.id)
