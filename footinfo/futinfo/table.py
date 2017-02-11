#!/usr/bin/env python

############################################################################################################################################################
#
#       File Name   :   get_football_table.py
#
#       Description :   Gets football table from various footballing leagues by scraping data from the BBC website
#
#       Author      :   Aniruth Oblah
#       
#
############################################################################################################################################################

import urllib.request
from html.parser import HTMLParser
from bs4 import BeautifulSoup


def get_table(*country):
    """
    Parse the BBC website to get the latest standings of various football leagues
    """

    url_dict = {'england':'http://www.bbc.com/sport/football/premier-league/table',
        'spain':'http://www.bbc.com/sport/football/spanish-la-liga/table',
        'italy':'http://www.bbc.com/sport/football/italian-serie-a/table',
        'germany':'http://www.bbc.com/sport/football/german-bundesliga/table',
        'scotland':'http://www.bbc.com/sport/football/scottish-premiership/table',
        'turkey':'http://www.bbc.com/sport/football/turkish-super-lig/table',
        'france':'http://www.bbc.com/sport/football/french-ligue-one/table',
        'usa':'http://www.bbc.com/sport/football/us-major-league/table',
        'usawest':'http://www.bbc.com/sport/football/us-major-league/table',
        'russia':'http://www.bbc.com/sport/football/russian-premier-league/table',
        'champ':'http://www.bbc.com/sport/football/championship/table',
        'nl':'http://www.bbc.com/sport/football/dutch-eredivisie/table',
        'aus':'http://www.bbc.com/sport/football/australian-a-league/table',
        'ireland':'http://www.bbc.com/sport/football/league-of-ireland-premier/table'
        }

    # argument is invalid return 
    if(country):
        league = str(country[0]).strip().lower()
        print("League: " + league)
        if (league in url_dict):
            url = url_dict[league]
        else:
            return "Invalid country name"
    else:
        league = 'england'
        url = url_dict[league]

    html = urllib.request.urlopen(url).read()
    bs = BeautifulSoup(html, "html.parser")
    tables = bs.findChildren('table')
    if(league == 'usawest'):
        prem_table = tables[1]
    else:
        prem_table = tables[0]
    rows = prem_table.findChildren('tr')
    skip = 0
    skip_row = 0
    count = 1
    table_list = []
    printablestring = ""
    heading = "No.".ljust(3) + "Team Name".ljust(21)
    for i in ['P','W','D','L','GF','GA','GD','PTS']:
        heading += str(i).rjust(4)
    table_list.append(heading)
    table_list.append("------------------------------------------------------------")
    for row in rows:
        if(skip_row <= 1):
            skip_row += 1
            continue
        team_info = str(count).ljust(3)
        cells = row.findChildren('td')
        for cell in cells:
            if skip == 0 or skip == 1 or skip == 11 or skip == 12 :
                skip = skip + 1
                continue
            value = cell.string
            if skip == 2:
                team_name = value[0:20]
                team_info +=  "" + str(team_name).ljust(21)
            else:
                team_info += value.rjust(4)
            skip = skip + 1
        table_list.append(team_info)
        skip = 0
        count += 1


    printablestring = '\n'.join(table_list)
    return(printablestring)



