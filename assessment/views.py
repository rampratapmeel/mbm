from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.contrib.auth import authenticate, login
from django.views import generic
from django.views.generic import View
from .models import Assessment,AssessmentQuestion, AssessmentResult
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from .filters import UserFilter
from .forms import ResultForm, QuestionForm, AssessmentForm
from django.db import transaction
from student.models import Student


class ShowResult(generic.ListView):
    model = AssessmentResult
    template_name = 'assessment/showresultfaculty.html'





class IndexView(generic.ListView):
    template_name = 'assessment/index.html'
    context_object_name = 'assessment_list'

    def get_queryset(self):
        return Assessment.objects.all()

class DetailView(generic.DetailView):
    model = Assessment
    template_name = 'assessment/question.html'

class MyAssessment(generic.ListView) :
    queryset = Assessment.objects.raw("select * from course_course,assessment_assessment where course_course.id=assessment_assessment.course_id ")
    context_object_name = 'obj'
    model = Assessment
    template_name = 'assessment/temp.html'



def assessment(request):
    if request.method == 'POST':
        form = AssessmentForm(request.POST or None)
        if form.is_valid():
            data = form.save(commit=False)
            data.save()
            return HttpResponseRedirect(reverse('assessment:detail',  args=(data.id,)))
    else:
        form = AssessmentForm()
    return render(request, 'assessment/assessment_form.html', {'form': form})



"""class AssessmentEntry(CreateView):
    model = Assessment
    #template_name = 'assessment/assessment_form.html'
    fields = ['course', 'type', 'start_date', 'duration', 'faculty_id', 'year']

    def object(self):
        return self.id




    def get_success_url(self, **kwargs):
        return reverse('assessment:detail', kwargs={'pk': self.object.pk})
"""

class AssessmentUpdate(UpdateView):
    model = Assessment
    #template_name = 'assessment/assessmentupdate_form.html'
    fields = ['course', 'type', 'start_date', 'duration', 'faculty_id', 'year']


"""def my_view(request, id):
    instance = Assessment.objects.get(id=id)
    form = AssessmentForm(request.POST or None, instance=instance)
    if form.is_valid():
          form.save()
          return redirect('assessment:index')
    return render(request, 'assessment/assessment_form.html', {'form': form})
"""





def post_new(request, assessment_id):
    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.assessment = Assessment.objects.get(pk=assessment_id)
            post.save()
            return redirect('assessment:detail', pk=post.assessment_id)
    else:
        form = QuestionForm()
    return render(request, 'assessment/assessmentquestion_form.html', {'form': form})




def createresult(request, result_id):

    question = AssessmentQuestion.objects.raw("select * from assessment_assessmentquestion where assessment_id= %s order "
                                              "by question_order",[result_id])
    students = Student.objects.raw("select * from student_student,course_courseenrollment,assessment_assessment where "
                                   "assessment_assessment.id = %s and assessment_assessment.course_id = course_courseenrollment.course_id "
                                   "and assessment_assessment.year =course_courseenrollment.year and "
                                   "student_student.student_id = course_courseenrollment.student_id ", [result_id])
    str = {'students':students, 'temp': question}

    if request.method == "POST":
            marks = request.POST.getlist('obtained_marks')
            i = 0
            for obj in students:
                for obje in question:

                    form = ResultForm(request.POST)
                    if form.is_valid():
                       post = form.save(commit=False)
                       post.student = Student.objects.get(pk=obj.id)
                       post.question =AssessmentQuestion.objects.get(pk=obje.id)
                       post.obtained_marks =marks[i]

                       post.save()
                       i += 1
                    else:
                        return HttpResponse('form is not valid')
            return redirect('assessment:index')

    else:
        form = ResultForm()
    return render(request, 'assessment/result.html', {'form': form, 'students': students, 'temp': question})







"""
def AssessmentQuestionEntry(request,pk):
    form = AssessmentQEForm(request.POST or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.assessment = pk
        obj.save()
"""

def search(request):
    assessment_list = Assessment.objects.all()
    assessment_filter = UserFilter(request.GET, queryset=assessment_list)
    return render(request, 'assessment/assessment_list.html', {'filter' : assessment_filter})


