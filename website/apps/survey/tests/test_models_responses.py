from textwrap import dedent
from website.apps.core.models import Culture, Source, Section
from website.apps.survey.models import Question, OptionQuestion, Response
from website.apps.survey.models import IntegerResponse, FloatResponse, TextResponse, \
    OptionResponse
from website.testutils import WithEditor


class WithBasicData(WithEditor):
    """Tests the Polymorphic Models"""

    def setUp(self):
        WithEditor.setUp(self)
        self.source = Source.objects.create(
            year=1991, author='Smith',
            slug='Smith1991', reference='S2',
            comment='c1', editor=self.editor)
        self.culture = Culture.objects.create(
            id=1,
            culture='Maori',
            slug='maori',
            editor=self.editor)
        self.section = Section.objects.create(
            section="Test",
            slug="test",
            editor=self.editor)
        self.subsection = Section.objects.create(
            section="Sub", slug="sub",
            editor=self.editor)
        self.question = Question.objects.create(
            id=1,
            section=self.section,
            subsection=self.subsection,
            number=1, question='Where are you?',
            information="..", editor=self.editor)


class TestResponse(WithBasicData):
    def setUp(self):
        WithBasicData.setUp(self)
        r = Response.objects.create(
            question=self.question,
            culture=self.culture,
            author=self.editor,
            source1=self.source
        )
        r.save()

    def test_repr(self):
        r = Response.objects.all()[0]
        assert repr(r) == 'Response: 1-1-Smith (1991): NA'

    def test_create(self):
        r = Response.objects.all()[0]
        assert r.author == self.editor
        assert r.culture == self.culture
        assert r.question == self.question
        assert r.source1 == self.source


class TestIntegerResponse(WithBasicData):
    def setUp(self):
        WithBasicData.setUp(self)
        r = IntegerResponse.objects.create(
            question=self.question,
            culture=self.culture,
            author=self.editor,
            source1=self.source,
            response=99
        )
        r.save()

    def test_repr(self):
        r = Response.objects.all()[0]
        self.assertEquals(repr(r), 'Response: 1-1-Smith (1991): 99')

    def test_get_from_response(self):
        assert len(Response.objects.all()) == 1

    def test_get_from_subclass(self):
        assert len(IntegerResponse.objects.all()) == 1

    def test_cant_get_from_subclass(self):
        assert len(FloatResponse.objects.all()) == 0
        assert len(TextResponse.objects.all()) == 0

    def test_create(self):
        r = IntegerResponse.objects.all()[0]
        assert r.author == self.editor
        assert r.culture == self.culture
        assert r.question == self.question
        assert r.source1 == self.source
        assert r.response == 99


class TestFloatResponse(WithBasicData):
    def setUp(self):
        WithBasicData.setUp(self)
        r = FloatResponse.objects.create(
            question=self.question,
            culture=self.culture,
            author=self.editor,
            source1=self.source,
            response=99.9
        )
        r.save()

    def test_repr(self):
        r = Response.objects.all()[0]
        self.assertEquals(repr(r), 'Response: 1-1-Smith (1991): 99.9')

    def test_get_from_response(self):
        assert len(Response.objects.all()) == 1

    def test_get_from_subclass(self):
        assert len(FloatResponse.objects.all()) == 1

    def test_cant_get_from_subclass(self):
        assert len(IntegerResponse.objects.all()) == 0
        assert len(TextResponse.objects.all()) == 0

    def test_create(self):
        r = FloatResponse.objects.all()[0]
        assert r.author == self.editor
        assert r.culture == self.culture
        assert r.question == self.question
        assert r.source1 == self.source
        assert r.response == 99.9


class TestTextResponse(WithBasicData):
    def setUp(self):
        WithBasicData.setUp(self)
        r = TextResponse.objects.create(
            question=self.question,
            culture=self.culture,
            author=self.editor,
            source1=self.source,
            response="This is \n Some Text"
        )
        r.save()

    def test_repr(self):
        r = Response.objects.all()[0]
        assert repr(r) == 'Response: 1-1-Smith (1991): This is \n Some Text'

    def test_get_from_response(self):
        assert len(Response.objects.all()) == 1

    def test_get_from_subclass(self):
        assert len(TextResponse.objects.all()) == 1

    def test_cant_get_from_subclass(self):
        assert len(IntegerResponse.objects.all()) == 0
        assert len(FloatResponse.objects.all()) == 0

    def test_create(self):
        r = TextResponse.objects.all()[0]
        assert r.author == self.editor
        assert r.culture == self.culture
        assert r.question == self.question
        assert r.source1 == self.source
        assert r.response == "This is \n Some Text"


class TestOptionResponse(WithBasicData):
    def setUp(self):
        WithBasicData.setUp(self)
        r = OptionResponse.objects.create(
            question=self.question,
            culture=self.culture,
            author=self.editor,
            source1=self.source,
            response="0",
            response_text="blah blah blah"
        )
        r.save()

    def test_repr(self):
        r = Response.objects.all()
        self.assertEquals(repr(r[0]), 'Response: 1-1-Smith (1991): 0')

    def test_get_from_response(self):
        assert len(Response.objects.all()) == 1

    def test_get_from_subclass(self):
        assert len(OptionResponse.objects.all()) == 1

    def test_cant_get_from_subclass(self):
        assert len(FloatResponse.objects.all()) == 0

    def test_create(self):
        r = OptionResponse.objects.all()[0]
        assert r.author == self.editor
        assert r.culture == self.culture
        assert r.question == self.question
        assert r.source1 == self.source
        assert r.response == "0"
        assert r.response_text == 'blah blah blah'

    def test_save_sets_response_text(self):
        q = OptionQuestion.objects.create(
            number=9,
            question="Is 9 a good number?",
            options=dedent("""
            (0) yes
            (1) no
            """),
            section=self.section,
            subsection=self.subsection,
            editor=self.editor
        )
        q.save()
        r = OptionResponse.objects.create(
            question=q,
            culture=self.culture,
            author=self.editor,
            source1=self.source,
            response='0',
        )
        r.save()
        assert r.response_text == 'yes'
        r.response = '1'
        r.save()
        assert r.response_text == 'no'


class TestHeterogenousResponses(WithBasicData):
    """Test that we can get a heterogenous mix of responses"""

    def setUp(self):
        WithBasicData.setUp(self)
        self.responses = []
        self.question2 = Question.objects.create(
            section=self.section,
            subsection=self.subsection,
            number=2, question='How old are you?',
            information="..", editor=self.editor)
        self.question3 = Question.objects.create(
            section=self.section,
            subsection=self.subsection,
            number=3, question='Where is Simon?',
            information="..", editor=self.editor)

        self.responses.append(TextResponse.objects.create(
            question=self.question,
            culture=self.culture,
            author=self.editor,
            source1=self.source,
            response="Hello world"
        ))
        self.responses.append(FloatResponse.objects.create(
            question=self.question2,
            culture=self.culture,
            author=self.editor,
            source1=self.source,
            response=99.9
        ))
        self.responses.append(IntegerResponse.objects.create(
            question=self.question3,
            culture=self.culture,
            author=self.editor,
            source1=self.source,
            response=1
        ))

    def test_count(self):
        assert len(Response.objects.all()) == 3

    def test_all(self):
        for r in Response.objects.all():
            assert r in self.responses
