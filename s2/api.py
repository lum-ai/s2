import requests

class AuthorStub(object):

    def __init__(self, **kwargs):
        self.authorId = kwargs["authorId"]
        self.name = kwargs.get("name", None)
        self.url = kwargs.get("url", None)

    def __str__(self):
        return self.authorId

    def __eq__(self, other):
        return isinstance(other, AuthorStub) and self.authorId == other.authorId

    def __hash__(self):
        return hash(self.authorId)

    def json(self):
        return {
            "authorId" : self.authorId,
            "name" : self.name,
            "url" : self.url
        }

    def full(self, **kwargs):
        return SemanticScholarAPI.author(self.authorId, **kwargs)

class Author(object):

    def __init__(self, **kwargs):
        self._kwargs = kwargs
        self.authorId = kwargs["authorId"]
        self.name = kwargs.get("name", None)
        self.aliases = kwargs.get("aliases", [])
        self.citationVelocity = kwargs.get("citationVelocity", None)
        self.influentialCitationCount = kwargs.get("influentialCitationCount", None)
        self.url = kwargs.get("url", None)

    def __str__(self):
        return self.authorId

    def __eq__(self, other):
        return isinstance(other, Author) and self.authorId == other.authorId

    def __hash__(self):
        return hash(self.authorId)

    def papers(self):
        for elem in self._kwargs.get("papers", []):
            yield SemanticScholarAPI.paper(elem["paperId"])

    def json(self):
        return self._kwargs

class PaperStub(object):

    def __init__(self, **kwargs):
        self.paperId = kwargs["paperId"]
        self.isInfluential = kwargs.get("isInfluential", False)
        self.title = kwargs.get("title", None)
        self.venue = kwargs.get("venue", None)
        self.year = kwargs.get("year", None)

    def __str__(self):
        return self.paperId

    def __eq__(self, other):
        return isinstance(other, PaperStub) and self.paperId == other.paperId

    def __hash__(self):
        return hash(self.paperId)

    def json(self):
        return {
            "paperId" : self.paperId,
            "isInfluential" : self.isInfluential,
            "title" : self.title,
            "venue" : self.venue,
            "year" : self.year,
        }

    def full(self, **kwargs):
        return SemanticScholarAPI.paper(self.paperId, **kwargs)

class Paper(object):

    def __init__(self, **kwargs):
        self.doi = kwargs.get("doi", None)
        self.citationVelocity = kwargs.get("citationVelocity", None)
        self.influentialCitationCount = kwargs.get("influentialCitationCount", None)
        self.url = kwargs.get("url", None)
        self.authors = [AuthorStub(**elem) for elem in kwargs.get("authors", [])]
        self.citations = [PaperStub(**elem) for elem in kwargs.get("citations", [])]
        self.references = [PaperStub(**elem) for elem in kwargs.get("references", [])]
        self.venue = kwargs.get("venue", None)
        self.references = kwargs.get("references", [])
        self.title = kwargs.get("title", None)
        self.year = kwargs.get("year", None)

    def __str__(self):
        return self.paperId

    def __eq__(self, other):
        return isinstance(other, Paper) and self.paperId == other.paperId

    def __hash__(self):
        return hash(self.paperId)

    def json(self):
        return self._kwargs

class SemanticScholarAPI(object):
    BASE_URL = "http://api.semanticscholar.org/v1"
    AUTHOR_ENDPOINT = "{}/{}".format(BASE_URL, "author")
    PAPER_ENDPOINT = "{}/{}".format(BASE_URL, "paper")

    @staticmethod
    def paper(paper_id, **kwargs):
        url = "{}/{}".format(SemanticScholarAPI.PAPER_ENDPOINT, paper_id)
        resp = requests.get(url, params=kwargs)
        return None if resp.status_code != 200 else Paper(**resp.json())

    @staticmethod
    def author(author_id, **kwargs):
        url = "{}/{}".format(SemanticScholarAPI.AUTHOR_ENDPOINT, author_id)
        resp = requests.get(url, params=kwargs)
        return None if resp.status_code != 200 else Author(**resp.json())

    @staticmethod
    def pdf_url(paper_id):
      return "http://pdfs.semanticscholar.org/{}/{}.pdf".format(paper_id[:4], paper_id[4:])
