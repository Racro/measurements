{"stats": {"/data/www.att.com": {"usr": [1.02, 2.94, 52.48, 76.77, 72.73, 60.4, 69.0, 80.0, 67.0, 76.0, 77.0, 87.0, 84.0, 70.0], "sys": [3.06, 1.96, 25.74, 22.22, 27.27, 39.6, 31.0, 20.0, 33.0, 24.0, 22.0, 12.0, 16.0, 7.0], "iowait": [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], "webStats": [7187, 7221]}, "decentraleyes": {"usr": [1.0, 3.96, 46.94, 77.78, 78.22, 82.83, 48.0, 63.64, 19.42, 67.71], "sys": [2.0, 4.95, 24.49, 21.21, 14.85, 14.14, 26.0, 12.12, 9.71, 14.58], "iowait": [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], "webStats": [3923, 3945]}, "scriptsafe": {"usr": [0.99, 1.98, 56.0, 81.19, 15.0, 0.0, 1.01, 0.0], "sys": [0.0, 0.99, 29.0, 16.83, 7.0, 2.0, 2.02, 0.0], "iowait": [0.0, 0.0, 0.0, 0.0, 2.0, 0.0, 0.0, 0.0], "webStats": [1790, 1790]}, "disconnect": {"usr": [8.25, 20.2, 68.0, 76.24, 84.69, 81.0, 64.0, 36.73, 43.0, 25.25], "sys": [2.06, 8.08, 27.0, 18.81, 11.22, 17.0, 19.0, 4.08, 16.0, 8.08], "iowait": [0.0, 1.01, 1.0, 0.0, 0.0, 0.0, 2.0, 1.02, 0.0, 0.0], "webStats": [3931, 3961]}, "noscript": {"usr": [0.0, 28.43, 36.36, 42.0, 68.32, 24.49, 1.0, 0.0, 1.01, 0.0], "sys": [1.98, 9.8, 19.19, 15.0, 19.8, 2.04, 0.0, 1.0, 1.01, 2.0], "iowait": [0.0, 0.0, 4.04, 1.0, 0.0, 1.02, 0.0, 0.0, 13.13, 0.0], "webStats": [3016, 3017]}, "ublock": {"usr": [0.0, 2.97, 64.36, 69.31, 77.0, 67.0, 61.0, 81.0, 64.0, 42.42, 7.14], "sys": [2.02, 0.0, 26.73, 19.8, 23.0, 33.0, 39.0, 19.0, 36.0, 13.13, 3.06], "iowait": [0.0, 0.0, 0.99, 3.96, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], "webStats": [4022, 4052]}, "canvas-antifp": {"usr": [1.98, 3.03, 54.08, 71.84, 77.78, 72.0, 67.0, 62.38, 87.88, 68.0, 67.0, 85.15, 84.0], "sys": [5.94, 4.04, 27.55, 25.24, 21.21, 28.0, 33.0, 37.62, 12.12, 32.0, 32.0, 14.85, 16.0], "iowait": [0.0, 0.0, 1.02, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], "webStats": [5208, 5244]}, "adblock": {"usr": [21.21, 40.4, 67.0, 70.71, 80.81, 65.35, 61.39, 74.75, 70.0, 45.45], "sys": [2.02, 20.2, 26.0, 14.14, 11.11, 23.76, 21.78, 22.22, 17.0, 8.08], "iowait": [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], "webStats": [3609, 3622]}, "adguard": {"usr": [1.02, 5.05, 28.57, 82.0, 62.24, 75.0, 80.37, 60.64, 74.75, 10.1, 79.8, 27.27], "sys": [2.04, 8.08, 14.29, 14.0, 18.37, 23.0, 19.63, 20.21, 13.13, 1.01, 19.19, 7.07], "iowait": [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], "webStats": [5096, 5131]}, "privacy-badger": {"usr": [2.0, 4.04, 9.8, 38.61, 73.47, 74.26, 81.0, 63.37, 61.62, 33.0, 19.19], "sys": [5.0, 2.02, 3.92, 13.86, 22.45, 24.75, 18.0, 20.79, 10.1, 6.0, 4.04], "iowait": [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.01, 0.0, 0.0], "webStats": [4808, 4820]}, "https": {"usr": [0.0, 15.0, 63.37, 83.17, 82.83, 72.0, 68.0, 70.0, 83.17, 69.0, 74.26, 83.67], "sys": [0.0, 8.0, 27.72, 16.83, 17.17, 28.0, 32.0, 29.0, 16.83, 30.0, 25.74, 16.33], "iowait": [0.0, 1.0, 1.98, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], "webStats": [4969, 5052]}, "ghostery": {"usr": [1.01, 2.94, 28.28, 71.72, 79.0, 73.0, 77.23, 65.66, 54.0, 41.0], "sys": [1.01, 3.92, 8.08, 10.1, 18.0, 25.0, 21.78, 16.16, 14.0, 7.0], "iowait": [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], "webStats": [3753, 3761]}, "user-agent": {"usr": [0.0, 3.96, 43.56, 26.0, 21.21, 80.0, 64.36, 65.66, 76.0, 81.0, 69.0, 77.23, 82.0, 85.86, 83.17, 59.0], "sys": [0.0, 2.97, 28.71, 14.0, 12.12, 19.0, 35.64, 34.34, 23.0, 19.0, 31.0, 20.79, 18.0, 14.14, 15.84, 9.0], "iowait": [0.0, 0.99, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], "webStats": [8099, 8147]}}}