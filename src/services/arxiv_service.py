import arxiv
from datetime import datetime

class AdvancedArxivClient:
    def __init__(self):
        self.client = arxiv.Client()
        self.cache = {}

    def search(self, query, max_results=10, sort_by='relevance'):
        """
        Search arXiv papers with caching and advanced options
        """
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
                "entry_id": result.entry_id,
                "journal_ref": result.journal_ref,
                "primary_category": result.primary_category
            })

        self.cache[cache_key] = results
        return results

    def get_paper_details(self, paper_id):
        """
        Get detailed information for a specific paper
        """
        try:
            paper = next(self.client.results(arxiv.Search(id_list=[paper_id])))
            return {
                "title": paper.title,
                "abstract": paper.summary,
                "pdf_url": paper.pdf_url,
                "authors": [author.name for author in paper.authors],
                "published": paper.published.strftime("%Y-%m-%d"),
                "updated": paper.updated.strftime("%Y-%m-%d"),
                "categories": paper.categories,
                "doi": paper.doi,
                "comment": paper.comment,
                "journal_ref": paper.journal_ref,
                "primary_category": paper.primary_category
            }
        except Exception as e:
            return {"error": f"Failed to fetch paper details: {str(e)}"}