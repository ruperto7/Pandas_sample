import pandas as pd
#import numpy as np
#from scipy.stats import ttest_ind

df=pd.read_csv("WA_Sales_Products_2012-14.csv")

''' Python 3.6.0 (v3.6.0:41df79263a11, Dec 23 2016, 08:06:12) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
 RESTART: C:\Users\711C\Downloads\_MOOCS DOST May 2018\MOD 3. Data Science\mod3 week5\Watson Analytics\wa.py 
>>> df.shape
(88475, 11)

>>> df.columns
Index(['Retailer country', 'Order method type', 'Retailer type',
       'Product line', 'Product type', 'Product', 'Year', 'Quarter', 'Revenue',
       'Quantity', 'Gross margin'],
      dtype='object')
	  
>>> df.head()
  Retailer country Order method type     ...      Quantity Gross margin
0    United States               Fax     ...           489     0.347548
1    United States               Fax     ...           252     0.474274
2    United States               Fax     ...           147     0.352772
3    United States               Fax     ...           303     0.282938
4    United States               Fax     ...          1415     0.291450

[5 rows x 11 columns]

>>> df.set_index(['Year', 'Quarter']).head()
             Retailer country     ...      Gross margin
Year Quarter                      ...                  
2012 Q1 2012    United States     ...          0.347548
     Q1 2012    United States     ...          0.474274
     Q1 2012    United States     ...          0.352772
     Q1 2012    United States     ...          0.282938
     Q1 2012    United States     ...          0.291450

[5 rows x 9 columns]

>>> df.groupby(['Retailer country','Year', 'Quarter']).head
<bound method GroupBy.head of <pandas.core.groupby.groupby.DataFrameGroupBy object at 0x0000025F3FD4AF28>>

>>> df.groupby(['Retailer country','Year', 'Quarter']).head()
      Retailer country Order method type     ...      Quantity Gross margin
0        United States               Fax     ...           489     0.347548
1        United States               Fax     ...           252     0.474274
2        United States               Fax     ...           147     0.352772
3        United States               Fax     ...           303     0.282938
4        United States               Fax     ...          1415     0.291450
864             Canada               Fax     ...           165     0.418630
865             Canada               Fax     ...           114     0.450544
866             Canada               Fax     ...            17     0.473455
867             Canada               Fax     ...           271     0.455317
868             Canada               Fax     ...           621     0.340707
1468            Mexico               Web     ...            21     0.474727
1469            Mexico               Web     ...            34     0.478828
1470            Mexico               Web     ...            26     0.451702
1471            Mexico               Web     ...            17     0.444782
1472            Mexico               Web     ...           126     0.340209
1833            Brazil               Web     ...           219     0.419206
1834            Brazil               Web     ...            43     0.478828
1835            Brazil               Web     ...           198     0.388419
1836            Brazil               Web     ...            93     0.458950
1837            Brazil               Web     ...            60     0.444223
2146             Japan               Fax     ...          7091     0.465823
2147             Japan               Fax     ...           957     0.466974
2148             Japan               Fax     ...           151     0.434205
2149             Japan               Fax     ...           462     0.467061
2150             Japan               Fax     ...           129     0.329056
2750         Singapore               Fax     ...           944     0.336810
2751         Singapore               Fax     ...           378     0.529480
2752         Singapore               Fax     ...           429     0.273356
2753         Singapore               Fax     ...           250     0.316417
2754         Singapore               Fax     ...           103     0.361866
...                ...               ...     ...           ...          ...
87166      Switzerland               Web     ...           108     0.402537
87167      Switzerland               Web     ...            68     0.460631
87168      Switzerland               Web     ...            42     0.445783
87169      Switzerland               Web     ...            27     0.425571
87170      Switzerland               Web     ...            39     0.584411
87390   United Kingdom         Telephone     ...          1309     0.489796
87391   United Kingdom         Telephone     ...           450     0.298984
87392   United Kingdom         Telephone     ...           426     0.410282
87393   United Kingdom         Telephone     ...           432     0.390939
87394   United Kingdom         Telephone     ...            72     0.321989
87677          Belgium               Web     ...            15     0.445783
87678          Belgium               Web     ...            19     0.495813
87679          Belgium               Web     ...            34     0.452254
87680          Belgium               Web     ...            22     0.445818
87681          Belgium               Web     ...            38     0.461416
87869          Austria               Web     ...            52     0.469245
87870          Austria               Web     ...            44     0.495813
87871          Austria               Web     ...            74     0.402537
87872          Austria               Web     ...           166     0.454891
87873          Austria               Web     ...            96     0.445801
88083            Italy         Telephone     ...           506     0.401272
88084            Italy         Telephone     ...           200     0.457647
88085            Italy         Telephone     ...           749     0.308878
88086            Italy         Telephone     ...           626     0.630000
88087            Italy         Telephone     ...          1322     0.479485
88281            Spain               Fax     ...           577     0.500000
88282            Spain               Fax     ...          1081     0.510444
88283            Spain               Fax     ...           728     0.378449
88284            Spain               Fax     ...           375     0.330068
88285            Spain               Fax     ...            94     0.386252

[1155 rows x 11 columns]
 
>>> df.groupby(['Retailer country','Year', 'Quarter']).head()
      Retailer country Order method type     ...      Quantity Gross margin
0        United States               Fax     ...           489     0.347548
1        United States               Fax     ...           252     0.474274
2        United States               Fax     ...           147     0.352772
3        United States               Fax     ...           303     0.282938
4        United States               Fax     ...          1415     0.291450
864             Canada               Fax     ...           165     0.418630
865             Canada               Fax     ...           114     0.450544
866             Canada               Fax     ...            17     0.473455
867             Canada               Fax     ...           271     0.455317
868             Canada               Fax     ...           621     0.340707
1468            Mexico               Web     ...            21     0.474727
1469            Mexico               Web     ...            34     0.478828
1470            Mexico               Web     ...            26     0.451702
1471            Mexico               Web     ...            17     0.444782
1472            Mexico               Web     ...           126     0.340209
1833            Brazil               Web     ...           219     0.419206
1834            Brazil               Web     ...            43     0.478828
1835            Brazil               Web     ...           198     0.388419
1836            Brazil               Web     ...            93     0.458950
1837            Brazil               Web     ...            60     0.444223
2146             Japan               Fax     ...          7091     0.465823
2147             Japan               Fax     ...           957     0.466974
2148             Japan               Fax     ...           151     0.434205
2149             Japan               Fax     ...           462     0.467061
2150             Japan               Fax     ...           129     0.329056
2750         Singapore               Fax     ...           944     0.336810
2751         Singapore               Fax     ...           378     0.529480
2752         Singapore               Fax     ...           429     0.273356
2753         Singapore               Fax     ...           250     0.316417
2754         Singapore               Fax     ...           103     0.361866
...                ...               ...     ...           ...          ...
87166      Switzerland               Web     ...           108     0.402537
87167      Switzerland               Web     ...            68     0.460631
87168      Switzerland               Web     ...            42     0.445783
87169      Switzerland               Web     ...            27     0.425571
87170      Switzerland               Web     ...            39     0.584411
87390   United Kingdom         Telephone     ...          1309     0.489796
87391   United Kingdom         Telephone     ...           450     0.298984
87392   United Kingdom         Telephone     ...           426     0.410282
87393   United Kingdom         Telephone     ...           432     0.390939
87394   United Kingdom         Telephone     ...            72     0.321989
87677          Belgium               Web     ...            15     0.445783
87678          Belgium               Web     ...            19     0.495813
87679          Belgium               Web     ...            34     0.452254
87680          Belgium               Web     ...            22     0.445818
87681          Belgium               Web     ...            38     0.461416
87869          Austria               Web     ...            52     0.469245
87870          Austria               Web     ...            44     0.495813
87871          Austria               Web     ...            74     0.402537
87872          Austria               Web     ...           166     0.454891
87873          Austria               Web     ...            96     0.445801
88083            Italy         Telephone     ...           506     0.401272
88084            Italy         Telephone     ...           200     0.457647
88085            Italy         Telephone     ...           749     0.308878
88086            Italy         Telephone     ...           626     0.630000
88087            Italy         Telephone     ...          1322     0.479485
88281            Spain               Fax     ...           577     0.500000
88282            Spain               Fax     ...          1081     0.510444
88283            Spain               Fax     ...           728     0.378449
88284            Spain               Fax     ...           375     0.330068
88285            Spain               Fax     ...            94     0.386252

[1155 rows x 11 columns]
>>> type(df.groupby(['Retailer country','Year', 'Quarter']))
<class 'pandas.core.groupby.groupby.DataFrameGroupBy'>

>>> df.set_index(['Year', 'Quarter']).groupby(['Retailer country','Year', 'Quarter']).head()
             Retailer country     ...      Gross margin
Year Quarter                      ...                  
2012 Q1 2012    United States     ...          0.347548
     Q1 2012    United States     ...          0.474274
     Q1 2012    United States     ...          0.352772
     Q1 2012    United States     ...          0.282938
     Q1 2012    United States     ...          0.291450
     Q1 2012           Canada     ...          0.418630
     Q1 2012           Canada     ...          0.450544
     Q1 2012           Canada     ...          0.473455
     Q1 2012           Canada     ...          0.455317
     Q1 2012           Canada     ...          0.340707
     Q1 2012           Mexico     ...          0.474727
     Q1 2012           Mexico     ...          0.478828
     Q1 2012           Mexico     ...          0.451702
     Q1 2012           Mexico     ...          0.444782
     Q1 2012           Mexico     ...          0.340209
     Q1 2012           Brazil     ...          0.419206
     Q1 2012           Brazil     ...          0.478828
     Q1 2012           Brazil     ...          0.388419
     Q1 2012           Brazil     ...          0.458950
     Q1 2012           Brazil     ...          0.444223
     Q1 2012            Japan     ...          0.465823
     Q1 2012            Japan     ...          0.466974
     Q1 2012            Japan     ...          0.434205
     Q1 2012            Japan     ...          0.467061
     Q1 2012            Japan     ...          0.329056
     Q1 2012        Singapore     ...          0.336810
     Q1 2012        Singapore     ...          0.529480
     Q1 2012        Singapore     ...          0.273356
     Q1 2012        Singapore     ...          0.316417
     Q1 2012        Singapore     ...          0.361866
...                       ...     ...               ...
2014 Q3 2014      Switzerland     ...          0.402537
     Q3 2014      Switzerland     ...          0.460631
     Q3 2014      Switzerland     ...          0.445783
     Q3 2014      Switzerland     ...          0.425571
     Q3 2014      Switzerland     ...          0.584411
     Q3 2014   United Kingdom     ...          0.489796
     Q3 2014   United Kingdom     ...          0.298984
     Q3 2014   United Kingdom     ...          0.410282
     Q3 2014   United Kingdom     ...          0.390939
     Q3 2014   United Kingdom     ...          0.321989
     Q3 2014          Belgium     ...          0.445783
     Q3 2014          Belgium     ...          0.495813
     Q3 2014          Belgium     ...          0.452254
     Q3 2014          Belgium     ...          0.445818
     Q3 2014          Belgium     ...          0.461416
     Q3 2014          Austria     ...          0.469245
     Q3 2014          Austria     ...          0.495813
     Q3 2014          Austria     ...          0.402537
     Q3 2014          Austria     ...          0.454891
     Q3 2014          Austria     ...          0.445801
     Q3 2014            Italy     ...          0.401272
     Q3 2014            Italy     ...          0.457647
     Q3 2014            Italy     ...          0.308878
     Q3 2014            Italy     ...          0.630000
     Q3 2014            Italy     ...          0.479485
     Q3 2014            Spain     ...          0.500000
     Q3 2014            Spain     ...          0.510444
     Q3 2014            Spain     ...          0.378449
     Q3 2014            Spain     ...          0.330068
     Q3 2014            Spain     ...          0.386252

[1155 rows x 9 columns]

>>> df.set_index(['Year', 'Quarter']).groupby(['Retailer country','Year', 'Quarter'])['Gross margin'].mean()
Retailer country  Year  Quarter
Australia         2012  Q1 2012    0.446321
                        Q2 2012    0.446051
                        Q3 2012    0.448517
                        Q4 2012    0.450948
                  2013  Q1 2013    0.456356
                        Q2 2013    0.453804
                        Q3 2013    0.461012
                        Q4 2013    0.457902
                  2014  Q1 2014    0.445961
                        Q2 2014    0.447167
                        Q3 2014    0.446856
Austria           2012  Q1 2012    0.448336
                        Q2 2012    0.441735
                        Q3 2012    0.447822
                        Q4 2012    0.446450
                  2013  Q1 2013    0.460925
                        Q2 2013    0.457862
                        Q3 2013    0.451601
                        Q4 2013    0.457137
                  2014  Q1 2014    0.448704
                        Q2 2014    0.450644
                        Q3 2014    0.447378
Belgium           2012  Q1 2012    0.446110
                        Q2 2012    0.444348
                        Q3 2012    0.447789
                        Q4 2012    0.436787
                  2013  Q1 2013    0.454073
                        Q2 2013    0.452210
                        Q3 2013    0.452904
                        Q4 2013    0.451540
                                     ...   
Switzerland       2012  Q4 2012    0.442738
                  2013  Q1 2013    0.454423
                        Q2 2013    0.454166
                        Q3 2013    0.457799
                        Q4 2013    0.456092
                  2014  Q1 2014    0.451758
                        Q2 2014    0.451976
                        Q3 2014    0.443259
United Kingdom    2012  Q1 2012    0.449795
                        Q2 2012    0.441519
                        Q3 2012    0.450643
                        Q4 2012    0.434737
                  2013  Q1 2013    0.454821
                        Q2 2013    0.452519
                        Q3 2013    0.457815
                        Q4 2013    0.456303
                  2014  Q1 2014    0.449550
                        Q2 2014    0.448519
                        Q3 2014    0.442138
United States     2012  Q1 2012    0.450253
                        Q2 2012    0.444415
                        Q3 2012    0.452620
                        Q4 2012    0.435313
                  2013  Q1 2013    0.436078
                        Q2 2013    0.459719
                        Q3 2013    0.461815
                        Q4 2013    0.454984
                  2014  Q1 2014    0.450494
                        Q2 2014    0.451570
                        Q3 2014    0.450442
Name: Gross margin, Length: 231, dtype: float64

>>> df.set_index(['Year', 'Quarter']).groupby(['Retailer country','Year', 'Quarter','Gross margin'])['Gross margin'].mean()
Retailer country  Year  Quarter  Gross margin
Australia         2012  Q1 2012  0.235294        0.235294
                                 0.243416        0.243416
                                 0.244681        0.244681
                                 0.260994        0.260994
                                 0.265588        0.265588
                                 0.273356        0.273356
                                 0.280691        0.280691
                                 0.281187        0.281187
                                 0.281444        0.281444
                                 0.282938        0.282938
                                 0.283633        0.283633
                                 0.284152        0.284152
                                 0.288952        0.288952
                                 0.291450        0.291450
                                 0.291657        0.291657
                                 0.294893        0.294893
                                 0.299203        0.299203
                                 0.301264        0.301264
                                 0.302363        0.302363
                                 0.313423        0.313423
                                 0.314776        0.314776
                                 0.316417        0.316417
                                 0.316895        0.316895
                                 0.316940        0.316940
                                 0.322122        0.322122
                                 0.322898        0.322898
                                 0.323234        0.323234
                                 0.325791        0.325791
                                 0.329056        0.329056
                                 0.329984        0.329984
                                                   ...   
United States     2014  Q3 2014  0.571001        0.571001
                                 0.573588        0.573588
                                 0.574841        0.574841
                                 0.578034        0.578034
                                 0.583463        0.583463
                                 0.584411        0.584411
                                 0.584531        0.584531
                                 0.587808        0.587808
                                 0.590518        0.590518
                                 0.601429        0.601429
                                 0.602011        0.602011
                                 0.604222        0.604222
                                 0.604543        0.604543
                                 0.608000        0.608000
                                 0.610000        0.610000
                                 0.615986        0.615986
                                 0.617452        0.617452
                                 0.625037        0.625037
                                 0.630000        0.630000
                                 0.632887        0.632887
                                 0.637652        0.637652
                                 0.642825        0.642825
                                 0.666993        0.666993
                                 0.667143        0.667143
                                 0.668097        0.668097
                                 0.690000        0.690000
                                 0.695507        0.695507
                                 0.731429        0.731429
                                 0.750924        0.750924
                                 0.752137        0.752137
Name: Gross margin, Length: 60606, dtype: float64

>>> df.set_index(['Year', 'Quarter']).groupby(['Retailer country','Year', 'Quarter'])['Gross margin'].mean()
Retailer country  Year  Quarter
Australia         2012  Q1 2012    0.446321
                        Q2 2012    0.446051
                        Q3 2012    0.448517
                        Q4 2012    0.450948
                  2013  Q1 2013    0.456356
                        Q2 2013    0.453804
                        Q3 2013    0.461012
                        Q4 2013    0.457902
                  2014  Q1 2014    0.445961
                        Q2 2014    0.447167
                        Q3 2014    0.446856
Austria           2012  Q1 2012    0.448336
                        Q2 2012    0.441735
                        Q3 2012    0.447822
                        Q4 2012    0.446450
                  2013  Q1 2013    0.460925
                        Q2 2013    0.457862
                        Q3 2013    0.451601
                        Q4 2013    0.457137
                  2014  Q1 2014    0.448704
                        Q2 2014    0.450644
                        Q3 2014    0.447378
Belgium           2012  Q1 2012    0.446110
                        Q2 2012    0.444348
                        Q3 2012    0.447789
                        Q4 2012    0.436787
                  2013  Q1 2013    0.454073
                        Q2 2013    0.452210
                        Q3 2013    0.452904
                        Q4 2013    0.451540
                                     ...   
Switzerland       2012  Q4 2012    0.442738
                  2013  Q1 2013    0.454423
                        Q2 2013    0.454166
                        Q3 2013    0.457799
                        Q4 2013    0.456092
                  2014  Q1 2014    0.451758
                        Q2 2014    0.451976
                        Q3 2014    0.443259
United Kingdom    2012  Q1 2012    0.449795
                        Q2 2012    0.441519
                        Q3 2012    0.450643
                        Q4 2012    0.434737
                  2013  Q1 2013    0.454821
                        Q2 2013    0.452519
                        Q3 2013    0.457815
                        Q4 2013    0.456303
                  2014  Q1 2014    0.449550
                        Q2 2014    0.448519
                        Q3 2014    0.442138
United States     2012  Q1 2012    0.450253
                        Q2 2012    0.444415
                        Q3 2012    0.452620
                        Q4 2012    0.435313
                  2013  Q1 2013    0.436078
                        Q2 2013    0.459719
                        Q3 2013    0.461815
                        Q4 2013    0.454984
                  2014  Q1 2014    0.450494
                        Q2 2014    0.451570
                        Q3 2014    0.450442
Name: Gross margin, Length: 231, dtype: float64

>>> df.set_index(['Year', 'Quarter'])
             Retailer country     ...      Gross margin
Year Quarter                      ...                  
2012 Q1 2012    United States     ...          0.347548
     Q1 2012    United States     ...          0.474274
     Q1 2012    United States     ...          0.352772
     Q1 2012    United States     ...          0.282938
     Q1 2012    United States     ...          0.291450
     Q1 2012    United States     ...          0.398146
     Q1 2012    United States     ...          0.335607
     Q1 2012    United States     ...          0.528960
     Q1 2012    United States     ...          0.434205
     Q1 2012    United States     ...          0.461493
     Q1 2012    United States     ...          0.361866
     Q1 2012    United States     ...          0.329056
     Q1 2012    United States     ...          0.291657
     Q1 2012    United States     ...          0.301264
     Q1 2012    United States     ...          0.314776
     Q1 2012    United States     ...          0.244681
     Q1 2012    United States     ...          0.283633
     Q1 2012    United States     ...          0.478433
     Q1 2012    United States     ...          0.514224
     Q1 2012    United States     ...          0.478723
     Q1 2012    United States     ...          0.476140
     Q1 2012    United States     ...          0.502170
     Q1 2012    United States     ...          0.427688
     Q1 2012    United States     ...          0.564981
     Q1 2012    United States     ...          0.589844
     Q1 2012    United States     ...          0.516440
     Q1 2012    United States     ...          0.481782
     Q1 2012    United States     ...          0.243416
     Q1 2012    United States     ...          0.336999
     Q1 2012    United States     ...          0.490206
...                       ...     ...               ...
2014 Q3 2014            Spain     ...          0.412525
     Q3 2014            Spain     ...          0.339685
     Q3 2014            Spain     ...          0.416140
     Q3 2014            Spain     ...          0.463847
     Q3 2014            Spain     ...          0.536567
     Q3 2014            Spain     ...          0.288314
     Q3 2014            Spain     ...          0.533911
     Q3 2014            Spain     ...          0.360705
     Q3 2014            Spain     ...          0.350936
     Q3 2014            Spain     ...          0.632887
     Q3 2014            Spain     ...          0.540000
     Q3 2014            Spain     ...          0.670543
     Q3 2014            Spain     ...          0.479485
     Q3 2014            Spain     ...          0.617452
     Q3 2014            Spain     ...          0.524254
     Q3 2014            Spain     ...          0.519169
     Q3 2014            Spain     ...          0.343656
     Q3 2014            Spain     ...          0.460043
     Q3 2014            Spain     ...          0.379974
     Q3 2014            Spain     ...          0.533518
     Q3 2014            Spain     ...          0.530075
     Q3 2014            Spain     ...          0.388587
     Q3 2014            Spain     ...          0.440525
     Q3 2014            Spain     ...          0.464877
     Q3 2014            Spain     ...          0.368511
     Q3 2014            Spain     ...          0.299114
     Q3 2014            Spain     ...          0.446287
     Q3 2014            Spain     ...          0.569420
     Q3 2014            Spain     ...          0.491667
     Q3 2014            Spain     ...          0.387895

[88475 rows x 9 columns]

>>> df.set_index(['Year', 'Quarter']).head()
             Retailer country     ...      Gross margin
Year Quarter                      ...                  
2012 Q1 2012    United States     ...          0.347548
     Q1 2012    United States     ...          0.474274
     Q1 2012    United States     ...          0.352772
     Q1 2012    United States     ...          0.282938
     Q1 2012    United States     ...          0.291450

[5 rows x 9 columns]

>>> type(df.columns)
<class 'pandas.core.indexes.base.Index'>
>>> '''


