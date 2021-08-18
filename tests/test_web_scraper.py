from web_scraper import __version__


def test_version():
    assert __version__ == '0.1.0'


from web_scraper.scraper import *

def test_get_citations_needed_number():
    url="https://en.wikipedia.org/wiki/History_of_Mexico"
    actual = get_citations_needed_number(url)
    expected = 5
    assert actual == expected

def test_get_citations_needed_report():
    url="https://en.wikipedia.org/wiki/History_of_Mexico"
    actual = get_citations_needed_report(url)
    expected = "During the three centuries of colonial rule, fewer than 700,000 Spaniards, most of them men, settled in Mexico.[citation needed] Europeans, Africans, and indigenous intermixed, creating a mixed-race casta population in a process known as mestizaje. Mestizos, people of mixed European-indigenous ancestry, constitute the majority of Mexico's population."
    assert actual == expected