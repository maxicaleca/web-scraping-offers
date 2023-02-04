from pages.promotions.prex import Prex
from pages.promotions.uala import Uala
import pages.base_page as base_page

promotions = [Prex(), Uala()]
for promo in promotions:
    results = promo.retrieve_promotions()
    base_page.export_results("json", results, promo.TYPE)
