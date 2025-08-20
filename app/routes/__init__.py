from .blueprints import (learn, compare, quiz)
from .views import (index, about, sitemap)

# { "rule": None, "func": None, "endpoint": None, "methods": None, "blueprint": bp },

routes_list = [
    index.index_route,
    about.about_route,
    sitemap.sitemap_route,
    learn.learn_bp_route,
    compare.compare_bp_route,
    quiz.quiz_bp_route,
]
