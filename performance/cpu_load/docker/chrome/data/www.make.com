{"stats": {"/data/www.make.com": {"usr": [0.0, 4.0, 22.0, 76.0, 69.64, 78.41, 84.85, 79.21, 87.88], "sys": [1.0, 3.0, 20.0, 23.0, 19.64, 13.64, 15.15, 20.79, 12.12], "iowait": [0.0, 0.0, 0.0, 0.0, 9.82, 0.0, 0.0, 0.0, 0.0], "webStats": [2739, 2739]}, "noscript": {"usr": [0.0, 14.85, 49.48, 72.28, 49.5, 36.73, 41.18, 28.71], "sys": [0.0, 14.85, 24.74, 17.82, 3.96, 3.06, 5.88, 3.96], "iowait": [0.0, 0.0, 9.28, 0.0, 0.0, 0.0, 0.0, 0.0], "webStats": [1752, 1752]}, "ghostery": {"usr": [1.0, 1.96, 20.0, 28.57, 45.0, 15.46, 70.3, 19.0, 27.0], "sys": [0.0, 2.94, 9.0, 8.16, 11.0, 16.49, 22.77, 8.0, 5.0], "iowait": [0.0, 0.0, 0.0, 3.06, 0.0, 1.03, 0.99, 0.0, 0.0], "webStats": [2398, 2399]}, "adguard": {"usr": [5.05, 1.03, 14.0, 32.35, 46.39, 53.54, 34.65, 14.14, 59.6, 38.24, 8.33], "sys": [4.04, 2.06, 7.0, 15.69, 21.65, 15.15, 9.9, 5.05, 10.1, 10.78, 1.04], "iowait": [0.0, 0.0, 0.0, 0.0, 3.09, 0.0, 0.0, 0.0, 0.0, 3.92, 0.0], "webStats": [4110, 4111]}, "decentraleyes": {"usr": [1.01, 3.96, 62.63, 26.8, 74.26, 20.0, 38.38, 24.0, 13.13], "sys": [1.01, 0.99, 31.31, 10.31, 18.81, 2.0, 8.08, 4.0, 9.09], "iowait": [0.0, 0.0, 2.02, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], "webStats": [2424, 2424]}, "canvas-antifp": {"usr": [0.0, 2.91, 12.24, 81.0, 82.18, 74.0, 80.0, 74.75], "sys": [0.0, 2.91, 12.24, 19.0, 15.84, 25.0, 19.0, 9.09], "iowait": [0.0, 0.97, 0.0, 0.0, 0.0, 0.0, 0.0, 1.01], "webStats": [1845, 1846]}, "https": {"usr": [0.0, 5.88, 50.5, 77.0, 79.21, 76.0, 86.0, 82.0, 67.0], "sys": [1.0, 3.92, 25.74, 22.0, 19.8, 11.0, 14.0, 9.0, 6.0], "iowait": [0.0, 0.0, 0.99, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], "webStats": [2600, 2600]}, "disconnect": {"usr": [13.13, 13.0, 31.63, 69.0, 69.7, 26.53, 50.51, 15.0, 11.22], "sys": [3.03, 4.0, 14.29, 23.0, 23.23, 8.16, 8.08, 4.0, 2.04], "iowait": [0.0, 0.0, 0.0, 0.0, 6.06, 5.1, 0.0, 0.0, 0.0], "webStats": [2600, 2601]}, "scriptsafe": {"usr": [0.0, 2.94, 56.12, 76.53, 48.0, 45.36, 40.0, 39.39], "sys": [1.0, 2.94, 26.53, 15.31, 7.0, 1.03, 4.0, 2.02], "iowait": [0.0, 0.0, 2.04, 0.0, 0.0, 0.0, 0.0, 0.0], "webStats": [1490, 1490]}, "ublock": {"usr": [1.01, 1.94, 52.94, 83.84, 54.0, 50.0, 74.0, 70.0, 61.22], "sys": [4.04, 2.91, 27.45, 16.16, 16.0, 8.16, 15.0, 5.0, 2.04], "iowait": [0.0, 0.0, 0.0, 0.0, 5.0, 0.0, 0.0, 0.0, 0.0], "webStats": [2095, 2096]}, "privacy-badger": {"usr": [3.0, 5.94, 11.88, 34.0, 71.29, 51.0, 15.0, 40.59, 13.27, 0.99], "sys": [3.0, 3.96, 5.94, 18.0, 26.73, 25.0, 2.0, 4.95, 1.02, 0.99], "iowait": [0.0, 0.0, 0.0, 0.0, 0.0, 3.0, 2.0, 0.0, 0.0, 0.0], "webStats": [2952, 2952]}, "adblock": {"usr": [0.99, 29.41, 37.0, 60.0, 60.0, 8.16, 47.47, 23.53, 9.18], "sys": [0.99, 24.51, 13.0, 15.0, 15.0, 11.22, 5.05, 8.82, 2.04], "iowait": [0.0, 1.96, 0.0, 0.0, 0.0, 5.1, 0.0, 0.0, 0.0], "webStats": [2036, 2036]}, "user-agent": {"usr": [1.0, 2.91, 37.62, 72.28, 77.55, 81.37, 82.0, 83.84, 86.0, 86.0], "sys": [0.0, 2.91, 27.72, 26.73, 22.45, 17.65, 18.0, 16.16, 14.0, 13.0], "iowait": [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], "webStats": [2674, 2685]}}}