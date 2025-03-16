import arxiv
import streamlit as st

class AdvancedArxivClient:
    def __init__(self):
        self.client = arxiv.Client()
        self.cache = {}

    def search(self, query, max_results=10, sort_by='relevance'):
        cache_key = f"{query}-{max_results}-{sort_by}"
        if cache_key in self.cache:
            return self.cache[cache_key]

        sort_criterion = {
            'relevance': arxiv.SortCriterion.Relevance,
            'submittedDate': arxiv.SortCriterion.SubmittedDate,
            'lastUpdatedDate': arxiv.SortCriterion.LastUpdatedDate
        }.get(sort_by, arxiv.SortCriterion.Relevance)

        search = arxiv.Search(
            query=query,
            max_results=max_results,
            sort_by=sort_criterion
        )

        results = []
        for result in self.client.results(search):
            results.append({
                "title": result.title,
                "abstract": result.summary,
                "pdf_url": result.pdf_url,
                "authors": [author.name for author in result.authors],
                "published": result.published.strftime("%Y-%m-%d"),
                "categories": result.categories,
                "doi": result.doi,
                "comment": result.comment,
                "entry_id": result.entry_id
            })

        self.cache[cache_key] = results
        return results