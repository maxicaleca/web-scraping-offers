import pages.base_page as base_page


class Prex:

    BASE_URL = "https://www.prexcard.com.ar/"
    URL = "https://www.prexcard.com.ar/promos"
    TYPE = "prex"

    def retrieve_promotions(self):
        document = base_page.process_document(self.URL)
        promos_data = document.xpath("//a[contains(@href, 'promos/')]")
        results = []
        for promo in promos_data:
            promo_url = self.BASE_URL + promo.attrib["href"]
            document = base_page.process_document(promo_url)
            information = document.xpath("//p[@class='mb-4']")
            promotion = {
                "details": information[1],
                "date": information[0],
                "title": document.xpath("//h2[@class='titulo']")[0]
            }
            for key in promotion.keys():
                promotion[key] = promotion[key].text_content().replace(" ", " ").strip().encode('UTF-8').decode('UTF-8')
            results.append(promotion)
        return results

