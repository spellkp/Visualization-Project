"""
Created on Sun Oct 13 18:51:14 2019

@author: kpsspell
"""

import os
import csv
import pandas as pd


os.chdir('/Users/kpsspell/Desktop/VisualizationProject/mergedData')
os.getcwd()

# Year 2015

y2015 = pd.read_csv('merged2015.csv', encoding = 'unicode_escape')
y2015.head()
y2015.shape

percent_missing15 = y2015.isnull().sum() * 100 / len(y2015)
missing_value_y2015 = pd.DataFrame({'column_name': y2015.columns,
                                 'percent_missing': percent_missing})

list(y2015.columns.values)
y2015['fatals'].unique()

# Year 2016

y2016 = pd.read_csv('merged2016.csv', encoding = 'unicode_escape')
y2016.head()
y2016.shape

percent_missing16 = y2016.isnull().sum() * 100 / len(y2016)
missing_value_y2016 = pd.DataFrame({'column_name': y2016.columns,
                                 'percent_missing': percent_missing16})

# Year 2017

y2017 = pd.read_csv('merged2017.csv', encoding = 'unicode_escape')
y2017.head()
y2017.shape

percent_missing17 = y2017.isnull().sum() * 100 / len(y2017)
missing_value_y2017 = pd.DataFrame({'column_name': y2017.columns,
                                 'percent_missing': percent_missing17})

#all_years = [y2015, y2016, y2017]
vertical_stack = pd.concat([y2015, y2016, y2017], axis=0)

#removing rows
clean_data = vertical_stack.drop(columns = [ 'VE_FORMS', 'PVH_INVL',  'PEDS',  'PERNOTMVIT', 'PERMVIT', 'SP_JUR', 'HARM_EV', 'MAN_COLL', 'REL_ROAD',  'SCH_BUS',  'RAIL', 'ARR_HOUR',  'ARR_MIN',  'HOSP_HR',  'HOSP_MN', 'VEH_NO',  'PER_NO', 'STR_VEH', 'MAKE',  'MAK_MOD',  'BODY_TYP', 'NOT_HOUR',  'NOT_MIN', 'CF1',  'CF2',  'CF3', 'RELJCT1',  'RELJCT2', 'ROLLOVER', 'MOD_YEAR', 'IMPACT1',  'FIRE_EXP',  'PER_TYP',  'INJ_SEV',  'SEAT_POS', 'AIR_BAG', 'REST_USE', 'REST_MIS',  'EJECTION',  'EJ_PATH',  'EXTRICAT', 'ALC_DET', 'ALC_STATUS', 'ATST_TYP',  'ALC_RES',  'DRUG_DET',  'DSTATUS',  'DRUGTST1',  'DRUGTST2',  'DRUGTST3',  'DRUGRES1',  'DRUGRES2',  'DRUGRES3', 'HOSPITAL',  'DOA',  'DEATH_DA',  'DEATH_MO',  'DEATH_YR',  'DEATH_HR',  'DEATH_MN',  'DEATH_TM',  'LAG_HRS',  'LAG_MINS', 'HIT_RUN',  'OWNER',  'MODEL',  'VIN',  'VIN_1',  'VIN_2',  'VIN_3',  'VIN_4',  'VIN_5',  'VIN_6',  'VIN_7',  'VIN_8',  'VIN_9',  'VIN_10',  'VIN_11',   'WORK_INJ',  'TOW_VEH',  'SPEC_USE',  'EMER_USE',  'REG_STAT',  'LOCATION',  'UNITTYPE', 'VIN_12', 'J_KNIFE',  'MCARR_I1',  'MCARR_I2',  'MCARR_ID',  'GVWR', 'CARGO_BT',  'HAZ_INV', 'HAZ_PLAC',  'HAZ_ID',  'HAZ_CNO',  'HAZ_REL', 'BUS_USE',  'TRAV_SP',  'UNDERIDE',  'ROLINLOC', 'DEFORMED',  'TOWED',  'M_HARM',  'DR_PRES',  'L_STATUS',  'L_TYPE',  'CDL_STAT', 'L_ENDORS',  'L_COMPL',  'L_RESTRI',  'DR_HGT',  'DR_WGT',  'DR_ZIP',  'PREV_ACC',  'PREV_SUS',  'PREV_DWI',  'PREV_SPD',  'PREV_OTH',  'FIRST_MO',  'FIRST_YR',  'LAST_MO',  'LAST_YR', 'VTRAFWAY',  'VNUM_LAN',  'VSPD_LIM',  'VALIGN',  'VPROFILE',  'VPAVETYP',  'VSURCOND',  'VTRAFCON',  'VTCONT_F',  'V_CONFIG', 'VEH_SC1',  'VEH_SC2', 'DR_SF1',  'DR_SF2',  'DR_SF3',  'DR_SF4', 'P_CRASH1',  'P_CRASH2',  'P_CRASH3',  'PCRASH4',  'PCRASH5', 'ACC_TYPE'])
#removing more columns that included identification numbers 
clean_data1 = clean_data.drop(columns = ['TWAY_ID', 'TWAY_ID2', 'ST_CASE','TRLR1VIN', 'TRLR2VIN', 'TRLR3VIN', 'MILEPT'])

#list(clean_data.columns.values)
list(clean_data1.columns.values)

#exporting clean data to csv
#export_data = clean_data.to_csv('/Users/kpsspell/Desktop/VisualizationProject/clean_data.csv')
export_data1 = clean_data1.to_csv('/Users/kpsspell/Desktop/VisualizationProject/clean_data1.csv')

#printing how many columns we will have to model with
columns1_update = list(clean_data1.columns)
level_counts = []
for i in columns1_update:
   levels = clean_data1[i].nunique()
   level_counts.append(levels)
sum(level_counts)
