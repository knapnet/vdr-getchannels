#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Versione Originale vdr-getchannels 0.7.0
#__author__     = "Armando Basile"
#__copyright__  = "Copyright 2011-2015"
#__credits__    = ["Mona66, KingOfSat"]
#__license__    = "GPL"
#__relase__     = "vdr-getchannels"
#__version__    = "0.7.0"
#__daterel__    = "2015-03-02"
#__maintainer__ = "Armando Basile"
#__email__      = "hmandevteam@gmail.com"

# Versione Modificata vdr-getchannels 0.7.2
__Mod_author__     = "Guido Cordaro"
__Mod_copyright__  = "Copyright 2016"
__Mod_credits__    = ["Armando Basile, Mona66, grazymax, ibibah, KingOfSat"]
__Mod_license__    = "GPL"
__Mod_relase__     = "vdr-getchannels"
__Mod_version__    = "0.7.2"
__Mod_daterel__    = "2016-16-02"
__Mod_maintainer__ = "Guido Cordaro"
__Mod_email__      = "guido.cordaro@gmail.com"



#import sys
import urllib
import string

import os.path
import argparse




# application parameters
class app_params:

    sat_list            = {'4.8E'                 : 'http://it.kingofsat.net/tv-4.8E.php',
                           '7.0E'                 : 'http://it.kingofsat.net/tv-7.0E.php',
                           '9.0E'                 : 'http://it.kingofsat.net/tv-9.0E.php',
                           '13.0E'                : 'http://it.kingofsat.net/tv-13.0E.php',
                           '16.0E'                : 'http://it.kingofsat.net/tv-16.0E.php',
                           '19.2E'                : 'http://it.kingofsat.net/tv-19.2E.php',
                           '23.5E'                : 'http://it.kingofsat.net/tv-23.5E.php',
                           '25.5E'                : 'http://it.kingofsat.net/tv-25.5E.php',
                           '26.0E'                : 'http://it.kingofsat.net/tv-26.0E.php',
                           '28.2E'                : 'http://it.kingofsat.net/tv-28.2E.php',
                           '30.5E'                : 'http://it.kingofsat.net/tv-30.5E.php',
                           '39.0E'                : 'http://it.kingofsat.net/tv-39.0E.php',
                           '42.0E'                : 'http://it.kingofsat.net/tv-42.0E.php',
                           '45.0E'                : 'http://it.kingofsat.net/tv-45.0E.php',
                           '68.5E'                : 'http://it.kingofsat.net/tv-68.5E.php',
                           '75.0E'                : 'http://it.kingofsat.net/tv-75.0E.php',
                           '0.8W'                 : 'http://it.kingofsat.net/tv-0.8W.php',
                           '4.0W'                 : 'http://it.kingofsat.net/tv-4.0W.php',
                           '5.0W'                 : 'http://it.kingofsat.net/tv-5.0W.php',
                           '7.0W'                 : 'http://it.kingofsat.net/tv-7.0W.php',
                           '8.0W'                 : 'http://it.kingofsat.net/tv-8.0W.php',
                           '12.5W'                : 'http://it.kingofsat.net/tv-12.5W.php',
                           '15.0W'                : 'http://it.kingofsat.net/tv-15.0W.php',
                           '24.5W'                : 'http://it.kingofsat.net/tv-24.5W.php',
                           '30.0W'                : 'http://it.kingofsat.net/tv-30.0W.php'}


    sat_id              = {'4.8E'                 : '4.8',
                           '7.0E'                 : '7.0',
                           '9.0E'                 : '9.0',
                           '13.0E'                : '13.0',
                           '16.0E'                : '16.0',
                           '19.2E'                : '19.2',
                           '23.5E'                : '23.5',
                           '25.5E'                : '25.5',
                           '26.0E'                : '26.0',
                           '28.2E'                : '28.2',
                           '30.5E'                : '30.5',
                           '39.0E'                : '39.0',
                           '42.0E'                : '42.0',
                           '45.0E'                : '45.0',
                           '68.5E'                : '68.5',
                           '75.0E'                : '75.0',
                           '0.8W'                 : '0.8',
                           '4.0W'                 : '4.0',
                           '5.0W'                 : '5.0',
                           '7.0W'                 : '7.0',
                           '8.0W'                 : '8.0',
                           '12.5W'                : '12.5',
                           '15.0W'                : '15.0',
                           '24.5W'                : '24.5',
                           '30.0W'                : '30.0'}


