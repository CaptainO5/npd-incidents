import os
from src.fetch import download
from src.extract import get_text_from, parse

def test_download_invalidurl():
    assert download("URL") is None

def test_download_validurl():
    file = download("https://www.normanok.gov/sites/default/files/documents/2024-03/2024-03-13_daily_incident_summary.pdf")
    assert os.path.exists(file)

def test_pdfread():
    file = download("https://www.normanok.gov/sites/default/files/documents/2024-03/2024-03-23_daily_incident_summary.pdf")
    assert type(get_text_from(file)) is str

def test_parse():
    file = download("https://www.normanok.gov/sites/default/files/documents/2024-03/2024-03-12_daily_incident_summary.pdf")
    assert parse(file) is not None