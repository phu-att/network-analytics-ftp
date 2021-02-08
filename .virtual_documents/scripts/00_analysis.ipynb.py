# import essential libraries
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial.distance import pdist
from matplotlib import rc
import networkx as nx


# # get_ipython().run_line_magic("%", " setup")
rc('font',**{'family':'sans-serif','sans-serif':['Computer Modern Roman']})
rc('text', usetex=True)


#data in 2020
dutch_eredivisie_2020 = pd.read_csv('https://raw.githubusercontent.com/ewenme/transfers/master/data/2020/dutch_eredivisie.csv')
enghlish_championship_2020 = pd.read_csv('https://raw.githubusercontent.com/ewenme/transfers/master/data/2020/english_championship.csv')
english_premier_2020 = pd.read_csv('https://raw.githubusercontent.com/ewenme/transfers/master/data/2020/english_premier_league.csv')
french_ligue_1_2020 = pd.read_csv('https://raw.githubusercontent.com/ewenme/transfers/master/data/2020/french_ligue_1.csv')
german_bundesliga_1_2020 = pd.read_csv('https://raw.githubusercontent.com/ewenme/transfers/master/data/2020/german_bundesliga_1.csv')
italian_serie_a_2020 = pd.read_csv('https://raw.githubusercontent.com/ewenme/transfers/master/data/2020/italian_serie_a.csv')
portugese_liga_nos_2020 = pd.read_csv('https://raw.githubusercontent.com/ewenme/transfers/master/data/2020/portugese_liga_nos.csv')
russian_premier_liga_2020 = pd.read_csv('https://raw.githubusercontent.com/ewenme/transfers/master/data/2020/russian_premier_liga.csv')
spanish_primera_division_2020 = pd.read_csv('https://raw.githubusercontent.com/ewenme/transfers/master/data/2020/spanish_primera_division.csv')

#data in 2019
dutch_eredivisie_2019 = pd.read_csv('https://raw.githubusercontent.com/ewenme/transfers/master/data/2019/dutch_eredivisie.csv')
enghlish_championship_2019 = pd.read_csv('https://raw.githubusercontent.com/ewenme/transfers/master/data/2019/english_championship.csv')
english_premier_2019= pd.read_csv('https://raw.githubusercontent.com/ewenme/transfers/master/data/2019/english_premier_league.csv')
french_ligue_1_2019 = pd.read_csv('https://raw.githubusercontent.com/ewenme/transfers/master/data/2019/french_ligue_1.csv')
german_bundesliga_1_2019 = pd.read_csv('https://raw.githubusercontent.com/ewenme/transfers/master/data/2019/german_bundesliga_1.csv')
italian_serie_a_2019 = pd.read_csv('https://raw.githubusercontent.com/ewenme/transfers/master/data/2019/italian_serie_a.csv')
portugese_liga_nos_2019 = pd.read_csv('https://raw.githubusercontent.com/ewenme/transfers/master/data/2019/portugese_liga_nos.csv')
russian_premier_liga_2019 = pd.read_csv('https://raw.githubusercontent.com/ewenme/transfers/master/data/2019/russian_premier_liga.csv')
spanish_primera_division_2019 = pd.read_csv('https://raw.githubusercontent.com/ewenme/transfers/master/data/2019/spanish_primera_division.csv')

# data in 2018
dutch_eredivisie_2018 = pd.read_csv('https://raw.githubusercontent.com/ewenme/transfers/master/data/2018/dutch_eredivisie.csv')
enghlish_championship_2018 = pd.read_csv('https://raw.githubusercontent.com/ewenme/transfers/master/data/2018/english_championship.csv')
english_premier_2018= pd.read_csv('https://raw.githubusercontent.com/ewenme/transfers/master/data/2018/english_premier_league.csv')
french_ligue_1_2018 = pd.read_csv('https://raw.githubusercontent.com/ewenme/transfers/master/data/2018/french_ligue_1.csv')
german_bundesliga_1_2018 = pd.read_csv('https://raw.githubusercontent.com/ewenme/transfers/master/data/2018/german_bundesliga_1.csv')
italian_serie_a_2018 = pd.read_csv('https://raw.githubusercontent.com/ewenme/transfers/master/data/2018/italian_serie_a.csv')
portugese_liga_nos_2018 = pd.read_csv('https://raw.githubusercontent.com/ewenme/transfers/master/data/2018/portugese_liga_nos.csv')
russian_premier_liga_2018 = pd.read_csv('https://raw.githubusercontent.com/ewenme/transfers/master/data/2018/russian_premier_liga.csv')
spanish_primera_division_2018 = pd.read_csv('https://raw.githubusercontent.com/ewenme/transfers/master/data/2018/spanish_primera_division.csv')

#data in 2017
dutch_eredivisie_2017 = pd.read_csv('https://raw.githubusercontent.com/ewenme/transfers/master/data/2017/dutch_eredivisie.csv')
enghlish_championship_2017 = pd.read_csv('https://raw.githubusercontent.com/ewenme/transfers/master/data/2017/english_championship.csv')
english_premier_2017= pd.read_csv('https://raw.githubusercontent.com/ewenme/transfers/master/data/2017/english_premier_league.csv')
french_ligue_1_2017 = pd.read_csv('https://raw.githubusercontent.com/ewenme/transfers/master/data/2017/french_ligue_1.csv')
german_bundesliga_1_2017 = pd.read_csv('https://raw.githubusercontent.com/ewenme/transfers/master/data/2017/german_bundesliga_1.csv')
italian_serie_a_2017 = pd.read_csv('https://raw.githubusercontent.com/ewenme/transfers/master/data/2017/italian_serie_a.csv')
portugese_liga_nos_2017 = pd.read_csv('https://raw.githubusercontent.com/ewenme/transfers/master/data/2017/portugese_liga_nos.csv')
russian_premier_liga_2017 = pd.read_csv('https://raw.githubusercontent.com/ewenme/transfers/master/data/2017/russian_premier_liga.csv')
spanish_primera_division_2017 = pd.read_csv('https://raw.githubusercontent.com/ewenme/transfers/master/data/2017/spanish_primera_division.csv')

#data in 2016
dutch_eredivisie_2016 = pd.read_csv('https://raw.githubusercontent.com/ewenme/transfers/master/data/2016/dutch_eredivisie.csv')
enghlish_championship_2016 = pd.read_csv('https://raw.githubusercontent.com/ewenme/transfers/master/data/2016/english_championship.csv')
english_premier_2016= pd.read_csv('https://raw.githubusercontent.com/ewenme/transfers/master/data/2016/english_premier_league.csv')
french_ligue_1_2016 = pd.read_csv('https://raw.githubusercontent.com/ewenme/transfers/master/data/2016/french_ligue_1.csv')
german_bundesliga_1_2016 = pd.read_csv('https://raw.githubusercontent.com/ewenme/transfers/master/data/2016/german_bundesliga_1.csv')
italian_serie_a_2016 = pd.read_csv('https://raw.githubusercontent.com/ewenme/transfers/master/data/2016/italian_serie_a.csv')
portugese_liga_nos_2016 = pd.read_csv('https://raw.githubusercontent.com/ewenme/transfers/master/data/2016/portugese_liga_nos.csv')
russian_premier_liga_2016 = pd.read_csv('https://raw.githubusercontent.com/ewenme/transfers/master/data/2016/russian_premier_liga.csv')
spanish_primera_division_2016 = pd.read_csv('https://raw.githubusercontent.com/ewenme/transfers/master/data/2016/spanish_primera_division.csv')