#                         - Nome Pacchetto        - CAID   - Paese - Posizione Satellite - Numero di Canali - Ultimo Aggiornamento
    caid_bouquets       = {'ABS-CBN'              : '0604', #Filipiny 5.0°W 0 15-02-2016 08:01:15 
                           'Akta'                 : '0500,0B00', #Rumunia 4.8°E 0 15-02-2016 08:01:06 
                           'AlJazeeraSport'       : '500', #Włochy 13.0°E / 25.5°E / 7.0°W 10 15-02-2016 08:00:18
                           'Austriasat'           : '0D05', #Austria 19.2°E 36 15-02-2016 08:00:26 
                           'Bis'                  : '0500,0100', #Francja 13.0°E / 19.2°E / 5.0°W 130 15-02-2016 07:59:57 
                           'Boom'                 : '0929', #Rumunia 4.0°W 0 15-02-2016 08:01:05 
                           'Bulsatcom'            : '0604,5501,5581', #Bułgaria 39.0°E 110 15-02-2016 08:01:03 
                           'CSLink'               : '0D0F,0666', #Czechy 19.2°E / 23.5°E 24 15-02-2016 08:00:31 
                           'CanalDigitaal'        : '0100,0622', #Holandia 19.2°E / 23.5°E 130 15-02-2016 08:00:30 
                           'CanalDigitalNordic'   : '0B00', #Szwecja 0.8°W 313 15-02-2016 07:59:39 
                           'CanalSat'             : '0500,0100,1811', #Francja 19.2°E 268 15-02-2016 08:00:40 
                           'ChelloMulticanal'     : '1802', #Hiszpania 24.5°W 16 15-02-2016 08:00:43 
                           'CyfrowyPolsat'        : '1803,1861', #Polska 13.0°E 318 15-02-2016 08:00:10 
                           'D-Smart'              : '092B', #Turcja 42.0°E 111 15-02-2016 08:01:13 
                           'DMC'                  : '0D04', #Holandia 15.0°W 34 15-02-2016 08:00:21 
                           'DigitAlb'             : '0B00', #Albania 16.0°E 86 15-02-2016 08:00:22 
                           'Digital+(Astra)'      : '0100,1810', #Hiszpania 19.2°E / 30.0°W 217 15-02-2016 08:17:53 
                           'Digital+(Hispasat)'   : '1810', #Hiszpania 30.0°W 133 15-02-2016 08:00:55 
                           'Digitürk'             : '0D00,0664', #Turcja 7.0°E / 42.0°E 343 15-02-2016 08:01:21 
                           'DolceTV'              : '092F', #Rumunia 39.0°E 138 15-02-2016 08:01:04 
                           'FocusSat'             : '0B02', #Rumunia 0.8°W 267 15-02-2016 07:59:46 
                           'Fransat'              : '0500', #Francja 5.0°W 65 15-02-2016 08:01:16 
                           'HD+'                  : '1830', #Niemcy 19.2°E 24 15-02-2016 08:00:41 
                           'HelloHD'              : '0BAA', #Węgry 9.0°E / 13.0°E / 16.0°E 0 15-02-2016 08:01:25 
                           'KabelDeutschland'     : '1834,1722,09C7', #Niemcy 19.2°E / 23.5°E 2 15-02-2016 08:00:31 
                           'Kabelkiosk'           : '0B00,09AF', #Niemcy 9.0°E / 13.0°E / 19.2°E 183 15-02-2016 08:01:28 
                           'LeBouquetdeCanal+'    : '0500', #Francja 26.0°E 0 15-02-2016 08:00:43 
                           'MTVNetworks'          : '0B00,0D00', #Brytania 13.0°E / 19.2°E / 30.5°E / 0.8°W 51 15-02-2016 07:59:56 
                           'MaxTV'                : '0500', #Chorwacja 16.0°E 67 15-02-2016 08:00:24 
                           'Mediaset'             : '1803', #Włochy 13.0°E / 5.0°W / 12.5°W 46 15-02-2016 08:00:04 
                           'Meo'                  : '0100', #Portugalia 30.0°W 150 15-02-2016 08:00:57 
                           'Mobistar'             : '0500', #Belgia 13.0°E / 19.2°E / 23.5°E 69 15-02-2016 07:59:54 
                           'Movistar+(Astra)'     : '0100,1810', #Hiszpania 30.0°W 133 15-02-2016 08:00:55 
                           'Movistar+(Hispasat)'  : '0100,1810', #Hiszpania 30.0°W 133 15-02-2016 08:00:55 
                           'MultichoiceAfrica'    : '1800', #Republika Południowe 36.0°E / 68.5°E 242 15-02-2016 08:01:01 
                           'MyTV'                 : '1800', #Republika Południowe 68.5°E 0 15-02-2016 08:01:17 
                           'NC+'                  : '0100,0B01', #Polska 13.0°E 326 15-02-2016 07:59:50 
                           'Nos'                  : '1802', #Portugalia 30.0°W 109 15-02-2016 08:00:58 
                           'ORFDigital'           : '0D05,0D95', #Austria 19.2°E 29 15-02-2016 08:00:42 
                           'OTE'                  : '099E', #Grecja 9.0°E / 39.0°E 101 15-02-2016 08:01:31 
                           'Orange'               : '0500', #Francja 13.0°E / 19.2°E / 5.0°W 305 15-02-2016 08:00:02 
                           'OrangePolska'         : '0500', #Polska 13.0°E 196 15-02-2016 08:00:06 
                           'Orbit'                : '0100,0668', #Zjednoczone Emiraty 8.0°W 3 15-02-2016 08:01:25 
                           'OrbitShowtimeNetwork' : '0100,0668', #Zjednoczone Emiraty 7.0°W 114 15-02-2016 08:01:23 
                           'PlatformaDV'          : '4AE1', #Rosja 9.0°E 0 15-02-2016 08:01:25 
                           'PlatformaHD'          : '4AE1', #Rosja 9.0°E 0 15-02-2016 08:01:32 
                           'RAI'                  : '0100', #Włochy 13.0°E 77 15-02-2016 08:00:12 
                           'RCSDigiTV'            : '1802,1880', #Rumunia 0.8°W 211 15-02-2016 07:59:42 
                           'RadugaTV'             : '0652', #Rosja 75.0°E 55 15-02-2016 08:01:24 
                           'SSR/SRG'              : '0500', #Szwajcara 13.0°E 17 15-02-2016 08:00:19 
                           'SatelliteBG'          : '0D06,0D96,0B01,0624', #Bułgaria 23.5°E 0 15-02-2016 08:00:42 
                           'SkyDeutschland'       : '1833,1834,1702,1722,09C4,09AF', #Niemcy 9.0°E / 19.2°E 195 15-02-2016 08:01:30 
                           'SkyDigital'           : '0963', #Wielka Brytania 28.2°E 448 15-02-2016 08:00:53 
                           'SkyItalia'            : '0919,093B,09CD', #Włochy 13.0°E 426 15-02-2016 08:00:18 
                           'SkyLink'              : '0D03,0D70,0D96,0624', #Słowacja 19.2°E / 23.5°E 51 15-02-2016 08:00:32 
                           'TVVlaanderen'         : '0100,0500', #Belgia 19.2°E / 23.5°E 97 15-02-2016 08:00:34 
                           'TVP'                  : '09B2', #Polska 7.0°E / 19.2°E 0 15-02-2016 08:01:17 
                           'TeleSat'              : '0100', #Belgia 13.0°E / 19.2°E / 23.5°E 73 15-02-2016 07:59:55 
                           'Telewizjanakartę'     : '0B00', #Polska 13.0°E 20 15-02-2016 08:00:20 
                           'TivùSat'              : '183D', #Włochy 13.0°E 37 15-02-2016 08:00:20 
                           'TotalTV'              : '091F', #Serbia 13.0°E / 16.0°E 201 15-02-2016 07:59:52 
                           'TringDigital'         : '0BAA', #Albania 16.0°E 42 15-02-2016 08:00:25 
                           'UPCDirect'            : '0D02,1815,0D97,0653', #Węgry 19.2°E / 0.8°W 207 15-02-2016 08:00:28 
                           'Viasat'               : '090F,093E', #Szwecja 4.8°E 293 15-02-2016 08:01:11 
                           'VisionTV'             : '0931', #Ukraina 4.8°E / 13.0°E 123 15-02-2016 08:01:07
                           'Vivacom'              : '09BD'} #Bułgaria 45.0°E 102 15-02-2016 08:01:14








