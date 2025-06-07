#!/usr/bin/env python3
import requests
import csv
import io
import sys
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# ← your search terms here:
KEYWORDS = ["Ableton"]  # ← adjust to your keywords

# the GitHub-Pages index
INDEX_URL = "https://nime-conference.github.io/NIME-bibliography/"

def find_csv_url(index_url: str) -> str:
    resp = requests.get(index_url)
    resp.raise_for_status()
    soup = BeautifulSoup(resp.text, "html.parser")
    for a in soup.find_all("a"):
        text = a.get_text(strip=True)
        if "Combined Paper Proceedings" in text and "CSV" in text:
            return urljoin(index_url, a["href"])
    raise RuntimeError("Could not find the CSV link on the index page!")

def fetch_papers(csv_url: str) -> list[dict]:
    resp = requests.get(csv_url)
    resp.raise_for_status()
    return list(csv.DictReader(io.StringIO(resp.text)))

def find_matching_papers(papers: list[dict], keywords: list[str]) -> list[dict]:
    matches = []
    for p in papers:
        blob = " ".join([
            p.get("title", ""),
            p.get("abstract", ""),
            p.get("keywords", "")
        ]).lower()
        for kw in keywords:
            if kw.lower() in blob:
                matches.append({
                    "year":       p.get("year", "n/a"),
                    "title":      p.get("title", "n/a"),
                    "doi":        p.get("doi",   "n/a"),
                    "matched_on": kw
                })
                break
    return matches

def save_results(hits: list[dict], keywords: list[str]):
    """Write results to a text file named after the keywords."""
    # build a safe filename: join keywords with underscores, replace spaces
    safe_name = "_".join(kw.replace(" ", "_") for kw in keywords)
    filename = f"{safe_name}.txt"

    with open(filename, "w", encoding="utf-8") as f:
        for h in hits:
            doi = h["doi"]
            link = f"https://doi.org/{doi}" if doi != "n/a" else "n/a"
            f.write(f"{h['year']} — {h['title']}\n")
            f.write(f"DOI link: {link}\n")
            f.write(f"Matched on: {h['matched_on']}\n\n")

    print(f"Results saved to {filename}")

def main():
    try:
        csv_url = find_csv_url(INDEX_URL)
    except Exception as e:
        print(f"ERROR: {e}", file=sys.stderr)
        sys.exit(1)

    try:
        papers = fetch_papers(csv_url)
    except Exception as e:
        print(f"ERROR fetching CSV at {csv_url}: {e}", file=sys.stderr)
        sys.exit(1)

    hits = find_matching_papers(papers, KEYWORDS)
    if not hits:
        print("No papers found with those keywords.")
        return

    print(f"Found {len(hits)} matching papers:\n")
    for h in hits:
        doi = h["doi"]
        link = f"https://doi.org/{doi}" if doi != "n/a" else "n/a"
        print(f"{h['year']} — {h['title']}")
        print(f"  DOI link: {link}")
        print(f"  Matched on: {h['matched_on']}\n")

    save_results(hits, KEYWORDS)

if __name__ == "__main__":
    main()
