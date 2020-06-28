
from django.http import HttpResponse, HttpResponseRedirect
from .models import building
from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from review.models import evaluation,facilityreview,moodreview



def index2(request):
    all_building=building.objects.all()
    return render(request,'myapp/index2.html',{'all_building':all_building})




def detail2(request,build_id):
    try:
        build=building.objects.get(pk=build_id)
    except building.DoesNotExist:
        raise Http404("Cafe does not exist")
    return render(request,'myapp/detail2.html',{'build':build})

def home(request):
    return render(request,'myapp/home.html')

def vote(request, build_id):
# question_id 에 해당하는 Question을 가져옴
    build=building.objects.get(pk=build_id)
    #building = get_object_or_404(building, pk=building_id)
    try:
        # request.POST는 dictionary이며, POST Method 를 통해 전달 받은 값들이 이름(Key)-값(Value) 형태로 저장되어 있음
        selected_evaluation = build.evaluation_set.get(pk=request.POST['evaluation'])
    except (KeyError, evaluation.DoesNotExist):
        # POST로 전달 받은 Choice가 존재 하지 않을 경우, error_message와 함께 다시 원래 페이지를 표시하도록 함 .
        return render(request, 'myapp/detail2.html', {
        'build': build,
        'error_message': "You didn't select a evaluation.",
        })
    else:
        # try 문에서 오류 없었을 경우, 선택지의 votes 값에 1을 더하고 저장
        selected_evaluation.votes += 1
        selected_evaluation.save()
        # 결과 화면으로 사용자를 이동 시킴
        return HttpResponseRedirect(reverse('myapp:detail2', args=(build.id,)))

def vote2(request, build_id):
# question_id 에 해당하는 Question을 가져옴
    build=building.objects.get(pk=build_id)
    #building = get_object_or_404(building, pk=building_id)
    try:
        # request.POST는 dictionary이며, POST Method 를 통해 전달 받은 값들이 이름(Key)-값(Value) 형태로 저장되어 있음
        selected_facilityreview = build.facilityreview_set.get(pk=request.POST['facilityreview'])
    except (KeyError, facilityreview.DoesNotExist):
        # POST로 전달 받은 Choice가 존재 하지 않을 경우, error_message와 함께 다시 원래 페이지를 표시하도록 함 .
        return render(request, 'myapp/detail2.html', {
        'build': build,
        'error_message': "You didn't select a evaluation.",
        })
    else:
        # try 문에서 오류 없었을 경우, 선택지의 votes 값에 1을 더하고 저장
        selected_facilityreview.f_votes += 1
        selected_facilityreview.save()
        # 결과 화면으로 사용자를 이동 시킴
        return HttpResponseRedirect(reverse('myapp:detail2', args=(build.id,)))

def vote3(request, build_id):
# question_id 에 해당하는 Question을 가져옴
    build=building.objects.get(pk=build_id)
    #building = get_object_or_404(building, pk=building_id)
    try:
        # request.POST는 dictionary이며, POST Method 를 통해 전달 받은 값들이 이름(Key)-값(Value) 형태로 저장되어 있음
        selected_moodreview = build.moodreview_set.get(pk=request.POST['moodreview'])
    except (KeyError, moodreview.DoesNotExist):
        # POST로 전달 받은 Choice가 존재 하지 않을 경우, error_message와 함께 다시 원래 페이지를 표시하도록 함 .
        return render(request, 'myapp/detail2.html', {
        'build': build,
        'error_message': "You didn't select a evaluation.",
        })
    else:
        # try 문에서 오류 없었을 경우, 선택지의 votes 값에 1을 더하고 저장
        selected_moodreview.m_votes += 1
        selected_moodreview.save()
        # 결과 화면으로 사용자를 이동 시킴
        return HttpResponseRedirect(reverse('myapp:detail2', args=(build.id,)))