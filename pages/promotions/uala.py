import json
import pages.base_page as base_page


def remove_extra_information(promo):
    for key in ["slug", "logo", "position", "featured", "image", "categoriesCollection", "sectionsCollection"]:
        try:
            promo.pop(key)
        except:
            pass
    promo["title"] = promo['name'] + ": " + promo['previewTitle']
    promo.pop('name')
    promo.pop('previewTitle')
    for key in promo.keys():
        if isinstance(promo[key], str):
            text = promo[key].encode('UTF-8').decode('UTF-8')
            promo[key] = text
    return promo


class Uala:

    URL = "https://www.uala.com.ar/promociones"
    TYPE = "uala"

    def retrieve_promotions(self):
        document = base_page.process_document(self.URL)
        promos_data = document.xpath("//script[@id='__NEXT_DATA__']")[0].text_content()
        promotions = json.loads(promos_data)['props']['pageProps']
        keys_to_remove = [key for key in promotions.keys() if "response" in key]
        promotions = {key: promotions[key] for key in promotions.keys() if key not in keys_to_remove}
        results = []
        for key in promotions.keys():
            for item in promotions[key]['promotionCollection']['items']:
                promo = remove_extra_information(item)
                results.append(promo)
        return results

