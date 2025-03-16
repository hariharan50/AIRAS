# Default configurations
DEFAULT_SETTINGS = {
    'current_page': 'Summarizer',
    'user_authenticated': False,
    'username': '',
    'selected_article': None,
    'search_history': [],
    'generated_summaries': {},
    'feedback_history': [],
    'selected_model': "Gemini",
    'user_api_keys': {
        'gemini': '', #apikey
        'openai': ''  #apikey
    }
}

# Users database (in production, this should be in a secure database)
USERS_DB = {
    'admin@quikeview.com': {'password': 'admin123', 'name': 'Admin'},
    'user@example.com': {'password': 'user123', 'name': 'Demo User'}
}

# API Configuration
API_CONFIG = {
    'arxiv_max_results': 10,
    'arxiv_sort_by': 'relevance',
    'summary_max_length': 1000,
    'cache_ttl': 3600
}