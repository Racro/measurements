{"stats": {"/data/www.varzesh3.com": {"usr": [1.0, 3.03, 38.83, 56.86, 77.0, 79.8, 58.59, 36.46, 47.0, 56.7, 22.68], "sys": [0.0, 5.05, 29.13, 29.41, 22.0, 15.15, 11.11, 5.21, 8.0, 15.46, 5.15], "iowait": [0.0, 0.0, 0.0, 1.96, 0.0, 0.0, 2.02, 0.0, 0.0, 0.0, 1.03], "webStats": [4413, 4414]}, "scriptsafe": {"usr": [0.0, 5.83, 48.08, 75.51, 71.57, 9.09, 4.08, 5.05, 4.04], "sys": [0.0, 4.85, 28.85, 20.41, 20.59, 3.03, 2.04, 4.04, 2.02], "iowait": [0.0, 0.0, 0.0, 4.08, 0.0, 0.0, 0.0, 0.0, 0.0], "webStats": [2819, 2819]}, "adguard": {"usr": [34.0, 7.22, 25.25, 39.39, 67.0, 56.0, 35.71, 14.85, 12.0, 37.0, 23.0, 17.17, 2.02, 2.0, 2.02], "sys": [2.0, 3.09, 6.06, 8.08, 16.0, 30.0, 11.22, 7.92, 8.0, 9.0, 6.0, 1.01, 0.0, 1.0, 2.02], "iowait": [3.0, 0.0, 0.0, 0.0, 0.0, 1.0, 5.1, 2.97, 2.0, 2.0, 0.0, 0.0, 0.0, 0.0, 0.0], "webStats": [8468, 8469]}, "https": {"usr": [0.0, 6.06, 11.11, 60.61, 75.0, 69.39, 78.0, 46.0, 35.05, 62.0, 27.27], "sys": [1.01, 10.1, 13.13, 22.22, 25.0, 15.31, 16.0, 5.0, 6.19, 15.0, 8.08], "iowait": [0.0, 0.0, 0.0, 3.03, 0.0, 4.08, 0.0, 4.0, 0.0, 0.0, 0.0], "webStats": [4810, 4810]}, "adblock": {"usr": [13.86, 57.58, 55.88, 34.69, 65.31, 47.52, 21.43, 13.27, 12.37, 37.07, 25.29, 13.0, 2.0, 1.01, 3.0], "sys": [3.96, 18.18, 15.69, 12.24, 16.33, 7.92, 8.16, 9.18, 6.19, 10.34, 8.05, 4.0, 1.0, 0.0, 1.0], "iowait": [1.98, 0.0, 3.92, 6.12, 0.0, 1.98, 0.0, 1.02, 0.0, 19.83, 5.75, 0.0, 0.0, 0.0, 6.0], "webStats": [8440, 8441]}, "disconnect": {"usr": [9.9, 14.29, 24.0, 48.45, 71.0, 73.0, 37.0, 21.43, 23.23, 20.2, 23.71, 40.4, 21.0, 14.0, 23.47, 39.6], "sys": [4.95, 2.04, 8.0, 25.77, 22.0, 18.0, 8.0, 10.2, 11.11, 7.07, 6.19, 9.09, 5.0, 5.0, 5.1, 13.86], "iowait": [0.0, 0.0, 4.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 5.05, 0.0, 2.02, 22.0, 0.0, 0.0, 0.0], "webStats": [9751, 9752]}, "ghostery": {"usr": [0.99, 2.94, 6.19, 26.26, 73.0, 46.0, 40.4, 16.1, 55.56, 34.69, 22.77, 16.67, 4.95, 3.19, 2.0, 2.06], "sys": [7.92, 0.98, 4.12, 14.14, 15.0, 17.0, 19.19, 5.08, 4.94, 7.14, 7.92, 3.92, 0.0, 4.26, 2.0, 4.12], "iowait": [0.0, 0.0, 1.03, 0.0, 0.0, 1.0, 0.0, 6.78, 1.23, 0.0, 4.95, 0.98, 0.0, 0.0, 0.0, 0.0], "webStats": [8964, 8965]}, "ublock": {"usr": [0.99, 0.98, 37.76, 75.0, 70.71, 87.0, 61.22, 26.26, 17.71, 15.0, 26.26], "sys": [0.99, 1.96, 19.39, 25.0, 21.21, 13.0, 4.08, 7.07, 7.29, 4.0, 3.03], "iowait": [0.0, 0.0, 21.43, 0.0, 0.0, 0.0, 1.02, 0.0, 0.0, 0.0, 1.01], "webStats": [3959, 3960]}, "privacy-badger": {"usr": [0.98, 2.97, 30.43, 50.49, 46.6, 9.57, 27.84, 50.0, 14.58, 10.2, 21.0, 29.29, 19.19, 19.59, 3.0, 1.01, 3.03, 2.02], "sys": [0.98, 4.95, 23.91, 28.16, 11.65, 4.26, 11.34, 11.0, 6.25, 8.16, 8.0, 8.08, 4.04, 12.37, 3.0, 3.03, 4.04, 2.02], "iowait": [0.0, 2.97, 2.17, 0.0, 0.0, 14.89, 0.0, 0.0, 3.12, 0.0, 1.0, 4.04, 0.0, 5.15, 1.0, 0.0, 0.0, 0.0], "webStats": [11569, 11571]}, "noscript": {"usr": [0.0, 11.11, 31.25, 63.0, 76.0, 86.0, 38.61, 11.11, 4.08, 4.12, 6.12], "sys": [2.0, 10.1, 25.0, 28.0, 24.0, 14.0, 6.93, 4.04, 1.02, 4.12, 0.0], "iowait": [0.0, 3.03, 0.0, 3.0, 0.0, 0.0, 1.98, 0.0, 0.0, 0.0, 0.0], "webStats": [3548, 3552]}, "canvas-antifp": {"usr": [1.01, 6.8, 52.94, 57.58, 81.0, 86.87, 50.51, 28.0, 18.0, 69.0, 30.21], "sys": [3.03, 13.59, 34.31, 20.2, 19.0, 13.13, 8.08, 7.0, 4.0, 14.0, 6.25], "iowait": [2.02, 0.0, 1.96, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], "webStats": [4267, 4269]}, "decentraleyes": {"usr": [0.0, 3.92, 25.53, 39.0, 57.0, 34.69, 8.25, 6.06, 6.0, 19.39, 19.0, 35.71, 6.93, 15.46, 30.0, 7.0, 0.0], "sys": [0.99, 1.96, 23.4, 14.0, 12.0, 6.12, 6.19, 6.06, 10.0, 4.08, 5.0, 9.18, 3.96, 3.09, 9.0, 5.0, 1.0], "iowait": [0.0, 0.0, 4.26, 10.0, 1.0, 1.02, 0.0, 0.0, 0.0, 0.0, 3.0, 0.0, 2.97, 5.15, 0.0, 0.0, 0.0], "webStats": [10467, 10468]}}}