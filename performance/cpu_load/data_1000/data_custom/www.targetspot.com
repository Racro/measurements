{"stats": {"/data/www.targetspot.com": {"usr": [0.0, 5.05, 64.65, 75.76, 83.17, 81.82, 58.76, 14.71, 2.02, 2.02], "sys": [9.09, 9.09, 23.23, 23.23, 15.84, 14.14, 13.4, 0.98, 2.02, 0.0], "iowait": [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], "webStats": [3561, 3575]}, "https": {"usr": [49.0, 4.04, 62.0, 81.82, 84.0, 73.74, 33.33, 10.1, 2.97], "sys": [26.0, 10.1, 19.0, 17.17, 12.0, 7.07, 8.08, 1.01, 0.99], "iowait": [4.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], "webStats": [2919, 2932]}, "privacy-badger": {"usr": [0.0, 4.85, 57.58, 75.0, 75.0, 42.57, 16.33, 7.0, 8.0, 3.03], "sys": [1.0, 1.94, 29.29, 22.0, 20.0, 12.87, 0.0, 1.0, 2.0, 0.0], "iowait": [0.0, 2.91, 7.07, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], "webStats": [3777, 3790]}, "ghostery": {"usr": [0.99, 2.97, 58.59, 49.49, 78.0, 58.59, 8.91, 38.0, 12.0, 1.0], "sys": [0.99, 0.99, 18.18, 14.14, 17.0, 19.19, 1.98, 9.0, 3.0, 0.0], "iowait": [0.0, 0.0, 0.0, 6.06, 0.0, 1.01, 0.0, 0.0, 0.0, 0.0], "webStats": [3351, 3371]}, "ublock": {"usr": [2.02, 2.97, 64.36, 76.0, 86.0, 69.0, 31.0, 0.0, 2.04, 1.02], "sys": [1.01, 1.98, 30.69, 24.0, 12.0, 7.0, 3.0, 1.02, 0.0, 1.02], "iowait": [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], "webStats": [3270, 3275]}, "noscript": {"usr": [2.0, 3.0, 58.0, 72.0, 76.24, 76.0, 82.0, 31.0, 3.03, 0.0, 0.0, 0.0], "sys": [4.0, 2.0, 28.0, 26.0, 20.79, 20.0, 15.0, 17.0, 1.01, 0.0, 0.0, 1.0], "iowait": [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], "webStats": [5368, 5368]}, "canvas-antifp": {"usr": [2.0, 9.0, 69.7, 77.23, 84.85, 67.33, 70.0, 20.41, 8.08, 1.98], "sys": [0.0, 8.0, 28.28, 20.79, 15.15, 12.87, 18.0, 4.08, 1.01, 1.98], "iowait": [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.99], "webStats": [3851, 3867]}, "decentraleyes": {"usr": [0.0, 3.92, 61.17, 68.37, 57.43, 43.88, 17.82, 13.54, 6.06, 7.07], "sys": [1.02, 5.88, 34.95, 18.37, 17.82, 15.31, 6.93, 5.21, 6.06, 1.01], "iowait": [0.0, 4.9, 0.0, 0.0, 2.97, 0.0, 0.0, 0.0, 1.01, 0.0], "webStats": [3806, 3822]}, "disconnect": {"usr": [11.46, 13.13, 73.0, 76.0, 80.0, 37.0, 16.33, 20.79, 12.0, 12.24], "sys": [2.08, 5.05, 20.0, 22.0, 19.0, 7.0, 2.04, 2.97, 4.0, 2.04], "iowait": [4.17, 0.0, 0.0, 0.0, 1.0, 0.0, 2.04, 0.0, 0.0, 0.0], "webStats": [3311, 3315]}, "adguard": {"usr": [6.0, 3.0, 67.01, 66.0, 51.02, 49.0, 15.31, 70.3, 39.6, 30.61], "sys": [3.0, 3.0, 18.56, 14.0, 14.29, 12.0, 6.12, 19.8, 23.76, 13.27], "iowait": [0.0, 0.0, 0.0, 0.0, 1.02, 0.0, 0.0, 0.0, 0.0, 5.1], "webStats": [3316, 3333]}, "scriptsafe": {"usr": [1.01, 35.0, 50.0, 9.18, 1.04, 2.02], "sys": [1.01, 9.0, 26.53, 5.1, 5.21, 3.03], "iowait": [0.0, 0.0, 0.0, 0.0, 3.12, 0.0], "webStats": [214, 214]}, "adblock": {"usr": [23.23, 15.84, 46.53, 69.7, 75.25, 40.0, 21.0, 6.06, 4.12, 0.99], "sys": [4.04, 12.87, 22.77, 21.21, 16.83, 10.0, 8.0, 1.01, 4.12, 0.99], "iowait": [0.0, 3.96, 2.97, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], "webStats": [3743, 3758]}}}