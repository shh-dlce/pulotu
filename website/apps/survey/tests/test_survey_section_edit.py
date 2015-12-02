from django.core.urlresolvers import reverse
from website.apps.survey.models import Question
from website.testutils import WithCompleteDatabase


class Tests(WithCompleteDatabase):
    """Tests the survey-section-edit view"""
    def setUp(self):
        WithCompleteDatabase.setUp(self)
        self.question_int = Question.objects.create(
            section=self.section,
            subsection=self.subsection,
            number=1,
            question='How old are you?',
            information="",
            response_type='Int',
            editor=self.editor)
        self.question_float = Question.objects.create(
            section=self.section,
            subsection=self.subsection,
            number=2,
            question='How far away is coffee?',
            information="",
            response_type='Float',
            editor=self.editor)
        self.question_text = Question.objects.create(
            section=self.section,
            subsection=self.subsection,
            number=3,
            question='What is your name?',
            information="",
            response_type='Text',
            editor=self.editor)

    def test_error_when_not_logged_in(self):
        url = reverse("survey-section-edit",
                      kwargs={'culture': 'english', 'section': 'test'})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response,
                             "/accounts/login/?next=%s" % url,
                             status_code=302,
                             target_status_code=200)

    def test_404_on_missing_culture(self):
        self.client.login(username="admin", password="test")
        response = self.client.get(reverse("survey-section-edit",
                                           kwargs={'culture': 'fudge',
                                                   'section': 'test'}))
        self.assertEqual(response.status_code, 404)

    def test_404_on_missing_section(self):
        self.client.login(username="admin", password="test")
        response = self.client.get(reverse("survey-section-edit",
                                           kwargs={'culture': 'maori',
                                                   'section': 'fudge'}))
        self.assertEqual(response.status_code, 404)

    def test_post(self):
        self.client.login(username="admin", password="test")
        response = self.client.post(reverse(
            "survey-section-edit", kwargs={'culture': 'maori', 'section': 'test'}))

    def test_page(self):
        self.client.login(username="admin", password="test")
        response = self.client.get(reverse("survey-section-edit",
                                           kwargs={'culture': 'maori',
                                                   'section': 'test'}))
        self.assertContains(response, self.question_int.question)
        self.assertContains(response, self.question_float.question)
        self.assertContains(response, self.question_text.question)
