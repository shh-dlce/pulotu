# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import DataMigration
from django.db import models

# isocode	language	classification
# from ethnologue17
# .mode tabs
# .header on
# .file out.txt
# SELECT isocode, language, classification FROM languages WHERE classification LIKE "Austronesian%"

AUSTRONESIAN = """
agf	Arguni	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, North Bomberai
amq	Amahai	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Central Maluku, East, Seram, Nunusaku, Piru Bay, East, Seram Straits, Uliase, Hatuhaha, Elpaputi
agk	Agta, Isarog	Austronesian, Malayo-Polynesian, Philippine, Greater Central Philippine, Central Philippine, Bikol, Coastal, Naga
aai	Arifama-Miniafia	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, Papuan Tip, Nuclear, North Papuan Mainland-D’Entrecasteaux, Are-Taupota, Are
amv	Ambelau	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Central Maluku, Ambelau
agn	Agutaynen	Austronesian, Malayo-Polynesian, Philippine, Kalamian
asz	As	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, South Halmahera-West New Guinea, West New Guinea, Cenderawasih Bay, Raja Ampat
atd	Manobo, Ata	Austronesian, Malayo-Polynesian, Philippine, Greater Central Philippine, Manobo, Central, South, Ata-Tigwa
agt	Agta, Central Cagayan	Austronesian, Malayo-Polynesian, Philippine, Northern Luzon, Northern Cordilleran, Cagayan Valley, Ibanagic, Gaddangic
agv	Dumagat, Remontado	Austronesian, Malayo-Polynesian, Philippine, Central Luzon, Sinauna
and	Ansus	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, South Halmahera-West New Guinea, West New Guinea, Cenderawasih Bay, Yapen, Central-Western
agw	Kahua	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, Southeast Solomonic, Malaita-San Cristobal, San Cristobal
ane	Xârâcùù	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, Remote Oceanic, New Caledonian, Southern, South, Xaracuu-Xaragure
atk	Ati	Austronesian, Malayo-Polynesian, Philippine, Greater Central Philippine, Central Philippine, Bisayan, Central, Peripheral
atl	Agta, Mt. Iraya	Austronesian, Malayo-Polynesian, Philippine, Greater Central Philippine, Central Philippine, Bikol, Coastal, Naga
agy	Alta, Southern	Austronesian, Malayo-Polynesian, Philippine, Northern Luzon, Meso-Cordilleran, Alta
atm	Ata	Austronesian, Malayo-Polynesian, Philippine, Greater Central Philippine, Central Philippine
aaw	Solong	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, North New Guinea, Ngero-Vitiaz, Vitiaz, Southwest New Britain, Arawe-Pasismanua, Arawe, West Arawe
agz	Agta, Mt. Iriga	Austronesian, Malayo-Polynesian, Philippine, Greater Central Philippine, Central Philippine, Bikol, Inland
aaz	Amarasi	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Timor-Babar, Nuclear Timor, Uab Meto
ahb	Axamb	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, Remote Oceanic, North and Central Vanuatu, Northeast Vanuatu-Banks Islands, Malekula Coastal
atp	Atta, Pudtol	Austronesian, Malayo-Polynesian, Philippine, Northern Luzon, Northern Cordilleran, Cagayan Valley, Ibanagic
atq	Aralle-Tabulahan	Austronesian, Malayo-Polynesian, South Sulawesi, Northern, Pitu Ulunna Salu
abc	Ayta, Ambala	Austronesian, Malayo-Polynesian, Philippine, Central Luzon, Sambalic
abd	Manide	Austronesian, Malayo-Polynesian, Philippine, Greater Central Philippine, Umiray Dumaget
att	Atta, Pamplona	Austronesian, Malayo-Polynesian, Philippine, Northern Luzon, Northern Cordilleran, Cagayan Valley, Ibanagic
abf	Abai Sungai	Austronesian, Malayo-Polynesian, North Borneo, Sabahan, Paitanic
aty	Aneityum	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, South Vanuatu, Aneityum
atz	Arta	Austronesian, Malayo-Polynesian, Philippine, Northern Luzon, Arta
aua	Asumboa	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Temotu, Utupua-Vanikoro, Utupua
abl	Lampung Nyo	Austronesian, Malayo-Polynesian, Lampung
aia	Arosi	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, Southeast Solomonic, Malaita-San Cristobal, San Cristobal
anx	Andra-Hus	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Admiralty Islands, Eastern, Manus, East
aud	Anuta	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, Remote Oceanic, Central Pacific, East Fijian-Polynesian, Polynesian, Nuclear, Samoic-Outlier, Futunic
abp	Ayta, Abellen	Austronesian, Malayo-Polynesian, Philippine, Central Luzon, Sambalic
aie	Amara	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, North New Guinea, Ngero-Vitiaz, Vitiaz, Southwest New Britain, Amara
aui	Anuki	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, Papuan Tip, Nuclear, North Papuan Mainland-D’Entrecasteaux, Anuki
aul	Aulua	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, Remote Oceanic, North and Central Vanuatu, Northeast Vanuatu-Banks Islands, Malekula Coastal
abx	Inabaknon	Austronesian, Malayo-Polynesian, Greater Barito, Sama-Bajaw, Abaknon
auq	Anus	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, North New Guinea, Sarmi-Jayapura Bay, Sarmi
aok	Arhö	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, Remote Oceanic, New Caledonian, Southern, South, Wailic
aol	Alor	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Bima-Lembata
aut	Austral	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, Remote Oceanic, Central Pacific, East Fijian-Polynesian, Polynesian, Nuclear, East, Central, Tahitic
ace	Aceh	Austronesian, Malayo-Polynesian, Malayo-Chamic, Chamic, Acehnese
aor	Aore	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, Remote Oceanic, North and Central Vanuatu, Northeast Vanuatu-Banks Islands, West Santo
ais	Amis, Nataoran	Austronesian, East Formosan, Central
aix	Aighon	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, North New Guinea, Ngero-Vitiaz, Vitiaz, Southwest New Britain, Arawe-Pasismanua, Pasismanua
avb	Avau	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, North New Guinea, Ngero-Vitiaz, Vitiaz, Southwest New Britain, Arawe-Pasismanua, Arawe, East Arawe
aoz	Uab Meto	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Timor-Babar, Nuclear Timor, Uab Meto
apb	Sa’a	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, Southeast Solomonic, Malaita-San Cristobal, Malaita, Southern
aji	Ajië	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, Remote Oceanic, New Caledonian, Southern, South, Wailic
apf	Agta, Pahanan	Austronesian, Malayo-Polynesian, Philippine, Northern Luzon, Northern Cordilleran, Northeastern Luzon
apg	Ampanang	Austronesian, Malayo-Polynesian, Greater Barito, Barito-Mahakam
akb	Batak Angkola	Austronesian, Malayo-Polynesian, Northwest Sumatra-Barrier Islands, Batak, Southern
apo	Ambul	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, North New Guinea, Ngero-Vitiaz, Vitiaz, Southwest New Britain, Arawe-Pasismanua, Arawe, West Arawe
app	Apma	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, Remote Oceanic, North and Central Vanuatu, Northeast Vanuatu-Banks Islands, East Vanuatu
akg	Anakalangu	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Sumba-Hawu, Sumba
apr	Arop-Lokep	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, North New Guinea, Ngero-Vitiaz, Vitiaz, Korap
aps	Arop-Sissano	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, North New Guinea, Schouten, Siau
akl	Inakeanon	Austronesian, Malayo-Polynesian, Philippine, Greater Central Philippine, Central Philippine, Bisayan, West, Aklan
apx	Aputai	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Timor-Babar, Southwest Maluku, Wetar
akr	Araki	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, Remote Oceanic, North and Central Vanuatu, Northeast Vanuatu-Banks Islands, West Santo
akt	Akolet	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, North New Guinea, Ngero-Vitiaz, Vitiaz, Southwest New Britain, Arawe-Pasismanua, Arawe, East Arawe
adr	Adonara	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Bima-Lembata
aqn	Alta, Northern	Austronesian, Malayo-Polynesian, Philippine, Northern Luzon, Meso-Cordilleran, Alta
aqr	Arhâ	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, Remote Oceanic, New Caledonian, Southern, South, Wailic
adz	Adzera	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, North New Guinea, Huon Gulf, Markham, Upper
axx	Xârâgurè	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, Remote Oceanic, New Caledonian, Southern, South, Xaracuu-Xaragure
aek	Haeke	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, Remote Oceanic, New Caledonian, Haekic
alj	Alangan	Austronesian, Malayo-Polynesian, Philippine, North Mangyan
alm	Amblong	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, Remote Oceanic, North and Central Vanuatu, Northeast Vanuatu-Banks Islands, West Santo
alo	Larike-Wakasihu	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Central Maluku, East, Seram, Nunusaku, Piru Bay, West, Hoamoal
alp	Alune	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Central Maluku, East, Seram, Nunusaku, Three Rivers, Amalumute, Northwest Seram, Ulat Inai
alu	’Are’are	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, Southeast Solomonic, Malaita-San Cristobal, Malaita, Southern
ays	Ayta, Sorsogon	Austronesian, Malayo-Polynesian, Philippine, Greater Central Philippine, Central Philippine
ayt	Ayta, Magbukun	Austronesian, Malayo-Polynesian, Philippine, Central Luzon, Sambalic
ayy	Ayta, Tayabas	Austronesian, Malayo-Polynesian, Philippine, Greater Central Philippine, Central Philippine
ami	Amis	Austronesian, East Formosan, Central
asl	Asilulu	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Central Maluku, East, Seram, Nunusaku, Piru Bay, West, Asilulu
amk	Ambai	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, South Halmahera-West New Guinea, West New Guinea, Cenderawasih Bay, Yapen, Central-Western
azt	Atta, Faire	Austronesian, Malayo-Polynesian, Philippine, Northern Luzon, Northern Cordilleran, Cagayan Valley, Ibanagic
baa	Babatana	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, Meso Melanesian, New Ireland, South New Ireland-Northwest Solomonic, Choiseul
bna	Bonerate	Austronesian, Malayo-Polynesian, Celebic, Eastern, Southeastern, Muna-Buton, Tukangbesi-Bonerate
btp	Budibud	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, Papuan Tip, Peripheral, Kilivila-Louisiades, Kilivila
bnb	Bookan	Austronesian, Malayo-Polynesian, North Borneo, North Sarawakan, Dayic, Murutic, Northern
bac	Badui	Austronesian, Malayo-Polynesian, Sundanese
btr	Baetora	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, Remote Oceanic, North and Central Vanuatu, Northeast Vanuatu-Banks Islands, East Vanuatu
bnd	Banda	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Central Maluku, East, Banda-Geser
bts	Batak Simalungun	Austronesian, Malayo-Polynesian, Northwest Sumatra-Barrier Islands, Batak, Simalungan
bne	Bintauna	Austronesian, Malayo-Polynesian, Philippine, Greater Central Philippine, Gorontalo-Mongondow, Gorontalic
bgs	Tagabawa	Austronesian, Malayo-Polynesian, Philippine, Greater Central Philippine, Manobo, South
bnf	Masiwang	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Central Maluku, East, Seram, Masiwang
bgt	Bughotu	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, Southeast Solomonic, Gela-Guadalcanal, Bughotu
baj	Barakai	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Aru
btw	Butuanon	Austronesian, Malayo-Polynesian, Philippine, Greater Central Philippine, Central Philippine, Bisayan, South, Butuan-Tausug
bnj	Tawbuid, Eastern	Austronesian, Malayo-Polynesian, Philippine, Greater Central Philippine, South Mangyan, Buhid-Taubuid
btx	Batak Karo	Austronesian, Malayo-Polynesian, Northwest Sumatra-Barrier Islands, Batak, Northern
bnk	Bierebo	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, Remote Oceanic, North and Central Vanuatu, Northeast Vanuatu-Banks Islands, Epi, Lamenu-Baki, Baki-Bierebo
bty	Bobot	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Central Maluku, East, Seram, Bobot
btz	Batak Alas-Kluet	Austronesian, Malayo-Polynesian, Northwest Sumatra-Barrier Islands, Batak, Northern
ban	Bali	Austronesian, Malayo-Polynesian, Bali-Sasak-Sumbawa
bgy	Benggoi	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Central Maluku, East, Seram, Manusela-Seti
bgz	Banggai	Austronesian, Malayo-Polynesian, Celebic, Eastern, Saluan-Banggai, Eastern
bnn	Bunun	Austronesian, Bunun
bno	Bantoanon	Austronesian, Malayo-Polynesian, Philippine, Greater Central Philippine, Central Philippine, Bisayan, Banton
buc	Bushi	Austronesian, Malayo-Polynesian, Greater Barito, East, Malagasy
bnp	Bola	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, Meso Melanesian, Willaumez
bhc	Biga	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, South Halmahera-West New Guinea, West New Guinea, Cenderawasih Bay, Raja Ampat
bnq	Bantik	Austronesian, Malayo-Polynesian, Philippine, Sangiric, Southern
bnr	Butmas-Tur	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, Remote Oceanic, North and Central Vanuatu, East Santo, South
bug	Bugis	Austronesian, Malayo-Polynesian, South Sulawesi, Bugis
bnu	Bentong	Austronesian, Malayo-Polynesian, South Sulawesi, Makassar
bay	Batuley	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Aru
buk	Bugawac	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, North New Guinea, Huon Gulf, North
bny	Bintulu	Austronesian, Malayo-Polynesian, North Borneo, North Sarawakan, Bintulu
bbc	Batak Toba	Austronesian, Malayo-Polynesian, Northwest Sumatra-Barrier Islands, Batak, Southern
bup	Busoa	Austronesian, Malayo-Polynesian, Celebic, Eastern, Southeastern, Muna-Buton, Nuclear Muna-Buton, Munan
bhp	Bima	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Bima-Lembata
bhq	Tukang Besi South	Austronesian, Malayo-Polynesian, Celebic, Eastern, Southeastern, Muna-Buton, Tukangbesi-Bonerate
bhr	Malagasy, Bara	Austronesian, Malayo-Polynesian, Greater Barito, East, Malagasy
bhv	Bahau	Austronesian, Malayo-Polynesian, North Borneo, North Sarawakan, Kayan-Kenyah, Kayanic, Kayan Proper
bbn	Uneapa	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, Meso Melanesian, Bali-Vitu
bhw	Biak	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, South Halmahera-West New Guinea, West New Guinea, Cenderawasih Bay, Biakic
bhz	Bada	Austronesian, Malayo-Polynesian, Celebic, Kaili-Pamona, Southern, Badaic
bvc	Baelelea	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, Southeast Solomonic, Malaita-San Cristobal, Malaita, Northern
bvd	Baeggu	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, Southeast Solomonic, Malaita-San Cristobal, Malaita, Northern
bve	Malay, Berau	Austronesian, Malayo-Polynesian, Malayo-Chamic, Malayic, Malay
bbv	Karnai	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, North New Guinea, Ngero-Vitiaz, Vitiaz, Korap
bvk	Bukat	Austronesian, Malayo-Polynesian, North Borneo, North Sarawakan, Kayan-Kenyah, Kayanic, Muller-Schwaner ’Punan’
bpa	Daakaka	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, Remote Oceanic, North and Central Vanuatu, Northeast Vanuatu-Banks Islands, East Vanuatu
bcd	Babar, North	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Babar, North
biq	Bipi	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Admiralty Islands, Eastern, Manus, West
bpg	Bonggo	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, North New Guinea, Sarmi-Jayapura Bay, Sarmi
bvt	Bati	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Central Maluku, East, Banda-Geser, Geser-Gorom
bch	Bariai	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, North New Guinea, Ngero-Vitiaz, Ngero, Bariai
bvu	Malay, Bukit	Austronesian, Malayo-Polynesian, Malayo-Chamic, Malayic, Malay
bpk	Orowe	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, Remote Oceanic, New Caledonian, Southern, South, Wailic
bcl	Bikol, Central	Austronesian, Malayo-Polynesian, Philippine, Greater Central Philippine, Central Philippine, Bikol, Coastal, Naga
bvy	Baybayanon	Austronesian, Malayo-Polynesian, Philippine, Greater Central Philippine, Central Philippine, Bisayan, Central, Warayan
bcm	Bannoni	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, Meso Melanesian, New Ireland, South New Ireland-Northwest Solomonic, Piva-Banoni
bwa	Bwatoo	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, Remote Oceanic, New Caledonian, Northern, North, Hmwaveke
bwb	Namosi-Naitasiri-Serua	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, Remote Oceanic, Central Pacific, West Fijian-Rotuman, West Fijian
bpr	Blaan, Koronadal	Austronesian, Malayo-Polynesian, Philippine, Bilic, Blaan
bwd	Bwaidoka	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, Papuan Tip, Nuclear, North Papuan Mainland-D’Entrecasteaux, Bwaidoga
bps	Blaan, Sarangani	Austronesian, Malayo-Polynesian, Philippine, Bilic, Blaan
bwf	Boselewa	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, Papuan Tip, Nuclear, North Papuan Mainland-D’Entrecasteaux, Dobu-Duau
bcu	Awad Bing	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, North New Guinea, Ngero-Vitiaz, Vitiaz, Bel, Astrolabe
bjk	Barok	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, Meso Melanesian, New Ireland, Madak
bpz	Bilba	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Timor-Babar, Nuclear Timor, Rote
bjl	Bulu	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, Meso Melanesian, Willaumez
bdb	Basap	Austronesian, Malayo-Polynesian, North Borneo, Rejang-Sajau
bjn	Banjar	Austronesian, Malayo-Polynesian, Malayo-Chamic, Malayic, Malay
bdd	Bunama	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, Papuan Tip, Nuclear, North Papuan Mainland-D’Entrecasteaux, Dobu-Duau
bjp	Fanamaket	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, Meso Melanesian, New Ireland, South New Ireland-Northwest Solomonic, Patpatar-Tolai
bdg	Bonggi	Austronesian, Malayo-Polynesian, North Borneo, Sabahan, Dusunic, Bisaya
bdl	Bajau, Indonesian	Austronesian, Malayo-Polynesian, Greater Barito, Sama-Bajaw, Sulu-Borneo, Borneo Coast Bajaw
bjx	Itneg, Banao	Austronesian, Malayo-Polynesian, Philippine, Northern Luzon, Meso-Cordilleran, South-Central Cordilleran, Central Cordilleran, North Central Cordilleran, Kalinga-Itneg, Kalinga
bxa	Tairaha	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, Southeast Solomonic, Malaita-San Cristobal, San Cristobal
bkd	Binukid	Austronesian, Malayo-Polynesian, Philippine, Greater Central Philippine, Manobo, North
bqr	Burusu	Austronesian, Malayo-Polynesian, North Borneo, Rejang-Sajau
bdr	Bajau, West Coast	Austronesian, Malayo-Polynesian, Greater Barito, Sama-Bajaw, Sulu-Borneo, Borneo Coast Bajaw
bxf	Minigir	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, Meso Melanesian, New Ireland, South New Ireland-Northwest Solomonic
bki	Baki	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, Remote Oceanic, North and Central Vanuatu, Northeast Vanuatu-Banks Islands, Epi, Lamenu-Baki, Baki-Bierebo
bxh	Buhutu	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, Papuan Tip, Nuclear, Suauic
bdx	Budong-Budong	Austronesian, Malayo-Polynesian, South Sulawesi, Seko, Panasuan
bkn	Bukitan	Austronesian, Malayo-Polynesian, North Borneo, Melanau-Kajang, Kajang
bed	Bedoanas	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, South Halmahera-West New Guinea, West New Guinea, Bomberai
bkr	Bakumpai	Austronesian, Malayo-Polynesian, Greater Barito, West, South
bks	Sorsoganon, Northern	Austronesian, Malayo-Polynesian, Philippine, Greater Central Philippine, Central Philippine, Bisayan, Central, Warayan
beg	Belait	Austronesian, Malayo-Polynesian, North Borneo, North Sarawakan, Berawan-Lower Baram, Lower Baram, Central, A
bku	Buhid	Austronesian, Malayo-Polynesian, Philippine, Greater Central Philippine, South Mangyan, Buhid-Taubuid
bei	Bakati’	Austronesian, Malayo-Polynesian, Land Dayak, Bakati’
brj	Bieria	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, Remote Oceanic, North and Central Vanuatu, Northeast Vanuatu-Banks Islands, Epi, Bieria-Maii
bkx	Baikeno	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Timor-Babar, Nuclear Timor, Uab Meto
bek	Bebeli	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, North New Guinea, Ngero-Vitiaz, Vitiaz, Southwest New Britain, Arawe-Pasismanua, Arawe, East Arawe
bkz	Bungku	Austronesian, Malayo-Polynesian, Celebic, Eastern, Southeastern, Bungku-Tolaki, Eastern, East Coast
bya	Batak	Austronesian, Malayo-Polynesian, Philippine, Greater Central Philippine, Palawanic
byd	Benyadu’	Austronesian, Malayo-Polynesian, Land Dayak
bep	Behoa	Austronesian, Malayo-Polynesian, Celebic, Kaili-Pamona, Southern, Badaic
bld	Bolango	Austronesian, Malayo-Polynesian, Philippine, Greater Central Philippine, Gorontalo-Mongondow, Gorontalic
brr	Birao	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, Southeast Solomonic, Gela-Guadalcanal, Guadalcanal
blf	Buol	Austronesian, Malayo-Polynesian, Philippine, Greater Central Philippine, Gorontalo-Mongondow, Gorontalic
brs	Baras	Austronesian, Malayo-Polynesian, Celebic, Kaili-Pamona, Northern, Kaili
blg	Balau	Austronesian, Malayo-Polynesian, Malayo-Chamic, Malayic, Ibanic
blj	Bolongan	Austronesian, Malayo-Polynesian, North Borneo, North Sarawakan, Dayic, Murutic, Tidong
bln	Bikol, Southern Catanduanes	Austronesian, Malayo-Polynesian, Philippine, Greater Central Philippine, Central Philippine, Bikol, Coastal, Virac
brz	Bilbil	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, North New Guinea, Ngero-Vitiaz, Vitiaz, Bel, Nuclear Bel, Northern
blp	Blablanga	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, Meso Melanesian, New Ireland, South New Ireland-Northwest Solomonic, Santa Isabel, Central
bsb	Bisaya, Brunei	Austronesian, Malayo-Polynesian, North Borneo, Sabahan, Dusunic, Bisaya, Southern
blq	Baluan-Pam	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Admiralty Islands, Eastern, Southeast Islands
byq	Basay	Austronesian, East Formosan, Northern
bls	Balaesang	Austronesian, Malayo-Polynesian, Celebic, Tomini-Tolitoli, Tomini, Southern
bfg	Kayan, Busang	Austronesian, Malayo-Polynesian, North Borneo, North Sarawakan, Kayan-Kenyah, Kayanic, Kayan Proper
blw	Balangao	Austronesian, Malayo-Polynesian, Philippine, Northern Luzon, Meso-Cordilleran, South-Central Cordilleran, Central Cordilleran, North Central Cordilleran, Nuclear Cordilleran, Balangaw
blx	Ayta, Mag-Indi	Austronesian, Malayo-Polynesian, Philippine, Central Luzon, Sambalic
blz	Balantak	Austronesian, Malayo-Polynesian, Celebic, Eastern, Saluan-Banggai, Eastern
bsm	Busami	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, South Halmahera-West New Guinea, West New Guinea, Cenderawasih Bay, Yapen, Central-Western
bzb	Andio	Austronesian, Malayo-Polynesian, Celebic, Eastern, Saluan-Banggai, Western
bmc	Biem	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, North New Guinea, Schouten, Kairiru-Manam, Manam
bzc	Malagasy, Southern Betsimisaraka	Austronesian, Malayo-Polynesian, Greater Barito, East, Malagasy
bzg	Babuza	Austronesian, Western Plains, Central Western Plains
bzh	Buang, Mapos	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, North New Guinea, Huon Gulf, South, Hote-Buang, Buang
bsu	Bahonsuai	Austronesian, Malayo-Polynesian, Celebic, Eastern, Southeastern, Bungku-Tolaki, Eastern, East Coast
bmk	Ghayavi	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, Papuan Tip, Nuclear, North Papuan Mainland-D’Entrecasteaux, Are-Taupota, Are
bfx	Bantayanon	Austronesian, Malayo-Polynesian, Philippine, Greater Central Philippine, Central Philippine, Bisayan, Central
bzl	Boano	Austronesian, Malayo-Polynesian, Celebic, Tomini-Tolitoli, Tolitoli
bmm	Malagasy, Northern Betsimisaraka	Austronesian, Malayo-Polynesian, Greater Barito, East, Malagasy
bsy	Bisaya, Sabah	Austronesian, Malayo-Polynesian, North Borneo, Sabahan, Dusunic, Bisaya
bmn	Bina	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, Papuan Tip, Peripheral, Central Papuan, Oumic, Magoric
bzn	Boano	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Central Maluku, East, Seram, Nunusaku, Piru Bay, West, Hoamoal
bgb	Bobongko	Austronesian, Malayo-Polynesian, Celebic, Eastern, Saluan-Banggai, Western, Saluanic
btd	Batak Dairi	Austronesian, Malayo-Polynesian, Northwest Sumatra-Barrier Islands, Batak, Northern
bzq	Buli	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, South Halmahera-West New Guinea, South Halmahera, Southeast
bth	Bidayuh, Biatah	Austronesian, Malayo-Polynesian, Land Dayak, Bidayuh, Core, Central
bgi	Giangan	Austronesian, Malayo-Polynesian, Philippine, Bilic
btj	Malay, Bacanese	Austronesian, Malayo-Polynesian, Malayo-Chamic, Malayic, Malay
btm	Batak Mandailing	Austronesian, Malayo-Polynesian, Northwest Sumatra-Barrier Islands, Batak, Southern
btn	Ratagnon	Austronesian, Malayo-Polynesian, Philippine, Greater Central Philippine, Central Philippine, Bisayan, West, Kuyan
bto	Bikol, Rinconada	Austronesian, Malayo-Polynesian, Philippine, Greater Central Philippine, Central Philippine, Bikol, Inland, Iriga
cgc	Kagayanen	Austronesian, Malayo-Polynesian, Philippine, Greater Central Philippine, Manobo, North
cha	Chamorro	Austronesian, Malayo-Polynesian, Chamorro
cml	Campalagian	Austronesian, Malayo-Polynesian, South Sulawesi, Bugis
cal	Carolinian	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, Remote Oceanic, Micronesian, Micronesian Proper, Ponapeic-Trukic, Trukic
cam	Cemuhî	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, Remote Oceanic, New Caledonian, Northern, Central
chk	Chuukese	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, Remote Oceanic, Micronesian, Micronesian Proper, Ponapeic-Trukic, Trukic
cia	Cia-Cia	Austronesian, Malayo-Polynesian, Celebic, Eastern, Southeastern, Muna-Buton, Nuclear Muna-Buton, Buton, West Buton
cir	Tiri	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, Remote Oceanic, New Caledonian, Southern, South, Zire-Tiri
cts	Bikol, Northern Catanduanes	Austronesian, Malayo-Polynesian, Philippine, Greater Central Philippine, Central Philippine, Bikol, Pandan
cbw	Kinabalian	Austronesian, Malayo-Polynesian, Philippine, Greater Central Philippine, Central Philippine, Bisayan, Central, Warayan
cja	Cham, Western	Austronesian, Malayo-Polynesian, Malayo-Chamic, Chamic, Coastal, Cham
cje	Chru	Austronesian, Malayo-Polynesian, Malayo-Chamic, Chamic, Highlands, Chru-Northern
cjm	Cham, Eastern	Austronesian, Malayo-Polynesian, Malayo-Chamic, Chamic, Coastal, Cham
cps	Capiznon	Austronesian, Malayo-Polynesian, Philippine, Greater Central Philippine, Central Philippine, Bisayan, Central, Peripheral
ckv	Kavalan	Austronesian, East Formosan, Northern
crc	Lonwolwol	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, Remote Oceanic, North and Central Vanuatu, Northeast Vanuatu-Banks Islands, East Vanuatu
ceb	Cebuano	Austronesian, Malayo-Polynesian, Philippine, Greater Central Philippine, Central Philippine, Bisayan, Cebuan
cyo	Cuyonon	Austronesian, Malayo-Polynesian, Philippine, Greater Central Philippine, Central Philippine, Bisayan, West, Kuyan
clu	Caluyanun	Austronesian, Malayo-Polynesian, Philippine, Greater Central Philippine, Central Philippine, Bisayan, West
dkk	Dakka	Austronesian, Malayo-Polynesian, South Sulawesi, Northern, Pitu Ulunna Salu
dac	Dambi	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, North New Guinea, Huon Gulf, South, Hote-Buang, Buang, Mumeng
dgc	Agta, Casiguran Dumagat	Austronesian, Malayo-Polynesian, Philippine, Northern Luzon, Northern Cordilleran, Northeastern Luzon, Northern
dkr	Kuijau	Austronesian, Malayo-Polynesian, North Borneo, Sabahan, Dusunic, Dusun
dad	Marik	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, North New Guinea, Ngero-Vitiaz, Vitiaz, Bel, Nuclear Bel, Southern
dru	Rukai	Austronesian, Rukai
dgg	Doga	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, Papuan Tip, Nuclear, North Papuan Mainland-D’Entrecasteaux, Are-Taupota, Are
dsn	Dusner	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, South Halmahera-West New Guinea, West New Guinea, Cenderawasih Bay, Biakic
dmg	Kinabatangan, Upper	Austronesian, Malayo-Polynesian, North Borneo, Sabahan, Paitanic, Upper Kinabatangan
dtb	Kadazan, Labuk-Kinabatangan	Austronesian, Malayo-Polynesian, North Borneo, Sabahan, Dusunic, Dusun, Eastern
dmr	Damar, East	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Timor-Babar, Southwest Maluku, East Damar
daw	Davawenyo	Austronesian, Malayo-Polynesian, Philippine, Greater Central Philippine, Central Philippine, Mansakan, Davawenyo
dms	Dampelas	Austronesian, Malayo-Polynesian, Celebic, Tomini-Tolitoli, Tomini, Southern
dmv	Dumpas	Austronesian, Malayo-Polynesian, North Borneo, Sabahan, Dusunic, Unclassified
dtp	Dusun, Central	Austronesian, Malayo-Polynesian, North Borneo, Sabahan, Dusunic, Dusun, Central
dtr	Lotud	Austronesian, Malayo-Polynesian, North Borneo, Sabahan, Dusunic, Dusun
dbj	Ida’an	Austronesian, Malayo-Polynesian, North Borneo, Sabahan, Ida’an
dhv	Drehu	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, Remote Oceanic, Loyalty Islands
dnk	Dengka	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Timor-Babar, Nuclear Timor, Rote
due	Agta, Umiray Dumaget	Austronesian, Malayo-Polynesian, Philippine, Greater Central Philippine, Umiray Dumaget
duf	Drubea	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, Remote Oceanic, New Caledonian, Southern, Extreme Southern
dul	Agta, Alabat Island	Austronesian, Malayo-Polynesian, Philippine, Greater Central Philippine, Umiray Dumaget
dun	Dusun Deyah	Austronesian, Malayo-Polynesian, Greater Barito, East, Central-South, Central
dij	Dai	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Babar, North
dob	Dobu	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, Papuan Tip, Nuclear, North Papuan Mainland-D’Entrecasteaux, Dobu-Duau
duo	Agta, Dupaninan	Austronesian, Malayo-Polynesian, Philippine, Northern Luzon, Northern Cordilleran, Northeastern Luzon, Northern
dup	Duano	Austronesian, Malayo-Polynesian, Malayo-Chamic, Malayic, Malay
duq	Dusun Malang	Austronesian, Malayo-Polynesian, Greater Barito, East, Central-South, South
dok	Dondo	Austronesian, Malayo-Polynesian, Celebic, Tomini-Tolitoli, Tomini, Northern
duw	Dusun Witu	Austronesian, Malayo-Polynesian, Greater Barito, East, Central-South, South
ddi	Goodenough, West	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, Papuan Tip, Nuclear, North Papuan Mainland-D’Entrecasteaux, Bwaidoga
don	Toura	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, Papuan Tip, Peripheral, Central Papuan, West Central Papuan, Nuclear
duy	Agta, Dicamay	Austronesian, Malayo-Polynesian, Philippine, Northern Luzon, Northern Cordilleran, Northeastern Luzon, Northern
dva	Duau	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, Papuan Tip, Nuclear, North Papuan Mainland-D’Entrecasteaux, Dobu-Duau
dor	Dori’o	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, Southeast Solomonic, Malaita-San Cristobal, Malaita, Southern
ddw	Dawera-Daweloor	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Babar, North
dix	Dixon Reef	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, Remote Oceanic, North and Central Vanuatu, Malekula Interior, Small Nambas
dww	Dawawa	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, Papuan Tip, Nuclear, North Papuan Mainland-D’Entrecasteaux, Kakabai
dyg	Agta, Villa Viciosa	Austronesian, Malayo-Polynesian, Philippine
dpp	Papar	Austronesian, Malayo-Polynesian, North Borneo, Sabahan, Dusunic, Dusun
drg	Rungus	Austronesian, Malayo-Polynesian, North Borneo, Sabahan, Dusunic, Dusun
djo	Jangkang	Austronesian, Malayo-Polynesian, Land Dayak, Southern
drn	Damar, West	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, West Damar
dro	Melanau, Daro-Matu	Austronesian, Malayo-Polynesian, North Borneo, Melanau-Kajang, Melanau
drr	Dororo	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, Meso Melanesian, New Ireland, South New Ireland-Northwest Solomonic, New Georgia, West
ebk	Bontok, Eastern	Austronesian, Malayo-Polynesian, Philippine, Northern Luzon, Meso-Cordilleran, South-Central Cordilleran, Central Cordilleran, North Central Cordilleran, Nuclear Cordilleran, Bontok-Kankanay, Bontok
etn	Eton	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, Remote Oceanic, North and Central Vanuatu, Northeast Vanuatu-Banks Islands, Central Vanuatu
elu	Elu	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Admiralty Islands, Eastern, Manus, East
emb	Embaloh	Austronesian, Malayo-Polynesian, South Sulawesi, Bugis, Tamanic
erg	Sie	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, South Vanuatu, Erromanga
emi	Mussau-Emira	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, St. Matthias
erk	Efate, South	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, Remote Oceanic, North and Central Vanuatu, Northeast Vanuatu-Banks Islands, Central Vanuatu
emw	Emplawas	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Babar, South, Southwest Babar
erw	Erokwanas	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, South Halmahera-West New Guinea, West New Guinea, Bomberai
end	Ende	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Bima-Lembata
faf	Fagani	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, Southeast Solomonic, Malaita-San Cristobal, San Cristobal
fud	Futuna, East	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, Remote Oceanic, Central Pacific, East Fijian-Polynesian, Polynesian, Nuclear, Samoic-Outlier, Futunic
fij	Fijian	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, Remote Oceanic, Central Pacific, East Fijian-Polynesian, East Fijian
fil	Filipino	Austronesian, Malayo-Polynesian, Philippine, Greater Central Philippine, Central Philippine, Tagalog
fos	Siraya	Austronesian, East Formosan, Southwest
frd	Fordata	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Southeast Maluku, Kei-Tanimbar, Kei-Fordata
far	Fataleka	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, Southeast Solomonic, Malaita-San Cristobal, Malaita, Northern
fut	Futuna-Aniwa	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, Remote Oceanic, Central Pacific, East Fijian-Polynesian, Polynesian, Nuclear, Samoic-Outlier, Futunic
frt	Fortsenal	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, Remote Oceanic, North and Central Vanuatu, Northeast Vanuatu-Banks Islands, West Santo
fbl	Bikol, West Albay	Austronesian, Malayo-Polynesian, Philippine, Greater Central Philippine, Central Philippine, Bikol, Inland
fwa	Fwâi	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, Remote Oceanic, New Caledonian, Northern, North, Nemi
gad	Gaddang	Austronesian, Malayo-Polynesian, Philippine, Northern Luzon, Northern Cordilleran, Cagayan Valley, Ibanagic, Gaddangic
gei	Gebe	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, South Halmahera-West New Guinea, West New Guinea, Cenderawasih Bay, Raja Ampat
gmb	Gula’alaa	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, Southeast Solomonic, Malaita-San Cristobal, Malaita, Northern
ges	Geser-Gorom	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Central Maluku, East, Banda-Geser, Geser-Gorom
gal	Galolen	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Timor-Babar, Nuclear Timor
gfk	Patpatar	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, Meso Melanesian, New Ireland, South New Ireland-Northwest Solomonic, Patpatar-Tolai
gga	Gao	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, Meso Melanesian, New Ireland, South New Ireland-Northwest Solomonic, Santa Isabel, East
gar	Galeya	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, Papuan Tip, Nuclear, North Papuan Mainland-D’Entrecasteaux, Dobu-Duau
gay	Gayo	Austronesian, Malayo-Polynesian, Northwest Sumatra-Barrier Islands
gnq	Gana	Austronesian, Malayo-Polynesian, North Borneo, Sabahan, Dusunic, Dusun
ggt	Gitua	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, North New Guinea, Ngero-Vitiaz, Ngero, Tuam
goc	Gorakor	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, North New Guinea, Huon Gulf, South, Hote-Buang, Buang, Mumeng
ghn	Ghanongga	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, Meso Melanesian, New Ireland, South New Ireland-Northwest Solomonic, New Georgia, West
gve	Duwet	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, North New Guinea, Huon Gulf, Markham, Lower, Busu
goo	Gone Dau	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, Remote Oceanic, Central Pacific, East Fijian-Polynesian, East Fijian
gop	Yeretuar	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, South Halmahera-West New Guinea, West New Guinea, Cenderawasih Bay, Yeretuar
gil	Kiribati	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, Remote Oceanic, Micronesian, Micronesian Proper, Ikiribati
goq	Gorap	Austronesian, Malayo-Polynesian, Unclassified
gor	Gorontalo	Austronesian, Malayo-Polynesian, Philippine, Greater Central Philippine, Gorontalo-Mongondow, Gorontalic
gip	Gimi	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, North New Guinea, Ngero-Vitiaz, Vitiaz, Southwest New Britain, Arawe-Pasismanua, Arawe, West Arawe
gvs	Gumawana	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, Papuan Tip, Nuclear, North Papuan Mainland-D’Entrecasteaux, Gumawana
gdd	Gedaged	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, North New Guinea, Ngero-Vitiaz, Vitiaz, Bel, Nuclear Bel, Northern
gdg	Ga’dang	Austronesian, Malayo-Polynesian, Philippine, Northern Luzon, Northern Cordilleran, Cagayan Valley, Ibanagic, Gaddangic
gri	Ghari	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, Southeast Solomonic, Gela-Guadalcanal, Guadalcanal
grm	Kota Marudu Talantang	Austronesian, Malayo-Polynesian, North Borneo, Sabahan, Dusunic, Dusun
gli	Guliguli	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, Meso Melanesian, New Ireland, South New Ireland-Northwest Solomonic, New Georgia, West
grw	Gweda	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, Papuan Tip, Nuclear, North Papuan Mainland-D’Entrecasteaux, Are-Taupota, Taupota
gzn	Gane	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, South Halmahera-West New Guinea, South Halmahera, East Makian-Gane
hah	Hahon	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, Meso Melanesian, New Ireland, South New Ireland-Northwest Solomonic, Nehan-North Bougainville, Saposa-Tinputz
hti	Hoti	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Central Maluku, East, Seram, East Seram
htu	Hitu	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Central Maluku, East, Seram, Nunusaku, Piru Bay, East, Seram Straits, Ambon
hik	Seit-Kaitetu	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Central Maluku, East, Seram, Nunusaku, Piru Bay, West, Asilulu
hnn	Hanunoo	Austronesian, Malayo-Polynesian, Philippine, Greater Central Philippine, South Mangyan, Hanunoo
hil	Hiligaynon	Austronesian, Malayo-Polynesian, Philippine, Greater Central Philippine, Central Philippine, Bisayan, Central, Peripheral
hud	Huaulu	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Central Maluku, East, Seram, Manusela-Seti
hao	Hakö	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, Meso Melanesian, New Ireland, South New Ireland-Northwest Solomonic, Nehan-North Bougainville, Buka, Halia
hoa	Hoava	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, Meso Melanesian, New Ireland, South New Ireland-Northwest Solomonic, New Georgia, West
hiw	Hiw	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, Remote Oceanic, North and Central Vanuatu, Northeast Vanuatu-Banks Islands, East Vanuatu
hob	Mari	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, North New Guinea, Huon Gulf, Markham, Upper, Mountain
hji	Haji	Austronesian, Malayo-Polynesian, Malayo-Chamic, Malayic, Malay
huk	Hulung	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Central Maluku, East, Seram, Nunusaku, Three Rivers, Amalumute, Northwest Seram, Hulung
hul	Hula	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, Papuan Tip, Peripheral, Central Papuan, Sinagoro-Keapara
haw	Hawaiian	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, Remote Oceanic, Central Pacific, East Fijian-Polynesian, Polynesian, Nuclear, East, Central, Marquesic
hla	Halia	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, Meso Melanesian, New Ireland, South New Ireland-Northwest Solomonic, Nehan-North Bougainville, Buka, Halia
huq	Tsat	Austronesian, Malayo-Polynesian, Malayo-Chamic, Chamic, Highlands, Chru-Northern, Northern Cham
hot	Hote	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, North New Guinea, Huon Gulf, South, Hote-Buang, Hote
hov	Hovongan	Austronesian, Malayo-Polynesian, North Borneo, North Sarawakan, Kayan-Kenyah, Kayanic, Muller-Schwaner ‘Punan’
hbu	Habun	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Timor-Babar, Nuclear Timor
huw	Hukumina	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Hukumina
hrc	Niwer Mil	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, Meso Melanesian, New Ireland, South New Ireland-Northwest Solomonic, Patpatar-Tolai
hvk	Haveke	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, Remote Oceanic, New Caledonian, Northern
hrk	Haruku	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Central Maluku, East, Seram, Nunusaku, Piru Bay
hvn	Hawu	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Sumba-Hawu, Hawu-Dhao
heg	Helong	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Timor-Babar, Nuclear Timor
hro	Haroi	Austronesian, Malayo-Polynesian, Malayo-Chamic, Chamic, Coastal
hgw	Haigwai	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, Papuan Tip, Nuclear, North Papuan Mainland-D’Entrecasteaux, Are-Taupota, Taupota
hrw	Warwar Feni	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, Meso Melanesian, New Ireland, South New Ireland-Northwest Solomonic, Patpatar-Tolai
iai	Iaai	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, Remote Oceanic, Loyalty Islands
ism	Masimasi	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, North New Guinea, Sarmi-Jayapura Bay, Sarmi
iba	Iban	Austronesian, Malayo-Polynesian, Malayo-Chamic, Malayic, Ibanic
imr	Imroing	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Babar, South, Southwest Babar
ind	Indonesian	Austronesian, Malayo-Polynesian, Malayo-Chamic, Malayic, Malay
ibg	Ibanag	Austronesian, Malayo-Polynesian, Philippine, Northern Luzon, Northern Cordilleran, Cagayan Valley, Ibanagic
ibl	Ibaloi	Austronesian, Malayo-Polynesian, Philippine, Northern Luzon, Meso-Cordilleran, South-Central Cordilleran, Southern Cordilleran, West Southern Cordilleran, Nuclear Southern Cordilleran, Ibaloy
itb	Itneg, Binongan	Austronesian, Malayo-Polynesian, Philippine, Northern Luzon, Meso-Cordilleran, South-Central Cordilleran, Central Cordilleran, North Central Cordilleran, Kalinga-Itneg, Itneg
inn	Isinai	Austronesian, Malayo-Polynesian, Philippine, Northern Luzon, Meso-Cordilleran, South-Central Cordilleran, Central Cordilleran, Isinai
iti	Itneg, Inlaod	Austronesian, Malayo-Polynesian, Philippine, Northern Luzon, Meso-Cordilleran, South-Central Cordilleran, Central Cordilleran, North Central Cordilleran, Kalinga-Itneg, Itneg
itt	Itneg, Maeng	Austronesian, Malayo-Polynesian, Philippine, Northern Luzon, Meso-Cordilleran, South-Central Cordilleran, Central Cordilleran, North Central Cordilleran, Kalinga-Itneg, Itneg
itv	Itawit	Austronesian, Malayo-Polynesian, Philippine, Northern Luzon, Northern Cordilleran, Cagayan Valley, Ibanagic
ity	Itneg, Moyadan	Austronesian, Malayo-Polynesian, Philippine, Northern Luzon, Meso-Cordilleran, South-Central Cordilleran, Central Cordilleran, North Central Cordilleran, Kalinga-Itneg, Itneg
ire	Yeresiam	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, South Halmahera-West New Guinea, West New Guinea, Cenderawasih Bay, Iresim
irh	Irarutu	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, South Halmahera-West New Guinea, South Halmahera
ivb	Ibatan	Austronesian, Malayo-Polynesian, Philippine, Bashiic, Ivatan
ivv	Ivatan	Austronesian, Malayo-Polynesian, Philippine, Bashiic, Ivatan
idt	Idaté	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Timor-Babar, Nuclear Timor
iwk	I-wak	Austronesian, Malayo-Polynesian, Philippine, Northern Luzon, Meso-Cordilleran, South-Central Cordilleran, Southern Cordilleran, West Southern Cordilleran, Nuclear Southern Cordilleran, Ibaloy
ila	Ile Ape	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Bima-Lembata
ifa	Ifugao, Amganad	Austronesian, Malayo-Polynesian, Philippine, Northern Luzon, Meso-Cordilleran, South-Central Cordilleran, Central Cordilleran, North Central Cordilleran, Nuclear Cordilleran, Ifugaw
ifb	Ifugao, Batad	Austronesian, Malayo-Polynesian, Philippine, Northern Luzon, Meso-Cordilleran, South-Central Cordilleran, Central Cordilleran, North Central Cordilleran, Nuclear Cordilleran, Ifugaw
iff	Ifo	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, South Vanuatu, Erromanga
ilk	Ilongot	Austronesian, Malayo-Polynesian, Philippine, Northern Luzon, Meso-Cordilleran, South-Central Cordilleran, Southern Cordilleran, Ilongot
iry	Iraya	Austronesian, Malayo-Polynesian, Philippine, North Mangyan
ifk	Ifugao, Tuwali	Austronesian, Malayo-Polynesian, Philippine, Northern Luzon, Meso-Cordilleran, South-Central Cordilleran, Central Cordilleran, North Central Cordilleran, Nuclear Cordilleran, Ifugaw
ill	Iranun	Austronesian, Malayo-Polynesian, Philippine, Greater Central Philippine, Danao, Maranao-Iranon
ilo	Ilocano	Austronesian, Malayo-Polynesian, Philippine, Northern Luzon, Ilocano
ifu	Ifugao, Mayoyao	Austronesian, Malayo-Polynesian, Philippine, Northern Luzon, Meso-Cordilleran, South-Central Cordilleran, Central Cordilleran, North Central Cordilleran, Nuclear Cordilleran, Ifugaw
isd	Isnag	Austronesian, Malayo-Polynesian, Philippine, Northern Luzon, Northern Cordilleran, Cagayan Valley, Isnag
ify	Kallahan, Keley-i	Austronesian, Malayo-Polynesian, Philippine, Northern Luzon, Meso-Cordilleran, South-Central Cordilleran, Southern Cordilleran, West Southern Cordilleran, Nuclear Southern Cordilleran, Kallahan
ilu	Ili’uun	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Timor-Babar, Southwest Maluku, Wetar
jra	Jarai	Austronesian, Malayo-Polynesian, Malayo-Chamic, Chamic, Highlands
jae	Yabem	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, North New Guinea, Huon Gulf, North
jaj	Zazao	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, Meso Melanesian, New Ireland, South New Ireland-Northwest Solomonic, Santa Isabel, Central
jak	Jakun	Austronesian, Malayo-Polynesian, Malayo-Chamic, Malayic, Malay
jal	Yalahatan	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Central Maluku, East, Seram, Nunusaku, Three Rivers
jmd	Yamdena	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Southeast Maluku, Kei-Tanimbar, Yamdena
jas	Javanese, New Caledonian	Austronesian, Malayo-Polynesian, Javanese
jau	Yaur	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, South Halmahera-West New Guinea, West New Guinea, Cenderawasih Bay, Yaur
jav	Javanese	Austronesian, Malayo-Polynesian, Javanese
jax	Malay, Jambi	Austronesian, Malayo-Polynesian, Malayo-Chamic, Malayic, Malay
jaz	Jawe	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, Remote Oceanic, New Caledonian, Northern, North, Nemi
jvn	Javanese, Caribbean	Austronesian, Malayo-Polynesian, Javanese
ktr	Kota Marudu Tinagas	Austronesian, Malayo-Polynesian, North Borneo, Sabahan, Dusunic, Dusun, Central
kne	Kankanaey	Austronesian, Malayo-Polynesian, Philippine, Northern Luzon, Meso-Cordilleran, South-Central Cordilleran, Central Cordilleran, North Central Cordilleran, Nuclear Cordilleran, Bontok-Kankanay, Kankanay
kae	Ketangalan	Austronesian, Unclassified
kag	Kajaman	Austronesian, Malayo-Polynesian, North Borneo, Melanau-Kajang, Kajang
kgx	Kamaru	Austronesian, Malayo-Polynesian, Celebic, Wotu-Wolio, Wolio-Kamaru
knl	Keninjal	Austronesian, Malayo-Polynesian, Malayo-Chamic, Malayic
kak	Kallahan, Kayapa	Austronesian, Malayo-Polynesian, Philippine, Northern Luzon, Meso-Cordilleran, South-Central Cordilleran, Southern Cordilleran, West Southern Cordilleran, Nuclear Southern Cordilleran, Kallahan
khc	Tukang Besi North	Austronesian, Malayo-Polynesian, Celebic, Eastern, Southeastern, Muna-Buton, Tukangbesi-Bonerate
kud	’Auhelawa	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, Papuan Tip, Nuclear, Suauic
kuk	Kepo’	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Bima-Lembata
khl	Lusi	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, North New Guinea, Ngero-Vitiaz, Ngero, Bariai
knx	Kendayan	Austronesian, Malayo-Polynesian, Malayo-Chamic, Malayic
koa	Konomala	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, Meso Melanesian, New Ireland, South New Ireland-Northwest Solomonic, Patpatar-Tolai
kod	Kodi	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Sumba-Hawu, Sumba
kuv	Kur	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Teor-Kur
kbi	Kaptiau	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, North New Guinea, Sarmi-Jayapura Bay, Sarmi
khz	Keapara	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, Papuan Tip, Peripheral, Central Papuan, Sinagoro-Keapara
kbm	Iwal	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, North New Guinea, Huon Gulf, South, Kaiwa
kvb	Kubu	Austronesian, Malayo-Polynesian, Malayo-Chamic, Malayic, Malay
kvc	Kove	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, North New Guinea, Ngero-Vitiaz, Ngero, Bariai
kve	Kalabakan	Austronesian, Malayo-Polynesian, North Borneo, North Sarawakan, Dayic, Murutic, Tidong
kos	Kosraean	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, Remote Oceanic, Micronesian, Micronesian Proper, Kusaiean
kvh	Komodo	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Bima-Lembata
kbt	Abadi	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, Papuan Tip, Peripheral, Central Papuan, West Central Papuan, Gabadi
kij	Kilivila	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, Papuan Tip, Peripheral, Kilivila-Louisiades, Kilivila
kbw	Kaiep	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, North New Guinea, Schouten, Kairiru-Manam, Kairiru
kvo	Dobel	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Aru
kvp	Kompane	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Aru
kpd	Koba	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Aru
kis	Kis	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, North New Guinea, Schouten, Kairiru-Manam, Manam
kvr	Kerinci	Austronesian, Malayo-Polynesian, Malayo-Chamic, Malayic, Malay
kpg	Kapingamarangi	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, Remote Oceanic, Central Pacific, East Fijian-Polynesian, Polynesian, Nuclear, Samoic-Outlier, Ellicean
kvv	Kola	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Aru
kcl	Kala	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, North New Guinea, Huon Gulf, North
kjc	Konjo, Coastal	Austronesian, Malayo-Polynesian, South Sulawesi, Makassar
kje	Kisar	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Timor-Babar, Southwest Maluku, Kisar-Roma
kwd	Kwaio	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, Southeast Solomonic, Malaita-San Cristobal, Malaita, Northern
kwf	Kwara’ae	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, Southeast Solomonic, Malaita-San Cristobal, Malaita, Northern
kji	Zabana	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, Meso Melanesian, New Ireland, South New Ireland-Northwest Solomonic, Santa Isabel, West
kwh	Kowiai	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, South Bomberai
kjk	Konjo, Highland	Austronesian, Malayo-Polynesian, South Sulawesi, Makassar
kjr	Kurudu	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, South Halmahera-West New Guinea, West New Guinea, Cenderawasih Bay, Yapen, East
kqe	Kalagan	Austronesian, Malayo-Polynesian, Philippine, Greater Central Philippine, Central Philippine, Mansakan, Western
kqf	Kakabai	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, Papuan Tip, Nuclear, North Papuan Mainland-D’Entrecasteaux, Kakabai
kdf	Mamusi	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, North New Guinea, Ngero-Vitiaz, Vitiaz, Mengen
kdk	Numèè	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, Remote Oceanic, New Caledonian, Southern, Extreme Southern
kxa	Kairiru	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, North New Guinea, Schouten, Kairiru-Manam, Kairiru
kkg	Kalinga, Mabaka Valley	Austronesian, Malayo-Polynesian, Philippine, Northern Luzon, Meso-Cordilleran, South-Central Cordilleran, Central Cordilleran, North Central Cordilleran, Kalinga-Itneg, Kalinga
kqr	Kimaragang	Austronesian, Malayo-Polynesian, North Borneo, Sabahan, Dusunic, Dusun
kxd	Brunei	Austronesian, Malayo-Polynesian, Malayo-Chamic, Malayic, Malay
kqt	Kadazan, Klias River	Austronesian, Malayo-Polynesian, North Borneo, Sabahan, Dusunic, Dusun
kkk	Kokota	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, Meso Melanesian, New Ireland, South New Ireland-Northwest Solomonic, Santa Isabel, Central
kqv	Okolod	Austronesian, Malayo-Polynesian, North Borneo, North Sarawakan, Dayic, Murutic, Murut
kxi	Keningau Murut	Austronesian, Malayo-Polynesian, North Borneo, North Sarawakan, Dayic, Murutic, Murut
kqw	Kandas	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, Meso Melanesian, New Ireland, South New Ireland-Northwest Solomonic, Patpatar-Tolai
kxn	Melanau, Kanowit-Tanjong	Austronesian, Malayo-Polynesian, North Borneo, Melanau-Kajang, Melanau
krd	Kairui-Midiki	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Timor-Babar, Nuclear Timor
krf	Koro	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, Remote Oceanic, North and Central Vanuatu, Northeast Vanuatu-Banks Islands, East Vanuatu
kxr	Koro	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Admiralty Islands, Eastern, Manus, East
kkv	Kangean	Austronesian, Malayo-Polynesian, Madurese
kei	Kei	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Southeast Maluku, Kei-Tanimbar, Kei-Fordata
krj	Kinaray-a	Austronesian, Malayo-Polynesian, Philippine, Greater Central Philippine, Central Philippine, Bisayan, West, Kinarayan
kkx	Kohin	Austronesian, Malayo-Polynesian, Greater Barito, West, North
kem	Kemak	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Timor-Babar, Nuclear Timor
kyb	Kalinga, Butbut	Austronesian, Malayo-Polynesian, Philippine, Northern Luzon, Meso-Cordilleran, South-Central Cordilleran, Central Cordilleran, North Central Cordilleran, Kalinga-Itneg, Kalinga
kyd	Karey	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Aru
klg	Tagakaulo	Austronesian, Malayo-Polynesian, Philippine, Greater Central Philippine, Central Philippine, Mansakan, Western
kli	Kalumpang	Austronesian, Malayo-Polynesian, South Sulawesi, Northern, Toraja-Sa’dan
kyi	Kiput	Austronesian, Malayo-Polynesian, North Borneo, North Sarawakan, Berawan-Lower Baram, Lower Baram, Central, A
kll	Kalagan, Kagan	Austronesian, Malayo-Polynesian, Philippine, Greater Central Philippine, Central Philippine, Mansakan, Western
kyj	Karao	Austronesian, Malayo-Polynesian, Philippine, Northern Luzon, Meso-Cordilleran, South-Central Cordilleran, Southern Cordilleran, West Southern Cordilleran, Nuclear Southern Cordilleran, Karaw
kyk	Kamayo	Austronesian, Malayo-Polynesian, Philippine, Greater Central Philippine, Central Philippine, Mansakan, Northern
ksc	Kalinga, Southern	Austronesian, Malayo-Polynesian, Philippine, Northern Luzon, Meso-Cordilleran, South-Central Cordilleran, Central Cordilleran, North Central Cordilleran, Kalinga-Itneg, Kalinga
ksd	Kuanua	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, Meso Melanesian, New Ireland, South New Ireland-Northwest Solomonic, Patpatar-Tolai
kse	Kuni	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, Papuan Tip, Peripheral, Central Papuan, West Central Papuan, Nuclear
kyn	Binukidnon, Northern	Austronesian, Malayo-Polynesian, Philippine, Greater Central Philippine, Central Philippine
ksg	Kusaghe	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, Meso Melanesian, New Ireland, South New Ireland-Northwest Solomonic, New Georgia, West
kys	Kayan, Baram	Austronesian, Malayo-Polynesian, North Borneo, North Sarawakan, Kayan-Kenyah, Kayanic, Kayan Proper
klv	Maskelynes	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, Remote Oceanic, North and Central Vanuatu, Northeast Vanuatu-Banks Islands, Malekula Coastal
klw	Lindu	Austronesian, Malayo-Polynesian, Celebic, Kaili-Pamona, Northern, Kaili
ksl	Kumalu	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, North New Guinea, Huon Gulf, South, Hote-Buang, Buang, Mumeng
klx	Koluwawa	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, Papuan Tip, Nuclear, North Papuan Mainland-D’Entrecasteaux, Bwaidoga
kly	Kalao	Austronesian, Malayo-Polynesian, Celebic, Wotu-Wolio, Kalao
ksn	Kasiguranin	Austronesian, Malayo-Polynesian, Philippine, Northern Luzon, Northern Cordilleran, Northeastern Luzon, Northern
kmd	Kalinga, Majukayang	Austronesian, Malayo-Polynesian, Philippine, Northern Luzon, Meso-Cordilleran, South-Central Cordilleran, Central Cordilleran, North Central Cordilleran, Kalinga-Itneg, Kalinga
kzb	Kaibobo	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Central Maluku, East, Seram, Nunusaku, Piru Bay, East
kzd	Kadai	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Central Maluku, Sula, Taliabo
kzf	Kaili, Da’a	Austronesian, Malayo-Polynesian, Celebic, Kaili-Pamona, Northern, Kaili
ksx	Kedang	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Bima-Lembata
kzi	Kelabit	Austronesian, Malayo-Polynesian, North Borneo, North Sarawakan, Dayic, Kelabitic
kmk	Kalinga, Limos	Austronesian, Malayo-Polynesian, Philippine, Northern Luzon, Meso-Cordilleran, South-Central Cordilleran, Central Cordilleran, North Central Cordilleran, Kalinga-Itneg, Kalinga
kzj	Kadazan, Coastal	Austronesian, Malayo-Polynesian, North Borneo, Sabahan, Dusunic, Dusun
kml	Kalinga, Tanudan	Austronesian, Malayo-Polynesian, Philippine, Northern Luzon, Meso-Cordilleran, South-Central Cordilleran, Central Cordilleran, North Central Cordilleran, Kalinga-Itneg, Kalinga
kzk	Kazukuru	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, Meso Melanesian, New Ireland, South New Ireland-Northwest Solomonic, New Georgia, West
kzl	Kayeli	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Central Maluku, East, Seram, Nunusaku, Kayeli
kgb	Kawe	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, South Halmahera-West New Guinea, West New Guinea, Cenderawasih Bay, Raja Ampat
kzp	Kaidipang	Austronesian, Malayo-Polynesian, Philippine, Greater Central Philippine, Gorontalo-Mongondow, Gorontalic
kge	Komering	Austronesian, Malayo-Polynesian, Lampung
kzs	Dusun, Sugut	Austronesian, Malayo-Polynesian, North Borneo, Sabahan, Dusunic, Dusun, Central
kzt	Dusun, Tambunan	Austronesian, Malayo-Polynesian, North Borneo, Sabahan, Dusunic, Dusun, Central
ktk	Kaniet	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Admiralty Islands, Western
kzu	Kayupulau	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, North New Guinea, Sarmi-Jayapura Bay, Jayapura Bay
ktm	Kurti	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Admiralty Islands, Eastern, Manus, East
kzx	Kamarian	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Central Maluku, East, Seram, Nunusaku, Piru Bay, East, Seram Straits, Uliase, Kamarian
knb	Kalinga, Lubuagan	Austronesian, Malayo-Polynesian, Philippine, Northern Luzon, Meso-Cordilleran, South-Central Cordilleran, Central Cordilleran, North Central Cordilleran, Kalinga-Itneg, Kalinga
ktq	Katabaga	Austronesian, Malayo-Polynesian, Unclassified
laa	Subanen, Southern	Austronesian, Malayo-Polynesian, Philippine, Greater Central Philippine, Subanon, Eastern
lpa	Lelepa	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, Remote Oceanic, North and Central Vanuatu, Northeast Vanuatu-Banks Islands, Central Vanuatu
ler	Lenkau	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Admiralty Islands, Eastern, Southeast Islands
let	Amio-Gelimi	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, North New Guinea, Ngero-Vitiaz, Vitiaz, Southwest New Britain, Arawe-Pasismanua, Arawe, East Arawe
leu	Kara	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, Meso Melanesian, New Ireland, Lavongai-Nalik
lle	Lele	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Admiralty Islands, Eastern, Manus, East
lra	Bakati’, Rara	Austronesian, Malayo-Polynesian, Land Dayak, Bakati’
lew	Kaili, Ledo	Austronesian, Malayo-Polynesian, Celebic, Kaili-Pamona, Northern, Kaili
llf	Hermit	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Admiralty Islands, Eastern, Manus, West
lex	Luang	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Timor-Babar, Southwest Maluku, Luang
llg	Lole	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Timor-Babar, Nuclear Timor, Rote
ley	Lemolang	Austronesian, Malayo-Polynesian, South Sulawesi, Lemolang
lga	Lungga	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, Meso Melanesian, New Ireland, South New Ireland-Northwest Solomonic, New Georgia, West
llk	Lelak	Austronesian, Malayo-Polynesian, North Borneo, North Sarawakan, Berawan-Lower Baram, Lower Baram, Central, B
lgb	Laghu	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, Meso Melanesian, New Ireland, South New Ireland-Northwest Solomonic, Santa Isabel, West
lrn	Lorang	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Aru
llm	Lasalimu	Austronesian, Malayo-Polynesian, Celebic, Eastern, Southeastern, Muna-Buton, Nuclear Muna-Buton, Buton, East Buton
lgi	Lengilu	Austronesian, Malayo-Polynesian, North Borneo, North Sarawakan, Dayic, Kelabitic
lgk	Neverver	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, Remote Oceanic, North and Central Vanuatu, Malekula Interior, Malekula Central
llp	Efate, North	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, Remote Oceanic, North and Central Vanuatu, Northeast Vanuatu-Banks Islands, Central Vanuatu
lrv	Larevat	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, Remote Oceanic, North and Central Vanuatu, Malekula Interior, Malekula Central
lgl	Wala	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, Southeast Solomonic, Malaita-San Cristobal, Malaita, Northern
llq	Lolak	Austronesian, Malayo-Polynesian, Philippine, Greater Central Philippine, Gorontalo-Mongondow, Gorontalic
lrz	Lemerig	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, Remote Oceanic, North and Central Vanuatu, Northeast Vanuatu-Banks Islands, East Vanuatu
llu	Lau	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, Southeast Solomonic, Malaita-San Cristobal, Malaita, Northern
law	Lauje	Austronesian, Malayo-Polynesian, Celebic, Tomini-Tolitoli, Tomini, Northern
llx	Lauan	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, Remote Oceanic, Central Pacific, East Fijian-Polynesian, East Fijian
lgr	Lengo	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, Southeast Solomonic, Gela-Guadalcanal, Gela
lmb	Merei	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, Remote Oceanic, North and Central Vanuatu, Northeast Vanuatu-Banks Islands, West Santo
laz	Aribwatsa	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, North New Guinea, Huon Gulf, Markham, Lower, Busu
lgu	Longgu	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, Southeast Solomonic, Malaita-San Cristobal, Malaita, Longgu
lbb	Label	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, Meso Melanesian, New Ireland, South New Ireland-Northwest Solomonic, Patpatar-Tolai
lhh	Laha	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Central Maluku, East, Seram, Nunusaku, Piru Bay, East, Seram Straits, Ambon
lmf	Lembata, South	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Bima-Lembata
lmg	Lamogai	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, North New Guinea, Ngero-Vitiaz, Vitiaz, Southwest New Britain, Bibling
lhn	Lahanan	Austronesian, Malayo-Polynesian, North Borneo, Melanau-Kajang, Kajang
lmj	Lembata, West	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Bima-Lembata
lbk	Bontok, Central	Austronesian, Malayo-Polynesian, Philippine, Northern Luzon, Meso-Cordilleran, South-Central Cordilleran, Central Cordilleran, North Central Cordilleran, Nuclear Cordilleran, Bontok-Kankanay, Bontok
lml	Hano	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, Remote Oceanic, North and Central Vanuatu, Northeast Vanuatu-Banks Islands, East Vanuatu
lbl	Bikol, Libon	Austronesian, Malayo-Polynesian, Philippine, Greater Central Philippine, Central Philippine, Bikol, Inland
lht	Lo-Toga	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, Remote Oceanic, North and Central Vanuatu, Northeast Vanuatu-Banks Islands, East Vanuatu
lti	Leti	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Timor-Babar, Southwest Maluku, Luang
lib	Likum	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Admiralty Islands, Eastern, Manus, West
lbq	Wampar	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, North New Guinea, Huon Gulf, Markham, Lower, Wampar
lmq	Lamatuka	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Bima-Lembata
ltu	Latu	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Central Maluku, East, Seram, Nunusaku, Piru Bay, East, Seram Straits, Uliase, Hatuhaha, Saparua
lid	Nyindrou	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Admiralty Islands, Eastern, Manus, West
lmr	Lamalera	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Bima-Lembata
lmu	Lamenu	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, Remote Oceanic, North and Central Vanuatu, Northeast Vanuatu-Banks Islands, Epi, Lamenu-Baki, Lamenu-Lewo
lmv	Lomaiviti	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, Remote Oceanic, Central Pacific, East Fijian-Polynesian, East Fijian
lbu	Labu	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, North New Guinea, Huon Gulf, Markham, Lower, Labu
lbv	Lavatbura-Lamusong	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, Meso Melanesian, New Ireland, Madak
lih	Lihir	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, Meso Melanesian, New Ireland, Tabar
lbw	Tolaki	Austronesian, Malayo-Polynesian, Celebic, Eastern, Southeastern, Bungku-Tolaki, Western, West Coast
lmy	Lamboya	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Sumba-Hawu, Sumba
lbx	Lawangan	Austronesian, Malayo-Polynesian, Greater Barito, East, North
lcc	Legenyem	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, South Halmahera-West New Guinea, West New Guinea, Cenderawasih Bay, Raja Ampat
lnd	Lun Bawang	Austronesian, Malayo-Polynesian, North Borneo, North Sarawakan, Dayic, Kelabitic
lcd	Lola	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Aru
lce	Sekak	Austronesian, Malayo-Polynesian, Malayo-Chamic, Malayic, Malay
lio	Liki	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, North New Guinea, Sarmi-Jayapura Bay, Sarmi
lcf	Lubu	Austronesian, Malayo-Polynesian, Malayo-Chamic, Malayic, Malay
lcl	Lisela	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Central Maluku, Buru
lcm	Tungag	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, Meso Melanesian, New Ireland, Lavongai-Nalik
lnn	Lorediakarkar	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, Remote Oceanic, North and Central Vanuatu, East Santo, South
lcs	Lisabata-Nuniali	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Central Maluku, East, Seram, Nunusaku, Three Rivers, Amalumute, Northwest Seram
lur	Laura	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Sumba-Hawu, Sumba
liw	Col	Austronesian, Malayo-Polynesian, Malayo-Chamic, Malayic, Malay
lix	Liabuku	Austronesian, Malayo-Polynesian, Celebic, Eastern, Southeastern, Muna-Buton, Nuclear Muna-Buton, Munan, Munic, Western
loc	Inonhan	Austronesian, Malayo-Polynesian, Philippine, Greater Central Philippine, Central Philippine, Bisayan, West, North Central
lje	Rampi	Austronesian, Malayo-Polynesian, Celebic, Kaili-Pamona, Southern
loe	Saluan	Austronesian, Malayo-Polynesian, Celebic, Eastern, Saluan-Banggai, Western, Saluanic
lji	Laiyolo	Austronesian, Malayo-Polynesian, Celebic, Wotu-Wolio, Kalao
lva	Makuva	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Timor-Babar, Nuclear Timor
ljl	Li’o	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Bima-Lembata
ljp	Lampung Api	Austronesian, Malayo-Polynesian, Lampung
lvu	Levuka	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Bima-Lembata
loj	Lou	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Admiralty Islands, Eastern, Southeast Islands
lka	Lakalei	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Timor-Babar, Nuclear Timor
lwe	Lewo Eleng	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Bima-Lembata
lwt	Lewotobi	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Bima-Lembata
lkj	Remun	Austronesian, Malayo-Polynesian, Malayo-Chamic, Malayic, Ibanic
los	Loniu	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Admiralty Islands, Eastern, Manus, Mokoreng-Loniu
lww	Lewo	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, Remote Oceanic, North and Central Vanuatu, Northeast Vanuatu-Banks Islands, Epi, Lamenu-Baki, Lamenu-Lewo
lkn	Lakon	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, Remote Oceanic, North and Central Vanuatu, Northeast Vanuatu-Banks Islands, East Vanuatu
lek	Leipon	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Admiralty Islands, Eastern, Manus, East
low	Lobu, Tampias	Austronesian, Malayo-Polynesian, North Borneo, Sabahan, Paitanic, Upper Kinabatangan
lzl	Litzlitz	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, Remote Oceanic, North and Central Vanuatu, Malekula Interior, Malekula Central
lox	Loun	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Central Maluku, East, Seram, Nunusaku, Three Rivers, Amalumute, Northwest Seram, Loun
mgl	Maleu-Kilenge	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, North New Guinea, Ngero-Vitiaz, Vitiaz, Kilenge-Maleu
mgm	Mambae	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Timor-Babar, Nuclear Timor
mna	Mbula	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, North New Guinea, Ngero-Vitiaz, Vitiaz, Mangap-Mbula
mad	Madura	Austronesian, Malayo-Polynesian, Madurese
mnb	Muna	Austronesian, Malayo-Polynesian, Celebic, Eastern, Southeastern, Muna-Buton, Nuclear Muna-Buton, Munan, Munic, Western
mah	Marshallese	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, Remote Oceanic, Micronesian, Micronesian Proper, Marshallese
mtt	Mota	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, Remote Oceanic, North and Central Vanuatu, Northeast Vanuatu-Banks Islands, East Vanuatu
mak	Makasar	Austronesian, Malayo-Polynesian, South Sulawesi, Makassar
mtw	Binukidnon, Southern	Austronesian, Malayo-Polynesian, Philippine, Greater Central Philippine, Central Philippine
mnl	Tiale	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, Remote Oceanic, North and Central Vanuatu, Northeast Vanuatu-Banks Islands, West Santo
mnv	Rennell-Bellona	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, Remote Oceanic, Central Pacific, East Fijian-Polynesian, Polynesian, Nuclear, Samoic-Outlier, Futunic
mui	Musi	Austronesian, Malayo-Polynesian, Malayo-Chamic, Malayic, Malay
mba	Higaonon	Austronesian, Malayo-Polynesian, Philippine, Greater Central Philippine, Manobo, North
mbb	Manobo, Western Bukidnon	Austronesian, Malayo-Polynesian, Philippine, Greater Central Philippine, Manobo, Central, West
mum	Maiwala	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, Papuan Tip, Nuclear, North Papuan Mainland-D’Entrecasteaux, Are-Taupota, Taupota
mbd	Manobo, Dibabawon	Austronesian, Malayo-Polynesian, Philippine, Greater Central Philippine, Manobo, Central, East
mbh	Mangseng	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, North New Guinea, Ngero-Vitiaz, Vitiaz, Southwest New Britain, Arawe-Pasismanua, Arawe
mog	Mongondow	Austronesian, Malayo-Polynesian, Philippine, Greater Central Philippine, Gorontalo-Mongondow, Mongondowic
mbi	Manobo, Ilianen	Austronesian, Malayo-Polynesian, Philippine, Greater Central Philippine, Manobo, Central, West
mbk	Malol	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, North New Guinea, Schouten, Siau
mhs	Buru	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Central Maluku, Buru
mva	Manam	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, North New Guinea, Schouten, Kairiru-Manam, Manam
mbq	Maisin	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, Papuan Tip, Nuclear, Maisin
mhy	Ma’anyan	Austronesian, Malayo-Polynesian, Greater Barito, East, Central-South, South
mhz	Mor	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, South Halmahera-West New Guinea, West New Guinea, Cenderawasih Bay, Mor
mvd	Mamboru	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Sumba-Hawu, Sumba
mbs	Manobo, Sarangani	Austronesian, Malayo-Polynesian, Philippine, Greater Central Philippine, Manobo, South
mbt	Manobo, Matigsalug	Austronesian, Malayo-Polynesian, Philippine, Greater Central Philippine, Manobo, Central, South, Ata-Tigwa
mox	Molima	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, Papuan Tip, Nuclear, North Papuan Mainland-D’Entrecasteaux, Bwaidoga
mvn	Minaveha	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, Papuan Tip, Nuclear, North Papuan Mainland-D’Entrecasteaux, Are-Taupota, Taupota
mvo	Marovo	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, Meso Melanesian, New Ireland, South New Ireland-Northwest Solomonic, New Georgia, East
mvp	Duri	Austronesian, Malayo-Polynesian, South Sulawesi, Northern, Masenrempulu
mvr	Marau	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, South Halmahera-West New Guinea, West New Guinea, Cenderawasih Bay, Yapen, Central-Western
min	Minangkabau	Austronesian, Malayo-Polynesian, Malayo-Chamic, Malayic, Malay
mvt	Mpotovoro	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, Remote Oceanic, North and Central Vanuatu, Northeast Vanuatu-Banks Islands, Malekula Coastal
mvv	Tagal Murut	Austronesian, Malayo-Polynesian, North Borneo, North Sarawakan, Dayic, Murutic, Murut
mpl	Watut, Middle	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, North New Guinea, Huon Gulf, Markham, Watut
mvx	Meoswar	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, South Halmahera-West New Guinea, West New Guinea, Cenderawasih Bay, Biakic
mpn	Mindiri	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, North New Guinea, Ngero-Vitiaz, Vitiaz, Bel, Astrolabe
mpo	Miu	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, North New Guinea, Ngero-Vitiaz, Vitiaz, Southwest New Britain, Arawe-Pasismanua, Pasismanua
mwa	Mwatebu	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, Papuan Tip, Nuclear, North Papuan Mainland-D’Entrecasteaux, Dobu-Duau
mwc	Are	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, Papuan Tip, Nuclear, North Papuan Mainland-D’Entrecasteaux, Are-Taupota, Are
mpr	Vangunu	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, Meso Melanesian, New Ireland, South New Ireland-Northwest Solomonic, New Georgia, East
mwg	Aiklep	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, North New Guinea, Ngero-Vitiaz, Vitiaz, Southwest New Britain, Arawe-Pasismanua, Arawe, West Arawe
mwh	Mouk-Aria	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, North New Guinea, Ngero-Vitiaz, Vitiaz, Southwest New Britain, Bibling
mwi	Ninde	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, Remote Oceanic, North and Central Vanuatu, Malekula Interior, Labo
mpx	Misima-Panaeati	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, Papuan Tip, Peripheral, Kilivila-Louisiades, Misima
mjk	Matukar	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, North New Guinea, Ngero-Vitiaz, Vitiaz, Bel, Nuclear Bel, Northern
mpy	Mapia	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, Remote Oceanic, Micronesian, Micronesian Proper, Ponapeic-Trukic, Trukic
mcy	Watut, South	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, North New Guinea, Huon Gulf, Markham, Watut
mjm	Medebur	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, North New Guinea, Schouten, Kairiru-Manam, Manam
mqa	Maba	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, South Halmahera-West New Guinea, South Halmahera, Southeast
mwo	Maewo, Central	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, Remote Oceanic, North and Central Vanuatu, Northeast Vanuatu-Banks Islands, East Vanuatu
mqc	Mangole	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Central Maluku, Sula
mqg	Malay, Kota Bangun Kutai	Austronesian, Malayo-Polynesian, Malayo-Chamic, Malayic, Malay
mwt	Moken	Austronesian, Malayo-Polynesian, Moklen
mqi	Mariri	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Aru
mdh	Maguindanaon	Austronesian, Malayo-Polynesian, Philippine, Greater Central Philippine, Danao, Magindanao
mqj	Mamasa	Austronesian, Malayo-Polynesian, South Sulawesi, Northern, Toraja-Sa’dan
mwv	Mentawai	Austronesian, Malayo-Polynesian, Northwest Sumatra-Barrier Islands
mqk	Manobo, Rajah Kabunsuwan	Austronesian, Malayo-Polynesian, Philippine, Greater Central Philippine, Manobo, Central, East
mqm	Marquesan, South	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, Remote Oceanic, Central Pacific, East Fijian-Polynesian, Polynesian, Nuclear, East, Central, Marquesic
mqn	Moronene	Austronesian, Malayo-Polynesian, Celebic, Eastern, Southeastern, Bungku-Tolaki, Eastern, Southwest
mqp	Manipa	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Central Maluku, East
mqq	Minokok	Austronesian, Malayo-Polynesian, North Borneo, Sabahan, Dusunic, Dusun, Central
mxd	Modang	Austronesian, Malayo-Polynesian, North Borneo, North Sarawakan, Kayan-Kenyah, Kayanic, Modang
mdr	Mandar	Austronesian, Malayo-Polynesian, South Sulawesi, Northern, Mandar
mxe	Mele-Fila	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, Remote Oceanic, Central Pacific, East Fijian-Polynesian, Polynesian, Nuclear, Samoic-Outlier, Futunic
mkj	Mokilese	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, Remote Oceanic, Micronesian, Micronesian Proper, Ponapeic-Trukic, Ponapeic
mqx	Mamuju	Austronesian, Malayo-Polynesian, South Sulawesi, Northern, Mamuju
mqy	Manggarai	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Bima-Lembata
mkm	Moklen	Austronesian, Malayo-Polynesian, Moklen
mqz	Pano	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, North New Guinea, Ngero-Vitiaz, Vitiaz, Korap
mxm	Meramera	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, Meso Melanesian, Willaumez
mrb	Marino	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, Remote Oceanic, North and Central Vanuatu, Northeast Vanuatu-Banks Islands, East Vanuatu
mxr	Murik	Austronesian, Malayo-Polynesian, North Borneo, North Sarawakan, Kayan-Kenyah, Kayanic, Murik Kayan
mee	Mengen	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, North New Guinea, Ngero-Vitiaz, Vitiaz, Mengen
mkt	Vamale	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, Remote Oceanic, New Caledonian, Northern
mkv	Mafea	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, Remote Oceanic, North and Central Vanuatu, Northeast Vanuatu-Banks Islands, West Santo
mri	Maori	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, Remote Oceanic, Central Pacific, East Fijian-Polynesian, Polynesian, Nuclear, East, Central, Tahitic
mkx	Manobo, Kinamiging	Austronesian, Malayo-Polynesian, Philippine, Greater Central Philippine, Manobo, North
mrk	Hmwaveke	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, Remote Oceanic, New Caledonian, Northern, North, Hmwaveke
mek	Mekeo	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, Papuan Tip, Peripheral, Central Papuan, West Central Papuan, Nuclear
mky	Makian, East	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, South Halmahera-West New Guinea, South Halmahera, East Makian-Gane
mrl	Mortlockese	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, Remote Oceanic, Micronesian, Micronesian Proper, Ponapeic-Trukic, Trukic
mel	Melanau, Central	Austronesian, Malayo-Polynesian, North Borneo, Melanau-Kajang, Melanau
mrm	Mwerlap	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, Remote Oceanic, North and Central Vanuatu, Northeast Vanuatu-Banks Islands, East Vanuatu
mla	Malo	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, Remote Oceanic, North and Central Vanuatu, Northeast Vanuatu-Banks Islands, West Santo
mrn	Cheke Holo	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, Meso Melanesian, New Ireland, South New Ireland-Northwest Solomonic, Santa Isabel, East
mxz	Masela, Central	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Babar, South, Masela-South Babar
meo	Malay, Kedah	Austronesian, Malayo-Polynesian, Malayo-Chamic, Malayic, Malay
mrp	Morouas	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, Remote Oceanic, North and Central Vanuatu, Northeast Vanuatu-Banks Islands, West Santo
mrq	Marquesan, North	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, Remote Oceanic, Central Pacific, East Fijian-Polynesian, Polynesian, Nuclear, East, Central, Marquesic
mrs	Maragus	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, Remote Oceanic, North and Central Vanuatu, Malekula Interior, Malekula Central
met	Mato	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, North New Guinea, Ngero-Vitiaz, Vitiaz, Roinji-Nenaya
mli	Malimpung	Austronesian, Malayo-Polynesian, South Sulawesi, Northern, Masenrempulu
meu	Motu	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, Papuan Tip, Peripheral, Central Papuan, Sinagoro-Keapara
mrv	Mangareva	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, Remote Oceanic, Central Pacific, East Fijian-Polynesian, Polynesian, Nuclear, East, Central, Marquesic
mrw	Maranao	Austronesian, Malayo-Polynesian, Philippine, Greater Central Philippine, Danao, Maranao-Iranon
mll	Malua Bay	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, Remote Oceanic, North and Central Vanuatu, Northeast Vanuatu-Banks Islands, Malekula Coastal
mry	Mandaya	Austronesian, Malayo-Polynesian, Philippine, Greater Central Philippine, Central Philippine, Mansakan, Eastern
mln	Malango	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, Southeast Solomonic, Gela-Guadalcanal, Guadalcanal
myl	Moma	Austronesian, Malayo-Polynesian, Celebic, Kaili-Pamona, Northern, Kaili
mfa	Malay, Pattani	Austronesian, Malayo-Polynesian, Malayo-Chamic, Malayic, Malay
mfb	Bangka	Austronesian, Malayo-Polynesian, Malayo-Chamic, Malayic, Malay
msb	Masbatenyo	Austronesian, Malayo-Polynesian, Philippine, Greater Central Philippine, Central Philippine, Bisayan, Central, Peripheral
mlu	To’abaita	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, Southeast Solomonic, Malaita-San Cristobal, Malaita, Northern
mlv	Mwotlap	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, Remote Oceanic, North and Central Vanuatu, Northeast Vanuatu-Banks Islands, East Vanuatu
msh	Malagasy, Masikoro	Austronesian, Malayo-Polynesian, Greater Barito, East, Malagasy
myw	Muyuw	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, Papuan Tip, Peripheral, Kilivila-Louisiades, Kilivila
msi	Malay, Sabah	Austronesian, Malayo-Polynesian, Malayo-Chamic, Malayic, Malay
mlx	Naha’ai	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, Remote Oceanic, North and Central Vanuatu, Northeast Vanuatu-Banks Islands, Malekula Coastal
mlz	Malaynon	Austronesian, Malayo-Polynesian, Philippine, Greater Central Philippine, Central Philippine, Bisayan, West, Aklan
msk	Mansaka	Austronesian, Malayo-Polynesian, Philippine, Greater Central Philippine, Central Philippine, Mansakan, Eastern
msm	Manobo, Agusan	Austronesian, Malayo-Polynesian, Philippine, Greater Central Philippine, Manobo, Central, East
msn	Vurës	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, Remote Oceanic, North and Central Vanuatu, Northeast Vanuatu-Banks Islands, East Vanuatu
mfp	Malay, Makassar	Austronesian, Malayo-Polynesian, Malayo-Chamic, Malayic, Malay
mme	Mae	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, Remote Oceanic, North and Central Vanuatu, Northeast Vanuatu-Banks Islands, Malekula Coastal
msq	Caac	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, Remote Oceanic, New Caledonian, Northern, Extreme Northern
mmg	Ambrym, North	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, Remote Oceanic, North and Central Vanuatu, Northeast Vanuatu-Banks Islands, East Vanuatu
mss	Masela, West	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Babar, South, Masela-South Babar
mft	Mokerang	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Admiralty Islands, Eastern, Manus, Mokoreng-Loniu
msu	Musom	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, North New Guinea, Huon Gulf, Markham, Lower, Busu
mmm	Maii	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, Remote Oceanic, North and Central Vanuatu, Northeast Vanuatu-Banks Islands, Epi, Bieria-Maii
mmn	Mamanwa	Austronesian, Malayo-Polynesian, Philippine, Greater Central Philippine, Central Philippine, Mamanwa
mmo	Buang, Mangga	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, North New Guinea, Huon Gulf, South, Hote-Buang, Buang
mta	Manobo, Cotabato	Austronesian, Malayo-Polynesian, Philippine, Greater Central Philippine, Manobo, South
mzq	Mori Atas	Austronesian, Malayo-Polynesian, Celebic, Eastern, Southeastern, Bungku-Tolaki, Western, Interior
mtd	Mualang	Austronesian, Malayo-Polynesian, Malayo-Chamic, Malayic, Ibanic
mmt	Malalamai	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, North New Guinea, Ngero-Vitiaz, Ngero, Bariai
mte	Mono	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, Meso Melanesian, New Ireland, South New Ireland-Northwest Solomonic, Mono-Uruava
mmw	Emae	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, Remote Oceanic, Central Pacific, East Fijian-Polynesian, Polynesian, Nuclear, Samoic-Outlier, Futunic
mth	Munggui	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, South Halmahera-West New Guinea, West New Guinea, Cenderawasih Bay, Yapen, Central-Western
mmx	Madak	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, Meso Melanesian, New Ireland, Madak
mzz	Maiadomu	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, Papuan Tip, Nuclear, North Papuan Mainland-D’Entrecasteaux, Bwaidoga
nfl	Äiwoo	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Temotu, Reefs-Santa Cruz
nlg	Gela	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, Southeast Solomonic, Gela-Guadalcanal, Gela
nae	Naka’ela	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Central Maluku, East, Seram, Nunusaku, Three Rivers, Amalumute, Northwest Seram, Ulat Inai
nak	Nakanai	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, Meso Melanesian, Willaumez
nsn	Nehan	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, Meso Melanesian, New Ireland, South New Ireland-Northwest Solomonic, Nehan-North Bougainville, Nehan
nal	Nalik	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, Meso Melanesian, New Ireland, Lavongai-Nalik
nss	Nali	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Admiralty Islands, Eastern, Manus, East
nlz	Nalögo	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Temotu, Reefs-Santa Cruz
nmb	V’ënen Taut	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, Remote Oceanic, North and Central Vanuatu, Malekula Interior, Malekula Central
nsw	Navut	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, Remote Oceanic, North and Central Vanuatu, Northeast Vanuatu-Banks Islands, West Santo
nau	Nauruan	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, Remote Oceanic, Micronesian, Nauruan
ngr	Engdewu	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Temotu, Reefs-Santa Cruz
nsy	Nasal	Austronesian, Malayo-Polynesian, Nasal
nmk	Namakura	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, Remote Oceanic, North and Central Vanuatu, Northeast Vanuatu-Banks Islands, Central Vanuatu
ntu	Natügu	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Temotu, Reefs-Santa Cruz
nms	Letemboi	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, Remote Oceanic, North and Central Vanuatu, Malekula Interior, Small Nambas
nmt	Namonuito	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, Remote Oceanic, Micronesian, Micronesian Proper, Ponapeic-Trukic, Trukic
nbn	Kuri	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Unclassified
nua	Yuanga	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, Remote Oceanic, New Caledonian, Northern, Extreme Northern
nmw	Nimoa	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, Papuan Tip, Peripheral, Kilivila-Louisiades, Nimoa-Sudest
nho	Takuu	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, Remote Oceanic, Central Pacific, East Fijian-Polynesian, Polynesian, Nuclear, Samoic-Outlier, Ellicean
nnd	Ambae, West	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, Remote Oceanic, North and Central Vanuatu, Northeast Vanuatu-Banks Islands, East Vanuatu
nul	Nusa Laut	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Central Maluku, East, Seram, Nunusaku, Piru Bay, East, Seram Straits, Uliase, Hatuhaha, Elpaputi
num	Niuafo’ou	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, Remote Oceanic, Central Pacific, East Fijian-Polynesian, Polynesian, Nuclear, Samoic-Outlier, East Uvean-Niuafo’ou
ncc	Ponam	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Admiralty Islands, Eastern, Manus, East
nni	Nuaulu, North	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Central Maluku, East, Seram, Sawai-Nuaulu
nia	Nias	Austronesian, Malayo-Polynesian, Northwest Sumatra-Barrier Islands, Nias
nuq	Nukumanu	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, Remote Oceanic, Central Pacific, East Fijian-Polynesian, Polynesian, Nuclear, Samoic-Outlier, Ellicean
ncf	Notsi	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, Meso Melanesian, New Ireland, Tabar
nur	Nukuria	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, Remote Oceanic, Central Pacific, East Fijian-Polynesian, Polynesian, Nuclear, Samoic-Outlier, Ellicean
ncn	Nauna	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Admiralty Islands, Eastern, Southeast Islands
nij	Ngaju	Austronesian, Malayo-Polynesian, Greater Barito, West, South
nil	Nila	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Timor-Babar, Southwest Maluku, Teun-Nila-Serua, Nila-Serua
nvh	Nasarian	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, Remote Oceanic, North and Central Vanuatu, Malekula Interior, Malekula Central
nwi	Tanna, Southwest	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, South Vanuatu, Tanna
niu	Niue	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, Remote Oceanic, Central Pacific, East Fijian-Polynesian, Polynesian, Tongic
nxa	Nauete	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Timor-Babar, Nuclear Timor
nxe	Nage	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Bima-Lembata
nxg	Ngad’a	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Bima-Lembata
nxl	Nuaulu, South	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Central Maluku, East, Seram, Sawai-Nuaulu
npn	Mondropolon	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Admiralty Islands, Eastern, Manus, West
nea	Ngad’a, Eastern	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Bima-Lembata
nke	Duke	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, Meso Melanesian, New Ireland, South New Ireland-Northwest Solomonic, New Georgia, West
npy	Napu	Austronesian, Malayo-Polynesian, Celebic, Kaili-Pamona, Southern, Badaic
nee	Nêlêmwa-Nixumwak	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, Remote Oceanic, New Caledonian, Northern, Extreme Northern
nek	Neku	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, Remote Oceanic, New Caledonian, Southern, South, Wailic
nkk	Nokuku	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, Remote Oceanic, North and Central Vanuatu, Northeast Vanuatu-Banks Islands, West Santo
nem	Nemi	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, Remote Oceanic, New Caledonian, Northern, North, Nemi
nen	Nengone	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, Remote Oceanic, Loyalty Islands
nkr	Nukuoro	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, Remote Oceanic, Central Pacific, East Fijian-Polynesian, Polynesian, Nuclear, Samoic-Outlier, Ellicean
nrg	Narango	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, Remote Oceanic, North and Central Vanuatu, Northeast Vanuatu-Banks Islands, West Santo
nrm	Narom	Austronesian, Malayo-Polynesian, North Borneo, North Sarawakan, Berawan-Lower Baram, Lower Baram, Central, B
nrz	Lala	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, Papuan Tip, Peripheral, Central Papuan, West Central Papuan, Nuclear
nfa	Dhao	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Sumba-Hawu, Hawu-Dhao
orz	Ormu	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, North New Guinea, Sarmi-Jayapura Bay, Jayapura Bay
obk	Bontok, Southern	Austronesian, Malayo-Polynesian, Philippine, Northern Luzon, Meso-Cordilleran, South-Central Cordilleran, Central Cordilleran, North Central Cordilleran, Nuclear Cordilleran, Bontok-Kankanay, Bontok
osi	Osing	Austronesian, Malayo-Polynesian, Javanese
obo	Manobo, Obo	Austronesian, Malayo-Polynesian, Philippine, Greater Central Philippine, Manobo, Central, South, Obo
onu	Unua	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, Remote Oceanic, North and Central Vanuatu, Northeast Vanuatu-Banks Islands, Malekula Coastal
otd	Ot Danum	Austronesian, Malayo-Polynesian, Greater Barito, West, North
olr	Olrat	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, Remote Oceanic, North and Central Vanuatu, Northeast Vanuatu-Banks Islands, East Vanuatu
omb	Ambae, East	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, Remote Oceanic, North and Central Vanuatu, Northeast Vanuatu-Banks Islands, East Vanuatu
ora	Oroha	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, Southeast Solomonic, Malaita-San Cristobal, Malaita, Southern
orn	Orang Kanaq	Austronesian, Malayo-Polynesian, Malayo-Chamic, Malayic, Malay
oum	Ouma	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, Papuan Tip, Peripheral, Central Papuan, Oumic
ojv	Ontong Java	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, Remote Oceanic, Central Pacific, East Fijian-Polynesian, Polynesian, Nuclear, Samoic-Outlier, Ellicean
ors	Orang Seletar	Austronesian, Malayo-Polynesian, Malayo-Chamic, Malayic, Malay
oni	Onin	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, North Bomberai
oyy	Oya’oya	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, Papuan Tip, Nuclear, Suauic
pmf	Pamona	Austronesian, Malayo-Polynesian, Celebic, Kaili-Pamona, Northern, Pamona
pri	Paicî	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, Remote Oceanic, New Caledonian, Northern, Central
pag	Pangasinan	Austronesian, Malayo-Polynesian, Philippine, Northern Luzon, Meso-Cordilleran, South-Central Cordilleran, Southern Cordilleran, West Southern Cordilleran
pgk	Rerep	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, Remote Oceanic, North and Central Vanuatu, Northeast Vanuatu-Banks Islands, Malekula Coastal
pmo	Pom	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, South Halmahera-West New Guinea, West New Guinea, Cenderawasih Bay, Yapen, Central-Western
pam	Pampangan	Austronesian, Malayo-Polynesian, Philippine, Central Luzon, Pampangan
pmt	Tuamotuan	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, Remote Oceanic, Central Pacific, East Fijian-Polynesian, Polynesian, Nuclear, East, Central, Tahitic
pat	Papitalai	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Admiralty Islands, Eastern, Manus, East
pna	Penan, Bah-Biau	Austronesian, Malayo-Polynesian, North Borneo, Rejang-Sajau
pau	Palauan	Austronesian, Malayo-Polynesian, Palauan
pnc	Pannei	Austronesian, Malayo-Polynesian, South Sulawesi, Northern, Pitu Ulunna Salu
pse	Malay, Central	Austronesian, Malayo-Polynesian, Malayo-Chamic, Malayic, Malay
pne	Penan, Western	Austronesian, Malayo-Polynesian, North Borneo, North Sarawakan, Kayan-Kenyah, Penan
pnh	Penrhyn	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, Remote Oceanic, Central Pacific, East Fijian-Polynesian, Polynesian, Nuclear, East, Central, Tahitic
pni	Aoheng	Austronesian, Malayo-Polynesian, North Borneo, North Sarawakan, Kayan-Kenyah, Kayanic, Muller-Schwaner ‘Punan’
psn	Panasuan	Austronesian, Malayo-Polynesian, South Sulawesi, Seko, Panasuan
pnm	Punan Batu 1	Austronesian, Malayo-Polynesian, North Borneo, Melanau-Kajang, Kajang
pif	Pingelapese	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, Remote Oceanic, Micronesian, Micronesian Proper, Ponapeic-Trukic, Ponapeic
pnp	Pancana	Austronesian, Malayo-Polynesian, Celebic, Eastern, Southeastern, Muna-Buton, Nuclear Muna-Buton, Munan, Munic, Western
pss	Kaulong	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, North New Guinea, Ngero-Vitiaz, Vitiaz, Southwest New Britain, Arawe-Pasismanua, Pasismanua
pns	Ponosakan	Austronesian, Malayo-Polynesian, Philippine, Greater Central Philippine, Gorontalo-Mongondow, Mongondowic
psw	Port Sandwich	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, Remote Oceanic, North and Central Vanuatu, Northeast Vanuatu-Banks Islands, Malekula Coastal
ptn	Patani	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, South Halmahera-West New Guinea, South Halmahera, Southeast
ptp	Patep	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, North New Guinea, Huon Gulf, South, Hote-Buang, Buang, Mumeng
ptr	Piamatsina	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, Remote Oceanic, North and Central Vanuatu, Northeast Vanuatu-Banks Islands, West Santo
piv	Vaeakau-Taumako	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, Remote Oceanic, Central Pacific, East Fijian-Polynesian, Polynesian, Nuclear, Samoic-Outlier, Futunic
ptt	Enrekang	Austronesian, Malayo-Polynesian, South Sulawesi, Northern, Masenrempulu
ptu	Bambam	Austronesian, Malayo-Polynesian, South Sulawesi, Northern, Pitu Ulunna Salu
pix	Piu	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, North New Guinea, Huon Gulf, South, Hote-Buang, Buang
ptv	Port Vato	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, Remote Oceanic, North and Central Vanuatu, Northeast Vanuatu-Banks Islands, East Vanuatu
piz	Pije	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, Remote Oceanic, New Caledonian, Northern, North, Nemi
puc	Punan Merap	Austronesian, Malayo-Polynesian, North Borneo, Rejang-Sajau
pkg	Pak-Tong	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Admiralty Islands, Eastern, Pak-Tong
pud	Punan Aput	Austronesian, Malayo-Polynesian, North Borneo, North Sarawakan, Kayan-Kenyah, Kayanic, Muller-Schwaner ‘Punan’
pon	Pohnpeian	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, Remote Oceanic, Micronesian, Micronesian Proper, Ponapeic-Trukic, Ponapeic
puf	Punan Merah	Austronesian, Malayo-Polynesian, North Borneo, North Sarawakan, Kayan-Kenyah, Kayanic, Muller-Schwaner ‘Punan’
pkp	Pukapuka	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, Remote Oceanic, Central Pacific, East Fijian-Polynesian, Polynesian, Nuclear, Samoic-Outlier, Pukapuka
pop	Pwapwâ	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, Remote Oceanic, New Caledonian, Northern, North
puj	Punan Tubu	Austronesian, Malayo-Polynesian, North Borneo, North Sarawakan, Punan Tubu
pku	Paku	Austronesian, Malayo-Polynesian, Greater Barito, East, Central-South, South
plb	Polonombauk	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, Remote Oceanic, North and Central Vanuatu, East Santo, South
plc	Palawano, Central	Austronesian, Malayo-Polynesian, Philippine, Greater Central Philippine, Palawanic
pdn	Fedan	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, North New Guinea, Sarmi-Jayapura Bay, Sarmi
put	Putoh	Austronesian, Malayo-Polynesian, North Borneo, North Sarawakan, Dayic, Kelabitic
pdo	Padoe	Austronesian, Malayo-Polynesian, Celebic, Eastern, Southeastern, Bungku-Tolaki, Western, Interior
ple	Palu’e	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Bima-Lembata
puw	Puluwatese	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, Remote Oceanic, Micronesian, Micronesian Proper, Ponapeic-Trukic, Trukic
plh	Paulohi	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Central Maluku, East, Seram, Nunusaku, Piru Bay, East, Seram Straits, Solehua
ppk	Uma	Austronesian, Malayo-Polynesian, Celebic, Kaili-Pamona, Southern
ppm	Papuma	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, South Halmahera-West New Guinea, West New Guinea, Cenderawasih Bay, Yapen, Central-Western
ppn	Papapana	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, Meso Melanesian, New Ireland, South New Ireland-Northwest Solomonic, Nehan-North Bougainville, Papapana
pee	Taje	Austronesian, Malayo-Polynesian, Celebic, Tomini-Tolitoli, Tomini, Southern
pwg	Gapapaiwa	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, Papuan Tip, Nuclear, North Papuan Mainland-D’Entrecasteaux, Are-Taupota, Are
ppr	Luhu	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Central Maluku, East, Seram, Nunusaku, Three Rivers, Amalumute, Northwest Seram
pwm	Molbog	Austronesian, Malayo-Polynesian, Philippine, Greater Central Philippine, Palawanic
pwn	Paiwan	Austronesian, Paiwan
pek	Penchal	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Admiralty Islands, Eastern, Southeast Islands
plt	Malagasy, Plateau	Austronesian, Malayo-Polynesian, Greater Barito, East, Malagasy
ppu	Papora-Hoanya	Austronesian, Western Plains, Central Western Plains
pel	Pekal	Austronesian, Malayo-Polynesian, Malayo-Chamic, Malayic, Malay
plv	Palawano, Southwest	Austronesian, Malayo-Polynesian, Philippine, Greater Central Philippine, Palawanic
plw	Palawano, Brooke’s Point	Austronesian, Malayo-Polynesian, Philippine, Greater Central Philippine, Palawanic
plz	Paluan	Austronesian, Malayo-Polynesian, North Borneo, North Sarawakan, Dayic, Murutic, Murut
pma	Paama	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, Remote Oceanic, North and Central Vanuatu, Northeast Vanuatu-Banks Islands, East Vanuatu
pex	Petats	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, Meso Melanesian, New Ireland, South New Ireland-Northwest Solomonic, Nehan-North Bougainville, Buka
prf	Paranan	Austronesian, Malayo-Polynesian, Philippine, Northern Luzon, Northern Cordilleran, Northeastern Luzon
pyu	Puyuma	Austronesian, Puyuma
pmc	Palumata	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Central Maluku, Buru
pez	Penan, Eastern	Austronesian, Malayo-Polynesian, North Borneo, North Sarawakan, Kayan-Kenyah, Penan
prh	Porohanon	Austronesian, Malayo-Polynesian, Philippine, Greater Central Philippine, Central Philippine, Bisayan, Central, Peripheral
pfa	Pááfang	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, Remote Oceanic, Micronesian, Micronesian Proper, Ponapeic-Trukic, Trukic
pme	Pwaamei	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, Remote Oceanic, New Caledonian, Northern, North
row	Dela-Oenale	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Timor-Babar, Nuclear Timor, Rote
rpn	Repanbitip	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, Remote Oceanic, North and Central Vanuatu, Malekula Interior, Small Nambas
rad	Rade	Austronesian, Malayo-Polynesian, Malayo-Chamic, Chamic, Highlands
rri	Ririo	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, Meso Melanesian, New Ireland, South New Ireland-Northwest Solomonic, Choiseul
rro	Waima	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, Papuan Tip, Peripheral, Central Papuan, West Central Papuan, Nuclear
rga	Roria	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, Remote Oceanic, North and Central Vanuatu, Northeast Vanuatu-Banks Islands, West Santo
rmm	Roma	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Timor-Babar, Southwest Maluku, Kisar-Roma
rai	Ramoaaina	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, Meso Melanesian, New Ireland, South New Ireland-Northwest Solomonic, Patpatar-Tolai
rak	Tulu-Bohuai	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Admiralty Islands, Eastern, Manus, West
rth	Ratahan	Austronesian, Malayo-Polynesian, Philippine, Sangiric, Southern
rgs	Roglai, Southern	Austronesian, Malayo-Polynesian, Malayo-Chamic, Chamic, Highlands, Chru-Northern, Northern Cham
rtm	Rotuman	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, Remote Oceanic, Central Pacific, West Fijian-Rotuman, Rotuman
rgu	Rikou	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Timor-Babar, Nuclear Timor, Rote
rap	Rapa Nui	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, Remote Oceanic, Central Pacific, East Fijian-Polynesian, Polynesian, Nuclear, East, Rapanui
rar	Rarotongan	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, Remote Oceanic, Central Pacific, East Fijian-Polynesian, Polynesian, Nuclear, East, Central, Tahitic
rug	Roviana	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, Meso Melanesian, New Ireland, South New Ireland-Northwest Solomonic, New Georgia, West
rir	Ribun	Austronesian, Malayo-Polynesian, Land Dayak, Southern
rnn	Roon	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, South Halmahera-West New Guinea, West New Guinea, Cenderawasih Bay, Yapen, Central-Western
riu	Riung	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Bima-Lembata
ray	Rapa	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, Remote Oceanic, Central Pacific, East Fijian-Polynesian, Polynesian, Nuclear, East, Central
rjg	Rajong	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Bima-Lembata
raz	Rahambuu	Austronesian, Malayo-Polynesian, Celebic, Eastern, Southeastern, Bungku-Tolaki, Western, West Coast
rob	Tae’	Austronesian, Malayo-Polynesian, South Sulawesi, Northern, Toraja-Sa’dan
rbk	Bontok, Northern	Austronesian, Malayo-Polynesian, Philippine, Northern Luzon, Meso-Cordilleran, South-Central Cordilleran, Central Cordilleran, North Central Cordilleran, Nuclear Cordilleran, Bontok-Kankanay, Bontok
roc	Roglai, Cacgia	Austronesian, Malayo-Polynesian, Malayo-Chamic, Chamic, Highlands, Chru-Northern, Northern Cham
ruu	Lobu, Lanas	Austronesian, Malayo-Polynesian, North Borneo, Sabahan, Paitanic, Upper Kinabatangan
rbl	Bikol, Miraya	Austronesian, Malayo-Polynesian, Philippine, Greater Central Philippine, Central Philippine, Bikol, Inland
rkh	Rakahanga-Manihiki	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, Remote Oceanic, Central Pacific, East Fijian-Polynesian, Polynesian, Nuclear, East, Central, Tahitic
roe	Ronji	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, North New Guinea, Ngero-Vitiaz, Vitiaz, Roinji-Nenaya
rog	Roglai, Northern	Austronesian, Malayo-Polynesian, Malayo-Chamic, Chamic, Highlands, Chru-Northern, Northern Cham
reb	Rembong	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Bima-Lembata
rol	Romblomanon	Austronesian, Malayo-Polynesian, Philippine, Greater Central Philippine, Central Philippine, Bisayan, Central, Romblon
ree	Kayan, Rejang	Austronesian, Malayo-Polynesian, North Borneo, North Sarawakan, Kayan-Kenyah, Kayanic, Kayan Proper
rej	Rejang	Austronesian, Malayo-Polynesian, Rejang
ror	Rongga	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Bima-Lembata
ssg	Seimat	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Admiralty Islands, Western
smk	Bolinao	Austronesian, Malayo-Polynesian, Philippine, Central Luzon, Sambalic
sgu	Salas	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Central Maluku, East, Seram, Manusela-Seti
sml	Sama, Central	Austronesian, Malayo-Polynesian, Greater Barito, Sama-Bajaw, Sulu-Borneo, Inner Sulu Sama
smo	Samoan	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, Remote Oceanic, Central Pacific, East Fijian-Polynesian, Polynesian, Nuclear, Samoic-Outlier, Samoan
sgz	Sursurunga	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, Meso Melanesian, New Ireland, South New Ireland-Northwest Solomonic, Patpatar-Tolai
sso	Sissano	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, North New Guinea, Schouten, Siau
smr	Simeulue	Austronesian, Malayo-Polynesian, Northwest Sumatra-Barrier Islands
ssq	So’a	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Bima-Lembata
smw	Sumbawa	Austronesian, Malayo-Polynesian, Bali-Sasak-Sumbawa, Sasak-Sumbawa
ssv	Shark Bay	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, Remote Oceanic, North and Central Vanuatu, East Santo, South
sas	Sasak	Austronesian, Malayo-Polynesian, Bali-Sasak-Sumbawa, Sasak-Sumbawa
sau	Saleman	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Central Maluku, East, Seram, Sawai-Nuaulu
snb	Sebuyau	Austronesian, Malayo-Polynesian, Malayo-Chamic, Malayic, Ibanic
ssz	Sengseng	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, North New Guinea, Ngero-Vitiaz, Vitiaz, Southwest New Britain, Arawe-Pasismanua, Pasismanua
snc	Sinaugoro	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, Papuan Tip, Peripheral, Central Papuan, Sinagoro-Keapara
sax	Sa	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, Remote Oceanic, North and Central Vanuatu, Northeast Vanuatu-Banks Islands, East Vanuatu
stb	Subanen, Northern	Austronesian, Malayo-Polynesian, Philippine, Greater Central Philippine, Subanon, Eastern
sne	Bidayuh, Bau	Austronesian, Malayo-Polynesian, Land Dayak, Bidayuh, Core, Western
ste	Liana-Seti	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Central Maluku, East, Seram, Manusela-Seti
sbb	Simbo	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, Meso Melanesian, New Ireland, South New Ireland-Northwest Solomonic, New Georgia, West
sbc	Kele	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Admiralty Islands, Eastern, Manus, East
sbe	Saliba	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, Papuan Tip, Nuclear, Suauic
snl	Sangil	Austronesian, Malayo-Polynesian, Philippine, Sangiric, Northern
sbh	Sori-Harengan	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Admiralty Islands, Eastern, Manus, West
stn	Owa	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, Southeast Solomonic, Malaita-San Cristobal, San Cristobal
sib	Sebop	Austronesian, Malayo-Polynesian, North Borneo, North Sarawakan, Kayan-Kenyah, Kenyah, Kayanic Kenyah
sbl	Sambal, Botolan	Austronesian, Malayo-Polynesian, Philippine, Central Luzon, Sambalic
sns	Nahavaq	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, Remote Oceanic, North and Central Vanuatu, Northeast Vanuatu-Banks Islands, Malekula Coastal
snv	Sa’ban	Austronesian, Malayo-Polynesian, North Borneo, North Sarawakan, Dayic, Kelabitic
sih	Sîshëë	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, Remote Oceanic, New Caledonian, Southern, South, Zire-Tiri
sbr	Sembakung Murut	Austronesian, Malayo-Polynesian, North Borneo, North Sarawakan, Dayic, Murutic, Tidong
sij	Numbami	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, North New Guinea, Huon Gulf, Numbami
stw	Satawalese	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, Remote Oceanic, Micronesian, Micronesian Proper, Ponapeic-Trukic, Trukic
sob	Sobei	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, North New Guinea, Sarmi-Jayapura Bay, Sarmi
suc	Subanon, Western	Austronesian, Malayo-Polynesian, Philippine, Greater Central Philippine, Subanon
sbx	Seberuang	Austronesian, Malayo-Polynesian, Malayo-Chamic, Malayic, Ibanic
sun	Sunda	Austronesian, Malayo-Polynesian, Sundanese
scg	Sanggau	Austronesian, Malayo-Polynesian, Land Dayak
sol	Solos	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, Meso Melanesian, New Ireland, South New Ireland-Northwest Solomonic, Nehan-North Bougainville, Solos
sjb	Sajau Basap	Austronesian, Malayo-Polynesian, North Borneo, Rejang-Sajau
svb	Ulau-Suain	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, North New Guinea, Schouten, Siau
sov	Sonsorol	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, Remote Oceanic, Micronesian, Micronesian Proper, Ponapeic-Trukic, Trukic
sjm	Mapun	Austronesian, Malayo-Polynesian, Greater Barito, Sama-Bajaw, Sulu-Borneo, Borneo Coast Bajaw
sve	Serili	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Babar, South, Masela-South Babar
sda	Toraja-Sa’dan	Austronesian, Malayo-Polynesian, South Sulawesi, Northern, Toraja-Sa’dan
sjr	Siar-Lak	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, Meso Melanesian, New Ireland, South New Ireland-Northwest Solomonic, Patpatar-Tolai
spb	Sepa	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Central Maluku, East, Seram, Nunusaku, Piru Bay, East
spe	Sepa	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, North New Guinea, Schouten, Kairiru-Manam, Manam
spg	Sian	Austronesian, Malayo-Polynesian, North Borneo, Melanau-Kajang, Kajang
ske	Seke	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, Remote Oceanic, North and Central Vanuatu, Northeast Vanuatu-Banks Islands, East Vanuatu
sdm	Semandang	Austronesian, Malayo-Polynesian, Land Dayak, Southern
skg	Malagasy, Sakalava	Austronesian, Malayo-Polynesian, Greater Barito, East, Malagasy
sdo	Bidayuh, Bukar-Sadong	Austronesian, Malayo-Polynesian, Land Dayak, Bidayuh, Eastern
skh	Sikule	Austronesian, Malayo-Polynesian, Northwest Sumatra-Barrier Islands, Nias
ski	Sika	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Bima-Lembata
spr	Saparua	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Central Maluku, East, Seram, Nunusaku, Piru Bay, East, Seram Straits, Uliase, Hatuhaha, Saparua
sps	Saposa	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, Meso Melanesian, New Ireland, South New Ireland-Northwest Solomonic, Nehan-North Bougainville, Saposa-Tinputz
swp	Suau	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, Papuan Tip, Nuclear, Suauic
sdu	Sarudu	Austronesian, Malayo-Polynesian, Celebic, Kaili-Pamona, Southern
skn	Subanon, Kolibugan	Austronesian, Malayo-Polynesian, Philippine, Greater Central Philippine, Subanon, Eastern
sdx	Melanau, Sibu	Austronesian, Malayo-Polynesian, North Borneo, Melanau-Kajang, Melanau
sko	Seko Tengah	Austronesian, Malayo-Polynesian, South Sulawesi, Seko
skp	Sekapan	Austronesian, Malayo-Polynesian, North Borneo, Melanau-Kajang, Kajang
sws	Seluwasan	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Southeast Maluku, Southern
swu	Suwawa	Austronesian, Malayo-Polynesian, Philippine, Greater Central Philippine, Gorontalo-Mongondow, Gorontalic
sww	Sowa	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, Remote Oceanic, North and Central Vanuatu, Northeast Vanuatu-Banks Islands, East Vanuatu
sku	Sakao	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, Remote Oceanic, North and Central Vanuatu, East Santo, North
skx	Seko Padang	Austronesian, Malayo-Polynesian, South Sulawesi, Seko
sky	Sikaiana	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, Remote Oceanic, Central Pacific, East Fijian-Polynesian, Polynesian, Nuclear, Samoic-Outlier, Ellicean
skz	Sekar	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, North Bomberai
sxn	Sangir	Austronesian, Malayo-Polynesian, Philippine, Sangiric, Northern
sxr	Saaroa	Austronesian, Tsouic
slg	Selungai Murut	Austronesian, Malayo-Polynesian, North Borneo, North Sarawakan, Dayic, Murutic, Murut
sre	Bakati’, Sara	Austronesian, Malayo-Polynesian, Land Dayak, Bakati’
srf	Nafi	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, North New Guinea, Huon Gulf, Markham, Lower, Busu
sya	Siang	Austronesian, Malayo-Polynesian, Greater Barito, West, North
srg	Sulod	Austronesian, Malayo-Polynesian, Philippine, Greater Central Philippine, Central Philippine
syb	Subanen, Central	Austronesian, Malayo-Polynesian, Philippine, Greater Central Philippine, Subanon, Eastern
seu	Serui-Laut	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, South Halmahera-West New Guinea, West New Guinea, Cenderawasih Bay, Yapen, Central-Western
srk	Serudung Murut	Austronesian, Malayo-Polynesian, North Borneo, North Sarawakan, Dayic, Murutic, Tidong
slm	Sama, Pangutaran	Austronesian, Malayo-Polynesian, Greater Barito, Sama-Bajaw, Sulu-Borneo, Western Sulu Sama
sew	Sewa Bay	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, Papuan Tip, Nuclear, North Papuan Mainland-D’Entrecasteaux, Dobu-Duau
slp	Lamaholot	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Bima-Lembata
sfe	Subanen, Eastern	Austronesian, Malayo-Polynesian, Philippine, Greater Central Philippine, Subanon, Eastern
slu	Selaru	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Southeast Maluku, Southern
sgb	Ayta, Mag-antsi	Austronesian, Malayo-Polynesian, Philippine, Central Luzon, Sambalic
srv	Sorsoganon, Southern	Austronesian, Malayo-Polynesian, Philippine, Greater Central Philippine, Central Philippine, Bisayan, Central, Warayan, Gubat
sgd	Surigaonon	Austronesian, Malayo-Polynesian, Philippine, Greater Central Philippine, Central Philippine, Bisayan, South
sly	Selayar	Austronesian, Malayo-Polynesian, South Sulawesi, Makassar
srw	Serua	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Timor-Babar, Southwest Maluku, Teun-Nila-Serua, Nila-Serua
szd	Seru	Austronesian, Malayo-Polynesian, North Borneo, Melanau-Kajang, Melanau
sge	Segai	Austronesian, Malayo-Polynesian, North Borneo, North Sarawakan, Kayan-Kenyah, Kayanic, Modang
slz	Ma’ya	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, South Halmahera-West New Guinea, West New Guinea, Cenderawasih Bay, Raja Ampat
sry	Sera	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, North New Guinea, Schouten, Siau
ssb	Sama, Southern	Austronesian, Malayo-Polynesian, Greater Barito, Sama-Bajaw, Sulu-Borneo, Inner Sulu Sama
szn	Sula	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Central Maluku, Sula
sse	Sama, Balangingih	Austronesian, Malayo-Polynesian, Greater Barito, Sama-Bajaw, Sulu-Borneo, Inner Sulu Sama
szw	Sawai	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, South Halmahera-West New Guinea, South Halmahera, Southeast
ssf	Thao	Austronesian, Western Plains, Thao
tmn	Taman	Austronesian, Malayo-Polynesian, South Sulawesi, Bugis, Tamanic
tgi	Lawunuia	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, Meso Melanesian, New Ireland, South New Ireland-Northwest Solomonic, Piva-Banoni
tmq	Tumleo	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, North New Guinea, Schouten, Siau
tsr	Akei	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, Remote Oceanic, North and Central Vanuatu, Northeast Vanuatu-Banks Islands, West Santo
tgl	Tagalog	Austronesian, Malayo-Polynesian, Philippine, Greater Central Philippine, Central Philippine, Tagalog
tmt	Tasmate	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, Remote Oceanic, North and Central Vanuatu, Northeast Vanuatu-Banks Islands, West Santo
tah	Tahitian	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, Remote Oceanic, Central Pacific, East Fijian-Polynesian, Polynesian, Nuclear, East, Central, Tahitic
tgn	Tandaganon	Austronesian, Malayo-Polynesian, Philippine, Greater Central Philippine, Central Philippine, Bisayan, South
tgo	Sudest	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, Papuan Tip, Peripheral, Kilivila-Louisiades, Nimoa-Sudest
tsu	Tsou	Austronesian, Tsouic
tgp	Tangoa	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, Remote Oceanic, North and Central Vanuatu, Northeast Vanuatu-Banks Islands, West Santo
tmw	Temuan	Austronesian, Malayo-Polynesian, Malayo-Chamic, Malayic, Malay
tgq	Tring	Austronesian, Malayo-Polynesian, North Borneo, North Sarawakan, Dayic, Kelabitic
tmy	Tami	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, North New Guinea, Ngero-Vitiaz, Vitiaz, Tami
tgs	Nume	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, Remote Oceanic, North and Central Vanuatu, Northeast Vanuatu-Banks Islands, East Vanuatu
tao	Yami	Austronesian, Malayo-Polynesian, Philippine, Bashiic, Yami
tgt	Tagbanwa, Central	Austronesian, Malayo-Polynesian, Philippine, Greater Central Philippine, Palawanic
tne	Kallahan, Tinoc	Austronesian, Malayo-Polynesian, Philippine, Northern Luzon, Meso-Cordilleran, South-Central Cordilleran, Southern Cordilleran, West Southern Cordilleran, Nuclear Southern Cordilleran, Kallahan
tte	Bwanabwana	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, Papuan Tip, Nuclear, Suauic
tni	Tandia	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, South Halmahera-West New Guinea, West New Guinea, Cenderawasih Bay, Tandia
ttg	Tutong	Austronesian, Malayo-Polynesian, North Borneo, North Sarawakan, Berawan-Lower Baram, Lower Baram, Central, B
tnk	Kwamera	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, South Vanuatu, Tanna
tnl	Lenakel	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, South Vanuatu, Tanna
tti	Tobati	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, North New Guinea, Sarmi-Jayapura Bay, Jayapura Bay
tay	Atayal	Austronesian, Atayalic
tnn	Tanna, North	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, South Vanuatu, Tanna
tnp	Whitesands	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, South Vanuatu, Tanna
tbc	Takia	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, North New Guinea, Ngero-Vitiaz, Vitiaz, Bel, Nuclear Bel, Northern
tns	Tenis	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, St. Matthias
ttp	Tombelala	Austronesian, Malayo-Polynesian, Celebic, Kaili-Pamona, Northern, Pamona
tbe	Tanibili	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Temotu, Utupua-Vanikoro, Utupua
tnt	Tontemboan	Austronesian, Malayo-Polynesian, Philippine, Minahasan, North
tbf	Mandara	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, Meso Melanesian, New Ireland, Lavongai-Nalik
tnw	Tonsawang	Austronesian, Malayo-Polynesian, Philippine, Minahasan
tnx	Tanema	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Temotu, Utupua-Vanikoro
ttu	Torau	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, Meso Melanesian, New Ireland, South New Ireland-Northwest Solomonic, Mono-Uruava
tbj	Tiang	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, Meso Melanesian, New Ireland, Lavongai-Nalik
ttv	Titan	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Admiralty Islands, Eastern, Manus, East
tbk	Tagbanwa, Calamian	Austronesian, Malayo-Polynesian, Philippine, Kalamian
ttw	Long Wat	Austronesian, Malayo-Polynesian, North Borneo, North Sarawakan, Kayan-Kenyah, Kenyah, Kayanic Kenyah
tbl	Tboli	Austronesian, Malayo-Polynesian, Philippine, Bilic, Tboli
tbo	Tawala	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, Papuan Tip, Nuclear, North Papuan Mainland-D’Entrecasteaux, Are-Taupota, Taupota
tuc	Mutu	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, North New Guinea, Ngero-Vitiaz, Ngero, Tuam
tid	Tidong	Austronesian, Malayo-Polynesian, North Borneo, North Sarawakan, Dayic, Murutic, Tidong
tbw	Tagbanwa	Austronesian, Malayo-Polynesian, Philippine, Greater Central Philippine, Palawanic
tom	Tombulu	Austronesian, Malayo-Polynesian, Philippine, Minahasan, North, Northeast
tbx	Kapin	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, North New Guinea, Huon Gulf, South, Hote-Buang, Buang
tih	Timugon Murut	Austronesian, Malayo-Polynesian, North Borneo, North Sarawakan, Dayic, Murutic, Murut
ton	Tongan	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, Remote Oceanic, Central Pacific, East Fijian-Polynesian, Polynesian, Tongic
tio	Teop	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, Meso Melanesian, New Ireland, South New Ireland-Northwest Solomonic, Nehan-North Bougainville, Saposa-Tinputz
tox	Tobian	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, Remote Oceanic, Micronesian, Micronesian Proper, Ponapeic-Trukic, Trukic
toy	Topoiyo	Austronesian, Malayo-Polynesian, Celebic, Kaili-Pamona, Northern, Kaili
tis	Itneg, Masadiit	Austronesian, Malayo-Polynesian, Philippine, Northern Luzon, Meso-Cordilleran, South-Central Cordilleran, Central Cordilleran, North Central Cordilleran, Kalinga-Itneg, Itneg
tpa	Taupota	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, Papuan Tip, Nuclear, North Papuan Mainland-D’Entrecasteaux, Are-Taupota, Taupota
tiu	Adasen	Austronesian, Malayo-Polynesian, Philippine, Northern Luzon, Northern Cordilleran, Cagayan Valley, Isnag
tva	Vaghua	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, Meso Melanesian, New Ireland, South New Ireland-Northwest Solomonic, Choiseul
tpf	Tarpia	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, North New Guinea, Sarmi-Jayapura Bay, Sarmi
tve	Te’un	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Timor-Babar, Southwest Maluku, Teun-Nila-Serua, Teun
tiy	Tiruray	Austronesian, Malayo-Polynesian, Philippine, Bilic
tvk	Ambrym, Southeast	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, Remote Oceanic, North and Central Vanuatu, Northeast Vanuatu-Banks Islands, East Vanuatu
tvl	Tuvaluan	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, Remote Oceanic, Central Pacific, East Fijian-Polynesian, Polynesian, Nuclear, Samoic-Outlier, Ellicean
tvm	Tela-Masbuar	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Babar, South, Southwest Babar
tjg	Tunjung	Austronesian, Malayo-Polynesian, Greater Barito, Barito-Mahakam
tvw	Sedoa	Austronesian, Malayo-Polynesian, Celebic, Kaili-Pamona, Northern, Kaili
tpv	Tanapag	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, Remote Oceanic, Micronesian, Micronesian Proper, Ponapeic-Trukic, Trukic
twb	Tawbuid, Western	Austronesian, Malayo-Polynesian, Philippine, Greater Central Philippine, South Mangyan, Buhid-Taubuid
tkd	Tukudede	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Timor-Babar, Nuclear Timor
tpz	Tinputz	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, Meso Melanesian, New Ireland, South New Ireland-Northwest Solomonic, Nehan-North Bougainville, Saposa-Tinputz
tkg	Malagasy, Tesaka	Austronesian, Malayo-Polynesian, Greater Barito, East, Malagasy
tql	Lehali	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, Remote Oceanic, North and Central Vanuatu, Northeast Vanuatu-Banks Islands, East Vanuatu
tdi	Tomadino	Austronesian, Malayo-Polynesian, Celebic, Eastern, Southeastern, Bungku-Tolaki, Western, Interior
tkl	Tokelauan	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, Remote Oceanic, Central Pacific, East Fijian-Polynesian, Polynesian, Nuclear, Samoic-Outlier, Tokelauan
tdj	Tajio	Austronesian, Malayo-Polynesian, Celebic, Tomini-Tolitoli, Tomini, Southern
tkp	Tikopia	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, Remote Oceanic, Central Pacific, East Fijian-Polynesian, Polynesian, Nuclear, Samoic-Outlier, Futunic
tqp	Tomoip	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, Meso Melanesian, New Ireland, Tomoip
tdn	Tondano	Austronesian, Malayo-Polynesian, Philippine, Minahasan, North, Northeast
twp	Ere	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Admiralty Islands, Eastern, Manus, East
tkw	Teanu	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Temotu, Utupua-Vanikoro
twu	Termanu	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Timor-Babar, Nuclear Timor, Rote
tdu	Dusun, Tempasuk	Austronesian, Malayo-Polynesian, North Borneo, Sabahan, Dusunic, Dusun, Central
trb	Terebu	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, North New Guinea, Schouten, Kairiru-Manam, Kairiru
twy	Tawoyan	Austronesian, Malayo-Polynesian, Greater Barito, East, North
tdx	Malagasy, Tandroy-Mahafaly	Austronesian, Malayo-Polynesian, Greater Barito, East, Malagasy
txa	Tombonuo	Austronesian, Malayo-Polynesian, North Borneo, Sabahan, Paitanic
tdy	Tadyawan	Austronesian, Malayo-Polynesian, Philippine, North Mangyan
tre	Tarangan, East	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Aru
txe	Totoli	Austronesian, Malayo-Polynesian, Celebic, Tomini-Tolitoli, Tolitoli
tld	Talaud	Austronesian, Malayo-Polynesian, Philippine, Sangiric, Southern
txm	Tomini	Austronesian, Malayo-Polynesian, Celebic, Tomini-Tolitoli, Tomini, Northern
txn	Tarangan, West	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Aru
txq	Tii	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Timor-Babar, Nuclear Timor, Rote
tlk	Taloki	Austronesian, Malayo-Polynesian, Celebic, Eastern, Southeastern, Bungku-Tolaki, Eastern, East Coast, Kulisusu
txs	Tonsea	Austronesian, Malayo-Polynesian, Philippine, Minahasan, North, Northeast
tlm	Tolomako	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, Remote Oceanic, North and Central Vanuatu, Northeast Vanuatu-Banks Islands, West Santo
tln	Talondo’	Austronesian, Malayo-Polynesian, South Sulawesi, Northern, Toraja-Sa’dan
txx	Tatana	Austronesian, Malayo-Polynesian, North Borneo, Sabahan, Dusunic, Bisaya
txy	Malagasy, Tanosy	Austronesian, Malayo-Polynesian, Greater Barito, East, Malagasy
tlr	Talise	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, Southeast Solomonic, Gela-Guadalcanal, Guadalcanal
tls	Tambotalo	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, Remote Oceanic, North and Central Vanuatu, Northeast Vanuatu-Banks Islands, West Santo
tlt	Teluti	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Central Maluku, East, Seram, Nunusaku, Piru Bay, East
tlu	Tulehu	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Central Maluku, East, Seram, Nunusaku, Piru Bay, East, Seram Straits, Ambon
trv	Taroko	Austronesian, Atayalic
tlv	Taliabu	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Central Maluku, Sula, Taliabo
tes	Tengger	Austronesian, Malayo-Polynesian, Javanese
tlx	Khehek	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Admiralty Islands, Eastern, Manus, West
trx	Bidayuh, Tringgus-Sembaan	Austronesian, Malayo-Polynesian, Land Dayak, Bidayuh, Core, Sembaan
tet	Tetun	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Timor-Babar, Nuclear Timor
tev	Teor	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Teor-Kur
tmb	Avava	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, Remote Oceanic, North and Central Vanuatu, Malekula Interior, Malekula Central
tsg	Tausug	Austronesian, Malayo-Polynesian, Philippine, Greater Central Philippine, Central Philippine, Bisayan, South, Butuan-Tausug
tmi	Tutuba	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, Remote Oceanic, North and Central Vanuatu, Northeast Vanuatu-Banks Islands, West Santo
tzn	Tugun	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Timor-Babar, Southwest Maluku, Wetar
tgb	Tobilung	Austronesian, Malayo-Polynesian, North Borneo, Sabahan, Dusunic, Dusun
tgc	Tigak	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, Meso Melanesian, New Ireland, Lavongai-Nalik
ums	Pendau	Austronesian, Malayo-Polynesian, Celebic, Tomini-Tolitoli, Tomini, Southern
una	Watut, North	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, North New Guinea, Huon Gulf, Markham, Watut
urv	Uruava	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, Meso Melanesian, New Ireland, South New Ireland-Northwest Solomonic, Mono-Uruava
ubl	Bikol, Buhi’non	Austronesian, Malayo-Polynesian, Philippine, Greater Central Philippine, Central Philippine, Bikol, Inland
ubr	Ubir	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, Papuan Tip, Nuclear, North Papuan Mainland-D’Entrecasteaux, Are-Taupota, Are
unu	Unubahe	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, Papuan Tip, Nuclear, Suauic
unz	Kaili, Unde	Austronesian, Malayo-Polynesian, Celebic, Kaili-Pamona, Northern, Kaili
udj	Ujir	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Aru
uli	Ulithian	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, Remote Oceanic, Micronesian, Micronesian Proper, Ponapeic-Trukic, Trukic
upv	Uripiv-Wala-Rano-Atchin	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, Remote Oceanic, North and Central Vanuatu, Northeast Vanuatu-Banks Islands, Malekula Coastal
utp	Amba	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Temotu, Utupua-Vanikoro, Utupua
ues	Kioko	Austronesian, Malayo-Polynesian, Celebic, Eastern, Southeastern, Muna-Buton, Nuclear Muna-Buton, Munan, Munic, Western
ulm	Ulumanda’	Austronesian, Malayo-Polynesian, South Sulawesi, Northern, Pitu Ulunna Salu
ulu	Uma’ Lung	Austronesian, Malayo-Polynesian, North Borneo, North Sarawakan, Kayan-Kenyah, Kenyah, Upper Pujungan
uun	Kulon-Pazeh	Austronesian, Northwest Formosan
uge	Ughele	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, Meso Melanesian, New Ireland, South New Ireland-Northwest Solomonic, New Georgia, West
uur	Ura	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, South Vanuatu, Erromanga
uve	Fagauvea	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, Remote Oceanic, Central Pacific, East Fijian-Polynesian, Polynesian, Nuclear, Samoic-Outlier, Futunic
urk	Urak Lawoi’	Austronesian, Malayo-Polynesian, Malayo-Chamic, Malayic
uvl	Lote	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, North New Guinea, Ngero-Vitiaz, Vitiaz, Mengen
umi	Ukit	Austronesian, Malayo-Polynesian, North Borneo, Melanau-Kajang, Kajang
urn	Uruangnirin	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, North Bomberai
urr	Löyöp	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, Remote Oceanic, North and Central Vanuatu, Northeast Vanuatu-Banks Islands, East Vanuatu
vkt	Malay, Tenggarong Kutai	Austronesian, Malayo-Polynesian, Malayo-Chamic, Malayic, Malay
vlp	Valpei	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, Remote Oceanic, North and Central Vanuatu, Northeast Vanuatu-Banks Islands, West Santo
vnk	Lovono	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Temotu, Utupua-Vanikoro
vnm	Neve’ei	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, Remote Oceanic, North and Central Vanuatu, Malekula Interior, Malekula Central
val	Vehes	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, North New Guinea, Huon Gulf, South, Hote-Buang, Buang
vnp	Vunapu	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, Remote Oceanic, North and Central Vanuatu, Northeast Vanuatu-Banks Islands, West Santo
vme	Masela, East	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Babar, South, Masela-South Babar
vao	Vao	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, Remote Oceanic, North and Central Vanuatu, Northeast Vanuatu-Banks Islands, Malekula Coastal
vra	Vera’a	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, Remote Oceanic, North and Central Vanuatu, Northeast Vanuatu-Banks Islands, East Vanuatu
vmg	Lungalunga	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, Meso Melanesian, New Ireland, South New Ireland-Northwest Solomonic, Mono-Uruava
vrs	Varisi	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, Meso Melanesian, New Ireland, South New Ireland-Northwest Solomonic, Choiseul
vrt	Banam Bay	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, Remote Oceanic, North and Central Vanuatu, Northeast Vanuatu-Banks Islands, Malekula Coastal
viv	Iduna	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, Papuan Tip, Nuclear, North Papuan Mainland-D’Entrecasteaux, Bwaidoga
vbb	Babar, Southeast	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Babar, South, Masela-South Babar
vbk	Bontok, Southwestern	Austronesian, Malayo-Polynesian, Philippine, Northern Luzon, Meso-Cordilleran, South-Central Cordilleran, Central Cordilleran, North Central Cordilleran, Nuclear Cordilleran, Bontok-Kankanay, Bontok
vkk	Kaur	Austronesian, Malayo-Polynesian, Malayo-Chamic, Malayic, Malay
vkl	Kulisusu	Austronesian, Malayo-Polynesian, Celebic, Eastern, Southeastern, Bungku-Tolaki, Eastern, East Coast, Kulisusu
vms	Moksela	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Central Maluku, Buru
vko	Kodeoha	Austronesian, Malayo-Polynesian, Celebic, Eastern, Southeastern, Bungku-Tolaki, Western, West Coast
weo	Wemale	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Central Maluku, East, Seram, Nunusaku, Three Rivers, Wemale
wab	Wab	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, North New Guinea, Ngero-Vitiaz, Vitiaz, Bel, Astrolabe
wad	Wandamen	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, South Halmahera-West New Guinea, West New Guinea, Cenderawasih Bay, Yapen, Central-Western
wet	Perai	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Timor-Babar, Southwest Maluku, Wetar
wag	Wa’ema	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, Papuan Tip, Nuclear, North Papuan Mainland-D’Entrecasteaux, Are-Taupota, Taupota
wew	Wejewa	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Sumba-Hawu, Sumba
wah	Watubela	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Central Maluku, East, Banda-Geser, Geser-Gorom
wrp	Waropen	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, South Halmahera-West New Guinea, West New Guinea, Cenderawasih Bay, Waropen
wgb	Wagawaga	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, Papuan Tip, Nuclear, Suauic
wmh	Waima’a	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Timor-Babar, Nuclear Timor
wru	Waru	Austronesian, Malayo-Polynesian, Celebic, Eastern, Southeastern, Bungku-Tolaki, Western, West Coast
wgo	Waigeo	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, South Halmahera-West New Guinea, West New Guinea, Cenderawasih Bay, Raja Ampat
wmm	Maiwa	Austronesian, Malayo-Polynesian, South Sulawesi, Northern, Masenrempulu
wmn	Waamwang	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, Remote Oceanic, New Caledonian, Northern, North, Hmwaveke
wrx	Wae Rana	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Bima-Lembata
wha	Manusela	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Central Maluku, East, Seram, Manusela-Seti
war	Waray-Waray	Austronesian, Malayo-Polynesian, Philippine, Greater Central Philippine, Central Philippine, Bisayan, Central, Warayan, Samar-Waray
whk	Kenyah, Wahau	Austronesian, Malayo-Polynesian, North Borneo, North Sarawakan, Kayan-Kenyah, Kenyah, Kayanic Kenyah
wsi	Wusi	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, Remote Oceanic, North and Central Vanuatu, Northeast Vanuatu-Banks Islands, West Santo
wat	Kaninuwa	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, Papuan Tip, Nuclear, North Papuan Mainland-D’Entrecasteaux, Are-Taupota, Are
whu	Kayan, Wahau	Austronesian, Malayo-Polynesian, North Borneo, North Sarawakan, Kayan-Kenyah, Kayanic, Kayan Proper
waz	Wampur	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, North New Guinea, Huon Gulf, Markham, Upper, Mountain
wnk	Wanukaka	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Sumba-Hawu, Sumba
wbb	Wabo	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, South Halmahera-West New Guinea, West New Guinea, Cenderawasih Bay, Yapen, East
wtw	Wotu	Austronesian, Malayo-Polynesian, Celebic, Wotu-Wolio
wiv	Vitu	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, Meso Melanesian, Bali-Vitu
woc	Wogeo	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, North New Guinea, Schouten, Kairiru-Manam, Manam
woe	Woleaian	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, Remote Oceanic, Micronesian, Micronesian Proper, Ponapeic-Trukic, Trukic
wkd	Mo	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, North New Guinea, Sarmi-Jayapura Bay, Sarmi
wuv	Wuvulu-Aua	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Admiralty Islands, Western
wbw	Woi	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, South Halmahera-West New Guinea, West New Guinea, Cenderawasih Bay, Yapen, Central-Western
wuy	Wauyai	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, South Halmahera-West New Guinea, West New Guinea, Cenderawasih Bay, Raja Ampat
wwo	Dorig	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, Remote Oceanic, North and Central Vanuatu, Northeast Vanuatu-Banks Islands, East Vanuatu
woo	Manombai	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Aru
wow	Wawonii	Austronesian, Malayo-Polynesian, Celebic, Eastern, Southeastern, Bungku-Tolaki, Eastern, East Coast
wed	Wedau	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, Papuan Tip, Nuclear, North Papuan Mainland-D’Entrecasteaux, Are-Taupota, Taupota
wlo	Wolio	Austronesian, Malayo-Polynesian, Celebic, Wotu-Wolio, Wolio-Kamaru
wlr	Wailapa	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, Remote Oceanic, North and Central Vanuatu, Northeast Vanuatu-Banks Islands, West Santo
wls	Wallisian	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, Remote Oceanic, Central Pacific, East Fijian-Polynesian, Polynesian, Nuclear, Samoic-Outlier, East Uvean-Niuafo’ou
wyy	Fijian, Western	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, Remote Oceanic, Central Pacific, West Fijian-Rotuman, West Fijian
xnb	Kanakanabu	Austronesian, Tsouic
xsy	Saisiyat	Austronesian, Northwest Formosan
xnn	Kankanay, Northern	Austronesian, Malayo-Polynesian, Philippine, Northern Luzon, Meso-Cordilleran, South-Central Cordilleran, Central Cordilleran, North Central Cordilleran, Nuclear Cordilleran, Bontok-Kankanay, Kankanay
xkd	Kayan, Mendalam	Austronesian, Malayo-Polynesian, North Borneo, North Sarawakan, Kayan-Kenyah, Kayanic, Kayan Proper
xke	Kereho	Austronesian, Malayo-Polynesian, North Borneo, North Sarawakan, Kayan-Kenyah, Kayanic, Muller-Schwaner ‘Punan’
xay	Kayan Mahakam	Austronesian, Malayo-Polynesian, North Borneo, North Sarawakan, Kayan-Kenyah, Kayanic, Kayan Proper
xkl	Kenyah, Mainstream	Austronesian, Malayo-Polynesian, North Borneo, North Sarawakan, Kayan-Kenyah, Kenyah
xkn	Kayan, Kayan River	Austronesian, Malayo-Polynesian, North Borneo, North Sarawakan, Kayan-Kenyah, Kayanic, Kayan Proper
xkq	Koroni	Austronesian, Malayo-Polynesian, Celebic, Eastern, Southeastern, Bungku-Tolaki, Eastern, East Coast, Kulisusu
xks	Kumbewaha	Austronesian, Malayo-Polynesian, Celebic, Eastern, Southeastern, Muna-Buton, Nuclear Muna-Buton, Buton, East Buton
xbr	Kambera	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Sumba-Hawu, Sumba
xkx	Karore	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, North New Guinea, Ngero-Vitiaz, Vitiaz, Southwest New Britain, Arawe-Pasismanua, Pasismanua
xky	Uma’ Lasan	Austronesian, Malayo-Polynesian, North Borneo, North Sarawakan, Kayan-Kenyah, Kenyah, Upper Pujungan
xdy	Malayic Dayak	Austronesian, Malayo-Polynesian, Malayo-Chamic, Malayic
xem	Kembayan	Austronesian, Malayo-Polynesian, Land Dayak, Southern
xsb	Sambal	Austronesian, Malayo-Polynesian, Philippine, Central Luzon, Sambalic
xsi	Sio	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, North New Guinea, Ngero-Vitiaz, Vitiaz, Sio
xxk	Ke’o	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Bima-Lembata
xmt	Matbat	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, South Halmahera-West New Guinea, West New Guinea, Cenderawasih Bay, Raja Ampat
xmv	Malagasy, Antankarana	Austronesian, Malayo-Polynesian, Greater Barito, East, Malagasy
xmw	Malagasy, Tsimihety	Austronesian, Malayo-Polynesian, Greater Barito, East, Malagasy
xmx	Maden	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, South Halmahera-West New Guinea, West New Guinea, Cenderawasih Bay, Raja Ampat
xmz	Mori Bawah	Austronesian, Malayo-Polynesian, Celebic, Eastern, Southeastern, Bungku-Tolaki, Eastern, East Coast
yly	Nyelâyu	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, Remote Oceanic, New Caledonian, Northern, Extreme Northern
yml	Iamalele	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, Papuan Tip, Nuclear, North Papuan Mainland-D’Entrecasteaux, Bwaidoga
ymn	Sunum	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, North New Guinea, Sarmi-Jayapura Bay, Sarmi
ymp	Yamap	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, North New Guinea, Huon Gulf, South, Hote-Buang, Hote
yap	Yapese	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Yapese
yob	Yoba	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, Papuan Tip, Peripheral, Central Papuan, Oumic, Magoric
yog	Yogad	Austronesian, Malayo-Polynesian, Philippine, Northern Luzon, Northern Cordilleran, Cagayan Valley, Ibanagic
yka	Yakan	Austronesian, Malayo-Polynesian, Greater Barito, Sama-Bajaw
ykk	Yakaikeke	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, Papuan Tip, Nuclear, North Papuan Mainland-D’Entrecasteaux, Are-Taupota, Taupota
ykm	Kap	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, North New Guinea, Schouten, Siau
ylb	Yaleba	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, Papuan Tip, Nuclear, Suauic
yrs	Yarsun	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, North New Guinea, Sarmi-Jayapura Bay, Sarmi
ylu	Aribwaung	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, North New Guinea, Huon Gulf, Markham, Lower, Busu
zsa	Sarasira	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, North New Guinea, Huon Gulf, Markham, Upper, Mountain
zsm	Malay, Standard	Austronesian, Malayo-Polynesian, Malayo-Chamic, Malayic, Malay
zsu	Sukurum	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, North New Guinea, Huon Gulf, Markham, Upper, Mountain
zka	Kaimbulawa	Austronesian, Malayo-Polynesian, Celebic, Eastern, Southeastern, Muna-Buton, Nuclear Muna-Buton, Munan, Munic
zlm	Malay	Austronesian, Malayo-Polynesian, Malayo-Chamic, Malayic, Malay
zbc	Berawan, Central	Austronesian, Malayo-Polynesian, North Borneo, North Sarawakan, Berawan-Lower Baram, Berawan, Central-East Berawan
zbe	Berawan, East	Austronesian, Malayo-Polynesian, North Borneo, North Sarawakan, Berawan-Lower Baram, Berawan, Central-East Berawan
zbt	Batui	Austronesian, Malayo-Polynesian, Celebic, Eastern, Saluan-Banggai, Western, Saluanic
zbw	Berawan, West	Austronesian, Malayo-Polynesian, North Borneo, North Sarawakan, Berawan-Lower Baram, Berawan
zeg	Zenag	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, North New Guinea, Huon Gulf, South, Hote-Buang, Buang, Mumeng
zmi	Negeri Sembilan Malay	Austronesian, Malayo-Polynesian, Malayo-Chamic, Malayic, Malay
zgr	Magori	Austronesian, Malayo-Polynesian, Central-Eastern Malayo-Polynesian, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, Papuan Tip, Peripheral, Central Papuan, Oumic, Magoric
"""