# main class to manage channels list generation
class getchannels:

    # Attributes


    # class constructor
    def __init__(self):

        # local attributes
        self.__outputList = list()
        self.__outputListLower = list()
        self.__transponder_list = list()
        self.__channels_bouquets  = list()
        self.__name_bouquets      = list()

        # check command line arguments before start
        self.__parse_args()

        # check if is present config file
        if self.__args.configfile != None:
            # check for config file presence

            if os.path.exists('./conf/' + self.__args.configfile) == False:
                # file not founded
                print 'specified config file not founded \n' + os.path.abspath('./conf/' + self.__args.configfile) + \
                      '\nplease check it and retry'
                exit(1)

            # process config file
            self.__parse_config_file()


        # process html code from kingofsat website
        self.__parse_kingofsat_list()

        # write output
        self.__write_output_file()
        #self.__write_output_file()
#        self.__write_output_std()

        return








    # check for command line arguments
    def __parse_args(self):

        # create parser for command line parameters
        parser = argparse.ArgumentParser(description='Generate channels list for VDR.')

        parser.add_argument('-u', '--upper', help='set to upper polarity digit in output',
                            action="store_true", dest='upper', default=False)

        parser.add_argument('-c', '--useconfig', type=str, metavar='FILENAME', dest='configfile', default=None,
                            help='enable use of config file, searched in "conf" subfolder, to generate output')

        parser.add_argument('-o', '--output', type=str, metavar='FILENAME', dest='outfile', required=True,
                            help='enable use of config file, searched in "conf" subfolder, to generate output')

        parser.add_argument('-l', '--list', type=str, metavar='LIST_ID', required=True,
                            dest='list_id', choices=app_params.sat_list.keys(),
                            help='''set KingOfSat source channels list used to generate local VDR channels list.
                                    Can use one of follow values: ''' + ", ".join(app_params.sat_list.keys()))

        parser.add_argument('-b', '--bouquet', type=str, metavar='BOUQUET', required=False,
                            dest='bouquet', choices=app_params.caid_bouquets.keys(),
                            help='''select bouquet from source channels list to get.
                            Can use one of follow values: ''' + ", ".join(app_params.caid_bouquets.keys()))

        # assign command line parse output to class attribute
        self.__args = parser.parse_args()
        return








    # read config file
    def __parse_config_file(self):
        # update local var with config file content
        file = open('./conf/' + self.__args.configfile, "r")
        cfgFile = file.read()
        file.close()

        # generate list with config file rows
        rows = cfgFile.split("\n")

        # loop for all rows in config file
        for row in rows:
            row = row.strip()
            # remove empty rows
            if len(row) > 0:
                # remove comments
                if row[0:1] != "#":
                    # update local vars with file content
                    self.__outputList.append(row)
                    self.__outputListLower.append(row.replace(" ", "").lower())








    # get html code from kingofsat using specified url and extract data
    def __parse_kingofsat_list(self):

        # get html
        f = urllib.urlopen(app_params.sat_list[self.__args.list_id])
        web_content = f.read()
        f.close()

        # split webpage content in many trasponder sections
        self.__transponder_list = web_content.split('''color="yellow">''' + app_params.sat_id[self.__args.list_id])

        # parse all transponder section founded
        for idx in range(1, len(self.__transponder_list)):
            self.__parse_transponder(self.__transponder_list[idx])








    # parse single transponder
    def __parse_transponder(self, trans_code):

        # offsets
        tra1=0
        tra2=0
        tmp=0

        # search initial transponder data
        tra1= string.find(trans_code, '''<td width="5%" class="bld">''')
        tmp = string.find(trans_code, '''<td width="5%" class="nbld">''')

        # check for second possible tag
        if tmp > 0 and tmp < tra1:
            tra1 = tmp+1

        # transponder frequency
        tra2= string.find(trans_code, ".", tra1+27)
        freq = trans_code[tra1+27:tra2]

        # polarity
        tra1 = string.find(trans_code, '''class="bld">''', tra2+1)
        tmp = string.find(trans_code, '''class="nbld">''', tra2+1)
        if tmp > 0 and tmp < tra1:
            tra1 = tmp+1

        tra2 = string.find(trans_code, "</td>", tra1+12)
        polar = trans_code[tra1+12:tra2]

        # check for polar digit representation
        if self.__args.upper == True:
            polar = polar.upper()
        else:
            polar = polar.lower()

        # dvb
        tra1 = string.find(trans_code, "DVB-", tra2+1)
        tra2 = string.find(trans_code, "</td>", tra1+4)
        dvb = trans_code[tra1+4:tra2]

        # modular
        tra1 = string.find(trans_code, '''">''', tra2+1)
        tra2 = string.find(trans_code, "</td>", tra1+2)
        modular = trans_code[tra1+2:tra2]

        # symbol rate
        tra1 = string.find(trans_code, '''class="bld">''', tra2+1)
        tmp = string.find(trans_code, '''class="nbld">''', tra2+1)
        if tmp > 0 and tmp < tra1:
            tra1 = tmp+1

        tra2 = string.find(trans_code, "</a>", tra1+12)
        sr = trans_code[tra1+12:tra2]

        # fec
        tra1 = string.find(trans_code, '''class="bld">''', tra2+1)
        tmp = string.find(trans_code, '''class="nbld">''', tra2+1)
        if tmp > 0 and tmp < tra1:
            tra1 = tmp+1

        tra2 = string.find(trans_code, "</a>", tra1+12)
        fec = trans_code[tra1+12:tra2]

        # network id
        tra1 = string.find(trans_code, "NID:", tra2+1)
        tra2 = string.find(trans_code, "</td>", tra1+4)
        nid = trans_code[tra1+4:tra2]
        nid = nid.replace('''<a class="n">''', "")
        nid = nid.replace("</a>", "").strip()

        # transponder id
        tra1 = string.find(trans_code, "TID:", tra2+1)
        tra2 = string.find(trans_code, "</td>", tra1+4)
        tid = trans_code[tra1+4:tra2]
        tid = tid.replace('''<a class="n">''', "")
        tid = tid.replace("</a>", "").strip()


        # check for dvb-s type
        if dvb == "S2":
            # update row and video pid with dvb-s2 parameters
            trparam  = "M5O35S1"
            vpidtype = "=27"
        else:
            # update row and video pid with dvb-s parameters
            trparam  = "M2S0"
            vpidtype = "=2"

        # create row template
        tmpRow = "<chname>;" + \
                 "<bouquet>:" + \
                 freq + ":" + \
                 polar + "C" + fec.replace("/","") + trparam + ":" + \
                 "S" +  self.__args.list_id + ":" + \
                 sr + ":" + \
                 "<vpid>" + vpidtype + ":" + \
                 "<apid>:" + \
                 "<subtxt>:" + \
                 "<caid>:" + \
                 "<sid>:" + \
                 nid + ":" + \
                 tid + \
                 ":0"

        # split remaining data in many channel sections
        tmpCh = trans_code[tra2+4:]
        tmpChCodes = tmpCh.split(''' title="Id: ''')

        # parse all channel section founded
        for idx in range(1, len(tmpChCodes)):
            tmpChList = self.__parse_channel(tmpChCodes[idx])

            # update templare row with returned values chName, bqt, sid, vpid, apid, subtxt
            for chInfos in tmpChList:
                chRow = tmpRow.replace("<chname>", chInfos[0])
                chRow = chRow.replace("<bouquet>", chInfos[1])
                chRow = chRow.replace("<sid>", chInfos[2])
                chRow = chRow.replace("<vpid>", chInfos[3])
                chRow = chRow.replace("<apid>", chInfos[4])
                chRow = chRow.replace("<subtxt>", chInfos[5])

                # check for caid value for this bouquet
                if app_params.caid_bouquets.has_key(chInfos[1]):
                    # know value
                    chRow = chRow.replace("<caid>", app_params.caid_bouquets[chInfos[1]])
                else:
                    # unknow value, set to '0'
                    chRow = chRow.replace("<caid>", "0")

                # check for config file usage
                if self.__args.configfile != None:
                    # try to found channel in our preset list from config file
                    try:
                        cfIdx = self.__outputListLower.index((chInfos[0] + ";" + chInfos[1]).replace(" ", "").lower())
                    except ValueError:
                        cfIdx = -1

                    # if founded channel, update row
                    if cfIdx >= 0:
                        # update row for channels in config file
                        self.__outputList[cfIdx] = chRow

                else:
                    # update total list
                    try:
                        # get already added channel position
                        ib = self.__name_bouquets.index(chInfos[1])
                    except ValueError:
                        # added new position for channel
                        self.__name_bouquets.append(chInfos[1])
                        self.__channels_bouquets.append("")
                        ib = len(self.__name_bouquets)-2

                    # update value
                    self.__channels_bouquets[ib] += chRow + "\n"








    # parse channel section
    def __parse_channel(self, channel_str):

        # offsets
        tra1=0
        tra2=0
        out_channel_list = list()

        # channel name
        tra2 = string.find(channel_str, "\"")
        chName = channel_str[tra1:tra2]

        # bouquets
        tra1 = string.find(channel_str, "<TD ", tra2+1)
        tra1 = string.find(channel_str, "<TD ", tra1+10)
        tra1 = string.find(channel_str, "<TD ", tra1+10)
        tra2 = string.find(channel_str, "</TD>", tra1+10)
        bqtStr = channel_str[tra1+10:tra2]
        bouquetList = self.__parse_bouquet(bqtStr)

        # service id
        tra1 = string.find(channel_str, "<TD ", tra2+3)
        tra1 = string.find(channel_str, "<TD ", tra1+10)
        tra1 = string.find(channel_str, ">", tra1+10)
        tra2 = string.find(channel_str, "<", tra1+1)
        sid = channel_str[tra1+1:tra2].strip()

        # video pid
        tra1 = string.find(channel_str, "<TD ", tra2+1)
        tra1 = string.find(channel_str, ">", tra1+10)
        tra2 = string.find(channel_str, "<", tra1+1)
        vpid = channel_str[tra1+1:tra2].strip()

        # audio pid
        tra1 = string.find(channel_str, "<TD ", tra2+1)
        tra1 = string.find(channel_str, ">", tra1+10)
        tra2 = string.find(channel_str, "</TD>", tra1+1)
        apidStr = channel_str[tra1:tra2].strip()
        apid = self.__parse_audio_pid(apidStr)

        # pcr
        tra1 = string.find(channel_str, "<TD ", tra2+1)
        tra1 = string.find(channel_str, "<TD ", tra1+10)
        tra1 = string.find(channel_str, ">", tra1+10)
        tra2 = string.find(channel_str, "<", tra1+1)
        pcr = channel_str[tra1+1:tra2].strip().replace("&nbsp;", "")

        # update video pid with pcr parameter if required
        if (pcr != vpid):
            vpid += "+" + pcr

        # Subtitles
        tra1 = string.find(channel_str, "<TD ", tra2+1)
        tra1 = string.find(channel_str, ">", tra1+10)
        tra2 = string.find(channel_str, "<", tra1+1)
        subtxt = channel_str[tra1+1:tra2].strip().replace("&nbsp;", "")

        if subtxt == "":
            subtxt = "0"


        # fill channels output list
        for bqt in bouquetList:
            out_channel_list.append([chName, bqt, sid, vpid, apid, subtxt])

        return out_channel_list








    # parse audio pid string
    def __parse_audio_pid(self, strPid):

        outAudioPid=""
        pidstop = 0
        tmpapid = ""
        tmpretapid = ""
        outDolbyPids = ""
        outOtherPids = ""
        dolbyPids = list()
        otherPids = list()


        # generate array of all audio pids sections
        audiopids = strPid.split("<br")

        # loop for each audio pid
        for audiopid in audiopids:
            # process audio pid section
            pidstart = string.find(audiopid, ">")
            pidstop  = string.find(audiopid, "<", pidstart+1)

            # check for characters next pid
            if pidstop < 0:
                # there is only audio pid in string section
                tmpapid=audiopid[pidstart+1:].replace("&nbsp;", "").strip()
            else:
                # there are other info in audio pid string
                tmpapid=audiopid[pidstart+1:pidstop].replace("&nbsp;", "").strip()

            # remove unused characters
            tmpapid = tmpapid.split(" ")[0]

            # retrieve other audio pid info from remaining characters
            tmpretapid = tmpapid + "=" + self.__parse_audio_pid_single(audiopid[pidstop:])

            # check for audio pid type
            if (tmpretapid.find("@106") > 0):
                # dolby digital audio pid
                dolbyPids.append(tmpretapid)
            else:
                # other audio pid
                otherPids.append(tmpretapid)

            #tmpapid+="=" + ParseAudioPidSingle(audiopid[pidstop:]) + ","

            # update audio pids output string
            #outAudioPid+=tmpapid

        # check for non dolby audio pid presence
        if (len(otherPids) > 0):
            # loop for each non dolby audio pid
            for itemPid in otherPids:
                outOtherPids += itemPid + ","

            # remove latest comma
            outOtherPids = outOtherPids[0:len(outOtherPids)-1]

        else:
            # no other audio pid presents
            outOtherPids = "0"


        # check for dolby audio pid presence
        if (len(dolbyPids) > 0):
            # loop for each dolby audio pid
            for itemPid in dolbyPids:
                outDolbyPids += itemPid + ","

            # remove latest comma
            outDolbyPids = outDolbyPids[0:len(outDolbyPids)-1]

        else:
            # no dolby audio pid presents
            outDolbyPids = ""


        # check for dolby pid presence
        if (outDolbyPids == ""):
            # output string contains only non dolby pids
            outAudioPid = outOtherPids
        else:
            # output string contains non dolby pids + ';' + dolby pids
            outAudioPid = str(outOtherPids) + ";" + outDolbyPids


        return outAudioPid








    # extract audio pid info from each audio pid
    def __parse_audio_pid_single(self, strInfo):
        outinfo = ""

        # parse audio type
        if string.find(strInfo, '''title="AC3''') > 0:
            outinfo = "@106"
        else:
            outinfo = "@4"


        # parse language name
        if string.find(strInfo, '''title="Italiano''') > 0:
            outinfo = "ita" + outinfo
        elif string.find(strInfo, '''title="Inglese''') > 0:
            outinfo = "eng" + outinfo
        elif string.find(strInfo, '''title="Polacco''') > 0:
            outinfo = "pol" + outinfo
        elif string.find(strInfo, '''title="Romeno''') > 0:
            outinfo = "rom" + outinfo
        elif string.find(strInfo, '''title="Farsi''') > 0:
            outinfo = "far" + outinfo
        elif string.find(strInfo, '''title="Portoghese''') > 0:
            outinfo = "por" + outinfo
        elif string.find(strInfo, '''title="Urdu''') > 0:
            outinfo = "urd" + outinfo
        elif string.find(strInfo, '''title="Francese''') > 0:
            outinfo = "fra" + outinfo
        elif string.find(strInfo, '''title="Tedesco''') > 0:
            outinfo = "ger" + outinfo
        elif string.find(strInfo, '''title="Arabo''') > 0:
            outinfo = "ara" + outinfo
        elif string.find(strInfo, '''title="Bengali''') > 0:
            outinfo = "ben" + outinfo
        elif string.find(strInfo, '''title="Tamil''') > 0:
            outinfo = "tam" + outinfo
        elif string.find(strInfo, '''title="Russo''') > 0:
            outinfo = "rus" + outinfo
        elif string.find(strInfo, '''title="Turco''') > 0:
            outinfo = "tur" + outinfo
        elif string.find(strInfo, '''title="Curdo''') > 0:
            outinfo = "kur" + outinfo
        elif string.find(strInfo, '''title="Afghan''') > 0:
            outinfo = "afg" + outinfo
        elif string.find(strInfo, '''title="Ceco''') > 0:
            outinfo = "cze" + outinfo
        elif string.find(strInfo, '''title="Ungherese''') > 0:
            outinfo = "hun" + outinfo
        elif string.find(strInfo, '''title="Olandese''') > 0:
            outinfo = "ned" + outinfo
        elif string.find(strInfo, '''title="Spagnolo''') > 0:
            outinfo = "esp" + outinfo
        elif string.find(strInfo, '''title="Macedone''') > 0:
            outinfo = "mac" + outinfo
        elif string.find(strInfo, '''title="Tailandese''') > 0:
            outinfo = "tha" + outinfo
        elif string.find(strInfo, '''title="Vietnamita''') > 0:
            outinfo = "vie" + outinfo
        elif string.find(strInfo, '''title="Greco''') > 0:
            outinfo = "gre" + outinfo
        elif string.find(strInfo, '''title="Somali''') > 0:
            outinfo = "som" + outinfo
        elif string.find(strInfo, '''title="Berbere''') > 0:
            outinfo = "ber" + outinfo
        elif string.find(strInfo, '''title="Azero''') > 0:
            outinfo = "aze" + outinfo
        else:
            outinfo = "oth" + outinfo

        return outinfo








    # parse bouquet section
    def __parse_bouquet(self, bouquetStr):

        # offsets
        tra1=0
        tra2=0

        bqtList = list()

        tra1 = string.find(bouquetStr, ">")
        tra2 = string.find(bouquetStr, '''href="''', tra1+1)

        # check for only one bouquet
        if tra2 < 0:
            tra2 = string.find(bouquetStr, "<", tra1+1)
            bqtList.append(bouquetStr[tra1+1:tra2].replace(" ", ""))
            return bqtList

        tra1 = tra2

        # loop for each other bouquet
        while tra1 > 0:
            tra1 = string.find(bouquetStr, ">", tra1+6)
            tra2 = string.find(bouquetStr, "</a>", tra1+1)
            bqtList.append(bouquetStr[tra1+1:tra2].replace(" ", ""))

            tra1 = string.find(bouquetStr, '''href="''', tra2+3)

        return bqtList








    # write output file (channels list)
    def __write_output_file(self):
        outputStr = ""
        outputStrMissing = ""

        # read and parse config file if is required
        if self.__args.configfile != None:
            # update output string using config data

            for item in self.__outputList:
                if string.find(item, ':') >= 0:
                    # channels informations founded on KingOfSat, so add it
                    outputStr += item + "\n"

                else:
                    # channels not founded, added in missing list
                    outputStrMissing += item + "\n"
        
        
        else:
            # update output string with all data
            for item in range(0, len(self.__name_bouquets)):
                outputStr += ":[ " + self.__name_bouquets[item] + " ]\n" + self.__channels_bouquets[item]
        
        
        # write data in to output file
        file = open(self.__args.outfile, "w")
        file.write(outputStr)
        file.close()
        
        # check for missing channels
        if (len(outputStrMissing) > 0):
            # write data in missing output file
            file = open(self.__args.outfile + '.missing', "w")
            file.write(outputStrMissing)
            file.close()








# EntryPoint
app=getchannels()
