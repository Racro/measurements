{"stats": {"/data/www.merriam-webster.com": {"usr": [0.0, 2.97, 70.71, 73.27, 81.82, 78.79, 79.21, 69.0, 65.66, 75.25, 71.0, 74.0, 80.73, 78.02, 76.0, 79.0, 74.0, 67.0, 76.0, 51.52, 19.19, 11.0, 7.22], "sys": [0.0, 2.97, 27.27, 24.75, 17.17, 21.21, 19.8, 30.0, 34.34, 23.76, 28.0, 26.0, 18.35, 21.98, 21.0, 20.0, 26.0, 32.0, 23.0, 10.1, 4.04, 2.0, 5.15], "iowait": [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 2.0, 0.0], "webStats": [14408, 14651]}, "adguard": {"usr": [1.0, 5.94, 79.0, 77.0, 19.59, 16.16, 29.79, 24.49], "sys": [2.0, 2.97, 20.0, 14.0, 2.06, 18.18, 12.77, 12.24], "iowait": [0.0, 0.0, 0.0, 0.0, 0.0, 3.03, 1.06, 17.35], "webStats": [1629, 1635]}, "ghostery": {"usr": [1.0, 5.05, 76.0, 42.16, 36.08, 30.1, 12.12, 24.74], "sys": [5.0, 3.03, 18.0, 7.84, 14.43, 17.48, 18.18, 11.34], "iowait": [0.0, 0.0, 5.0, 0.0, 3.09, 0.97, 1.01, 4.12], "webStats": [1487, 1487]}, "https": {"usr": [1.0, 6.0, 58.0, 79.0, 83.17, 77.78, 78.22, 75.0, 76.0, 72.0, 76.0, 74.0, 78.0, 78.79, 80.0, 79.0, 70.59, 74.0, 78.79, 76.0, 44.55, 16.49, 8.16, 5.0], "sys": [0.0, 7.0, 32.0, 20.0, 15.84, 22.22, 21.78, 25.0, 24.0, 27.0, 24.0, 26.0, 22.0, 21.21, 20.0, 17.0, 22.55, 25.0, 20.2, 24.0, 8.91, 2.06, 2.04, 3.0], "iowait": [0.0, 10.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.96, 0.0, 1.01, 0.0, 0.0, 0.0, 0.0, 0.0], "webStats": [14476, 14733]}, "scriptsafe": {"usr": [0.0, 31.31, 79.0, 11.0, 1.87, 3.26, 0.99], "sys": [2.0, 14.14, 20.0, 4.0, 4.67, 4.35, 0.99], "iowait": [0.0, 0.0, 0.0, 17.0, 59.81, 1.09, 0.0], "webStats": [749, 749]}, "privacy-badger": {"usr": [66.0, 32.35, 48.48, 75.25, 74.75, 75.25, 57.14, 4.04, 13.13, 3.0, 3.96], "sys": [13.0, 6.86, 39.39, 21.78, 25.25, 23.76, 16.33, 3.03, 5.05, 3.0, 3.96], "iowait": [0.0, 0.0, 1.01, 0.0, 0.0, 0.0, 0.0, 2.02, 0.0, 2.0, 0.99], "webStats": [3967, 3996]}, "noscript": {"usr": [0.0, 1.98, 69.7, 78.0, 10.0, 0.0, 3.03, 1.0], "sys": [0.0, 0.99, 24.24, 21.0, 6.0, 0.0, 2.02, 0.0], "iowait": [0.0, 0.0, 5.05, 0.0, 0.0, 0.0, 0.0, 0.0], "webStats": [1246, 1247]}, "canvas-antifp": {"usr": [0.98, 3.03, 72.28, 80.0, 81.0, 79.0, 80.0, 73.0, 72.28, 75.76, 78.0, 84.0, 71.72, 71.29, 78.79, 75.25, 65.31, 23.47, 17.17, 8.25], "sys": [0.98, 6.06, 24.75, 19.0, 18.0, 20.0, 19.0, 27.0, 26.73, 23.23, 22.0, 16.0, 13.13, 26.73, 18.18, 23.76, 16.33, 4.08, 6.06, 1.03], "iowait": [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.01, 0.0, 0.0, 0.0, 0.0, 0.0], "webStats": [11791, 11986]}, "disconnect": {"usr": [10.1, 20.62, 72.0, 70.0, 69.31, 19.79, 9.18, 8.16, 10.1], "sys": [3.03, 9.28, 24.0, 16.0, 17.82, 10.42, 7.14, 5.1, 5.05], "iowait": [0.0, 0.0, 0.0, 13.0, 10.89, 0.0, 4.08, 0.0, 0.0], "webStats": [2404, 2404]}, "ublock": {"usr": [1.02, 4.9, 72.28, 79.21, 52.53, 9.0, 4.08, 4.04, 4.95], "sys": [0.0, 1.96, 24.75, 18.81, 10.1, 5.0, 3.06, 6.06, 2.97], "iowait": [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], "webStats": [2089, 2089]}, "decentraleyes": {"usr": [1.98, 9.0, 73.27, 74.49, 74.0, 77.0, 64.0, 67.0, 77.0, 81.0, 66.67, 51.52, 30.3, 72.73, 76.0, 53.47, 4.08, 2.02, 0.0, 1.01], "sys": [8.91, 7.0, 24.75, 23.47, 26.0, 23.0, 36.0, 33.0, 23.0, 19.0, 12.75, 19.19, 13.13, 27.27, 24.0, 16.83, 0.0, 3.03, 0.0, 0.0], "iowait": [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 6.06, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 4.04], "webStats": [10919, 11108]}, "adblock": {"usr": [15.31, 37.76, 66.67, 64.0, 78.79, 13.0, 8.08, 25.26, 9.28], "sys": [2.04, 8.16, 28.43, 27.0, 14.14, 4.0, 3.03, 5.26, 2.06], "iowait": [0.0, 0.0, 0.0, 3.0, 2.02, 0.0, 0.0, 1.05, 0.0], "webStats": [2264, 2266]}}}