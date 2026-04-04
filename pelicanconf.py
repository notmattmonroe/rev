AUTHOR = 'Rev Matt'
SITENAME = 'revmatt'
SITEURL = ''  # overridden in publishconf.py

PATH = 'content'
THEME = 'theme'

TIMEZONE = 'America/Chicago'
DEFAULT_LANG = 'en'

# Blog URL structure — matches original Django routes
ARTICLE_URL     = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'

# Archive pages
YEAR_ARCHIVE_SAVE_AS    = 'blog/{date:%Y}/index.html'
YEAR_ARCHIVE_URL        = 'blog/{date:%Y}/'
MONTH_ARCHIVE_SAVE_AS   = 'blog/{date:%Y}/{date:%m}/index.html'
MONTH_ARCHIVE_URL       = 'blog/{date:%Y}/{date:%m}/'

# Categories / tags
CATEGORY_URL     = 'blog/category/{slug}/'
CATEGORY_SAVE_AS = 'blog/category/{slug}/index.html'
TAG_URL          = 'blog/tag/{slug}/'
TAG_SAVE_AS      = 'blog/tag/{slug}/index.html'

# Pages (/about/, /sites/)
PAGE_URL     = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'

USE_FOLDER_AS_CATEGORY = False
DEFAULT_CATEGORY = 'personal'

# Put the paginated blog index at /blog/ instead of /
INDEX_SAVE_AS = 'blog/index.html'

# Custom index pages for reviews and projects sections
TEMPLATE_PAGES = {
    'reviews_index.html':  'reviews/index.html',
    'projects_index.html': 'projects/index.html',
}

STATIC_PATHS = ['extras', '_redirects']

# Pagination
DEFAULT_PAGINATION = 10
DEFAULT_ORPHANS    = 2

# Disqus
DISQUS_SITENAME = 'revmatt'

# Feed generation (off locally, enabled in publishconf)
FEED_ALL_ATOM        = None
CATEGORY_FEED_ATOM   = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM     = None
AUTHOR_FEED_RSS      = None

# Extra files to copy to output root
EXTRA_PATH_METADATA = {
    'extras/quotes.json': {'path': 'extras/quotes.json'},
    '_redirects':         {'path': '_redirects'},
}