#data ion 2015
dutch_eredivisie_2015 = pd.read_csv('https://raw.githubusercontent.com/ewenme/transfers/master/data/2015/dutch_eredivisie.csv')
enghlish_championship_2015 = pd.read_csv('https://raw.githubusercontent.com/ewenme/transfers/master/data/2015/english_championship.csv')
english_premier_2015= pd.read_csv('https://raw.githubusercontent.com/ewenme/transfers/master/data/2015/english_premier_league.csv')
french_ligue_1_2015 = pd.read_csv('https://raw.githubusercontent.com/ewenme/transfers/master/data/2015/french_ligue_1.csv')
german_bundesliga_1_2015 = pd.read_csv('https://raw.githubusercontent.com/ewenme/transfers/master/data/2015/german_bundesliga_1.csv')
italian_serie_a_2015 = pd.read_csv('https://raw.githubusercontent.com/ewenme/transfers/master/data/2015/italian_serie_a.csv')
portugese_liga_nos_2015 = pd.read_csv('https://raw.githubusercontent.com/ewenme/transfers/master/data/2015/portugese_liga_nos.csv')
russian_premier_liga_2015 = pd.read_csv('https://raw.githubusercontent.com/ewenme/transfers/master/data/2015/russian_premier_liga.csv')
spanish_primera_division_2015 = pd.read_csv('https://raw.githubusercontent.com/ewenme/transfers/master/data/2015/spanish_primera_division.csv')

#data in 2014
dutch_eredivisie_2014 = pd.read_csv('https://raw.githubusercontent.com/ewenme/transfers/master/data/2014/dutch_eredivisie.csv')
enghlish_championship_2014 = pd.read_csv('https://raw.githubusercontent.com/ewenme/transfers/master/data/2014/english_championship.csv')
english_premier_2014= pd.read_csv('https://raw.githubusercontent.com/ewenme/transfers/master/data/2014/english_premier_league.csv')
french_ligue_1_2014 = pd.read_csv('https://raw.githubusercontent.com/ewenme/transfers/master/data/2014/french_ligue_1.csv')
german_bundesliga_1_2014 = pd.read_csv('https://raw.githubusercontent.com/ewenme/transfers/master/data/2014/german_bundesliga_1.csv')
italian_serie_a_2014 = pd.read_csv('https://raw.githubusercontent.com/ewenme/transfers/master/data/2014/italian_serie_a.csv')
portugese_liga_nos_2014 = pd.read_csv('https://raw.githubusercontent.com/ewenme/transfers/master/data/2014/portugese_liga_nos.csv')
russian_premier_liga_2014 = pd.read_csv('https://raw.githubusercontent.com/ewenme/transfers/master/data/2014/russian_premier_liga.csv')
spanish_primera_division_2014 = pd.read_csv('https://raw.githubusercontent.com/ewenme/transfers/master/data/2014/spanish_primera_division.csv')

#data in 2013
dutch_eredivisie_2013 = pd.read_csv('https://raw.githubusercontent.com/ewenme/transfers/master/data/2013/dutch_eredivisie.csv')
enghlish_championship_2013 = pd.read_csv('https://raw.githubusercontent.com/ewenme/transfers/master/data/2013/english_championship.csv')
english_premier_2013= pd.read_csv('https://raw.githubusercontent.com/ewenme/transfers/master/data/2013/english_premier_league.csv')
french_ligue_1_2013 = pd.read_csv('https://raw.githubusercontent.com/ewenme/transfers/master/data/2013/french_ligue_1.csv')
german_bundesliga_1_2013 = pd.read_csv('https://raw.githubusercontent.com/ewenme/transfers/master/data/2013/german_bundesliga_1.csv')
italian_serie_a_2013 = pd.read_csv('https://raw.githubusercontent.com/ewenme/transfers/master/data/2013/italian_serie_a.csv')
portugese_liga_nos_2013 = pd.read_csv('https://raw.githubusercontent.com/ewenme/transfers/master/data/2013/portugese_liga_nos.csv')
russian_premier_liga_2013 = pd.read_csv('https://raw.githubusercontent.com/ewenme/transfers/master/data/2013/russian_premier_liga.csv')
spanish_primera_division_2013 = pd.read_csv('https://raw.githubusercontent.com/ewenme/transfers/master/data/2013/spanish_primera_division.csv')

#data in 2012
dutch_eredivisie_2012 = pd.read_csv('https://raw.githubusercontent.com/ewenme/transfers/master/data/2012/dutch_eredivisie.csv')
enghlish_championship_2012 = pd.read_csv('https://raw.githubusercontent.com/ewenme/transfers/master/data/2012/english_championship.csv')
english_premier_2012= pd.read_csv('https://raw.githubusercontent.com/ewenme/transfers/master/data/2012/english_premier_league.csv')
french_ligue_1_2012 = pd.read_csv('https://raw.githubusercontent.com/ewenme/transfers/master/data/2012/french_ligue_1.csv')
german_bundesliga_1_2012 = pd.read_csv('https://raw.githubusercontent.com/ewenme/transfers/master/data/2012/german_bundesliga_1.csv')
italian_serie_a_2012 = pd.read_csv('https://raw.githubusercontent.com/ewenme/transfers/master/data/2012/italian_serie_a.csv')
portugese_liga_nos_2012 = pd.read_csv('https://raw.githubusercontent.com/ewenme/transfers/master/data/2012/portugese_liga_nos.csv')
russian_premier_liga_2012 = pd.read_csv('https://raw.githubusercontent.com/ewenme/transfers/master/data/2012/russian_premier_liga.csv')
spanish_primera_division_2012 = pd.read_csv('https://raw.githubusercontent.com/ewenme/transfers/master/data/2012/spanish_primera_division.csv')

#data in 2011
dutch_eredivisie_2011 = pd.read_csv('https://raw.githubusercontent.com/ewenme/transfers/master/data/2011/dutch_eredivisie.csv')
enghlish_championship_2011 = pd.read_csv('https://raw.githubusercontent.com/ewenme/transfers/master/data/2011/english_championship.csv')
english_premier_2011= pd.read_csv('https://raw.githubusercontent.com/ewenme/transfers/master/data/2011/english_premier_league.csv')
french_ligue_1_2011 = pd.read_csv('https://raw.githubusercontent.com/ewenme/transfers/master/data/2011/french_ligue_1.csv')
german_bundesliga_1_2011 = pd.read_csv('https://raw.githubusercontent.com/ewenme/transfers/master/data/2011/german_bundesliga_1.csv')
italian_serie_a_2011 = pd.read_csv('https://raw.githubusercontent.com/ewenme/transfers/master/data/2011/italian_serie_a.csv')
portugese_liga_nos_2011 = pd.read_csv('https://raw.githubusercontent.com/ewenme/transfers/master/data/2011/portugese_liga_nos.csv')
russian_premier_liga_2011 = pd.read_csv('https://raw.githubusercontent.com/ewenme/transfers/master/data/2011/russian_premier_liga.csv')
spanish_primera_division_2011 = pd.read_csv('https://raw.githubusercontent.com/ewenme/transfers/master/data/2011/spanish_primera_division.csv')

#data in 2010
dutch_eredivisie_2010 = pd.read_csv('https://raw.githubusercontent.com/ewenme/transfers/master/data/2010/dutch_eredivisie.csv')
enghlish_championship_2010 = pd.read_csv('https://raw.githubusercontent.com/ewenme/transfers/master/data/2010/english_championship.csv')
english_premier_2010= pd.read_csv('https://raw.githubusercontent.com/ewenme/transfers/master/data/2010/english_premier_league.csv')
french_ligue_1_2010 = pd.read_csv('https://raw.githubusercontent.com/ewenme/transfers/master/data/2010/french_ligue_1.csv')
german_bundesliga_1_2010 = pd.read_csv('https://raw.githubusercontent.com/ewenme/transfers/master/data/2010/german_bundesliga_1.csv')
italian_serie_a_2010 = pd.read_csv('https://raw.githubusercontent.com/ewenme/transfers/master/data/2010/italian_serie_a.csv')
portugese_liga_nos_2010 = pd.read_csv('https://raw.githubusercontent.com/ewenme/transfers/master/data/2010/portugese_liga_nos.csv')
russian_premier_liga_2010 = pd.read_csv('https://raw.githubusercontent.com/ewenme/transfers/master/data/2010/russian_premier_liga.csv')
spanish_primera_division_2010 = pd.read_csv('https://raw.githubusercontent.com/ewenme/transfers/master/data/2010/spanish_primera_division.csv')


