{"stats": {"/data/www.atlassian.com": {"usr": [0.0, 4.95, 61.22, 71.72, 81.0, 75.0, 81.0, 75.0, 63.27, 19.59, 5.05, 1.98, 1.02], "sys": [0.0, 2.97, 31.63, 27.27, 16.0, 25.0, 19.0, 24.0, 10.2, 6.19, 9.09, 6.93, 1.02], "iowait": [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.01, 0.0, 2.04], "webStats": [6414, 6425]}, "disconnect": {"usr": [12.12, 17.0, 50.51, 74.26, 78.79, 74.0, 67.0, 20.0, 22.45, 14.0, 8.16], "sys": [5.05, 3.0, 17.17, 23.76, 20.2, 26.0, 19.0, 5.0, 4.08, 2.0, 4.08], "iowait": [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], "webStats": [4756, 4759]}, "scriptsafe": {"usr": [0.0, 0.99, 61.0, 86.14, 63.0, 6.0, 0.99, 1.0, 0.0], "sys": [1.01, 2.97, 27.0, 12.87, 19.0, 7.0, 0.99, 3.0, 0.0], "iowait": [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], "webStats": [2604, 2604]}, "adblock": {"usr": [15.84, 30.0, 66.67, 80.0, 82.0, 76.24, 67.0, 58.16, 9.0, 10.1, 6.06, 0.0], "sys": [2.97, 15.0, 28.28, 20.0, 17.0, 22.77, 22.0, 14.29, 2.0, 1.01, 4.04, 0.0], "iowait": [0.0, 0.0, 1.01, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], "webStats": [5815, 5825]}, "privacy-badger": {"usr": [0.0, 2.02, 60.2, 80.0, 76.24, 82.83, 79.0, 16.0, 0.93, 2.15, 1.02], "sys": [4.04, 7.07, 32.65, 20.0, 22.77, 16.16, 21.0, 6.0, 1.87, 1.08, 0.0], "iowait": [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], "webStats": [4902, 4909]}, "ublock": {"usr": [0.0, 2.0, 55.88, 74.0, 84.0, 79.0, 74.75, 13.0, 4.0, 0.0, 0.0], "sys": [2.0, 0.0, 31.37, 26.0, 16.0, 20.0, 20.2, 4.0, 1.0, 1.01, 2.04], "iowait": [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], "webStats": [4704, 4709]}, "adguard": {"usr": [4.08, 7.07, 44.44, 80.81, 81.0, 69.31, 59.18, 83.0, 40.82, 62.0], "sys": [2.04, 2.02, 14.14, 19.19, 19.0, 21.78, 18.37, 17.0, 15.31, 21.0], "iowait": [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], "webStats": [3708, 3710]}, "https": {"usr": [1.0, 5.94, 64.36, 76.77, 79.41, 74.75, 79.0, 71.29, 83.84, 16.16, 8.08, 2.0, 0.0], "sys": [2.0, 7.92, 24.75, 23.23, 19.61, 25.25, 21.0, 28.71, 14.14, 3.03, 1.01, 1.0, 6.06], "iowait": [0.0, 0.99, 0.99, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.01, 0.0, 0.0, 0.0], "webStats": [6649, 6728]}, "canvas-antifp": {"usr": [1.98, 1.98, 48.48, 59.0, 82.0, 80.81, 81.19, 76.0, 80.0, 22.0, 9.0, 1.0, 1.0], "sys": [5.94, 5.94, 27.27, 25.0, 17.0, 19.19, 17.82, 23.0, 13.0, 6.0, 2.0, 2.0, 4.0], "iowait": [0.0, 0.0, 2.02, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], "webStats": [6658, 6673]}, "ghostery": {"usr": [1.01, 7.22, 77.23, 78.22, 78.79, 75.0, 68.37, 18.0, 4.08, 3.03, 1.02], "sys": [3.03, 4.12, 18.81, 20.79, 21.21, 23.0, 24.49, 2.0, 1.02, 7.07, 3.06], "iowait": [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.02, 0.0, 1.02, 0.0, 0.0], "webStats": [4610, 4622]}, "noscript": {"usr": [0.0, 4.04, 36.73, 77.78, 77.23, 82.0, 27.55, 0.99, 0.0], "sys": [0.0, 2.02, 26.53, 22.22, 21.78, 18.0, 9.18, 0.99, 0.0], "iowait": [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], "webStats": [2421, 2421]}, "decentraleyes": {"usr": [0.0, 2.91, 59.6, 79.8, 74.0, 73.0, 45.0, 32.0, 50.0, 16.0, 10.0, 7.29, 4.0, 3.06], "sys": [3.03, 2.91, 32.32, 20.2, 26.0, 19.0, 18.0, 10.0, 17.0, 8.0, 1.0, 6.25, 1.0, 0.0], "iowait": [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], "webStats": [7065, 7072]}}}