class Migration(DataMigration):

    def forwards(self, orm):
        editor = orm['auth.user'].objects.all()[0]
        Language = orm['core.Language']
        for line in AUSTRONESIAN.split("\n"):
            line = line.strip()
            if len(line) > 0:
                line = line.split("\t")
                assert len(line) == 3
                isocode = line[0]
                assert len(isocode) == 3
                language = line[1]
                classif = line[2]
                assert classif.startswith('Austronesian')
                
                l = Language.objects.create(
                    isocode = isocode,
                    language = language,
                    classification = classif,
                    editor = editor
                )
                l.save()

    def backwards(self, orm):
        "Write your backwards methods here."

    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'core.language': {
            'Meta': {'ordering': "['language']", 'unique_together': "(('isocode', 'language'),)", 'object_name': 'Language', 'db_table': "'languages'"},
            'added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'classification': ('django.db.models.fields.TextField', [], {}),
            'editor': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'isocode': ('django.db.models.fields.CharField', [], {'max_length': '3', 'db_index': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_index': 'True'})
        },
        u'core.source': {
            'Meta': {'ordering': "['author', 'year']", 'object_name': 'Source', 'db_table': "'sources'", 'index_together': "[['author', 'year']]"},
            'added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'author': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_index': 'True'}),
            'bibtex': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'comment': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'editor': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'reference': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '64'}),
            'year': ('django.db.models.fields.IntegerField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['core']
    symmetrical = True
