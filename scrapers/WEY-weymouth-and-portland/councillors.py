from lgsf.councillors.scrapers import ModGovCouncillorScraper


class Scraper(ModGovCouncillorScraper):
    base_url = "http://moderngovdcp.dorsetforyou.gov.uk"
    disabled = True
