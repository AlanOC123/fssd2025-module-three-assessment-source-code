from .blueprints import (explore, timeline, quiz)
from .app import (index, about, sitemap)

# { "rule": None, "func": None, "endpoint": None, "methods": None, "blueprint": bp },

routes_list = [
    index.index_route,
    about.about_route,
    sitemap.sitemap_route,
    explore.explore_bp_route,
    timeline.compare_bp_route,
    quiz.quiz_bp_route,
]
