from django.contrib.auth.models import User
from django.test import TestCase
from django.forms import ValidationError
from textwrap import dedent
from website.apps.core.models import Culture, Source, Section
from website.apps.survey.models import Question, OptionQuestion, TextResponse
from website.apps.survey.forms import IntegerResponseForm, FloatResponseForm, \
    TextResponseForm
from website.apps.survey.forms import construct_section_forms


class Test_Form_ConstructSectionForms(TestCase):
    """Tests the construct_section_forms"""

    def setUp(self):
        self.editor = User.objects.create(username='admin')
        self.culture = Culture.objects.create(
            culture='Maori', slug='maori', editor=self.editor)
        self.section_one = Section.objects.create(
            section="Test", slug="test", editor=self.editor)
        self.section_two = Section.objects.create(
            section="Example", slug="example", editor=self.editor)
        self.question_int = Question.objects.create(
            section=self.section_one,
            subsection=self.section_two,
            number=1,
            question='How old are you?',
            information="",
            response_type='Int',
            editor=self.editor)
        self.question_float = Question.objects.create(
            section=self.section_one,
            subsection=self.section_two,
            number=2,
            question='How far away is coffee?',
            information="",
            response_type='Float',
            editor=self.editor)
        self.question_text = Question.objects.create(
            section=self.section_two,
            subsection=self.section_two,
            number=3,
            question='What is your name?',
            information="",
            response_type='Text',
            editor=self.editor)
        self.source = Source.objects.create(
            year=1991,
            author='Smith',
            slug='Smith1991',
            reference='S2',
            comment='c1',
            editor=self.editor)

    def test_args(self):
        with self.assertRaises(AssertionError):
            construct_section_forms(None, None, self.section_one)
        with self.assertRaises(AssertionError):
            construct_section_forms(None, self.culture, None)
        with self.assertRaises(AssertionError):
            construct_section_forms(None, None, None)

    def test_attrs_get_set(self):
        """test that the various attrs needed in templates are set on the form"""
        for section in (self.section_one, self.section_two):
            forms = construct_section_forms(None, self.culture, section)
            for f in forms:
                assert hasattr(f, 'qnumber')
                assert f.qnumber == f.initial['question'].number
                assert hasattr(f, 'qinformation')
                assert f.qinformation == f.initial['question'].information
                assert hasattr(f, 'qtext')
                assert f.qtext == f.initial['question'].question

    def test_section_filtering(self):
        """test that construct_section_forms filters the right questions"""
        forms_one = construct_section_forms(None, self.culture, self.section_one)
        assert len(forms_one) == 2
        assert forms_one[0].initial['question'].number == 1
        assert forms_one[1].initial['question'].number == 2

        forms_two = construct_section_forms(None, self.culture, self.section_two)
        assert len(forms_two) == 1
        assert forms_two[0].initial['question'].number == 3

    def test_correct_formtypes(self):
        forms_one = construct_section_forms(None, self.culture, self.section_one)
        assert len(forms_one) == 2
        assert type(forms_one[0]) == IntegerResponseForm
        assert type(forms_one[1]) == FloatResponseForm

        forms_two = construct_section_forms(None, self.culture, self.section_two)
        assert len(forms_two) == 1
        assert type(forms_two[0]) == TextResponseForm

    def test_loads_existing_info_in_database(self):
        """Does info that's already in the database get loaded?"""
        # section two has self.question_text
        resp = TextResponse.objects.create(
            author=self.editor,
            question=self.question_text,
            culture=self.culture,
            source1=self.source,
            codersnotes="Dummy answer",
            response='Lorem ipsum...'
        )
        forms = construct_section_forms(None, self.culture, self.section_two)
        assert len(forms) == 1
        assert forms[0].instance == resp
        assert forms[0].initial['codersnotes'] == resp.codersnotes
        assert forms[0].initial['response'] == resp.response

    def test_loads_post_data(self):
        """Does POST information get injected?"""
        return
        postdata = {
            '1-source': 1,
            '1-codersnotes': u'note',
            '1-response': u'77',
            '1-question': self.question_int.id,
            '1-culture': self.culture.id,
        }
        forms = construct_section_forms(postdata, self.culture, self.section_one)
        assert len(forms) == 2
        assert forms[0].is_valid()
        resp = forms[0].save(commit=False)
        assert resp.source_id == 1
        assert resp.codersnotes == postdata['1-codersnotes']
        assert resp.response == int(postdata['1-response'])
        assert resp.question_id == self.question_int.id
        assert resp.culture_id == self.culture.id

    def test_load_post_data_into_correct_object(self):
        return
        postdata = {
            '1-source': 1,
            '1-codersnotes': u'note',
            '1-response': u'77',
            '1-question': self.question_int.id,
            '1-culture': self.culture.id,
        }
        forms = construct_section_forms(postdata, self.culture, self.section_one)
        assert len(forms) == 2
        # Second form has id 2 - should NOT have changed!
        with self.assertRaises(ValueError):
            resp = forms[1].save(commit=False)
        assert forms[1].cleaned_data['response'] is None

    def test_cant_override_culture(self):
        return
        other_culture = Culture.objects.create(
            culture='French', slug='french', editor=self.editor)
        postdata = {
            '3-source1': '1',
            '3-codersnotes': u'note',
            '3-response': u'77',
            '3-question': self.question_text.id,
            '3-culture': other_culture.id,
        }
        forms = construct_section_forms(
            postdata,
            self.culture,
            # correct - this comes from the view.
            self.section_two)

        assert len(forms) == 1
        self.assert_(forms[0].is_valid())
        resp = forms[0].save(commit=False)
        assert resp.culture_id == self.culture.id
        assert resp.culture_id != other_culture.id

    def test_cant_override_question(self):
        return
        postdata = {
            '3-source': 1,
            '3-codersnotes': u'note',
            '3-response': u'77',
            '3-question': self.question_int.id,  # NOTE not question_text
            '3-culture': self.culture.id,
        }
        forms = construct_section_forms(postdata, self.culture, self.section_two)

        assert len(forms) == 1
        assert forms[0].is_valid()
        resp = forms[0].save(commit=False)
        assert resp.question_id == self.question_text.id
        assert resp.question_id != self.question_int.id