# concat the data
data = pd.concat([dutch_eredivisie_2010, english_premier_2010, french_ligue_1_2010, german_bundesliga_1_2010, italian_serie_a_2010, portugese_liga_nos_2010, russian_premier_liga_2010, spanish_primera_division_2010,
                  dutch_eredivisie_2011, english_premier_2011, french_ligue_1_2011, german_bundesliga_1_2011, italian_serie_a_2011, portugese_liga_nos_2011, russian_premier_liga_2011, spanish_primera_division_2011,
                  dutch_eredivisie_2012, english_premier_2012, french_ligue_1_2012, german_bundesliga_1_2012, italian_serie_a_2012, portugese_liga_nos_2012, russian_premier_liga_2012, spanish_primera_division_2012,
                  dutch_eredivisie_2013, english_premier_2013, french_ligue_1_2013, german_bundesliga_1_2013, italian_serie_a_2013, portugese_liga_nos_2013, russian_premier_liga_2013, spanish_primera_division_2013,
                  dutch_eredivisie_2014, english_premier_2014, french_ligue_1_2014, german_bundesliga_1_2014, italian_serie_a_2014, portugese_liga_nos_2014, russian_premier_liga_2014, spanish_primera_division_2014,
                  dutch_eredivisie_2015, english_premier_2015, french_ligue_1_2015, german_bundesliga_1_2015, italian_serie_a_2015, portugese_liga_nos_2015, russian_premier_liga_2015, spanish_primera_division_2015,
                  dutch_eredivisie_2016, english_premier_2016, french_ligue_1_2016, german_bundesliga_1_2016, italian_serie_a_2016, portugese_liga_nos_2016, russian_premier_liga_2016, spanish_primera_division_2016,
                  dutch_eredivisie_2017, english_premier_2017, french_ligue_1_2017, german_bundesliga_1_2017, italian_serie_a_2017, portugese_liga_nos_2017, russian_premier_liga_2017, spanish_primera_division_2017,
                  dutch_eredivisie_2018, english_premier_2018, french_ligue_1_2018, german_bundesliga_1_2018, italian_serie_a_2018, portugese_liga_nos_2018, russian_premier_liga_2018, spanish_primera_division_2018, 
                  dutch_eredivisie_2019, english_premier_2019, french_ligue_1_2019, german_bundesliga_1_2019, italian_serie_a_2019, portugese_liga_nos_2019, russian_premier_liga_2019, spanish_primera_division_2019,
                  dutch_eredivisie_2020, english_premier_2020, french_ligue_1_2020, german_bundesliga_1_2020, italian_serie_a_2020, portugese_liga_nos_2020, russian_premier_liga_2020, spanish_primera_division_2020],
                  ignore_index = True, axis=0)


################## start of cleaning #########################


# include external data to fix inconsistent names of football clubs
# change directory to where 'football_dataset_final.xlsx' file is located
to_append = pd.read_excel('/football_dataset_final.xlsx')
to_append = to_append.iloc[:, [0, 4, 6]]


to_append.info()


to_append


## focus club_name, change all the inconsistent names into the one unique name
for row_append in to_append.itertuples():
    for row_data in data.itertuples():
        if row_data.club_name == row_append.Team or row_data.club_name == row_append.club_name or row_data.club_name == row_append.club_involved_name:
            data["club_name"]= data["club_name"].replace([row_data.club_name], row_append.Team)
            
        else:
            pass
            


## focus club_involved_name, change all the inconsistent names into the one unique name
for row_append in to_append.itertuples():
    for row_data in data.itertuples():
        if row_data.club_involved_name == row_append.Team or row_data.club_involved_name == row_append.club_name or row_data.club_involved_name == row_append.club_involved_name:
            data["club_involved_name"]= data["club_involved_name"].replace([row_data.club_involved_name], row_append.Team)
            
        else:
            pass


## Change the names of the remaining three teams
# 1
data["club_name"]= data["club_name"].replace(['Parma FC'], 'Parma')
# 2
data["club_name"]= data["club_name"].replace(['Terek Grozny'], 'Akhmat Grozny')
# 3
data["club_name"]= data["club_name"].replace(['Dinamo Moscow'], 'Dynamo Moscow')


# identify all unique tier 1 teams in consideration
nodes = list(data['club_name'].unique())


# create df to not pollute the original data
df = data


# filter out teams that are not tier 1
df = df[df['club_name'].isin(nodes)]

df = df[df['club_involved_name'].isin(nodes)]

# after we have all tier 1 in both club_name and club_involved_name, we can safely
# filter 'out' in transfer_movement out, as the network we are considering
# is undirected
df = df.loc[df['transfer_movement'] == 'in', :]


# data to use 
df


################## end of cleaning #########################


#data for each league in 11 years
data_england = data[data['league_name']=='Premier League']
data_dutch = data[data['league_name']=='Eredivisie']
data_french = data[data['league_name']=='Ligue 1']
data_german = data[data['league_name']=='1 Bundesliga']
data_italian = data[data['league_name']=='Serie A']
data_portugese = data[data['league_name']=='Liga Nos']
data_russian = data[data['league_name']=='Premier Liga']
data_spanish = data[data['league_name']=='Primera Division']


#create name lists 
english_team = list(np.asarray(data_england['club_name'].unique()))
dutch_team = list(np.asarray(data_dutch['club_name'].unique()))
french_team = list(np.asarray(data_french['club_name'].unique()))
german_team = list(np.asarray(data_german['club_name'].unique()))
italian_team = list(np.asarray(data_italian['club_name'].unique()))
portugese_team = list(np.asarray(data_portugese['club_name'].unique()))
russian_team = list(np.asarray(data_russian['club_name'].unique()))
spanish_team = list(np.asarray(data_spanish['club_name'].unique()))


#create list of all club names
all_club_names = list(np.asarray(data['club_name'].unique())) 


#create color list
color_list = []
for n in all_club_names:
    if n in english_team:
        color_list.append('purple')
    elif n in dutch_team:
        color_list.append('yellow')
    elif n in french_team:
        color_list.append('blue')
    elif n in german_team:
        color_list.append('pink')
    elif n in italian_team:
        color_list.append('orange')
    elif n in portugese_team:
        color_list.append('green')
    elif n in russian_team:
        color_list.append('darkred')
    else:
        color_list.append('black')


# pick transfer period and year
df2010s = df.loc[(df['year'] == 2010) & (df['transfer_period'] == 'Summer'), :]

# select only tier 1 teams
df2010s = df2010s[df2010s['club_name'].isin(nodes)]

df2010s = df2010s[df2010s['club_involved_name'].isin(nodes)]

df2010s = df2010s.loc[df2010s['transfer_movement'] == 'in', :]


# create edges
edges = list(zip(df2010s.club_name, df2010s.club_involved_name))
len(edges)


# populate a graph
G10s = nx.Graph()


# add all the possible nodes
G10s.add_nodes_from(nodes)

# add edges 2010 summer
G10s.add_edges_from(edges)


# create a color list
color_list_2010 = []
for n in G10s.nodes():
    if n in english_team:
        color_list_2010.append('tab:blue')
    elif n in dutch_team:
        color_list_2010.append('tab:orange')
    elif n in french_team:
        color_list_2010.append('tab:green')
    elif n in german_team:
        color_list_2010.append('tab:red')
    elif n in italian_team:
        color_list_2010.append('tab:purple')
    elif n in portugese_team:
        color_list_2010.append('tab:brown')
    elif n in russian_team:
        color_list_2010.append('tab:pink')
    else:
        color_list_2010.append('tab:gray')
