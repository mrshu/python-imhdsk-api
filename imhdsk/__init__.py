import requests
from lxml import html

IMHD_URL = "http://imhd.zoznam.sk/ba/planovac-cesty-vyhladanie-spojenia.html?"\
    "spojenieodkial={0}&spojeniekam={1}"


class Route(object):
    begin_time = None
    end_time = None

    drives = []

    def __repr__(self):
        return ' -- '.join(map(str, self.drives))


class Drive(object):
    begin_time = None
    end_time = None

    line = None

    start = None
    dest = None

    walk = False

    length = 0

    def __repr__(self):
        if self.walk:
            return "{0} -> {1}: {2}".format(self.start, self.dest, self.length)
        else:
            return "({3}) {0} -> ({4}) {1}: {2}".format(self.start, self.dest,
                                                        self.length,
                                                        self.begin_time,
                                                        self.end_time)

from lxml import etree


def routes(start, dest):
    r = requests.get(IMHD_URL.format(start, dest))
    tree = html.fromstring(r.text)

    out_routes = []
    routes = tree.xpath('//div[@class="sp"]/table')[1:]
    for route in routes:
        line = None
        out_route = Route()
        out_route.drives = []

        for tr in route.xpath('./tr')[1:]:
            line = None

            line = tr.xpath('./td[1]/span/text()')
            if len(line) > 0:
                line = line[0]

            walker = tr.xpath('./td[1]/img')
            if len(walker) > 0 and \
                    walker[0].get('src') == '/data/img/chodec.png':

                drv = Drive()
                drv.walk = True

                drv.start = tr.xpath('./td[2]/b[1]/text()')[0]
                dest = tr.xpath('./td[2]/b[2]/text()')
                if dest == []:
                    drv.dest = drv.start
                else:
                    drv.dest = tr.xpath('./td[2]/b[2]/text()')[0]

                drv.length = tr.xpath('./td[2]/text()')[-1]
                out_route.drives.append(drv)

            tables = tr.xpath('./td[1]/table')
            if len(tables) > 0:
                drv = Drive()
                tables = tr.xpath('./td[1]/table')

                drv.begin_time = tables[0].xpath('./tr/td[1]/b/text()')[0]
                drv.start = tables[0].xpath('./tr/td[2]/b/text()')[0]
                drv.end_time = tables[1].xpath('./tr/td[1]/b/text()')[0]
                drv.dest = tables[1].xpath('./tr/td[2]/b/text()')[0]

                drv.length = tr.xpath('./td/div/table/tr[1]/td[1]/text()')[-1] \
                    .split(',')[-1]
                drv.line = line

                out_route.drives.append(drv)

        out_route.begin_time = out_route.drives[0].begin_time
        out_route.end_time = out_route.drives[-1].end_time
        out_routes.append(out_route)

    return out_routes
