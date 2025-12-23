import bibtexparser
import csv
import re

bib_file = "publications.bib"
tsv_file = "citations.tsv"

def make_slug(title):
    return re.sub(r'\W+', '-', title.lower()).strip('-')

def parse_date(entry):
    year = entry.get("year", "9999")
    month = entry.get("month", "01")
    day = "01"
    month_map = {
        "jan": "01", "feb": "02", "mar": "03", "apr": "04",
        "may": "05", "jun": "06", "jul": "07", "aug": "08",
        "sep": "09", "oct": "10", "nov": "11", "dec": "12"
    }
    month = month.lower()[:3]
    month = month_map.get(month, "01")
    return f"{year}-{month}-{day}"

def sentence_case(title):
    if not title:
        return ""
    title = re.sub(r'{|}', '', title)
    title = title.lower()
    title = title[0].upper() + title[1:]
    return title
def format_authors_apa(author_field):
    """
    Converts BibTeX author field to APA format: Last, F., Last, F., & Last, F.
    Every occurrence of Halls, D. is bold and italic (***Halls, D.***)
    """
    authors = [a.strip() for a in author_field.replace("\n","").split(" and ")]
    formatted = []

    for a in authors:
        if "," in a:  # Last, First
            last, first = [p.strip() for p in a.split(",", 1)]
        else:  # First Last
            parts = a.strip().split()
            last = parts[-1]
            first = " ".join(parts[:-1])
        initials = " ".join([f"{n[0]}." for n in first.split() if n])
        name = f"{last}, {initials}"
        # Bold & italic every Halls, D.
        if last.lower() == "halls" and initials.upper() == "D.":
            name = f"***{name}***"
        formatted.append(name)

    if len(formatted) > 1:
        return ", ".join(formatted[:-1]) + ", & " + formatted[-1]
    else:
        return formatted[0]



with open(bib_file, encoding='utf-8') as f:
    bib_database = bibtexparser.load(f)

with open(tsv_file, "w", encoding='utf-8', newline='') as tsv:
    writer = csv.writer(tsv, delimiter='\t')
    writer.writerow(["pub_date", "title", "venue", "excerpt", "citation", "url_slug", "paper_url", "slides_url"])

    for entry in bib_database.entries:
        title = sentence_case(entry.get("title", ""))
        pub_date = parse_date(entry)
        venue = entry.get("journal") or entry.get("booktitle") or ""
        volume = entry.get("volume", "")
        number = entry.get("number", "")
        pages = entry.get("pages", "")
        authors = entry.get("author", "")
        paper_url = entry.get("url", "")
        slides_url = ""
        excerpt = entry.get("abstract", "")

        authors_apa = format_authors_apa(authors)
        citation = f"{authors_apa} ({entry.get('year','')}). {title}."
        if venue:
            citation += f" *{venue}*"
        if volume:
            citation += f", {volume}"
        if number:
            citation += f"({number})"
        if pages:
            citation += f", {pages}"
        citation += "."
        if paper_url:
            citation += f" {paper_url}"

        url_slug = make_slug(title)

        writer.writerow([pub_date, title, venue, excerpt, citation, url_slug, paper_url, slides_url])
        print(citation)

print(f"TSV saved to {tsv_file} with APA-style citations.")
