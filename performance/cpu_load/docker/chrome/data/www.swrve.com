{"stats": {"/data/www.swrve.com": {"usr": [2.11, 1.98, 63.64, 73.53, 78.57, 44.9, 32.67, 63.16, 31.31, 29.0, 30.61, 33.67], "sys": [5.26, 1.98, 33.33, 25.49, 18.37, 6.12, 5.94, 10.53, 3.03, 3.0, 10.2, 2.04], "iowait": [0.0, 0.0, 0.0, 0.0, 1.02, 0.0, 1.98, 0.0, 0.0, 0.0, 0.0, 0.0], "webStats": [5432, 5446]}, "adguard": {"usr": [4.0, 14.14, 9.18, 7.22, 8.0, 5.0, 14.56, 39.39, 27.27, 12.24, 40.21, 52.48, 63.64, 1.02, 1.0, 0.0, 0.0], "sys": [2.0, 5.05, 2.04, 2.06, 3.0, 2.0, 7.77, 23.23, 12.12, 5.1, 12.37, 12.87, 13.13, 1.02, 2.0, 0.0, 0.0], "iowait": [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 3.03, 3.03, 0.0, 14.43, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], "webStats": [10798, 10800]}, "disconnect": {"usr": [21.05, 18.18, 18.09, 17.53, 22.11, 27.0, 32.29, 25.0, 28.87, 32.65, 45.05, 30.93, 18.09, 22.68, 46.39, 71.72, 57.02, 24.14, 14.29, 26.26, 18.81, 15.62], "sys": [6.32, 12.12, 7.45, 8.25, 8.42, 18.0, 13.54, 16.67, 19.59, 22.45, 24.18, 18.56, 6.38, 10.31, 18.56, 21.21, 21.93, 29.89, 4.08, 3.03, 2.97, 3.12], "iowait": [4.21, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.03, 1.02, 5.49, 0.0, 0.0, 0.0, 0.0, 0.0, 7.02, 2.3, 0.0, 0.0, 0.0, 0.0], "webStats": [15910, 15911]}, "canvas-antifp": {"usr": [0.0, 2.97, 32.65, 44.55, 72.0, 87.0, 47.96, 8.25, 19.8, 32.99, 31.63, 28.28, 32.32], "sys": [0.0, 1.98, 25.51, 15.84, 26.0, 13.0, 9.18, 6.19, 8.91, 4.12, 9.18, 2.02, 4.04], "iowait": [0.0, 0.0, 3.06, 0.0, 0.0, 0.0, 0.0, 0.0, 0.99, 0.0, 0.0, 0.0, 0.0], "webStats": [6674, 6675]}, "ublock": {"usr": [2.97, 6.0, 49.49, 76.77, 72.0, 61.46, 38.14, 57.43, 70.0, 27.27, 32.0, 34.0, 27.0], "sys": [0.99, 13.0, 24.24, 22.22, 14.0, 9.38, 11.34, 6.93, 6.0, 3.03, 2.0, 1.0, 2.0], "iowait": [0.0, 1.0, 0.0, 0.0, 9.0, 2.08, 1.03, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], "webStats": [6111, 6138]}, "scriptsafe": {"usr": [1.01, 3.0, 35.0, 77.0, 62.0, 0.0, 1.0, 1.0], "sys": [1.01, 5.0, 18.0, 23.0, 26.0, 0.0, 1.0, 2.0], "iowait": [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], "webStats": [1696, 1696]}, "privacy-badger": {"usr": [0.0, 21.0, 65.66, 65.0, 29.29, 14.29, 2.06, 1.01], "sys": [2.97, 18.0, 29.29, 18.0, 7.07, 6.12, 4.12, 2.02], "iowait": [0.0, 0.0, 2.02, 0.0, 2.02, 0.0, 0.0, 0.0], "webStats": [1933, 1935]}, "adblock": {"usr": [34.69, 37.62, 60.0, 77.23, 68.37, 20.2, 27.0, 11.11, 3.03], "sys": [2.04, 15.84, 24.0, 21.78, 15.31, 2.02, 5.0, 3.03, 8.08], "iowait": [3.06, 7.92, 11.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], "webStats": [2490, 2492]}, "decentraleyes": {"usr": [0.0, 3.96, 47.52, 76.24, 45.92, 17.0, 1.0, 1.0, 0.99], "sys": [0.0, 2.97, 25.74, 21.78, 15.31, 13.0, 0.0, 1.0, 1.98], "iowait": [0.0, 7.92, 0.99, 0.0, 15.31, 3.0, 0.0, 29.0, 6.93], "webStats": [2300, 2302]}, "noscript": {"usr": [1.0, 13.13, 54.0, 70.71, 77.0, 65.35, 15.31, 0.99, 1.01, 1.0, 2.0], "sys": [2.0, 8.08, 22.0, 25.25, 21.0, 16.83, 4.08, 0.99, 7.07, 1.0, 3.0], "iowait": [0.0, 0.0, 0.0, 2.02, 0.0, 1.98, 0.0, 0.0, 0.0, 0.0, 0.0], "webStats": [4657, 4657]}, "https": {"usr": [0.99, 12.0, 55.0, 62.0, 84.16, 63.64, 34.69, 33.33, 38.38, 34.69, 28.71, 33.33, 32.0], "sys": [1.98, 7.0, 31.0, 27.0, 14.85, 9.09, 6.12, 8.08, 5.05, 2.04, 2.97, 4.04, 1.0], "iowait": [0.0, 10.0, 1.0, 1.0, 0.0, 0.0, 4.08, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], "webStats": [6491, 6494]}, "ghostery": {"usr": [5.94, 8.16, 26.53, 64.65, 72.73, 63.37, 19.0, 2.02, 13.13, 0.0], "sys": [30.69, 8.16, 14.29, 20.2, 20.2, 26.73, 4.0, 5.05, 2.02, 0.0], "iowait": [0.99, 0.0, 0.0, 0.0, 0.0, 4.95, 4.0, 0.0, 0.0, 0.0], "webStats": [3201, 3205]}}}