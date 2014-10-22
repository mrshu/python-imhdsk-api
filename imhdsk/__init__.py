import requests
from lxml import html

IMHD_URL = "http://imhd.zoznam.sk/{2}/planovac-cesty-vyhladanie-spojenia.html?" \
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
            return "[{5}] ({3}) {0} -> ({4}) {1}: {2}".format(self.start,
                                                              self.dest,
                                                              self.length,
                                                              self.begin_time,
                                                              self.end_time,
                                                              self.line)

from lxml import etree


def routes(start, dest, city='ba'):
    r = requests.get(IMHD_URL.format(start, dest, city))
    tree = html.fromstring(r.text)

    routes = []
    html_routes = tree.xpath('//div[@class="sp"]/table')[1:]
    for route_table in html_routes:
        line = None
        route = Route()
        route.drives = []

        line = None
        for tr in route_table.xpath('./tr')[1:]:

            l = tr.xpath('./td[1]/span/text()')
            if len(l) > 0:
                line = l[0]

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
                route.drives.append(drv)

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

                route.drives.append(drv)

        route.begin_time = route.drives[0].begin_time
        route.end_time = route.drives[-1].end_time
        routes.append(route)

    return routes
