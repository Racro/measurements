{"stats": {"/data/www.deepl.com": {"usr": [0.0, 5.05, 13.13, 66.33, 81.0, 76.24, 85.86, 20.79, 2.04, 0.0, 1.01], "sys": [0.0, 4.04, 11.11, 22.45, 19.0, 21.78, 14.14, 5.94, 0.0, 0.99, 1.01], "iowait": [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 9.9, 0.0, 0.0, 0.0], "webStats": [4671, 4671]}, "scriptsafe": {"usr": [0.99, 4.9, 41.67, 68.0, 52.04, 0.0, 2.0, 1.01], "sys": [0.99, 0.98, 17.71, 31.0, 13.27, 1.0, 2.0, 0.0], "iowait": [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], "webStats": [1617, 1617]}, "adblock": {"usr": [31.63, 39.18, 59.79, 82.83, 83.17, 64.29, 26.0, 13.13, 2.0, 0.0], "sys": [6.12, 20.62, 24.74, 16.16, 16.83, 11.22, 4.0, 2.02, 0.0, 0.97], "iowait": [13.27, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], "webStats": [3499, 3500]}, "disconnect": {"usr": [19.39, 18.37, 48.45, 67.0, 78.22, 80.81, 75.0, 50.0, 18.18, 13.0, 11.0], "sys": [9.18, 22.45, 48.45, 31.0, 20.79, 18.18, 21.0, 13.0, 6.06, 2.0, 8.0], "iowait": [0.0, 0.0, 1.03, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], "webStats": [5022, 5022]}, "privacy-badger": {"usr": [0.99, 4.04, 36.94, 73.12, 84.0, 72.16, 12.84, 1.14, 0.98, 0.0], "sys": [0.99, 5.05, 19.82, 23.66, 16.0, 15.46, 0.92, 1.14, 2.94, 1.01], "iowait": [0.0, 0.0, 19.82, 2.15, 0.0, 5.15, 0.0, 1.14, 0.0, 0.0], "webStats": [3782, 3782]}, "https": {"usr": [1.02, 9.9, 52.53, 80.0, 76.0, 83.0, 30.97, 4.65, 1.0, 1.0], "sys": [1.02, 9.9, 34.34, 19.0, 22.0, 16.0, 7.08, 4.65, 0.0, 1.0], "iowait": [0.0, 0.0, 3.03, 0.0, 0.0, 0.0, 8.85, 0.0, 0.0, 0.0], "webStats": [3640, 3641]}, "decentraleyes": {"usr": [2.02, 3.03, 16.49, 54.64, 76.0, 84.0, 14.14, 1.01, 0.99, 1.01, 1.01], "sys": [11.11, 2.02, 16.49, 30.93, 22.0, 15.0, 4.04, 2.02, 0.0, 1.01, 16.16], "iowait": [0.0, 0.0, 1.03, 0.0, 0.0, 0.0, 0.0, 0.0, 17.82, 0.0, 0.0], "webStats": [4028, 4029]}, "ublock": {"usr": [0.0, 3.92, 27.0, 78.22, 79.0, 86.0, 43.0, 6.06, 0.99, 1.02], "sys": [4.08, 1.96, 24.0, 20.79, 20.0, 14.0, 5.0, 3.03, 0.0, 0.0], "iowait": [0.0, 0.0, 4.0, 0.0, 0.0, 0.0, 0.0, 0.0, 4.95, 0.0], "webStats": [3933, 3933]}, "noscript": {"usr": [1.0, 20.0, 40.2, 38.0, 43.0, 5.0, 75.42, 57.32, 9.09, 0.0, 0.99, 1.0], "sys": [2.0, 14.0, 26.47, 21.0, 11.0, 5.0, 19.49, 6.1, 3.03, 5.1, 2.97, 0.0], "iowait": [0.0, 0.0, 2.94, 2.0, 0.0, 0.0, 0.0, 1.22, 0.0, 8.16, 0.0, 0.0], "webStats": [5154, 5154]}, "ghostery": {"usr": [2.13, 20.21, 42.0, 80.39, 69.7, 51.52, 34.0, 13.13, 17.71], "sys": [17.02, 15.96, 29.0, 15.69, 18.18, 20.2, 11.0, 9.09, 8.33], "iowait": [0.0, 0.0, 1.0, 0.98, 0.0, 3.03, 21.0, 1.01, 0.0], "webStats": [2651, 2651]}, "canvas-antifp": {"usr": [0.0, 4.0, 54.0, 80.81, 83.0, 85.0, 22.77, 3.06, 0.99, 1.02], "sys": [0.0, 2.0, 32.0, 18.18, 17.0, 11.0, 2.97, 1.02, 2.97, 0.0], "iowait": [6.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 6.93, 0.0], "webStats": [3602, 3603]}, "adguard": {"usr": [2.04, 12.0, 23.53, 80.41, 82.0, 66.33, 43.88, 16.0, 2.04, 1.03], "sys": [1.02, 4.0, 8.82, 13.4, 17.0, 24.49, 18.37, 2.0, 2.04, 4.12], "iowait": [0.0, 0.0, 7.84, 5.15, 0.0, 0.0, 12.24, 0.0, 0.0, 0.0], "webStats": [3533, 3534]}}}