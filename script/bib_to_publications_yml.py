import os, re
from datetime import datetime
import bibtexparser
import yaml

BIB_PATH = "assets/pubs.bib"
OUT_PATH = "_data/publications.yml"

def clean(s: str) -> str:
    if not s:
        return ""
    # bibtex 중괄호 제거 + 공백 정리
    s = s.replace("{", "").replace("}", "")
    s = re.sub(r"\s+", " ", s).strip()
    return s

def year_to_date(entry) -> str:
    y = (entry.get("year") or "").strip()
    # Jekyll sort 안정 위해 YYYY-MM-DD 형태 유지
    if y.isdigit():
        return f"{int(y):04d}-01-01"
    return "1900-01-01"

def make_link(entry) -> str:
    doi = clean(entry.get("doi", ""))
    url = clean(entry.get("url", ""))
    if doi:
        # doi만 있는 경우가 많아서 DOI 우선
        if doi.startswith("http"):
            return doi
        return "https://doi.org/" + doi
    return url

def venue(entry) -> str:
    return clean(entry.get("journal") or entry.get("booktitle") or entry.get("publisher") or "")

def main():
    if not os.path.exists(BIB_PATH):
        raise FileNotFoundError(f"Missing {BIB_PATH}. Upload your BibTeX export here.")

    with open(BIB_PATH, "r", encoding="utf-8") as f:
        db = bibtexparser.load(f)

    pubs = []
    for e in db.entries:
        title = clean(e.get("title", ""))
        if not title:
            continue

        pubs.append({
            "title": title,
            "author": clean(e.get("author", "")),
            "journal": venue(e) or "—",
            "date": year_to_date(e),
            "link": make_link(e)
        })

    # 최신순 정렬
    pubs.sort(key=lambda x: x["date"], reverse=True)

    os.makedirs("_data", exist_ok=True)
    with open(OUT_PATH, "w", encoding="utf-8") as f:
        yaml.safe_dump(pubs, f, allow_unicode=True, sort_keys=False)

if __name__ == "__main__":
    main()