len(color_list_2010)


fig = plt.figure(figsize=(12, 12))
pos = nx.spring_layout(G10s)
options = {'node_color': color_list_2010,
           'alpha': 0.75,
           'node_size': 400,
           'width': 1,
           'with_labels': False}
nx.draw(G10s,pos = pos, **options)


# pick transfer period and year
df2020w = df.loc[(df['year'] <= 2020) , :]

# select only tier 1 teams
df2020w = df2020w[df2020w['club_name'].isin(nodes)]

df2020w = df2020w[df2020w['club_involved_name'].isin(nodes)]

df2020w = df2020w.loc[df2020w['transfer_movement'] == 'in', :]


df2020w


# create edges
edges = list(zip(df2020w.club_name, df2020w.club_involved_name))
len(edges)


# populate a graph
G20w = nx.Graph()


# add all the possible nodes
G20w.add_nodes_from(nodes)

# add edges 2010 summer
G20w.add_edges_from(edges)


# create a color list
color_list_2020 = []
for n in G20w.nodes():
    if n in english_team:
        color_list_2020.append('tab:blue')
    elif n in dutch_team:
        color_list_2020.append('tab:orange')
    elif n in french_team:
        color_list_2020.append('tab:green')
    elif n in german_team:
        color_list_2020.append('tab:red')
    elif n in italian_team:
        color_list_2020.append('tab:purple')
    elif n in portugese_team:
        color_list_2020.append('tab:brown')
    elif n in russian_team:
        color_list_2020.append('tab:pink')
    else:
        color_list_2020.append('tab:gray')
len(color_list_2020)


fig = plt.figure(figsize=(12, 12))
pos = nx.spring_layout(G20w)
options = {'node_color': color_list_2020,
           'alpha': 0.75,
           'node_size': 400,
           'width': 1,
           'with_labels': False}
nx.draw(G20w,pos = pos, **options)


# definition to extract data
def extract_data(year, summer = 0):
    '''
    param year: year interested (aggregated <= year)
    
    param summer: if = 1, we consider summer transactional period only for year == year 
            but winter and summer for year < year
            
            if = 0 (default), we consider both summer and winter transactional periods, for all years
    return: dataframe with year <= year, and for that year, either winter + summer or just summer
    
    '''
    # pick transfer period and year
    df_i = df.loc[(df['year'] <= year) , :]
    
    if summer == 1:
        df_i = df_i.drop(df_i[(df_i.transfer_period == 'Winter') & (df_i.year == year)].index)
        
    # select only tier 1 teams
    df_i = df_i[df_i['club_name'].isin(nodes)]

    df_i = df_i[df_i['club_involved_name'].isin(nodes)]

    df_i = df_i.loc[df_i['transfer_movement'] == 'in', :]
    
    # return the desire dataframe
    return df_i




# In an randomized network the proportion of teams in each league are: 
e = len(english_team)/num_nodes 
d =len(dutch_team)/num_nodes 
f =len(french_team)/num_nodes 
g =len(german_team)/num_nodes 
i =len(italian_team)/num_nodes 
p =len(portugese_team)/num_nodes 
r =len(russian_team)/num_nodes 
s =len(spanish_team)/num_nodes

# check validity
assert e+d+f+g+i+p+r+s == 1



# the probability of the nodes connecting in the ideal network where nodes are equally likely to 
# connect with one another is 1 = e^2 + d^2 + f^2 +g^2 + i^2 + p^2 + r^2 +s^2 + 2ed + 2ef + 2eg +
# 2ei + 2ep + 2er + 2es + 2df + 2dg+ 2di + 2dp + 2dr + 2ds + 2fg + 2fi + 2fp + 2fr + 2fs +
# 2gi + 2gp + 2gr + 2gs + 2ip + 2ir + 2is + 2pr + 2ps + 2rs

# --+ let's v = 2ed + 2ef + 2eg + 2ei + 2ep + 2er + 2es + 2df + 2dg+ 2di + 2dp + 2dr + 2ds + 
# --+ 2fg + 2fi + 2fp + 2fr + 2fs + 2gi + 2gp + 2gr + 2gs + 2ip + 2ir + 2is + 2pr + 2ps + 2rs

############### if p_het <<<< v then there is a evidence of homophily in the network ###############
############### homophily test ###############
v =  2*e*d + 2*e*f + 2*e*g + 2*e*i + 2*e*p + 2*e*r + 2*e*s + 2*d*f + 2*d*g+ 2*d*i + 2*d*p + 2*d*r + 2*d*s +  2*f*g + 2*f*i + 2*f*p + 2*f*r + 2*f*s + 2*g*i + 2*g*p + 2*g*r + 2*g*s + 2*i*p + 2*i*r + 2*i*s + 2*p*r + 2*p*s + 2*r*s

## hence there is a presense 
assert p_het_10s < v


v


test = e**2 + d**2 + f**2 +g**2 + i**2 + p**2 + r**2 +s**2 
test


# check the validity of the equation
assert v + test == 1


# get the number of all in-in ties
def get_count_dd(link):
    '''
    param: link is the dataframe containing two necessary columns:
           1. source (team that buys a player from target)
           2. tarket (team that sells a player to source)
    return: counts of domestic trades 
    
    '''
    c_dd = 0
    # iterate over one row at the time for the dataframe, and +1 to c_dd if 
    # both columns situated in the same league
    for j in link.itertuples():
        if j.source in english_team and j.target in english_team:
            c_dd += 1
        elif j.source in dutch_team and j.target in dutch_team:
            c_dd += 1
        elif j.source in french_team and j.target in french_team:
            c_dd += 1
        elif j.source in german_team and j.target in german_team:
            c_dd += 1
        elif j.source in italian_team and j.target in italian_team:
            c_dd += 1
        elif j.source in portugese_team and j.target in portugese_team:
            c_dd += 1
        elif j.source in russian_team and j.target in russian_team:
            c_dd += 1
        elif j.source in spanish_team and j.target in spanish_team:
            c_dd += 1
        
        else:
            pass
    # return counts of domestic trades
    return c_dd




# extract the proportion of cross-league trades for each period, assuming links stay conntected
# once they formed
to_store = []
i_i_ties = []
d_d_ties = []
for year in range(2010,2021):
    for i in [1,0]:
        to_use = extract_data(year, summer = i) # extract data one period starting from
                                                # zero to the last period (22)
        graph = nx.Graph() # populate a graph
        edges = list(zip(to_use.club_name, to_use.club_involved_name)) # to put in edges
        graph.add_nodes_from(nodes) # add all the possible nodes
        graph.add_edges_from(edges) # add edges
        l = list(graph.edges()) # get edges with no redundancies
        l = pd.DataFrame(l, columns = ['source', 'target']) # create a DF from list of tuples
        num_all = len(l) # count all the links
        #print('the total number of edges is for year {0}:'.format(year))
        #print(num_all)
        c_dd = get_count_dd(l) # get the total trades within same lagues
        #print('the total number of in-in ties is:')
        #print(c_dd)
        c_ii = num_all - c_dd # get the number of cross-league links
        #print('the total number of in-out ties is:')
        #print(c_ii)
        p_het = c_ii/num_all # calculate the proportion of cross-league links to the total
        to_store.append(p_het) # store this value
        graph.clear() # clear graph 
        
      


to_store


# set font size
plt.rcParams.update({'font.size': 18})


# draw homophilous evolution

# pupulate figure
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(1,1,1)

# create a proportion of cross-league links plot from a real network 
ax.scatter(x = np.arange(0,22), y = to_store, label = 'Real Network', color = 'tab:blue')

# plot a probability of cross-league links from the randomized network 
ax.hlines(y = v, xmin = 0, xmax = 22, label = 'Randomized Network (Probability)', color = 'tab:red', linestyles = 'dashed')

