from pages.promotions.prex import Prex
from pages.promotions.uala import Uala
import pages.base_page as base_page
from optparse import OptionParser


class ExportExecutor:
    @staticmethod
    def export_data(extension):
        promotions = [Prex(), Uala()]
        for promo in promotions:
            results = promo.retrieve_promotions()
            base_page.export_results(extension, results, promo.TYPE)


if __name__ == "__main__":
    parser = OptionParser()
    parser.add_option("-e",
                      "--extension",
                      dest="extension",
                      help="extension to export. json or csv")

    (options, args) = parser.parse_args()
    if (not options.extension) or (options.extension not in ["json", "csv"]):
        parser.error("Extension file is required. Valid ones: json, csv.")
    ExportExecutor.export_data(extension=options.extension)
