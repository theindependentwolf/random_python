#!/usr/bin/env python

############################################################################################################################################################
#
#       File Name   :   get_football_table.py
#
#       Description :   Get injury lists of various teams. Default is Liverpool
#
#       Author      :   Aniruth Oblah
#       
#
############################################################################################################################################################

import urllib.request
from html.parser import HTMLParser
from bs4 import BeautifulSoup



def injuries_teams():
    """
    Get list of teams for which injury list is available

    Args: None
    
    Return: string containing all the commmands available for get_injuries method
    """

    team_list = ["hull","sunderland","saints","palace","watford","stoke","arsenal","everton","liverpool","whu - For West Ham","swansea","wba - For West Brom","city - For Man City","burnley","spurs","boro - For Middlesborough","united - For Scum","leicester","chelsea","bournemouth"]
    printable_string = "\n".join(team_list)
    return(printable_string)





def get_injuries(team):
    """
    Returns injuries for a team

    Args: team (str): Team Name for which injury list is to be returned

    Return: returns a formmatted string containing all the injuries
    """

    teams={'hull':'Hull City away shirt',
        'sunderland':'Sunderland away shirt',
        'saints':'Southampton away shirt',
        'palace':'Crystal Palace away shirt',
        'watford':'Watford away shirt',
        'stoke':'Stoke City away shirt',
        'arsenal':'Arsenal away shirt',
        'everton':'Everton away shirt',
        'liverpool':'Liverpool away shirt',
        'whu':'West Ham United away shirt',
        'swansea':'Swansea City away shirt',
        'wba':'West Bromwich Albion away shirt',
        'city':'Manchester City away shirt',
        'burnley':'Burnley away shirt',
        'spurs':'Tottenham Hotspur away shirt',
        'boro':'Middlesbrough away shirt',
        'united':'Manchester United away shirt',
        'leicester':'Leicester City away shirt',
        'chelsea':'Chelsea away shirt',
        'bournemouth':'Bournemouth away shirt'}

    team_name = teams.get(team[0].strip().lower(), 'Liverpool away shirt')

    url = "http://www.physioroom.com/news/english_premier_league/epl_injury_table.php"
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, "html.parser")
    lp = soup.find(alt=team_name).parent.parent.parent.next_sibling.next_sibling
    if(not lp):
        return("```No reported injuries.```")
    player_info = ""
    heading = "Name".ljust(15) + "Injury".ljust(25) + "Return Date".ljust(15) + "\n" + "-----------------------------------------------------------" + "\n"
    player_list = []
    player_list.append(heading)

    while True:
        if(lp.has_attr('id')):
                break
        else:
            tdlist = lp.find_all('td')# player_info = tdlist[0].string+"\t"+tdlist[1].string+"\t"+tdlist[3].string
            if(tdlist[1].find('a')):
                player_info = str(tdlist[0].string.strip()).ljust(15) + str(tdlist[1].find('a').string.strip()).ljust(25)  + str(tdlist[3].string.strip()).ljust(15)
                player_list.append(player_info.strip())
            else:
                player_info = str(tdlist[0].string.strip()).ljust(15) + str(tdlist[1].string.strip()).ljust(25) + str(tdlist[3].string.strip()).ljust(15)
                player_list.append(player_info.strip())
        lp=lp.findNext('tr')
    printable_string = "\n".join(player_list)
    return(printable_string)