# decorate
ax.vlines(x = 0, ymin = 0.285, ymax = 0.58,  color = 'tab:grey')
ax.vlines(x = 0, ymin = 0.67, ymax = 0.85,  color = 'tab:grey')
ax.vlines(x = 1, ymin = 0.295, ymax = 0.58, color = 'tab:grey')
ax.vlines(x = 1, ymin = 0.67, ymax = 0.85, color = 'tab:grey')
ax.vlines(x = 2, ymin = 0.315, ymax = 0.58, color = 'tab:grey')
ax.vlines(x = 2, ymin = 0.67, ymax = 0.85, color = 'tab:grey')
ax.text(x = -1, y = 0.6, s= 'More Evidence \n of Homophily')
ax.vlines(x = 20, ymin = 0.49, ymax = 0.58 , color = 'tab:grey')
ax.vlines(x = 20, ymin = 0.67, ymax = 0.85, color = 'tab:grey')
ax.vlines(x = 21, ymin = 0.49, ymax = 0.58,  color = 'tab:grey')
ax.vlines(x = 21, ymin = 0.67, ymax = 0.85, color = 'tab:grey')
ax.text(x = 18, y = 0.6, s= 'Less Evidence \n of Homophily')  


# add legend and labels
ax.legend(loc = 'lower right', framealpha = 1 )
ax.set_xlabel('Period')
ax.set_ylabel('Proportion of Cross-League Transactions')
ax.set_title('Comparison Between Randomized and Real Networks')

# remove borders
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.spines['bottom'].set_visible(False)

# save fig
out_f = os.path.join(os.getcwd(), 'fig1.pdf')
plt.savefig(out_f,
            transparent=True,
            bbox_inches='tight',
            pad_inches=0)


# show
plt.show()


def extract_data_to_use(year):
    '''
    param year: year interested (aggregated <= year)
          
    result: dataframe that contains year <= year
    
    '''
    # pick transfer period and year
    df_i = df.loc[(df['year'] == year) , :]
    
    # select only tier 1 teams
    df_i = df_i[df_i['club_name'].isin(nodes)]

    df_i = df_i[df_i['club_involved_name'].isin(nodes)]
    
    # select only transfer_movement == 'in', to make the data more
    # manageable
    df_i = df_i.loc[df_i['transfer_movement'] == 'in', :]
    
    # return the dataframe
    return df_i




# extract the proportion of cross-league trades for each period, assuming links do not stay conntected
# once they formed
to_store = []
i_i_ties = []
d_d_ties = []
for year in range(2010,2021):
    to_use = extract_data_to_use(year) # extract data one period starting from
                                        # zero (2010) to the last period (2020)
    graph = nx.Graph() # populate graph
    edges = list(zip(to_use.club_name, to_use.club_involved_name)) # to add edges in the network
    graph.add_nodes_from(nodes) # add all possible nodes
    graph.add_edges_from(edges) # add edges
    l = list(graph.edges())     # get edges with no redundancies
    l = pd.DataFrame(l, columns = ['source', 'target']) 
    num_all = len(l) # count all links
    #print('the total number of edges is for year {0}:'.format(year))
    #print(num_all)
    c_dd = get_count_dd(l) # get total number of domestic links
    #print('the total number of in-in ties is:')
    #print(c_dd)
    c_ii = num_all - c_dd # get the number of cross-league links
    #print('the total number of in-out ties is:')
    #print(c_ii)
    p_het = c_ii/num_all # calculate the proportion of cross-league links to the total
    to_store.append(p_het) # store the value
    graph.clear() # clear graph


to_store


# draw homophilous evolution assuming links do not stay connected

# populate figure
fig = plt.figure(figsize=(8, 10))
ax = fig.add_subplot(1,1,1)

# create a proportion of cross-league links plot from a real network 
ax.scatter(x = np.arange(2010,2021), y = to_store, label = 'Real Network')

# plot a probability of cross-league links from the randomized network 
ax.hlines(y = v, xmin = 2010, xmax = 2020, label = 'Randomized Network', color = 'tab:red', linestyles = 'dashed')

# decorate
ax.vlines(x = 2010, ymin = 0.3, ymax = 0.58,  color = 'tab:grey')
ax.vlines(x = 2010, ymin = 0.65, ymax = 0.85,  color = 'tab:grey')
ax.vlines(x = 2011, ymin = 0.31, ymax = 0.58, color = 'tab:grey')
ax.vlines(x = 2011, ymin = 0.65, ymax = 0.85, color = 'tab:grey')
ax.vlines(x = 2012, ymin = 0.34, ymax = 0.58, color = 'tab:grey')
ax.vlines(x = 2012, ymin = 0.65, ymax = 0.85, color = 'tab:grey')
ax.text(x = 2010, y = 0.6, s= 'More Evidence \n of Homophily')
ax.vlines(x = 2019, ymin = 0.44, ymax = 0.58 , color = 'tab:grey')
ax.vlines(x = 2019, ymin = 0.67, ymax = 0.85, color = 'tab:grey')
ax.vlines(x = 2020, ymin = 0.44, ymax = 0.58,  color = 'tab:grey')
ax.vlines(x = 2020, ymin = 0.67, ymax = 0.85, color = 'tab:grey')
ax.text(x = 2018, y = 0.6, s= 'Less Evidence \n of Homophily') 

# add legend and labels
plt.legend(loc = 'lower right', framealpha = 1)
ax.set_xlabel('Year')
ax.set_title('Comparison Between Randomized and Real Networks')
ax.set_ylabel('Proportion of Cross-League Transactions')

# remove borders
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.spines['bottom'].set_visible(False)

# save fig
out_f = os.path.join(os.getcwd(), 'fig2.pdf')
plt.savefig(out_f,
            transparent=True,
            bbox_inches='tight',
            pad_inches=0)

# show 
plt.show()


### create a definition to run simulation comparing randomized network to observed network


def assess_hompohily(_g,
                    _p,
                     _n,
                     _c_dd, _c_ii, _c_di,
                     _n_iterations, league):
    '''
    :param _g: an observed network (Numpy matrix)
    :param _p: proportion of teams in the interest league in the network
    :param _n: count of nodes in network
    :param _c_dd: count of interested domestic team - domestic team  ties in the observed network
    :param _c_ii: count of other international team - intertional team ties in the observed network
    :param _c_di: count of domestic team - international team ties in the observed network
    :param _n_iterations: count
    :param league: interested league (String)
    :return: list of cosine similarity scores along with descriptive
             statistics
    '''

    # fix seed
    np.random.seed(000)

    # containers
    # --+ count ties by type (homophilous Vs heterophilous)
    _r_ff, _r_fm, _r_mm = 0, 0, 0
    # --+ distance between observed and simulated data
    _dist = []

    # iterate over simulated distribution of teams
    for iteration in range(_n_iterations):
        # --+ reshuffling the gender of nodes; teams in the interest league is coded as 1
        _reshuffled = np.random.binomial(1, _p, size=n)
        # --+ iterate over each dyad in g
        for i in range(n):
            for j in range(n):
                # --+ sample the tie in the network
                t = [g[i][j]][0]   
                # --+ if tie is present, evaluate whether it's a homphilous or
                # --- heterophilous tie based on the reshuffled network
                if t == 1:
                    h = np.sum([_reshuffled[i], _reshuffled[j]])
                    if h == 2:
                        _r_ff += 1
                    elif h == 1:
                        _r_fm += 1
                    elif h == 0:
                        _r_mm += 1
                    else:
                        pass
                else:
                    pass

        # get the distance between the observed and simulated distribution
        # of ties with respect to three following categories: (i)
        # domestic-domestic; (ii) domestic-international; (iii) intetnational-international.
        _observed = np.array([_c_dd, _c_di, _c_ii])
        _simulated = np.array([_r_ff, _r_fm, _r_mm])
        to_append = pdist([_observed, _simulated], metric='cosine')
        _dist.append(to_append[0])

    # return statistics on the distance between the observed and simulated
    # distributions of ties with respect to type (homophilopus Vs.
    # heterophilous)
    
    _mean, _std, _min, _max = np.mean(_dist), np.std(_dist),\
                              np.min(_dist), np.max(_dist)
    print(80 * '-',
          'Descriptive statistics on observed-simulated ' \
          'distances',
          80 * '-',
          'Mean: get_ipython().run_line_magic("s'", " % np.round(_mean, 2),")
          'Std. dev.: get_ipython().run_line_magic("s'", " % np.round(_std, 2),")
          'Min: get_ipython().run_line_magic("s'", " % np.round(_min, 2),")
          'Max: get_ipython().run_line_magic("s'", " % np.round(_max, 2),")
          end='\n',
          sep='\n')
    # --+ plot the distribution of sum of squares
    fig = plt.figure(figsize=(6, 4))
    ax = fig.add_subplot(1, 1, 1)
    ax.hist(_dist,
            bins=50, cumulative=False, density=False,
            color='orange', alpha=0.5,
            histtype='bar')
    ax.set_xlabel(r'Cosine similarity')
    ax.set_ylabel(r'Number of simulation runs')
    ax.set_title(r'Evidence of Homophily in {}'.format(league))
    # decorate
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['left'].set_visible(False)
    
    # save fig
    out_f = os.path.join(os.getcwd(), '{0}.pdf'.format(league))
    plt.savefig(out_f,
            transparent=True,
            bbox_inches='tight',
            pad_inches=0)
    
    # --+ return objects
    return(_dist, [_mean, _std, _min, _max])