class Test_OptionResponseForm(TestCase):
    """Tests the OptionResponseForm"""

    def setUp(self):
        self.editor = User.objects.create(username='admin')
        self.culture = Culture.objects.create(
            culture='Maori',
            slug='maori', editor=self.editor)
        self.section = Section.objects.create(
            section="Test",
            slug="test",
            editor=self.editor)
        self.subsection = Section.objects.create(
            section="Sub",
            slug="sub",
            editor=self.editor)
        self.question = OptionQuestion.objects.create(
            number=8,
            question="Belief that inanimate objects have supernatural properties",
            options=dedent("""
            (?) Missing data
            (0) absent
            (1) present
            """),
            section=self.section,
            subsection=self.subsection,
            editor=self.editor)
        self.source = Source.objects.create(
            year=1991,
            author='Smith',
            slug='Smith1991',
            reference='S2',
            comment='c1',
            editor=self.editor)

    def test_form_choices(self):
        form = construct_section_forms(None, self.culture, self.section)[0]
        return
        assert form.fields['response'].choices == form.initial['question'].get_choices(
            with_empty=True)
        assert form.fields['response'].choices == self.question.get_choices(
            with_empty=True)

    def test_form_valid(self):
        form = construct_section_forms(None, self.culture, self.section)[0]
        return
        for valid in ('?', '0', '1', 0, 1):
            assert str(valid) == form.fields['response'].clean(valid)

    def test_form_invalid(self):
        form = construct_section_forms(None, self.culture, self.section)[0]
        return
        for invalid in (None, 2, 3, 4, 'fudge', ['a', 'b']):
            with self.assertRaises(ValidationError):
                form.fields['response'].clean(invalid)
