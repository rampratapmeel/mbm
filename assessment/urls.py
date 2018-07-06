from django.conf.urls import url
from assessment import views
from django.contrib.auth.views import login

app_name = 'assessment'

urlpatterns = [

    url(r'^$', views.IndexView.as_view(), name='index'),



    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^assessment/update/(?P<pk>[0-9]+)/$', views.AssessmentUpdate.as_view(), name='update'),
    url(r'^result/(?P<result_id>[0-9]+)/$', views.createresult, name='result'),
url(r'^assessment/entry/$', views.assessment, name='assessment-entry'),
#url(r'^assessment/update/(?P<id>[0-9]+)/$', views.my_view, name='update'),
    url(r'^myassessment$', views.MyAssessment.as_view(), name='myassessment'),
    url(r'^myassessmentlist/$', views.search, name='search'),
#url(r'^myresult/(?P<pk>[0-9]+)/$', views.ResultCreate.as_view(), name='myresult'),
url(r'^assessmentquestion/entry/(?P<assessment_id>[0-9]+)/$', views.post_new, name='assessmentquestion-entry'),
    url(r'^showresult/$', views.ShowResult.as_view(), name='showresult'),
]