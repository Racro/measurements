{"stats": {"https": {"usr": [1.02, 4.0, 66.34, 68.69, 80.0, 79.21, 75.76, 76.24, 71.0, 66.0, 67.0, 73.74, 74.26, 71.0, 74.0, 71.29, 76.77, 66.0, 68.69, 76.0, 66.0, 72.73, 71.0, 60.61, 50.98, 21.43, 18.75, 22.45], "sys": [0.0, 5.0, 30.69, 28.28, 19.0, 17.82, 23.23, 20.79, 29.0, 33.0, 31.0, 23.23, 24.75, 28.0, 25.0, 27.72, 22.22, 33.0, 27.27, 24.0, 33.0, 18.18, 27.0, 18.18, 14.71, 4.08, 5.21, 3.06], "iowait": [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], "webStats": [21629, 21638]}, "adguard": {"usr": [5.05, 4.0, 63.92, 82.0, 78.79, 78.0, 63.0, 12.12, 6.06, 1.01], "sys": [0.0, 4.0, 18.56, 15.0, 19.19, 22.0, 19.0, 3.03, 3.03, 0.0], "iowait": [1.01, 0.0, 0.0, 0.0, 1.01, 0.0, 1.0, 0.0, 1.01, 0.0], "webStats": [3340, 3342]}, "canvas-antifp": {"usr": [0.0, 7.0, 68.32, 76.0, 80.0, 76.0, 77.78, 74.26, 69.7, 65.35, 73.0, 75.0, 75.0, 71.29, 73.74, 80.0, 65.0, 69.0, 73.0, 78.22, 69.7, 69.31, 50.0, 23.66, 72.28, 30.93, 37.37, 19.19, 17.17], "sys": [0.0, 4.0, 28.71, 23.0, 20.0, 23.0, 21.21, 23.76, 30.3, 31.68, 26.0, 25.0, 24.0, 26.73, 24.24, 19.0, 32.0, 29.0, 27.0, 20.79, 29.29, 28.71, 17.65, 17.2, 18.81, 4.12, 11.11, 4.04, 4.04], "iowait": [0.0, 0.0, 0.99, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 3.92, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], "webStats": [21998, 22028]}, "privacy-badger": {"usr": [0.0, 7.62, 66.32, 76.24, 71.72, 45.45, 17.82, 2.06, 6.06, 7.84], "sys": [1.01, 5.71, 26.32, 19.8, 21.21, 12.12, 2.97, 3.09, 8.08, 3.92], "iowait": [0.0, 3.81, 1.05, 0.99, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], "webStats": [3609, 3615]}, "ublock": {"usr": [0.0, 19.39, 68.0, 70.0, 82.0, 33.33, 7.22, 8.91, 14.14], "sys": [0.0, 11.22, 31.0, 28.0, 18.0, 1.96, 4.12, 2.97, 13.13], "iowait": [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], "webStats": [2599, 2605]}, "noscript": {"usr": [1.0, 22.45, 71.29, 76.24, 62.24, 10.1, 0.0, 0.0, 0.0], "sys": [0.0, 16.33, 24.75, 22.77, 8.16, 2.02, 1.02, 3.03, 2.04], "iowait": [0.0, 0.0, 1.98, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], "webStats": [2437, 2437]}, "ghostery": {"usr": [0.0, 3.92, 26.8, 52.0, 74.75, 74.26, 46.08, 4.12, 2.0, 0.0, 1.0], "sys": [1.03, 0.98, 9.28, 14.0, 22.22, 23.76, 14.71, 2.06, 5.0, 4.0, 0.0], "iowait": [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.96, 0.0, 0.0, 0.0, 0.0], "webStats": [4043, 4044]}, "decentraleyes": {"usr": [1.01, 3.96, 66.34, 78.0, 78.0, 73.74, 61.39, 69.0, 76.0, 70.3, 74.75, 72.0, 75.0, 74.26, 74.75, 60.4, 69.7, 57.0, 32.32, 24.0, 8.91, 8.16, 16.16, 27.27, 8.25, 44.55, 25.25, 4.04, 3.09, 10.89], "sys": [2.02, 2.97, 28.71, 20.0, 21.0, 25.25, 31.68, 30.0, 24.0, 27.72, 24.24, 28.0, 24.0, 22.77, 24.24, 38.61, 28.28, 34.0, 15.15, 7.0, 5.94, 4.08, 3.03, 4.04, 6.19, 12.87, 4.04, 2.02, 0.0, 1.98], "iowait": [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 6.93, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 3.96, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], "webStats": [23599, 23603]}, "adblock": {"usr": [30.69, 38.38, 68.0, 74.0, 77.0, 75.0, 26.0, 77.23, 38.14, 21.43], "sys": [1.98, 20.2, 31.0, 24.0, 21.0, 17.0, 4.0, 18.81, 11.34, 10.2], "iowait": [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.02], "webStats": [3696, 3698]}, "disconnect": {"usr": [9.18, 13.0, 63.0, 72.73, 56.86, 17.35, 11.22, 11.88, 30.61], "sys": [3.06, 6.0, 27.0, 26.26, 14.71, 5.1, 3.06, 3.96, 5.1], "iowait": [0.0, 0.0, 0.0, 0.0, 1.96, 0.0, 0.0, 0.0, 0.0], "webStats": [2118, 2120]}, "scriptsafe": {"usr": [0.0, 14.0, 68.63, 76.0, 1.03, 2.02, 1.0, 0.0], "sys": [1.01, 5.0, 27.45, 19.0, 2.06, 5.05, 1.0, 7.0], "iowait": [0.0, 0.0, 0.0, 2.0, 2.06, 2.02, 0.0, 0.0], "webStats": [1326, 1326]}, "/data/www.lastnighton.com": {"usr": [0.0, 2.02, 40.4, 76.0, 72.0, 80.0, 72.0, 81.19, 76.77, 64.36, 66.0, 72.73, 67.33, 75.76, 76.0, 77.0, 70.0, 70.3, 70.0, 79.0, 58.0, 30.21, 12.12, 9.28, 34.69, 19.19, 10.0, 40.4, 80.81, 72.0, 47.96, 17.17, 26.26, 20.2, 19.61, 23.47, 50.51, 17.17, 17.89, 30.3, 20.41, 19.59, 28.57, 29.7, 64.65, 40.82, 29.0, 29.9, 59.0, 58.42, 80.0, 25.77, 50.52, 28.28, 18.56, 18.18, 21.05, 26.73, 25.25, 23.76, 64.65, 52.0, 26.26, 17.0, 24.24], "sys": [0.0, 2.02, 21.21, 20.0, 25.0, 19.0, 27.0, 16.83, 23.23, 35.64, 32.0, 27.27, 30.69, 24.24, 21.0, 22.0, 29.0, 28.71, 27.0, 20.0, 15.0, 12.5, 5.05, 4.12, 13.27, 6.06, 6.0, 6.06, 18.18, 26.0, 19.39, 4.04, 9.09, 8.08, 5.88, 4.08, 8.08, 11.11, 4.21, 5.05, 4.08, 3.09, 4.08, 12.87, 35.35, 6.12, 3.0, 12.37, 30.0, 15.84, 15.0, 7.22, 9.28, 7.07, 4.12, 8.08, 8.42, 10.89, 13.13, 13.86, 18.18, 11.0, 6.06, 4.0, 3.03], "iowait": [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.02, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.01, 0.0, 0.0, 0.0, 0.0, 7.07, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], "webStats": [58453, 58486]}}}