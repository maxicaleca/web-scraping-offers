from datetime import datetime
from lxml import html
import requests
import json
import csv
import os


def process_document(url):
    session = requests.session()
    re = session.get(url=url)
    document = html.fromstring(re.content)
    return document


def export_results(method, results, promo_type):
    variables = {
        "promo_type": promo_type,
        "extension": method,
        "datetime": datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    }
    file_name = "%(promo_type)s-%(datetime)s.%(extension)s" % variables
    file_name = file_name.replace('/', "-").replace(' ', "_").replace(":", "-")

    if method == "json":
        final_path = os.path.join(os.getcwd(), file_name)
        with open(final_path, 'w') as output_file:
            json.dump(results, output_file, indent=4, ensure_ascii=False)

    if method == "csv":
        file_name = file_name.replace(".json", ".csv")
        data_file = open(file_name, 'w')
        csv_writer = csv.writer(data_file)
        count = 0
        for promo in results:
            if count == 0:
                header = promo.keys()
                csv_writer.writerow(header)
                count += 1
            csv_writer.writerow(promo.values())
        data_file.close()

    if os.path.exists(file_name):
        print("File %s has been saved" % file_name)
