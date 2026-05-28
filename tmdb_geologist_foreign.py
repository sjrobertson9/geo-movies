#!/usr/bin/env python3
"""
tmdb_geologist_foreign.py
─────────────────────────
Pulls all movies tagged "geologist" (keyword ID 161281) from TMDB,
filters to non-English originals, and writes a CSV.

Usage:
    python tmdb_geologist_foreign.py --api-key YOUR_KEY_HERE

Get a free API key at: https://www.themoviedb.org/settings/api
"""

import argparse
import csv
import sys
import time
import urllib.request
import json

KEYWORD_ID = 161281       # "geologist"
KEYWORD_ID_GEO = 192938  # "geology" — run both for fuller coverage
BASE = "https://api.themoviedb.org/3"


def fetch(url, api_key):
    sep = "&" if "?" in url else "?"
    full = f"{url}{sep}api_key={api_key}&language=en-US"
    with urllib.request.urlopen(full) as r:
        return json.loads(r.read())


def all_movies_for_keyword(keyword_id, api_key):
    """Page through keyword/movies endpoint, return all results."""
    movies = []
    page = 1
    while True:
        url = f"{BASE}/keyword/{keyword_id}/movies?page={page}&include_adult=false"
        data = fetch(url, api_key)
        movies.extend(data.get("results", []))
        if page >= data.get("total_pages", 1):
            break
        page += 1
        time.sleep(0.25)   # be polite to the API
    return movies


def enrich(movie_id, api_key):
    """Fetch full movie details: original_language, genres, overview."""
    url = f"{BASE}/movie/{movie_id}"
    try:
        return fetch(url, api_key)
    except Exception:
        return {}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--api-key", required=True, help="TMDB API key")
    parser.add_argument(
        "--include-english", action="store_true",
        help="Include English-language films too (default: foreign only)"
    )
    parser.add_argument(
        "--both-keywords", action="store_true",
        help="Also pull keyword 192938 ('geology') for wider coverage"
    )
    parser.add_argument(
        "--out", default="geologist_foreign_films.csv",
        help="Output CSV filename"
    )
    args = parser.parse_args()

    print("Fetching 'geologist' keyword movies...")
    movies = all_movies_for_keyword(KEYWORD_ID, args.api_key)

    if args.both_keywords:
        print("Fetching 'geology' keyword movies...")
        movies += all_movies_for_keyword(KEYWORD_ID_GEO, args.api_key)

    # Deduplicate by TMDB ID
    seen = {}
    for m in movies:
        seen[m["id"]] = m
    movies = list(seen.values())
    print(f"  {len(movies)} unique movies found across keywords")

    # Enrich and filter
    rows = []
    for i, m in enumerate(movies, 1):
        detail = enrich(m["id"], args.api_key)
        lang = detail.get("original_language", "")
        if not args.include_english and lang == "en":
            continue

        rows.append({
            "tmdb_id":           m["id"],
            "title":             detail.get("title", m.get("title", "")),
            "original_title":    detail.get("original_title", ""),
            "original_language": lang,
            "release_date":      detail.get("release_date", ""),
            "year":              (detail.get("release_date") or "")[:4],
            "genres":            ", ".join(g["name"] for g in detail.get("genres", [])),
            "runtime_min":       detail.get("runtime", ""),
            "production_countries": ", ".join(
                c["name"] for c in detail.get("production_countries", [])
            ),
            "overview":          detail.get("overview", "").replace("\n", " "),
            "tmdb_url":          f"https://www.themoviedb.org/movie/{m['id']}",
        })

        if i % 10 == 0:
            print(f"  enriched {i}/{len(movies)}...")
        time.sleep(0.25)

    # Sort by year
    rows.sort(key=lambda r: r["year"] or "0")

    # Write CSV
    fieldnames = [
        "tmdb_id", "title", "original_title", "original_language",
        "year", "release_date", "genres", "runtime_min",
        "production_countries", "overview", "tmdb_url"
    ]
    with open(args.out, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    print(f"\nDone. {len(rows)} non-English films written to: {args.out}")

    # Quick summary by language
    from collections import Counter
    langs = Counter(r["original_language"] for r in rows)
    print("\nLanguage breakdown:")
    for lang, count in langs.most_common():
        print(f"  {lang:6s}  {count}")


if __name__ == "__main__":
    main()
