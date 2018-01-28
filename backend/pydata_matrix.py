from numpy import *
xl = {'data': [['Active CHB HBeAg-positive', 'id', nan, 0.016, nan, 0.0147, 0.07, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, 0.006, 0.0011, 'mort 0'], ['Active CHB HBeAg-negative', 0.0016, 'id', 0.028, nan, 0.0072, 0.016, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, 0.006, 0.0011, 'mort 0'], ['Compensated Cirrhosis', nan, nan, 'id', 0.039, 0.0316, nan, 0.063, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, 0.015, 0.0489, 'mort 0'], ['Decompensated Cirrhosis', nan, nan, nan, 'id', 0.071, nan, nan, nan, 0.012, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, 0.15, 'mort 0'], ['HCC', nan, nan, nan, nan, 'id', nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, 0.07, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, 0.151, 'mort 0'], ['Inactive', nan, 'age 0', 'age 1', nan, nan, 'id', nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, 'age 2', nan, 'mort 0'], ['Viral Suppression Cirrhosis', nan, nan, nan, nan, 0.0158, nan, 'id', nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, 0.01, 0.0244, 'mort 0'], ['Viral Suppression Decompensated Cirrhosis', nan, nan, nan, nan, 0.0355, nan, nan, 'id', nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, 0.075, 'mort 0'], ['Liver Transplantation Decompensated Cirrhosis Year 1', nan, nan, nan, nan, nan, nan, nan, nan, nan, 'id', nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, 0.17, 'mort 0'], ['Liver Transplantation Decompensated Cirrhosis Year 2', nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, 'id', nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, 0.2, 'mort 0'], ['Liver Transplantation Decompensated Cirrhosis Year 3', nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, 'id', nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, 0.22, 'mort 0'], ['Liver Transplantation Decompensated Cirrhosis Year 4', nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, 'id', nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, 0.24, 'mort 0'], ['Liver Transplantation Decompensated Cirrhosis Year 5', nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, 'id', nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, 0.25, 'mort 0'], ['Liver Transplantation Decompensated Cirrhosis Year 6', nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, 'id', nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, 0.26, 'mort 0'], ['Liver Transplantation Decompensated Cirrhosis Year 7', nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, 'id', nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, 0.28, 'mort 0'], ['Liver Transplantation Decompensated Cirrhosis Year 8', nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, 'id', nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, 0.29, 'mort 0'], ['Liver Transplantation Decompensated Cirrhosis Year 9', nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, 'id', nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, 0.3, 'mort 0'], ['Liver Transplantation Decompensated Cirrhosis Year 10', nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, 'id', nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, 0.32, 'mort 0'], ['Liver Transplantation HCC Year 1', nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, 'id', nan, nan, nan, nan, nan, nan, nan, nan, nan, 0.16, 'mort 0'], ['Liver Transplantation HCC Year 2', nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, 'id', nan, nan, nan, nan, nan, nan, nan, nan, 0.24, 'mort 0'], ['Liver Transplantation HCC Year 3', nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, 'id', nan, nan, nan, nan, nan, nan, nan, 0.27, 'mort 0'], ['Liver Transplantation HCC Year 4', nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, 'id', nan, nan, nan, nan, nan, nan, 0.3, 'mort 0'], ['Liver Transplantation HCC Year 5', nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, 'id', nan, nan, nan, nan, nan, 0.32, 'mort 0'], ['Liver Transplantation HCC Year 6', nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, 'id', nan, nan, nan, nan, 0.34, 'mort 0'], ['Liver Transplantation HCC Year 7', nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, 'id', nan, nan, nan, 0.35, 'mort 0'], ['Liver Transplantation HCC Year 8', nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, 'id', nan, nan, 0.37, 'mort 0'], ['Liver Transplantation HCC Year 9', nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, 'id', nan, 0.38, 'mort 0'], ['Liver Transplantation HCC Year 10', nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, 'id', nan, 0.39, 'mort 0'], ['HBsAg loss', nan, nan, 0.0028, nan, 0.00091, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, 'id', nan, 'mort 0'], ['HBV Death', nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, 'id', nan], ['Death other', nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, 'id']], 'gender': [['Active CHB HBeAg-positive', nan, nan, 1.0, nan, 1.0, 1.0, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, 1.0, nan], ['Active CHB HBeAg-negative', nan, nan, 1.0, nan, 1.0, 1.0, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, 1.0, nan], ['Compensated Cirrhosis', nan, nan, nan, 1.0, 1.0, nan, 1.0, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, 1.0, nan], ['Decompensated Cirrhosis', nan, nan, nan, nan, 1.0, nan, nan, nan, 1.0, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, 1.0, nan], ['HCC', nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, 1.0, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, 1.0, nan], ['Inactive', nan, 1.0, 1.0, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan], ['Viral Suppression Cirrhosis', nan, nan, nan, nan, 1.0, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, 1.0, nan], ['Viral Suppression Decompensated Cirrhosis', nan, nan, nan, nan, 1.0, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, 1.0, nan], ['Liver Transplantation Decompensated Cirrhosis Year 1', nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, 1.0, nan], ['Liver Transplantation Decompensated Cirrhosis Year 2', nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, 1.0, nan], ['Liver Transplantation Decompensated Cirrhosis Year 3', nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, 1.0, nan], ['Liver Transplantation Decompensated Cirrhosis Year 4', nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, 1.0, nan], ['Liver Transplantation Decompensated Cirrhosis Year 5', nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, 1.0, nan], ['Liver Transplantation Decompensated Cirrhosis Year 6', nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, 1.0, nan], ['Liver Transplantation Decompensated Cirrhosis Year 7', nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, 1.0, nan], ['Liver Transplantation Decompensated Cirrhosis Year 8', nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, 1.0, nan], ['Liver Transplantation Decompensated Cirrhosis Year 9', nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, 1.0, nan], ['Liver Transplantation Decompensated Cirrhosis Year 10', nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, 1.0, nan], ['Liver Transplantation HCC Year 1', nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, 1.0, nan], ['Liver Transplantation HCC Year 2', nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, 1.0, nan], ['Liver Transplantation HCC Year 3', nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, 1.0, nan], ['Liver Transplantation HCC Year 4', nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, 1.0, nan], ['Liver Transplantation HCC Year 5', nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, 1.0, nan], ['Liver Transplantation HCC Year 6', nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, 1.0, nan], ['Liver Transplantation HCC Year 7', nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, 1.0, nan], ['Liver Transplantation HCC Year 8', nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, 1.0, nan], ['Liver Transplantation HCC Year 9', nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, 1.0, nan], ['Liver Transplantation HCC Year 10', nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, 1.0, nan], ['HBsAg loss', nan, nan, 1.0, nan, 1.0, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan], ['HBV Death', nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan], ['Death other', nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan]], 'mort': [[0.0, 0.0], [1.0, 0.000445], [2.0, 0.000301], [3.0, 0.00024], [4.0, 0.000183], [5.0, 0.000169], [6.0, 0.00015], [7.0, 0.000134], [8.0, 0.000115], [9.0, 9.7e-05], [10.0, 8.5e-05], [11.0, 9.2e-05], [12.0, 0.000132], [13.0, 0.000213], [14.0, 0.000323], [15.0, 0.000439], [16.0, 0.000552], [17.0, 0.000675], [18.0, 0.000807], [19.0, 0.000942], [20.0, 0.001085], [21.0, 0.001216], [22.0, 0.00131], [23.0, 0.001353], [24.0, 0.001358], [25.0, 0.001351], [26.0, 0.001349], [27.0, 0.001353], [28.0, 0.001371], [29.0, 0.001399], [30.0, 0.001432], [31.0, 0.001464], [32.0, 0.001496], [33.0, 0.001528], [34.0, 0.001563], [35.0, 0.001613], [36.0, 0.001682], [37.0, 0.001764], [38.0, 0.001857], [39.0, 0.001964], [40.0, 0.002083], [41.0, 0.002227], [42.0, 0.002414], [43.0, 0.002653], [44.0, 0.002939], [45.0, 0.003243], [46.0, 0.003563], [47.0, 0.003922], [48.0, 0.00432], [49.0, 0.004749], [50.0, 0.005193], [51.0, 0.005647], [52.0, 0.006122], [53.0, 0.00663], [54.0, 0.007181], [55.0, 0.007779], [56.0, 0.008415], [57.0, 0.009074], [58.0, 0.009727], [59.0, 0.010371], [60.0, 0.011034], [61.0, 0.011738], [62.0, 0.012489], [63.0, 0.013335], [64.0, 0.014319], [65.0, 0.015482], [66.0, 0.016824], [67.0, 0.01833], [68.0, 0.0199], [69.0, 0.021539], [70.0, 0.023396], [71.0, 0.025476], [72.0, 0.027794], [73.0, 0.03035], [74.0, 0.033204], [75.0, 0.036345], [76.0, 0.039788], [77.0, 0.04372], [78.0, 0.048335], [79.0, 0.05365], [80.0, 0.059565], [81.0, 0.065848], [82.0, 0.072956], [83.0, 0.080741], [84.0, 0.089357], [85.0, 0.09965], [86.0, 0.110901], [87.0, 0.123146], [88.0, 0.136412], [89.0, 0.15071], [90.0, 0.166038], [91.0, 0.182374], [92.0, 0.199676], [93.0, 0.21788], [94.0, 0.236903], [95.0, 0.256636], [96.0, 0.276954], [97.0, 0.297713], [98.0, 0.318755], [99.0, 0.339914], [100.0, 1.0], [nan, 0.000382], [nan, 0.000225], [nan, 0.000175], [nan, 0.000151], [nan, 0.000132], [nan, 0.000117], [nan, 0.000106], [nan, 9.6e-05], [nan, 8.8e-05], [nan, 8.4e-05], [nan, 8.7e-05], [nan, 0.000102], [nan, 0.000129], [nan, 0.000166], [nan, 0.000207], [nan, 0.000247], [nan, 0.000286], [nan, 0.00032], [nan, 0.000351], [nan, 0.000384], [nan, 0.000416], [nan, 0.000445], [nan, 0.000467], [nan, 0.000486], [nan, 0.000505], [nan, 0.000526], [nan, 0.000553], [nan, 0.000587], [nan, 0.000627], [nan, 0.000673], [nan, 0.000721], [nan, 0.000766], [nan, 0.000805], [nan, 0.000842], [nan, 0.000888], [nan, 0.000947], [nan, 0.001017], [nan, 0.001099], [nan, 0.001192], [nan, 0.001291], [nan, 0.001402], [nan, 0.001535], [nan, 0.001695], [nan, 0.001879], [nan, 0.00207], [nan, 0.002268], [nan, 0.002486], [nan, 0.002725], [nan, 0.002977], [nan, 0.003245], [nan, 0.003514], [nan, 0.003776], [nan, 0.004029], [nan, 0.004289], [nan, 0.004564], [nan, 0.004875], [nan, 0.005234], [nan, 0.005647], [nan, 0.006103], [nan, 0.006589], [nan, 0.007104], [nan, 0.007665], [nan, 0.008303], [nan, 0.00905], [nan, 0.009953], [nan, 0.011001], [nan, 0.012124], [nan, 0.01325], [nan, 0.014419], [nan, 0.015718], [nan, 0.017201], [nan, 0.018896], [nan, 0.020818], [nan, 0.022996], [nan, 0.025387], [nan, 0.02809], [nan, 0.031225], [nan, 0.034786], [nan, 0.038792], [nan, 0.043109], [nan, 0.0478], [nan, 0.053181], [nan, 0.059365], [nan, 0.066859], [nan, 0.075391], [nan, 0.084744], [nan, 0.095072], [nan, 0.106427], [nan, 0.118857], [nan, 0.132396], [nan, 0.147063], [nan, 0.162859], [nan, 0.179765], [nan, 0.197737], [nan, 0.216706], [nan, 0.236577], [nan, 0.257228], [nan, 0.278515], [nan, 0.300271], [nan, 1.0]], 'age': [[0.0, 0.0, 0.0, 0.0], [1.0, 0.009, 0.00038, 0.008], [2.0, nan, nan, nan], [3.0, nan, nan, nan], [4.0, nan, nan, nan], [5.0, nan, nan, nan], [6.0, nan, nan, nan], [7.0, nan, nan, nan], [8.0, nan, nan, nan], [9.0, nan, nan, nan], [10.0, nan, nan, nan], [11.0, nan, nan, nan], [12.0, nan, nan, nan], [13.0, nan, nan, nan], [14.0, nan, nan, nan], [15.0, nan, nan, nan], [16.0, nan, nan, nan], [17.0, nan, nan, nan], [18.0, nan, nan, nan], [19.0, nan, nan, nan], [20.0, nan, nan, nan], [21.0, nan, nan, nan], [22.0, nan, nan, nan], [23.0, nan, nan, nan], [24.0, nan, nan, nan], [25.0, nan, nan, nan], [26.0, nan, nan, nan], [27.0, nan, nan, nan], [28.0, nan, nan, nan], [29.0, nan, nan, nan], [30.0, 0.014, 0.00049, 0.011], [31.0, nan, nan, nan], [32.0, nan, nan, nan], [33.0, nan, nan, nan], [34.0, nan, nan, nan], [35.0, nan, nan, nan], [36.0, nan, nan, nan], [37.0, nan, nan, nan], [38.0, nan, nan, nan], [39.0, nan, nan, nan], [40.0, 0.028, 0.00068, 0.017], [41.0, nan, nan, nan], [42.0, nan, nan, nan], [43.0, nan, nan, nan], [44.0, nan, nan, nan], [45.0, nan, nan, nan], [46.0, nan, nan, nan], [47.0, nan, nan, nan], [48.0, nan, nan, nan], [49.0, nan, nan, nan], [50.0, 0.2, 0.0015, 0.018], [51.0, nan, nan, nan], [52.0, nan, nan, nan], [53.0, nan, nan, nan], [54.0, nan, nan, nan], [55.0, nan, nan, nan], [56.0, nan, nan, nan], [57.0, nan, nan, nan], [58.0, nan, nan, nan], [59.0, nan, nan, nan], [60.0, nan, nan, nan], [61.0, nan, nan, nan], [62.0, nan, nan, nan], [63.0, nan, nan, nan], [64.0, nan, nan, nan], [65.0, nan, nan, nan], [66.0, nan, nan, nan], [67.0, nan, nan, nan], [68.0, nan, nan, nan], [69.0, nan, nan, nan], [70.0, nan, nan, nan], [71.0, nan, nan, nan], [72.0, nan, nan, nan], [73.0, nan, nan, nan], [74.0, nan, nan, nan], [75.0, nan, nan, nan], [76.0, nan, nan, nan], [77.0, nan, nan, nan], [78.0, nan, nan, nan], [79.0, nan, nan, nan], [80.0, nan, nan, nan], [81.0, nan, nan, nan], [82.0, nan, nan, nan], [83.0, nan, nan, nan], [84.0, nan, nan, nan], [85.0, nan, nan, nan], [86.0, nan, nan, nan], [87.0, nan, nan, nan], [88.0, nan, nan, nan], [89.0, nan, nan, nan], [90.0, nan, nan, nan], [91.0, nan, nan, nan], [92.0, nan, nan, nan], [93.0, nan, nan, nan], [94.0, nan, nan, nan], [95.0, nan, nan, nan], [96.0, nan, nan, nan], [97.0, nan, nan, nan], [98.0, nan, nan, nan], [99.0, nan, nan, nan], [100.0, nan, nan, nan]], 'cirr_year': [[0.0, 0.17], [1.0, 0.2], [2.0, 0.22], [3.0, 0.24], [4.0, 0.25], [5.0, 0.26], [6.0, 0.28], [7.0, 0.29], [8.0, 0.3], [9.0, 0.32]], 'trans_year': [[0.0, 0.16], [1.0, 0.24], [2.0, 0.27], [3.0, 0.3], [4.0, 0.32], [5.0, 0.34], [6.0, 0.35], [7.0, 0.37], [8.0, 0.38], [9.0, 0.39]], 'Natural History': [['Active CHB HBeAg-positive', nan, nan, 0.016, nan, 0.0147, 0.07, nan, nan, nan, 0.006, 0.0011, 'See Table B'], ['Active CHB HBeAg-negative', 0.0016, nan, 0.028, nan, 0.0072, 0.016, nan, nan, nan, 0.006, 0.0011, 'See Table B'], ['Compensated Cirrhosis', nan, nan, nan, 0.039, 0.0316, nan, 0.063, nan, nan, 0.015, 0.0489, 'See Table B'], ['Decompensated Cirrhosis', nan, nan, nan, nan, 0.071, nan, nan, 0.012, nan, nan, 0.15, 'See Table B'], ['HCC', nan, nan, nan, nan, nan, nan, nan, nan, 0.07, nan, 0.151, 'See Table B'], ['Inactive', nan, '<30 years 0.009, 30-39 years 0.014, 40-49 years 0.028, 50+ years 0.020', '<30 years 0.00038, 30-39 years 0.00049, 40-49 years 0.00068, 50+ years 0.0015', nan, nan, nan, nan, nan, nan, '<30 years 0.008, 30-39 years 0.011, 40-49 years 0.017, 50+ years 0.018', nan, 'See Table B'], ['Viral Suppression Cirrhosis', nan, nan, nan, nan, 0.0158, nan, nan, nan, nan, 0.01, 0.0244, 'See Table B'], ['Viral Suppression Decompensated Cirrhosis', nan, nan, nan, nan, 0.0355, nan, nan, nan, nan, nan, 0.075, 'See Table B'], ['Liver Transplantation Decompensated Cirrhosis', nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, 'See Table A', 'See Table B'], ['Liver Transplantation HCC', nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, 'See Table A', 'See Table B'], ['HBsAg loss', nan, nan, 0.0028, nan, 0.00091, nan, nan, nan, nan, nan, nan, 'See Table B'], ['HBV Death', nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, 'Terminal', 'Terminal'], ['Death other', nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, 'Terminal', 'Terminal']], 'Treatment model': [[nan, 'From', 'Active CHB HBeAg-positive', 'Active CHB HBeAg-negative', 'Compensated Cirrhosis', 'Decompensated Cirrhosis', 'HCC', 'Viral Suppression CHB', 'Viral Suppression Compensated Cirrhosis', 'Viral Suppression Decompensated Cirrhosis', 'Liver Transplantation Decompensated Cirrhosis', 'Liver Transplantation HCC', 'HBsAg loss', 'HBV Death', 'Death other'], [nan, 'Active CHB HBeAg-positive', '#', '-', '-', '-', 0.007, 0.7, '-', '-', '-', '-', 0.03, '-', 'See Table B'], [nan, 'Active CHB HBeAg-negative', '-', '#', '-', '-', 0.0035, 0.9, '-', '-', '-', '-', 0.01, '-', 'See Table B'], [nan, 'Compensated Cirrhosis', '-', '-', '#', 0.018, 0.016, '-', 0.78, '-', '-', '-', 0.017, 0.024, 'See Table B'], [nan, 'Decompensated Cirrhosis', '-', '-', '-', '#', 0.035, '-', '-', 0.78, 0.012, '-', '-', 0.075, 'See Table B'], [nan, 'HCC', '-', '-', '-', '-', '#', '-', '-', '-', '-', 0.07, '-', 0.12, 'See Table B'], [nan, 'Viral Suppression CHB', '-', '-', '-', '-', 0.001, '#', '-', '-', '-', '-', 0.015, '-', 'See Table B'], [nan, 'Viral Suppression Compensated Cirrhosis', '-', '-', '-', '-', 0.008, '-', '#', '-', '-', '-', 0.015, 0.012, 'See Table B'], [nan, 'Viral Suppression Decompensated Cirrhosis', '-', '-', '-', '-', 0.003, '-', '-', '#', '-', '-', '-', 0.061, 'See Table B'], [nan, 'Liver Transplantation Decompensated Cirrhosis', '-', '-', '-', '-', '-', '-', '-', '-', '#', '-', '-', 'See Table A', 'See Table B'], [nan, 'Liver Transplantation HCC', '-', '-', '-', '-', '-', '-', '-', '-', '-', '#', '-', 'See Table A', 'See Table B'], [nan, 'HBV Death', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '#', '-', nan], [nan, 'Death other', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', 'Terminal', 'Terminal'], [nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, '-', '-', '-', 'Terminal', 'Terminal'], [nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan], [nan, '* 50% reduction for females', nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan], [nan, 'example: HCC to HBV Death = 0.12/2', nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan], [nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan], [nan, '# stay in that health state ', nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan]], 'Table A': [[nan, nan], ['From Liver Transplantation Decompensated Cirrhosis', nan], ['To HBV-related death year 1', 0.17], ['To HBV-related death year 2', 0.2], ['To HBV-related death year 3', 0.22], ['To HBV-related death year 4', 0.24], ['To HBV-related death year 5', 0.25], ['To HBV-related death year 6', 0.26], ['To HBV-related death year 7', 0.28], ['To HBV-related death year 8', 0.29], ['To HBV-related death year 9', 0.3], ['To HBV-related death year 10', 0.32], [nan, nan], ['From Liver Transplantation HCC', nan], ['To HBV-related death year 1', 0.16], ['To HBV-related death year 2', 0.24], ['To HBV-related death year 3', 0.27], ['To HBV-related death year 4', 0.3], ['To HBV-related death year 5', 0.32], ['To HBV-related death year 6', 0.34], ['To HBV-related death year 7', 0.35], ['To HBV-related death year 8', 0.37], ['To HBV-related death year 9', 0.38], ['To HBV-related death year 10', 0.39], [nan, nan], ['* 50% reduction in females', nan]], 'Background mortalityTable B': [[nan, nan, 'Index', 'Value', 'Value', nan, nan, nan], [nan, nan, 1, 0.000445, 0.000382, nan, nan, nan], [nan, nan, 2, 0.000301, 0.000225, nan, nan, nan], [nan, nan, 3, 0.00024, 0.000175, nan, nan, nan], [nan, nan, 4, 0.000183, 0.000151, nan, nan, nan], [nan, nan, 5, 0.000169, 0.000132, nan, nan, nan], [nan, nan, 6, 0.00015, 0.000117, nan, nan, nan], [nan, nan, 7, 0.000134, 0.000106, nan, nan, nan], [nan, nan, 8, 0.000115, 9.6e-05, nan, nan, nan], [nan, nan, 9, 9.7e-05, 8.8e-05, nan, nan, nan], [nan, nan, 10, 8.5e-05, 8.4e-05, nan, nan, nan], [nan, nan, 11, 9.2e-05, 8.7e-05, nan, nan, nan], [nan, nan, 12, 0.000132, 0.000102, nan, nan, nan], [nan, nan, 13, 0.000213, 0.000129, nan, nan, nan], [nan, nan, 14, 0.000323, 0.000166, nan, nan, nan], [nan, nan, 15, 0.000439, 0.000207, nan, nan, nan], [nan, nan, 16, 0.000552, 0.000247, nan, nan, nan], [nan, nan, 17, 0.000675, 0.000286, nan, nan, nan], [nan, nan, 18, 0.000807, 0.00032, nan, nan, '* 50% reduction for females'], [nan, nan, 19, 0.000942, 0.000351, nan, nan, 'example: HCC to HBV Death = 0.151/2'], [nan, nan, 20, 0.001085, 0.000384, nan, nan, nan], [nan, nan, 21, 0.001216, 0.000416, nan, nan, '# stay in that health state '], [nan, nan, 22, 0.00131, 0.000445, nan, nan, nan], [nan, nan, 23, 0.001353, 0.000467, nan, nan, nan], [nan, nan, 24, 0.001358, 0.000486, nan, nan, nan], [nan, nan, 25, 0.001351, 0.000505, nan, nan, nan], [nan, nan, 26, 0.001349, 0.000526, nan, nan, nan], [nan, nan, 27, 0.001353, 0.000553, nan, nan, nan], [nan, nan, 28, 0.001371, 0.000587, nan, nan, nan], [nan, nan, 29, 0.001399, 0.000627, nan, nan, nan], [nan, nan, 30, 0.001432, 0.000673, nan, nan, nan], [nan, nan, 31, 0.001464, 0.000721, nan, nan, nan], [nan, nan, 32, 0.001496, 0.000766, nan, nan, nan], [nan, nan, 33, 0.001528, 0.000805, nan, nan, nan], [nan, nan, 34, 0.001563, 0.000842, nan, nan, nan], [nan, nan, 35, 0.001613, 0.000888, nan, nan, nan], [nan, nan, 36, 0.001682, 0.000947, nan, nan, nan], [nan, nan, 37, 0.001764, 0.001017, nan, nan, nan], [nan, nan, 38, 0.001857, 0.001099, nan, nan, nan], [nan, nan, 39, 0.001964, 0.001192, nan, nan, nan], [nan, nan, 40, 0.002083, 0.001291, nan, nan, nan], [nan, nan, 41, 0.002227, 0.001402, nan, nan, nan], [nan, nan, 42, 0.002414, 0.001535, nan, nan, nan], [nan, nan, 43, 0.002653, 0.001695, nan, nan, nan], [nan, nan, 44, 0.002939, 0.001879, nan, nan, nan], [nan, nan, 45, 0.003243, 0.00207, nan, nan, nan], [nan, nan, 46, 0.003563, 0.002268, nan, nan, nan], [nan, nan, 47, 0.003922, 0.002486, nan, nan, nan], [nan, nan, 48, 0.00432, 0.002725, nan, nan, nan], [nan, nan, 49, 0.004749, 0.002977, nan, nan, nan], [nan, nan, 50, 0.005193, 0.003245, nan, nan, nan], [nan, nan, 51, 0.005647, 0.003514, nan, nan, nan], [nan, nan, 52, 0.006122, 0.003776, nan, nan, nan], [nan, nan, 53, 0.00663, 0.004029, nan, nan, nan], [nan, nan, 54, 0.007181, 0.004289, nan, nan, nan], [nan, nan, 55, 0.007779, 0.004564, nan, nan, nan], [nan, nan, 56, 0.008415, 0.004875, nan, nan, nan], [nan, nan, 57, 0.009074, 0.005234, nan, nan, nan], [nan, nan, 58, 0.009727, 0.005647, nan, nan, nan], [nan, nan, 59, 0.010371, 0.006103, nan, nan, nan], [nan, nan, 60, 0.011034, 0.006589, nan, nan, nan], [nan, nan, 61, 0.011738, 0.007104, nan, nan, nan], [nan, nan, 62, 0.012489, 0.007665, nan, nan, nan], [nan, nan, 63, 0.013335, 0.008303, nan, nan, nan], [nan, nan, 64, 0.014319, 0.00905, nan, nan, nan], [nan, nan, 65, 0.015482, 0.009953, nan, nan, nan], [nan, nan, 66, 0.016824, 0.011001, nan, nan, nan], [nan, nan, 67, 0.01833, 0.012124, nan, nan, nan], [nan, nan, 68, 0.0199, 0.01325, nan, nan, nan], [nan, nan, 69, 0.021539, 0.014419, nan, nan, nan], [nan, nan, 70, 0.023396, 0.015718, nan, nan, nan], [nan, nan, 71, 0.025476, 0.017201, nan, nan, nan], [nan, nan, 72, 0.027794, 0.018896, nan, nan, nan], [nan, nan, 73, 0.03035, 0.020818, nan, nan, nan], [nan, nan, 74, 0.033204, 0.022996, nan, nan, nan], [nan, nan, 75, 0.036345, 0.025387, nan, nan, nan], [nan, nan, 76, 0.039788, 0.02809, nan, nan, nan], [nan, nan, 77, 0.04372, 0.031225, nan, nan, nan], [nan, nan, 78, 0.048335, 0.034786, nan, nan, nan], [nan, nan, 79, 0.05365, 0.038792, nan, nan, nan], [nan, nan, 80, 0.059565, 0.043109, nan, nan, nan], [nan, nan, 81, 0.065848, 0.0478, nan, nan, nan], [nan, nan, 82, 0.072956, 0.053181, nan, nan, nan], [nan, nan, 83, 0.080741, 0.059365, nan, nan, nan], [nan, nan, 84, 0.089357, 0.066859, nan, nan, nan], [nan, nan, 85, 0.09965, 0.075391, nan, nan, nan], [nan, nan, 86, 0.110901, 0.084744, nan, nan, nan], [nan, nan, 87, 0.123146, 0.095072, nan, nan, nan], [nan, nan, 88, 0.136412, 0.106427, nan, nan, nan], [nan, nan, 89, 0.15071, 0.118857, nan, nan, nan], [nan, nan, 90, 0.166038, 0.132396, nan, nan, nan], [nan, nan, 91, 0.182374, 0.147063, nan, nan, nan], [nan, nan, 92, 0.199676, 0.162859, nan, nan, nan], [nan, nan, 93, 0.21788, 0.179765, nan, nan, nan], [nan, nan, 94, 0.236903, 0.197737, nan, nan, nan], [nan, nan, 95, 0.256636, 0.216706, nan, nan, nan], [nan, nan, 96, 0.276954, 0.236577, nan, nan, nan], [nan, nan, 97, 0.297713, 0.257228, nan, nan, nan], [nan, nan, 98, 0.318755, 0.278515, nan, nan, nan], [nan, nan, 99, 0.339914, 0.300271, nan, nan, nan], [nan, nan, 100, 1, 1, nan, nan, nan]]}