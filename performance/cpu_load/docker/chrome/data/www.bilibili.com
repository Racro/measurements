{"stats": {"/data/www.bilibili.com": {"usr": [0.0, 5.38, 51.0, 60.0, 86.0, 71.29, 63.0, 47.0, 38.54, 28.28], "sys": [1.06, 5.38, 30.0, 24.0, 13.0, 25.74, 20.0, 9.0, 2.08, 4.04], "iowait": [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], "webStats": [3579, 3678]}, "decentraleyes": {"usr": [0.0, 2.08, 40.4, 51.02, 80.2, 58.16, 30.3, 4.26, 5.26, 3.12], "sys": [1.06, 1.04, 29.29, 15.31, 14.85, 18.37, 4.04, 3.19, 6.32, 3.12], "iowait": [0.0, 0.0, 1.01, 0.0, 0.0, 0.0, 0.0, 1.06, 0.0, 0.0], "webStats": [3329, 3364]}, "https": {"usr": [0.0, 5.26, 58.25, 36.73, 54.08, 73.47, 33.67, 8.33, 6.32, 5.21, 5.21, 8.25, 7.22, 7.37, 4.3, 55.0, 64.65, 67.33, 71.72, 49.48, 31.18, 36.46, 34.38], "sys": [0.0, 7.37, 30.1, 6.12, 15.31, 12.24, 5.1, 4.17, 3.16, 3.12, 6.25, 5.15, 2.06, 4.21, 3.23, 17.0, 11.11, 14.85, 22.22, 4.12, 6.45, 5.21, 3.12], "iowait": [0.0, 0.0, 2.91, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], "webStats": [15580, 15665]}, "noscript": {"usr": [0.0, 3.06, 48.98, 21.43, 78.0, 84.69, 13.83, 0.0, 3.19, 0.0], "sys": [3.19, 2.04, 26.53, 9.18, 20.0, 9.18, 3.19, 1.08, 0.0, 1.05], "iowait": [0.0, 0.0, 1.02, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], "webStats": [3396, 3397]}, "adblock": {"usr": [23.4, 36.63, 31.63, 22.45, 12.5, 25.77, 10.31, 39.18, 20.41, 6.32, 7.22, 4.3, 7.45, 11.46, 10.31, 7.14, 5.1, 20.62, 74.0, 35.35, 13.4, 23.47, 29.17, 42.27, 14.74, 4.3, 4.21, 3.19], "sys": [4.26, 20.79, 16.33, 14.29, 5.21, 6.19, 8.25, 9.28, 5.1, 2.11, 3.09, 3.23, 2.13, 3.12, 4.12, 6.12, 5.1, 5.15, 22.0, 13.13, 4.12, 6.12, 6.25, 9.28, 5.26, 4.3, 10.53, 4.26], "iowait": [0.0, 0.99, 0.0, 1.02, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 3.09, 1.02, 0.0, 0.0, 0.0, 3.03, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], "webStats": [21433, 21469]}, "privacy-badger": {"usr": [0.0, 4.17, 10.2, 23.16, 58.82, 77.0, 80.0, 55.1, 15.46, 4.21, 1.06, 0.0], "sys": [0.0, 7.29, 6.12, 10.53, 22.55, 22.0, 19.0, 14.29, 2.06, 1.05, 1.06, 0.0], "iowait": [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.02, 0.0, 0.0, 0.0, 0.0], "webStats": [5113, 5172]}, "disconnect": {"usr": [10.53, 24.21, 57.14, 35.05, 35.71, 47.42, 28.57, 20.62, 19.39, 15.46, 19.19, 16.67, 20.83, 66.67, 42.27, 57.29, 61.0, 26.32, 11.58, 12.63, 23.71], "sys": [12.63, 12.63, 21.43, 13.4, 15.31, 9.28, 6.12, 5.15, 8.16, 10.31, 6.06, 5.21, 10.42, 12.12, 8.25, 11.46, 18.0, 4.21, 3.16, 3.16, 5.15], "iowait": [0.0, 0.0, 3.06, 0.0, 0.0, 1.03, 0.0, 0.0, 0.0, 0.0, 1.01, 0.0, 0.0, 0.0, 8.25, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], "webStats": [14572, 14595]}, "scriptsafe": {"usr": [0.0, 18.0, 54.0, 64.36, 28.12, 0.0, 2.15, 1.04], "sys": [0.0, 13.0, 25.0, 22.77, 3.12, 7.37, 0.0, 4.17], "iowait": [0.0, 0.0, 2.0, 0.0, 0.0, 0.0, 0.0, 0.0], "webStats": [2073, 2073]}, "ublock": {"usr": [1.03, 8.51, 40.4, 44.44, 87.0, 28.57, 6.32, 6.32, 9.18, 7.14, 62.63, 82.83, 70.71, 42.71, 38.61, 31.96], "sys": [9.28, 6.38, 21.21, 15.15, 12.0, 9.18, 3.16, 7.37, 3.06, 4.08, 18.18, 16.16, 13.13, 6.25, 4.95, 3.09], "iowait": [0.0, 0.0, 2.02, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.02, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], "webStats": [9359, 9452]}, "ghostery": {"usr": [1.06, 6.38, 6.38, 30.61, 46.08, 56.0, 7.22, 9.9, 9.47, 14.14, 4.26, 6.25, 37.5, 61.0, 12.5, 34.38, 14.29, 24.74], "sys": [8.51, 7.45, 5.32, 11.22, 19.61, 16.0, 3.09, 3.96, 5.26, 5.05, 3.19, 2.08, 6.25, 10.0, 3.12, 9.38, 4.08, 10.31], "iowait": [0.0, 0.0, 3.19, 0.0, 0.0, 1.0, 0.0, 1.98, 11.58, 1.01, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], "webStats": [11688, 11696]}, "canvas-antifp": {"usr": [0.0, 3.16, 45.1, 52.04, 73.74, 20.2, 9.18, 6.38, 6.32, 6.25, 9.38, 9.09, 7.29, 7.37, 7.14, 9.38, 21.88, 73.47, 48.48, 82.18, 38.14, 17.53, 32.65, 20.2], "sys": [3.19, 3.16, 35.29, 20.41, 15.15, 11.11, 4.08, 2.13, 4.21, 5.21, 4.17, 3.03, 7.29, 3.16, 3.06, 2.08, 2.08, 16.33, 17.17, 13.86, 7.22, 2.06, 6.12, 3.03], "iowait": [0.0, 0.0, 0.98, 0.0, 1.01, 0.0, 0.0, 0.0, 0.0, 0.0, 1.04, 1.01, 0.0, 0.0, 0.0, 3.12, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], "webStats": [16770, 16776]}, "adguard": {"usr": [2.11, 5.32, 11.34, 29.17, 16.16, 61.39, 43.88, 24.74, 6.19, 6.38, 8.0, 11.22, 6.25, 4.17, 8.25, 5.38, 8.16, 21.65, 84.0, 32.65, 32.65, 64.71, 17.89, 2.08, 1.06, 3.12], "sys": [5.26, 2.13, 8.25, 11.46, 9.09, 30.69, 18.37, 5.15, 5.15, 4.26, 5.0, 5.1, 3.12, 6.25, 4.12, 4.3, 5.1, 7.22, 16.0, 17.35, 6.12, 14.71, 4.21, 2.08, 6.38, 4.17], "iowait": [0.0, 0.0, 0.0, 0.0, 0.0, 0.99, 0.0, 0.0, 1.03, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.03, 0.0, 1.02, 0.0, 0.98, 0.0, 0.0, 0.0, 0.0], "webStats": [19233, 19268]}}}