# consider in 2020
df20 = extract_data(2020)
df20
G20.clear()

# generate a network
G20 = nx.Graph()

# create edges
edges = list(zip(df20.club_name, df20.club_involved_name))

# add all the possible nodes
G20.add_nodes_from(nodes)   # so the hyphothesis is that all the transactions happening in teams that have
                             # been in tier 1 leagues are meaningful, in terms of performance evaluation

# add edges 2010 summer
G20.add_edges_from(edges)

len(G20.edges())

# total numbers of nodes
n = 260


# extract list of all transaction and transform it do DF
all_20 = list(G20.edges())

all_20 = pd.DataFrame(all_20, columns = ['club_name', 'club_involved_name'])

total_edges = len(G20.edges())


# consider english teams

# proportion of english teams
p = len(english_team)/n

# --+ all transaction involved premeir league 2020
pm20 = all_20[all_20['club_name'].isin(english_team)]
c_tt_eng20 = len(pm20)

# --+ all transaction involving international teams 2020
c_ii = total_edges - c_tt_eng20

# --+ all transaction involving domestic teams 2020
pm20 = pm20[pm20['club_involved_name'].isin(english_team)]
c_dd = len(pm20)

# --+ all transaction involving domestic and international teams 2020
c_di = c_tt_eng20 - c_dd

# transform network to NumpyMatrix
g = nx.to_numpy_matrix(G20)
g = np.array(g)

# get the cosine similarity
outcome = assess_hompohily(_g=g, _p=p, _n=n,
                           _c_ii=c_ii, _c_dd=c_dd, _c_di=c_di,
                           _n_iterations=1000, league = 'the Premier League 2020')


# consider spanish teams

# proportion of english teams
p = len(spanish_team)/n

# --+ all transaction involved La Liga 2020
sn20 = all_20[all_20['club_name'].isin(spanish_team)]
c_tt_sn20 = len(sn20)

# --+ all transaction involving international teams 2020
c_ii = total_edges - c_tt_sn20

# --+ all transaction involving domestic teams 2020
sn20 = sn20[sn20['club_involved_name'].isin(spanish_team)]
c_dd = len(sn20)

# --+ all transaction involving domestic and international teams 2020
c_di = c_tt_sn20 - c_dd

# transform network to NumpyMatrix
g = nx.to_numpy_matrix(G20)
g = np.array(g)

# get the cosine similarity
outcome = assess_hompohily(_g=g, _p=p, _n=n,
                           _c_ii=c_ii, _c_dd=c_dd, _c_di=c_di,
                           _n_iterations=1000, league = 'La Liga 2020')


# consider portugese teams

# proportion of english teams
p = len(portugese_team)/n

# --+ all transaction involved La Liga 2020
p20 = all_20[all_20['club_name'].isin(portugese_team)]
c_tt_p20 = len(p20)

# --+ all transaction involving international teams 2020
c_ii = total_edges - c_tt_p20

# --+ all transaction involving domestic teams 2020
p20 = p20[p20['club_involved_name'].isin(portugese_team)]
c_dd = len(p20)

# --+ all transaction involving domestic and international teams 2020
c_di = c_tt_p20 - c_dd

# transform network to NumpyMatrix
g = nx.to_numpy_matrix(G20)
g = np.array(g)

# get the cosine similarity
outcome = assess_hompohily(_g=g, _p=p, _n=n,
                           _c_ii=c_ii, _c_dd=c_dd, _c_di=c_di,
                           _n_iterations=1000, league = 'the Primeira Liga 2020')


# consider italian teams

# proportion of english teams
p = len(italian_team)/n

# --+ all transaction involved La Liga 2020
it20 = all_20[all_20['club_name'].isin(italian_team)]
c_tt_it20 = len(it20)

# --+ all transaction involving international teams 2020
c_ii = total_edges - c_tt_it20

# --+ all transaction involving domestic teams 2020
it20 = it20[it20['club_involved_name'].isin(italian_team)]
c_dd = len(it20)

# --+ all transaction involving domestic and international teams 2020
c_di = c_tt_it20 - c_dd

# transform network to NumpyMatrix
g = nx.to_numpy_matrix(G20)
g = np.array(g)

# get the cosine similarity
outcome = assess_hompohily(_g=g, _p=p, _n=n,
                           _c_ii=c_ii, _c_dd=c_dd, _c_di=c_di,
                           _n_iterations=1000, league = 'Serie A 2020')


# consider russian teams

# proportion of english teams
p = len(russian_team)/n

# --+ all transaction involved La Liga 2020
rs20 = all_20[all_20['club_name'].isin(russian_team)]
c_tt_rs20 = len(rs20)

# --+ all transaction involving international teams 2020
c_ii = total_edges - c_tt_rs20

# --+ all transaction involving domestic teams 2020
rs20 = rs20[rs20['club_involved_name'].isin(russian_team)]
c_dd = len(rs20)

# --+ all transaction involving domestic and international teams 2020
c_di = c_tt_rs20 - c_dd

# transform network to NumpyMatrix
g = nx.to_numpy_matrix(G20)
g = np.array(g)

# get the cosine similarity
outcome = assess_hompohily(_g=g, _p=p, _n=n,
                           _c_ii=c_ii, _c_dd=c_dd, _c_di=c_di,
                           _n_iterations=1000, league = 'the Russian Premier League 2020')


# consider ducth teams

# proportion of english teams
p = len(dutch_team)/n

# --+ all transaction involved La Liga 2020
d20 = all_20[all_20['club_name'].isin(dutch_team)]
c_tt_d20 = len(d20)

# --+ all transaction involving international teams 2020
c_ii = total_edges - c_tt_d20

# --+ all transaction involving domestic teams 2020
d20 = d20[d20['club_involved_name'].isin(dutch_team)]
c_dd = len(d20)

# --+ all transaction involving domestic and international teams 2020
c_di = c_tt_d20 - c_dd

# transform network to NumpyMatrix
g = nx.to_numpy_matrix(G20)
g = np.array(g)

# get the cosine similarity
outcome = assess_hompohily(_g=g, _p=p, _n=n,
                           _c_ii=c_ii, _c_dd=c_dd, _c_di=c_di,
                           _n_iterations=1000, league = 'Eredivisie 2020')


