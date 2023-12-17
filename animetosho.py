# VERSION: 1.00
# AUTHORS: ALAA_BRAHIM
# LICENSING INFORMATION

#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <https://www.gnu.org/licenses/>.

from html.parser import HTMLParser
from helpers import download_file, retrieve_url
from novaprinter import prettyPrinter


class animetosho(object):
    url = "https://animetosho.org"
    name = "Anime Tosho"
    supported_categories = {
        "all": [""]
    }

    def __init__(self):
        pass

    def download_torrent(self, info):
        print(download_file(info))

    def search(self, what, cat='all'):
        results = []
        for page in range(1, 10):
            url = f"https://animetosho.org/search?q={what}&page={page}"
            try:
                data = retrieve_url(url)
                parser = self.DataExtractor()
                parser.feed(data)
                results = parser.get_results()
                parser.close()
                if len(results) == 0:
                    break
            except Exception:
                break
            for result in results[::-1]:
                prettyPrinter(result)

    class DataExtractor(HTMLParser):
        def __init__(self):
            super().__init__()
            self.in_corret_tag = False
            self.found_size = False
            self.found_name = False
            self.save_name_data = False
            self.look_for_magnet = False
            self.look_for_seeds = False
            self.results = []
            self.current_result = {"engine_url": "https://animetosho.org/"}

        def handle_starttag(self, tag, attrs):
            for attr in attrs:
                attribute = attr[0]
                attribute_values = attr[1].split()
                if attribute == 'class' and "home_list_entry" in attribute_values\
                        and "home_list_entry_compl_1" in attribute_values:
                    self.in_corret_tag = True

                if self.in_corret_tag:
                    if attribute == 'class' and "size" in attribute_values:
                        self.found_size = True

                    if self.found_size:
                        if attribute == 'title':
                            size = attribute_values[3].replace(",", "")
                            self.current_result["size"] = size
                            self.found_size = False

                    if attribute == 'class' and "link" in attribute_values:
                        self.found_name = True

                    if self.found_name:
                        if tag == "a":
                            description = attribute_values[0]
                            self.current_result["desc_link"] = description
                            self.save_name_data = True
                            self.found_name = False

                    if attribute == 'class' and "links" in attribute_values:
                        self.look_for_magnet = True
                        self.look_for_seeds = True

                    if self.look_for_magnet:
                        if tag == "a":
                            if attribute_values[0].startswith("magnet:?xt"):
                                self.current_result["link"] = attribute_values[0]
                                self.look_for_magnet = False

                    if self.look_for_seeds:
                        if tag == "span":
                            if attribute == "title":
                                seeds, leech = attr[1].split("/")
                                seeds = seeds.split(": ")[1].strip()
                                leech = leech.split(": ")[1].strip()
                                self.current_result["seeds"] = seeds
                                self.current_result["leech"] = leech

                    self.check_current_result_completed()

        def handle_data(self, data):
            if self.save_name_data:
                self.current_result["name"] = data
                self.save_name_data = False

        def check_current_result_completed(self):
            if len(self.current_result) == 7:
                self.results.append(self.current_result)
                self.current_result = {"engine_url": "https://animetosho.org/"}
                self.in_corret_tag = False

        def get_results(self):
            return self.results


if __name__ == "__main__":
    a = animetosho()
    a.search("zom+judas")
