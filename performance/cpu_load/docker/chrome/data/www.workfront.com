{"stats": {"/data/www.workfront.com": {"usr": [1.0, 2.97, 59.0, 79.8, 84.0, 80.0, 81.0, 76.0, 80.0, 79.0], "sys": [2.0, 1.98, 31.0, 20.2, 16.0, 20.0, 19.0, 23.0, 19.0, 21.0], "iowait": [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], "webStats": [3251, 3263]}, "ublock": {"usr": [0.0, 11.22, 69.7, 78.0, 85.0, 80.0, 19.79, 13.13, 81.0, 35.35, 47.42, 53.0, 20.0], "sys": [0.0, 10.2, 25.25, 22.0, 15.0, 16.0, 4.17, 5.05, 16.0, 2.02, 16.49, 6.0, 6.0], "iowait": [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.03, 0.0, 0.0], "webStats": [5924, 5939]}, "adguard": {"usr": [27.27, 25.77, 79.0, 71.29, 79.0, 79.8, 78.0, 78.0], "sys": [55.56, 34.02, 20.0, 14.85, 20.0, 19.19, 22.0, 22.0], "iowait": [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], "webStats": [2147, 2174]}, "ghostery": {"usr": [0.99, 2.97, 27.72, 84.0, 80.81, 78.0, 78.0, 64.0, 60.0], "sys": [0.99, 0.99, 11.88, 16.0, 13.13, 21.0, 20.0, 19.0, 13.0], "iowait": [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 2.0, 0.0], "webStats": [2751, 2767]}, "noscript": {"usr": [0.0, 4.81, 42.86, 79.0, 79.41, 44.9, 2.04, 0.0, 0.0], "sys": [0.0, 1.92, 19.39, 19.0, 17.65, 6.12, 5.1, 1.0, 4.08], "iowait": [1.02, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], "webStats": [2738, 2739]}, "https": {"usr": [0.0, 4.85, 68.37, 72.28, 81.0, 83.17, 77.78, 33.33, 75.0, 82.0, 76.0, 80.2], "sys": [4.04, 0.97, 14.29, 25.74, 17.0, 15.84, 13.13, 12.12, 24.0, 18.0, 22.0, 19.8], "iowait": [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], "webStats": [5784, 5804]}, "adblock": {"usr": [14.14, 44.44, 75.24, 82.47, 82.0, 79.8, 80.0, 79.8, 76.0], "sys": [7.07, 20.2, 22.86, 16.49, 18.0, 19.19, 17.0, 16.16, 19.0], "iowait": [0.0, 1.01, 0.95, 0.0, 0.0, 1.01, 0.0, 0.0, 0.0], "webStats": [2382, 2398]}, "scriptsafe": {"usr": [0.99, 4.9, 68.0, 75.76, 58.0, 0.0, 2.0, 0.0], "sys": [0.99, 1.96, 21.0, 22.22, 18.0, 2.0, 2.0, 0.0], "iowait": [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], "webStats": [1640, 1640]}, "privacy-badger": {"usr": [0.0, 6.06, 66.0, 79.0, 80.2, 38.61, 19.0, 24.24, 64.65], "sys": [3.0, 10.1, 29.0, 21.0, 18.81, 9.9, 6.0, 8.08, 12.12], "iowait": [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], "webStats": [2793, 2806]}, "decentraleyes": {"usr": [1.0, 4.0, 64.36, 80.2, 80.0, 70.0, 80.81, 82.83, 79.21, 72.73], "sys": [5.0, 3.0, 24.75, 18.81, 20.0, 29.0, 18.18, 17.17, 18.81, 14.14], "iowait": [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], "webStats": [3079, 3110]}, "disconnect": {"usr": [11.11, 14.14, 44.9, 70.71, 79.0, 81.0, 64.0, 30.21, 27.72, 55.56, 60.2], "sys": [8.08, 8.08, 15.31, 18.18, 19.0, 19.0, 22.0, 7.29, 9.9, 14.14, 6.12], "iowait": [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], "webStats": [3996, 4016]}, "canvas-antifp": {"usr": [1.0, 5.0, 66.0, 77.0, 78.79, 91.09, 45.92, 30.0, 74.0, 76.0, 79.0, 85.0], "sys": [1.0, 9.0, 18.0, 21.0, 21.21, 8.91, 12.24, 6.0, 25.0, 23.0, 21.0, 15.0], "iowait": [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.02, 0.0, 0.0, 0.0, 0.0, 0.0], "webStats": [5852, 5866]}}}