# consider french teams

# proportion of english teams
p = len(french_team)/n

# --+ all transaction involved La Liga 2020
f20 = all_20[all_20['club_name'].isin(french_team)]
c_tt_f20 = len(f20)

# --+ all transaction involving international teams 2020
c_ii = total_edges - c_tt_f20

# --+ all transaction involving domestic teams 2020
f20 = f20[f20['club_involved_name'].isin(french_team)]
c_dd = len(f20)

# --+ all transaction involving domestic and international teams 2020
c_di = c_tt_f20 - c_dd

# transform network to NumpyMatrix
g = nx.to_numpy_matrix(G20)
g = np.array(g)

# get the cosine similarity
outcome = assess_hompohily(_g=g, _p=p, _n=n,
                           _c_ii=c_ii, _c_dd=c_dd, _c_di=c_di,
                           _n_iterations=1000, league = 'France Ligue 1')


# consider german teams

# proportion of english teams
p = len(german_team)/n

# --+ all transaction involved La Liga 2020
g20 = all_20[all_20['club_name'].isin(german_team)]
c_tt_g20 = len(g20)

# --+ all transaction involving international teams 2020
c_ii = total_edges - c_tt_g20

# --+ all transaction involving domestic teams 2020
g20 = g20[g20['club_involved_name'].isin(german_team)]
c_dd = len(g20)

# --+ all transaction involving domestic and international teams 2020
c_di = c_tt_g20 - c_dd

# transform network to NumpyMatrix
g = nx.to_numpy_matrix(G20)
g = np.array(g)

# get the cosine similarity
outcome = assess_hompohily(_g=g, _p=p, _n=n,
                           _c_ii=c_ii, _c_dd=c_dd, _c_di=c_di,
                           _n_iterations=1000, league = 'Bundesliga 2020')


# import datetime to deal with data
import datetime 


# load additional data to analyse performance
# change directory to where 'tier1_team_performance.xlsx' file is located
pfm = pd.read_excel('/tier1_team_performance.xlsx')


# clean data
pfm["season"]= pfm["season"].replace(['2019/20',
 '2018/19',
 '2017/18',
 '2016/17',
 '2015/16',
 '2014/15',
 '2013/14',
 '2012/13',
 '2011/12',
 '2010/11',
 '2014/16',
 datetime.datetime(2011, 12, 1, 0, 0),
 datetime.datetime(2010, 11, 1, 0, 0)], [2019, 2018, 2017, 2016, 2015, 2014, 2013, 2012, 2011, 2010, 2014, 2011, 2010] )



# check --> we need 2010 --> 2019 ######################## Very important
season = list(pfm['season'].unique())
season


len(pfm['season'].unique())


# this is important, we want 2010 --> 2019, not the other way around
season.reverse()
season


# check --> we need 2010 --> 2019 ######################## Very important
season


# prepare data
top_position = np.arange(1,11)
bottom_position = np.arange(10,21)
season = list(pfm['season'].unique())


# separate data into two cetegories: 1.performing teams and 2.unperforming teams
pfm_top = pfm[pfm['position'].isin(top_position)]
pfm_bottom = pfm[pfm['position'].isin(bottom_position)]


# find average homophily index for top teams each year
h_i_t = []
for year in season:
    to_use = []
    df = extract_data(year) # extact data 
    team = pfm_top.loc[pfm_top['season'] == year, :] # extract year interested
    team = team['team'].unique() # identify all unique teams
    G = nx.Graph() # populate graph
    edges = list(zip(df.club_name, df.club_involved_name))
    G.add_nodes_from(nodes) 
    G.add_edges_from(edges)
    for team in team:
        list_t = list(G.edges(team))
        list_t = pd.DataFrame(list_t,columns = ['source', 'target'] )
        c_t = len(list_t) # count total number of link
        c_dd = get_count_dd(list_t) # get the domestic links
        if c_t == 0: # ignore team that are not in the dataset
            pass
        else:
            homo_index = c_dd/c_t # calculate homophily index
            to_use.append(homo_index)
    
    to_append = np.mean(to_use) # average the homophily index for the year
    h_i_t.append(to_append)
    G.clear()
            


h_i_t


# find average homophily index for unperforming teams each year
h_i_b = []
for year in season:
    to_use = []
    df = extract_data(year)
    team = pfm_bottom.loc[pfm_bottom['season'] == year, :]
    team = team['team'].unique()
    G = nx.Graph()
    edges = list(zip(df.club_name, df.club_involved_name))
    G.add_nodes_from(nodes)
    G.add_edges_from(edges)
    for team in team:
        list_t = list(G.edges(team))
        list_t = pd.DataFrame(list_t,columns = ['source', 'target'] )
        c_t = len(list_t)
        c_dd = get_count_dd(list_t)
        if c_t == 0:
            pass
        else:
            homo_index = c_dd/c_t
            to_use.append(homo_index)
    
    to_append = np.mean(to_use)
    h_i_b.append(to_append)
    G.clear()
    



h_i_b


# prepare data to plot

# multiply homophily index by 100 to make it a percentage form
## --+ top 
h_i_t_pct = np.array(h_i_t)*100
## --+ low
h_i_b_pct = np.array(h_i_b)*100

# average a winning percentage for top teams yearly basis
w_p_t = pfm_top.groupby('season')['win_percentage'].mean()
w_p_t_pct = np.array(w_p_t)*100

# average a winning percentage for bottom teams yearly basis
w_p_b = pfm_bottom.groupby('season')['win_percentage'].mean()
w_p_b_pct = np.array(w_p_b)*100



## plot changes in performances and homophily indexes for top 10 performing teams and bottom
# 10 performing teams, on average, on a yearly-basis

# populate axes and figure
fig = plt.figure(figsize=(15, 10))
ax = fig.add_subplot(1, 2, 1)
ax1 = fig.add_subplot(1, 2, 2)

# plot performance through time line graphs for top and bottom teams
line = ax.plot(season,  w_p_t_pct, color = 'tab:gray', label = 'Winning Percentage') # top
line1 = ax1.plot( season,  w_p_b_pct, color = 'tab:gray') # bottom

# set y range the same, to make both comparible
ax.set_ylim(20,50)
ax1.set_ylim(20,50) 

# create a second y axis for both ax and ax1, with same x axis respectively
#--+ plot homophily index through time  
ax2 = ax.twinx()
scatter2 = ax2.scatter(x = season, y = h_i_t_pct, color = 'tab:blue', label = 'Homophily') # top
ax3 = ax1.twinx()
scatter3 = ax3.scatter(x = season, y = h_i_b_pct, color = 'tab:blue')

# set y range the same, to make both comparible
ax2.set_ylim(60,90)
ax3.set_ylim(60,90)


# set axes names and titles
ax.set_xlabel('Year')
ax.set_ylabel('Average Winning Mathces (\get_ipython().run_line_magic(")',", " color = 'tab:gray')")
ax.set_title('Top Teams')
ax1.set_xlabel('Year')
ax3.set_ylabel('Homophily Index(\get_ipython().run_line_magic(")',", " color = 'tab:blue')")
ax1.set_title('Bottom Teams')

# set ticks
ax2.set_yticks([])
ax1.set_yticks([])

# remove borders
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.spines['left'].set_visible(False)
ax2.spines['bottom'].set_visible(False)
ax2.spines['left'].set_visible(False)
ax2.spines['right'].set_visible(False)
ax2.spines['top'].set_visible(False)
ax1.spines['right'].set_visible(False)
ax1.spines['top'].set_visible(False)
ax1.spines['bottom'].set_visible(False)
ax1.spines['left'].set_visible(False)
ax3.spines['bottom'].set_visible(False)
ax3.spines['left'].set_visible(False)
ax3.spines['right'].set_visible(False)
ax3.spines['top'].set_visible(False)

