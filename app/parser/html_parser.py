# !/usr/bin/python3.5.1
from html.parser import HTMLParser
import os


# flask guide: https://www.makeuseof.com/tag/python-javascript-communicate-json/
# flask: https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-xviii-deployment-on-the-heroku-cloud-legacy
# python flask host solution 1 https://www.pythonanywhere.com/details/flask_hosting OR heroku


class FormulaOneDNFParser(HTMLParser):
    """
    HTML parser for F1 DNFs.
    """

    def __init__(self):
        HTMLParser.__init__(self)
        self.is_td_tag = False
        self.ret = 0        # Retirement (Not Classified)
        self.nc = 0         # Not Classified (finished)
        self.dnq = 0        # Dit Not Qualify
        self.dnpq = 0       # Did Not Pre Qualify
        self.dsq = 0        # Disqualified
        self.dns = 0        # Did Not Start
        self.dnp = 0        # Did Not Practice
        self.ex = 0         # Excluded
        self.dna = 0        # Dit Not Arrive
        self.wd = 0         # withdrawn
        self.finish = 0     # Classified Finish

    def handle_starttag(self, tag, attrs):
        """
        Parses HTML start tags to tell the parser if it can consider the data in the tag or not.
        :param tag: the HTML tag being processed.
        :param attrs: the HTML tag's attribute.
        """
        try:
            if tag == 'td' and any('background-color' in attr for attr in attrs[0]):
                self.is_td_tag = True
            else:
                self.is_td_tag = False
        except IndexError:
            self.is_td_tag = False

    def handle_endtag(self, tag):
        """
        Parses HTML end tags to reset the boolean telling the parser if it can consider the data in the tag or not.
        :param tag: the HTML tag being processed.
        """
        if tag == 'td':
            self.is_td_tag = False

    def handle_data(self, data):
        """
        Processes the text nodes between html <td> tags.
        :param data: the text data.
        """
        if self.is_td_tag:
            if data == 'Ret':
                self.ret += 1
            elif data == 'NC':
                self.nc += 1
            elif data == 'DNQ':
                self.dnq += 1
            elif data == 'DNPQ':
                self.dnpq += 1
            elif data == 'DSQ':
                self.dsq += 1
            elif data == 'DNS':
                self.dns += 1
            elif data == 'DNP':
                self.dnp += 1
            elif data == 'EX':
                self.ex += 1
            elif data == 'DNA':
                self.dna += 1
            elif data == 'WD':
                self.wd += 1
            try:
                if isinstance(int(data), int):
                    self.finish += 1
            except ValueError:
                pass

    def get_ret(self):
        """Return the number of retirements."""
        return self.ret

    def get_nc(self):
        """Return the number of NC (Not Classified, finished race)."""
        return self.nc

    def get_dnq(self):
        """Return the number of DNQ (Did Not Qualify)."""
        return self.dnq

    def get_dnpq(self):
        """Return the number of DNPQ (Dit Not Pre Qualify)."""
        return self.dnpq

    def get_dsq(self):
        """Return the number of Disqualifications."""
        return self.dsq

    def get_dns(self):
        """Return the number of DNS (Did Not Start)."""
        return self.dns

    def get_dnp(self):
        """Return the number of DNP (Did Not Practice)."""
        return self.dnp

    def get_ex(self):
        """Return the number of exclusions."""
        return self.ex

    def get_dna(self):
        """Return the number of DNA (Did Not Arrive)."""
        return self.dna

    def get_wdn(self):
        """Return the number of withdraws."""
        return self.wd

    def get_classified_finish(self):
        return self.finish

    def get_total_entries(self):
        return self.get_classified_finish() + self.get_total_dnf()

    def get_total_dnf(self):
        """Return the sum of all possible DNFs."""
        return self.ret + self.nc + self.dnq + self.dnpq + self.dsq + self.dns + self.dnp + self.ex + self.dna + self.wd

    def print_dnf_stats(self):
        print("---------")
        print("Retirements: {}".format(self.get_ret()))
        print("NC: {}".format(self.get_nc()))
        print("DNQ: {}".format(self.get_dnq()))
        print("DNPQ: {}".format(self.get_dnpq()))
        print("DSQ: {}".format(self.get_dsq()))
        print("DNS: {}".format(self.get_dns()))
        print("DNP: {}".format(self.get_dnp()))
        print("Exclusions: {}".format(self.get_ex()))
        print("DNA: {}".format(self.get_dna()))
        print("WD: {}".format(self.get_wdn()))
        print("Total DNF: {}".format(self.get_total_dnf()))
        print("---------")
        print("Total Classified finishes = {}".format(self.get_classified_finish()))
        print("Total race entries = {}".format(self.get_total_entries()))
        print("\n---------------------------------------------------------------------------")
        print("---------------------------------------------------------------------------\n")

    def error(self, message):
        pass


def main():
    for filename in sorted(os.listdir(os.path.join(os.getcwd(), 'raw_data'))):
        parser = FormulaOneDNFParser()
        with open(os.path.join(os.getcwd(), 'raw_data', filename), 'r') as file:
            for line in file:
                parser.feed(line)
        print("{} Season".format(filename[:4]))
        parser.print_dnf_stats()


if __name__ == '__main__':
    main()
