{"stats": {"/data/www.today.com": {"usr": [1.0, 5.94, 56.44, 69.39, 74.26, 87.13, 84.0, 78.79, 80.2, 82.0, 81.0, 82.0, 85.0, 81.0, 74.75, 28.0, 23.23, 9.09], "sys": [0.0, 7.92, 34.65, 28.57, 24.75, 12.87, 16.0, 20.2, 18.81, 18.0, 19.0, 18.0, 15.0, 18.0, 10.1, 5.0, 2.02, 3.03], "iowait": [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], "webStats": [11796, 11798]}, "https": {"usr": [0.0, 14.0, 58.59, 66.34, 77.0, 87.0, 83.0, 82.0, 83.0, 80.0, 87.0, 88.0, 78.0, 82.0, 67.35, 27.45, 18.0, 5.1], "sys": [1.02, 15.0, 31.31, 32.67, 23.0, 13.0, 17.0, 17.0, 17.0, 20.0, 13.0, 11.0, 21.0, 18.0, 16.33, 3.92, 4.0, 3.06], "iowait": [0.0, 0.0, 2.02, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], "webStats": [11647, 11651]}, "adblock": {"usr": [10.1, 42.86, 63.0, 87.13, 75.51, 84.0, 74.0, 75.25, 80.81, 79.0, 90.0, 64.0, 37.0, 46.0, 67.35, 54.55], "sys": [3.03, 24.49, 22.0, 12.87, 24.49, 16.0, 25.0, 12.87, 19.19, 21.0, 10.0, 8.0, 6.0, 10.0, 10.2, 9.09], "iowait": [2.02, 1.02, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], "webStats": [9265, 9266]}, "disconnect": {"usr": [12.0, 16.0, 51.52, 68.69, 80.2, 78.0, 71.72, 58.59, 19.0, 11.11, 5.1], "sys": [4.0, 5.0, 19.19, 29.29, 19.8, 22.0, 20.2, 5.05, 4.0, 7.07, 2.04], "iowait": [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], "webStats": [4626, 4626]}, "noscript": {"usr": [0.0, 30.61, 68.0, 75.0, 84.0, 48.0, 5.05, 0.0, 0.0], "sys": [6.06, 17.35, 32.0, 25.0, 14.0, 8.0, 1.01, 1.0, 0.0], "iowait": [0.0, 1.02, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], "webStats": [2814, 2814]}, "privacy-badger": {"usr": [1.0, 23.47, 72.0, 70.41, 87.0, 78.79, 75.25, 84.0, 43.43, 2.02, 9.9, 37.76], "sys": [0.0, 24.49, 26.0, 24.49, 9.0, 19.19, 23.76, 16.0, 6.06, 0.0, 3.96, 8.16], "iowait": [0.0, 1.02, 0.0, 0.0, 0.0, 2.02, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], "webStats": [5292, 5293]}, "ghostery": {"usr": [1.01, 1.96, 46.08, 80.61, 85.15, 76.0, 72.73, 78.5, 84.04, 39.0, 16.33, 3.06, 3.0, 4.0], "sys": [0.0, 1.96, 14.71, 18.37, 12.87, 23.0, 25.25, 20.56, 15.96, 8.0, 10.2, 10.2, 3.0, 9.0], "iowait": [0.0, 0.0, 2.94, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.02, 2.0, 0.0], "webStats": [6875, 6876]}, "adguard": {"usr": [4.95, 4.04, 74.75, 80.0, 84.31, 70.41, 78.0, 83.0, 81.0, 81.0, 83.0, 76.0, 41.0, 57.43, 70.71, 57.58], "sys": [1.98, 2.02, 24.24, 20.0, 15.69, 28.57, 22.0, 17.0, 18.0, 19.0, 17.0, 13.0, 4.0, 7.92, 12.12, 10.1], "iowait": [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], "webStats": [9501, 9502]}, "decentraleyes": {"usr": [0.0, 3.92, 71.72, 77.0, 79.0, 77.23, 77.0, 82.0, 78.0, 70.71, 36.36, 33.66, 50.0, 52.58], "sys": [1.01, 0.98, 28.28, 23.0, 21.0, 21.78, 23.0, 18.0, 21.0, 13.13, 3.03, 3.96, 8.16, 10.31], "iowait": [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], "webStats": [7346, 7350]}, "scriptsafe": {"usr": [1.0, 3.92, 71.0, 68.0, 87.0, 51.52, 1.98, 1.0, 0.0], "sys": [2.0, 0.98, 26.0, 30.0, 10.0, 4.04, 1.98, 0.0, 0.0], "iowait": [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], "webStats": [2132, 2132]}, "ublock": {"usr": [0.0, 17.17, 65.35, 69.0, 87.0, 89.9, 90.0, 87.0, 29.29, 4.95, 3.96, 3.09], "sys": [1.0, 7.07, 33.66, 30.0, 13.0, 10.1, 10.0, 12.0, 4.04, 1.98, 1.98, 2.06], "iowait": [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], "webStats": [5188, 5189]}, "canvas-antifp": {"usr": [0.0, 3.0, 67.0, 69.0, 74.0, 84.0, 86.0, 76.0, 79.21, 86.0, 88.0, 82.0, 73.74, 72.28, 65.66, 25.0, 21.43, 7.29], "sys": [0.0, 11.0, 32.0, 30.0, 25.0, 16.0, 14.0, 23.0, 20.79, 14.0, 11.0, 18.0, 25.25, 26.73, 6.06, 5.0, 1.02, 3.12], "iowait": [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 3.03, 0.0, 0.0, 0.0], "webStats": [11181, 11183]}, "user-agent": {"usr": [1.01, 6.6, 69.79, 69.0, 80.0, 78.0, 78.0, 81.19, 84.85, 78.0, 89.11, 77.78, 82.0, 83.0, 49.49, 11.11], "sys": [1.01, 17.92, 26.04, 30.0, 18.0, 21.0, 22.0, 17.82, 15.15, 21.0, 10.89, 22.22, 17.0, 17.0, 8.08, 2.02], "iowait": [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], "webStats": [9835, 9846]}}}