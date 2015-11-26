import autocomplete_light

from website.apps.core.views import RobotsTxt
from website.apps.core.views import SourceIndex, SourceDetail
from website.apps.core.views import LanguageIndex, LanguageDetail
from website.apps.core.views import CultureIndex, CultureDetail, CultureEdit
from website.apps.survey.views import QuestionIndex, QuestionDetail
from website.apps.survey.views import SurveyIndex, SurveyCultureIndex
from django.contrib.auth.models import User
from website.apps.core.models import Section, Culture, Source, Language
from website.apps.survey.models import Question, Response

autocomplete_light.register(Source, search_fields=['author'],
    autocomplete_js_attributes={'placeholder':'Response'},)