from django.forms import ModelForm, forms
from .models import AssessmentResult, AssessmentQuestion, Assessment
from django.forms.models import modelformset_factory, inlineformset_factory
from bootstrap_datepicker_plus import DatePickerInput

from django.contrib.admin.widgets import AdminDateWidget
from django.forms.fields import DateField


class ResultForm(ModelForm):
    class Meta:
        model = AssessmentResult
        fields = ['obtained_marks']




class QuestionForm(ModelForm):
    class Meta:
        model = AssessmentQuestion
        fields = ['question_type', 'text', 'max_marks', 'question_order', 'marking_scheme', 'outcome']



class AssessmentForm(ModelForm):
    class Meta:
        model = Assessment
        fields = ['course', 'type', 'start_date', 'duration', 'faculty_id', 'year']
