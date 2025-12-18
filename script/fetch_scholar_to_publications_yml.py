import os
from datetime import date
from scholarly import scholarly
import yaml

USER_ID = os.getenv("GSCHOLAR_USER_ID", "FTExVZIAAAAJ")

def safe_year_to_date(y: str) -> str:
    # Jekyll sort를 위해 YYYY-MM-DD 형태 유지 (월/일 모르면 01-01)
    try:
        yy = int(str(y).strip())
        return f"{yy:04d}-01-01"
    except:
        return "1900-01-01"

def main():
    author = scholarly.search_author_id(USER_ID)
    author = scholarly.fill(author, sections=["publications"])

    pubs = []
    for p in author.get("publications", []):
        pub = scholarly.fill(p)
        bib = pub.get("bib", {})

        title = (bib.get("title") or "").strip()
        if not title:
            continue

        authors = (bib.get("author") or "").strip()
        venue = (bib.get("journal") or bib.get("booktitle") or bib.get("publisher") or "").strip()
        year = bib.get("year") or ""
        link = pub.get("pub_url") or bib.get("url") or ""

        pubs.append({
            "title": title,
            "author": authors,
            "journal": venue if venue else "—",
            "date": safe_year_to_date(year),
            "link": link
        })

    # 최신순 정렬
    pubs.sort(key=lambda x: x["date"], reverse=True)

    os.makedirs("_data", exist_ok=True)
    with open("_data/publications.yml", "w", encoding="utf-8") as f:
        yaml.safe_dump(pubs, f, allow_unicode=True, sort_keys=False)

if __name__ == "__main__":
    main()