# set figure name
fig.suptitle('Comparison of Average Homophily \n and Performance Across Years')

season = list(pfm['season'].unique())

# set legend
fig.legend(frameon= True)

# save fig
out_f = os.path.join(os.getcwd(), 'fig3.pdf')
plt.savefig(out_f,
            transparent=True,
            bbox_inches='tight',
            pad_inches=0)

# show
plt.show()    


# import important libraries for regression
import statsmodels.api as sm
from statsmodels.sandbox.regression.predstd import wls_prediction_std


## conduct a regression on the top performing teams


pfm_top.info()


########## check that it is still in increasing ############
season


# if it is 
season.reverse()


season


# identify teams that are not in our original dataset
h_i_t = []
team_not_use = []
for year in season:
    to_use = []
    df = extract_data(year)
    team = pfm_top.loc[pfm_top['season'] == year, :]
    team = team['team'].unique()
    G = nx.Graph()
    edges = list(zip(df.club_name, df.club_involved_name))
    G.add_nodes_from(nodes)
    G.add_edges_from(edges)
    for team in team:
        list_t = list(G.edges(team))
        list_t = pd.DataFrame(list_t,columns = ['source', 'target'] )
        c_t = len(list_t)
        c_dd = get_count_dd(list_t)
        if c_t == 0:
            team_not_use.append(team)  # append teams not appearing in the data
            
        else:
            homo_index = c_dd/c_t
            h_i_t.append(homo_index)
    
    
    
    G.clear()
    
    


# remove those teams that are out in our original dataset
pfm_top_new = pfm_top[~pfm_top['team'].isin(team_not_use)]


pfm_top_new


# find average homophily index for all top teams each year and concat them to winning_percentage
# to further analysis
h_i_t = []
for year in season:
    to_use = []
    df = extract_data(year)
    team = pfm_top_new.loc[pfm_top_new['season'] == year, :]
    team = team['team'].unique()
    w_p  = pfm_top_new.loc[pfm_top_new['season'] == year, :]
    G = nx.Graph()
    edges = list(zip(df.club_name, df.club_involved_name))
    G.add_nodes_from(nodes)
    G.add_edges_from(edges)
    for team in team:
        list_t = list(G.edges(team))
        list_t = pd.DataFrame(list_t,columns = ['source', 'target'] )
        c_t = len(list_t)
        c_dd = get_count_dd(list_t)
        if c_t == 0:
            pass
            
        else:
            homo_index = c_dd/c_t
            win = list(w_p.loc[w_p['team'] == team, 'win_percentage'])
            win = win[0]
            h_i_t.append((homo_index, team, year,win ))
            
    
    
    
    G.clear()


# create a dataframe contanning homophily index and winning_percentage
pfm_top_new = pd.DataFrame(h_i_t, columns = ['Homophily Index', 'team', 'year', 'win_percentage'])
pfm_top_new


# define the regression model
m_0 = sm.OLS(endog=pfm_top_new['win_percentage'],
             exog=pfm_top_new['Homophily Index'])

# fit the model
m_0_res = m_0.fit()

print(m_0_res.summary())


# use the Newey-West to account for possible heteroskedasticity and autocorrelation
res = sm.stats.sandwich_covariance.cov_hac(m_0_res)
res


## conduct a regression on the bottom performing teams


pfm_bottom.info()


# identify teams that are not in our original dataset
h_i_b = []
team_not_use = []
for year in season:
    to_use = []
    df = extract_data(year)
    team = pfm_bottom.loc[pfm_bottom['season'] == year, :]
    team = team['team'].unique()
    G = nx.Graph()
    edges = list(zip(df.club_name, df.club_involved_name))
    G.add_nodes_from(nodes)
    G.add_edges_from(edges)
    for team in team:
        list_t = list(G.edges(team))
        list_t = pd.DataFrame(list_t,columns = ['source', 'target'] )
        c_t = len(list_t)
        c_dd = get_count_dd(list_t)
        if c_t == 0:
            team_not_use.append(team)
        else:
            homo_index = c_dd/c_t
            h_i_b.append(homo_index)
    
    
    
    G.clear()
    
    


len(team_not_use)


# remove rows with teams that do not appear in our original dataset
pfm_bottom_new = pfm_bottom[~pfm_bottom['team'].isin(team_not_use)]


len(pfm_bottom_new)


# find average homophily index for all bottom teams each year and concat them to winning_percentage
# to further analysis
h_i_b = []
for year in season:
    to_use = []
    df = extract_data(year)
    team = pfm_bottom_new.loc[pfm_bottom_new['season'] == year, :]
    team = team['team'].unique()
    w_p  = pfm_bottom_new.loc[pfm_bottom_new['season'] == year, :]
    G = nx.Graph()
    edges = list(zip(df.club_name, df.club_involved_name))
    G.add_nodes_from(nodes)
    G.add_edges_from(edges)
    for team in team:
        list_t = list(G.edges(team))
        list_t = pd.DataFrame(list_t,columns = ['source', 'target'] )
        c_t = len(list_t)
        c_dd = get_count_dd(list_t)
        if c_t == 0:
            pass
        else:
            homo_index = c_dd/c_t
            win = list(w_p.loc[w_p['team'] == team, 'win_percentage'])
            win = win[0]
            h_i_b.append((homo_index, team, year,win ))
    
    
    
    G.clear()
    
    


# create a dataframe to use in the regression analysis
pfm_bottom_new = pd.DataFrame(h_i_b, columns = ['Homophily Index', 'team', 'year', 'win_percentage'])
pfm_bottom_new


# define the regression model
m_1 = sm.OLS(endog=pfm_bottom_new['win_percentage'],
             exog=pfm_bottom_new['Homophily Index'])

# fit the model
m_1_res = m_1.fit()

print(m_1_res.summary())


# use the Newey-West to account for possible heteroskedasticity and autocorrelation
res = sm.stats.sandwich_covariance.cov_hac(m_1_res)
res


## regression for all data


# create a list containing all teams in the original dataset
teams = list(data['club_name'].unique())
len(teams)


# filter out alien teams
pfm_all = pfm[pfm['team'].isin(teams)]


pfm


pfm_all = pfm[~pfm['team'].isin(team_not_use)]


pfm_all = pfm


pfm_all


# find average homophily index for all teams each year
h_i_all = []
team_not_use = []
for year in season:
    to_use = []
    df = extract_data(year)
    team = pfm_all.loc[pfm_all['season'] == year, :]
    team = team['team'].unique()
    w_p  = pfm_all.loc[pfm_all['season'] == year, :]
    G = nx.Graph()
    edges = list(zip(df.club_name, df.club_involved_name))
    G.add_nodes_from(nodes)
    G.add_edges_from(edges)
    for team in team:
        
        list_t = list(G.edges(team))
        list_t = pd.DataFrame(list_t,columns = ['source', 'target'] )
        c_t = len(list_t)
        c_dd = get_count_dd(list_t)
        if c_t == 0:
            team_not_use.append(team)
        else:
            homo_index = c_dd/c_t
            win = list(w_p.loc[w_p['team'] == team, 'win_percentage'])
            win = win[0]
            
            h_i_all.append((homo_index, team, year,win ))
    
    
    G.clear()
    
    


# create a dataframe to be used in the regression analysis 
pfm_all_new = pd.DataFrame(h_i_all, columns = ['Homophily Index', 'team', 'year', 'win_percentage'])
pfm_all_new


# define the regression model
m_2 = sm.OLS(endog=pfm_all_new['win_percentage'],
             exog=pfm_all_new['Homophily Index'])

# fit the model
m_2_res = m_2.fit()

print(m_2_res.summary())


# use the Newey-West to account for possible heteroskedasticity and autocorrelation
res = sm.stats.sandwich_covariance.cov_hac(m_2_res)
res
