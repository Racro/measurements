{"stats": {"/data/www.target.com": {"usr": [0.0, 5.0, 48.48, 76.24, 78.0, 65.0, 69.0, 66.67, 88.12, 80.81, 66.0, 81.19, 86.14, 72.73, 14.29, 0.99], "sys": [1.04, 2.0, 25.25, 21.78, 21.0, 35.0, 31.0, 33.33, 11.88, 19.19, 34.0, 17.82, 12.87, 12.12, 1.02, 0.99], "iowait": [0.0, 0.0, 3.03, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.99, 0.0, 0.0, 0.0, 0.0], "webStats": [8618, 8628]}, "ghostery": {"usr": [0.99, 4.81, 52.04, 76.0, 75.25, 76.0, 76.0, 81.82, 29.7, 8.08], "sys": [7.92, 0.96, 17.35, 21.0, 24.75, 23.0, 22.0, 18.18, 4.95, 0.0], "iowait": [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], "webStats": [3646, 3652]}, "canvas-antifp": {"usr": [0.0, 3.0, 69.0, 70.0, 84.0, 69.0, 76.0, 75.0, 76.0, 68.0, 88.0, 73.0, 77.0, 86.14, 31.68, 7.22], "sys": [4.04, 7.0, 29.0, 28.0, 15.0, 31.0, 22.0, 25.0, 24.0, 31.0, 12.0, 27.0, 23.0, 12.87, 6.93, 2.06], "iowait": [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 8.91, 0.0], "webStats": [8685, 8697]}, "https": {"usr": [0.0, 4.04, 46.46, 78.0, 69.31, 68.0, 68.0, 64.0, 74.0, 88.12, 75.76, 71.0, 84.16, 79.8, 48.48, 9.0], "sys": [3.0, 3.03, 25.25, 21.0, 26.73, 30.0, 32.0, 36.0, 26.0, 11.88, 24.24, 28.0, 15.84, 17.17, 9.09, 2.0], "iowait": [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 2.02, 0.0, 0.0], "webStats": [8556, 8584]}, "privacy-badger": {"usr": [0.0, 4.9, 57.0, 73.74, 77.23, 76.77, 84.16, 57.58, 13.0, 11.0, 9.0], "sys": [2.04, 7.84, 35.0, 25.25, 22.77, 15.15, 15.84, 11.11, 1.0, 0.0, 2.0], "iowait": [0.0, 0.0, 0.0, 1.01, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], "webStats": [4187, 4193]}, "disconnect": {"usr": [12.87, 15.84, 44.9, 70.59, 68.0, 81.0, 78.57, 80.2, 70.71, 9.28, 9.0, 17.0], "sys": [5.94, 7.92, 21.43, 24.51, 30.0, 19.0, 16.33, 18.81, 18.18, 4.12, 3.0, 1.0], "iowait": [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 5.1, 0.0, 0.0, 0.0, 4.0, 0.0], "webStats": [5258, 5261]}, "noscript": {"usr": [1.98, 4.04, 65.31, 47.52, 2.06, 1.98, 2.06, 1.02], "sys": [3.96, 5.05, 31.63, 18.81, 3.09, 3.96, 0.0, 2.04], "iowait": [0.99, 0.0, 0.0, 0.99, 0.0, 0.0, 0.0, 0.0], "webStats": [1091, 1091]}, "decentraleyes": {"usr": [0.0, 3.96, 34.34, 72.0, 76.77, 77.23, 74.0, 77.0, 85.0, 84.0, 27.55], "sys": [6.0, 1.98, 26.26, 17.0, 22.22, 20.79, 21.0, 23.0, 14.0, 16.0, 4.08], "iowait": [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 3.0, 0.0, 0.0, 0.0, 0.0], "webStats": [4285, 4286]}, "adguard": {"usr": [4.08, 4.0, 45.92, 66.0, 78.22, 80.0, 80.81, 83.0, 79.0, 11.11, 4.26, 8.33], "sys": [5.1, 7.0, 18.37, 19.0, 21.78, 20.0, 19.19, 17.0, 12.0, 1.01, 10.64, 5.21], "iowait": [0.0, 0.0, 2.04, 6.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.06, 0.0], "webStats": [4950, 4954]}, "ublock": {"usr": [2.08, 2.02, 50.5, 73.27, 71.29, 61.0, 66.67, 67.0, 93.0, 70.0, 81.37, 53.0, 8.08, 0.0], "sys": [4.17, 4.04, 17.82, 21.78, 26.73, 32.0, 33.33, 33.0, 7.0, 30.0, 15.69, 8.0, 2.02, 1.0], "iowait": [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], "webStats": [7026, 7029]}, "scriptsafe": {"usr": [0.0, 7.07, 51.49, 62.89, 8.08, 3.0, 1.0, 2.97], "sys": [5.21, 6.06, 20.79, 29.9, 6.06, 2.0, 2.0, 1.98], "iowait": [0.0, 0.0, 0.0, 1.03, 1.01, 0.0, 1.0, 0.0], "webStats": [1350, 1350]}, "adblock": {"usr": [30.3, 37.76, 71.0, 79.8, 81.19, 77.55, 83.17, 81.82, 32.0, 6.93, 7.07], "sys": [4.04, 13.27, 27.0, 18.18, 18.81, 17.35, 16.83, 17.17, 8.0, 0.99, 1.01], "iowait": [0.0, 0.0, 0.0, 2.02, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], "webStats": [4330, 4333]}}}