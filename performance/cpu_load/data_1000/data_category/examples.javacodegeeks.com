{"stats": {"/data/examples.javacodegeeks.com": {"usr": [0.99, 16.16, 70.0, 80.81, 68.24, 56.86, 64.0, 67.0, 73.0, 71.0, 69.31, 72.73, 74.0, 67.0, 68.0, 67.0, 72.28, 69.0, 69.0, 71.29, 70.71, 73.0, 72.0, 73.0, 77.0, 77.0, 75.25, 76.77, 73.0, 72.0, 77.0, 75.0, 74.26, 75.0, 72.0, 80.31, 71.23, 72.73, 82.0, 91.0, 63.0, 39.39, 24.24, 35.64, 23.16, 48.0, 79.0, 70.41, 75.76, 76.24, 87.0, 78.0, 70.0, 39.0, 45.36], "sys": [0.99, 10.1, 24.0, 19.19, 11.49, 37.25, 36.0, 33.0, 26.0, 29.0, 30.69, 27.27, 25.0, 32.0, 32.0, 32.0, 26.73, 31.0, 31.0, 27.72, 27.27, 27.0, 27.0, 26.0, 23.0, 23.0, 23.76, 23.23, 27.0, 28.0, 23.0, 25.0, 25.74, 25.0, 27.0, 19.69, 27.4, 27.27, 17.0, 9.0, 11.0, 5.05, 4.04, 8.91, 3.16, 12.0, 21.0, 11.22, 24.24, 22.77, 13.0, 22.0, 16.0, 14.0, 11.34], "iowait": [0.0, 0.0, 5.0, 0.0, 6.76, 5.88, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], "webStats": [45781, 45942]}, "adblock": {"usr": [1.0, 29.9, 73.74, 73.27, 56.0, 76.77, 61.0, 73.0, 49.0], "sys": [1.0, 23.71, 26.26, 25.74, 14.0, 18.18, 16.0, 17.0, 47.0], "iowait": [0.0, 5.15, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], "webStats": [2271, 2283]}, "decentraleyes": {"usr": [1.01, 2.02, 53.92, 76.77, 62.0, 69.0, 70.0, 72.0], "sys": [0.0, 2.02, 18.63, 21.21, 35.0, 31.0, 30.0, 27.0], "iowait": [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], "webStats": [1720, 1731]}, "disconnect": {"usr": [27.0, 17.53, 56.57, 69.7, 39.18, 38.83, 16.49, 10.1], "sys": [5.0, 6.19, 16.16, 24.24, 23.71, 14.56, 14.43, 5.05], "iowait": [0.0, 0.0, 10.1, 1.01, 2.06, 4.85, 0.0, 0.0], "webStats": [1159, 1162]}, "ghostery": {"usr": [0.0, 4.85, 56.57, 65.66, 23.47, 14.0, 3.0, 34.34], "sys": [1.01, 0.97, 16.16, 12.12, 4.08, 4.0, 1.0, 6.06], "iowait": [0.0, 0.0, 0.0, 1.01, 0.0, 0.0, 0.0, 0.0], "webStats": [1384, 1389]}, "https": {"usr": [0.0, 19.42, 64.58, 76.0, 85.15, 71.0, 68.0, 72.0, 78.22, 71.43, 78.0, 76.47, 64.65, 68.32, 60.0, 75.76, 71.0, 70.0, 70.0, 74.0, 74.0, 77.23, 75.76, 78.0, 81.0, 79.21, 85.0, 73.0, 72.0, 75.0, 77.0, 76.24, 81.82, 82.0, 78.0, 83.0, 82.0, 85.0, 89.11, 73.47, 45.45, 22.45, 18.18, 35.79, 20.2, 21.43, 51.02, 84.0, 78.0, 84.0, 60.2, 58.59, 39.8, 23.71], "sys": [1.01, 13.59, 23.96, 24.0, 13.86, 29.0, 31.0, 27.0, 21.78, 27.55, 22.0, 22.55, 32.32, 30.69, 40.0, 24.24, 29.0, 29.0, 30.0, 26.0, 26.0, 21.78, 24.24, 21.0, 19.0, 20.79, 15.0, 27.0, 26.0, 25.0, 23.0, 21.78, 17.17, 18.0, 22.0, 16.0, 18.0, 15.0, 10.89, 8.16, 10.1, 6.12, 4.04, 6.32, 4.04, 4.08, 11.22, 16.0, 22.0, 16.0, 7.14, 12.12, 5.1, 3.09], "iowait": [0.0, 0.0, 6.25, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 2.02, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 9.18, 10.1, 4.21, 0.0, 2.04, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], "webStats": [46044, 46167]}, "noscript": {"usr": [0.0, 20.0, 67.68, 81.19, 17.35, 0.0, 0.0, 0.0], "sys": [1.01, 16.0, 27.27, 18.81, 1.02, 2.06, 1.01, 1.01], "iowait": [0.0, 0.0, 5.05, 0.0, 0.0, 0.0, 0.0, 0.0], "webStats": [1737, 1738]}, "privacy-badger": {"usr": [0.0, 3.03, 56.57, 35.71, 10.2, 20.62, 25.51, 0.97], "sys": [1.02, 5.05, 16.16, 14.29, 8.16, 12.37, 14.29, 0.0], "iowait": [0.0, 0.0, 0.0, 0.0, 0.0, 19.59, 12.24, 0.0], "webStats": [1031, 1038]}, "ublock": {"usr": [0.0, 15.0, 66.34, 81.82, 24.0, 5.05, 1.61, 0.0], "sys": [0.0, 8.0, 27.72, 17.17, 8.0, 3.03, 3.23, 1.32], "iowait": [0.0, 1.0, 3.96, 0.0, 3.0, 0.0, 3.23, 27.63], "webStats": [1401, 1410]}, "scriptsafe": {"usr": [1.02, 22.33, 67.0, 64.0, 0.0, 5.1, 0.0, 1.01], "sys": [0.0, 12.62, 24.0, 17.0, 4.0, 3.06, 1.02, 0.0], "iowait": [0.0, 0.0, 4.0, 0.0, 2.0, 8.16, 0.0, 0.0], "webStats": [1464, 1464]}, "canvas-antifp": {"usr": [1.01, 1.98, 52.0, 71.29, 81.82, 75.0, 64.0, 70.71, 71.29, 71.0, 78.0, 78.22, 69.7, 69.0, 63.0, 69.0, 68.0, 70.0, 77.0, 70.3, 71.0, 73.74, 76.0, 73.0, 79.0, 79.25, 69.47, 72.0, 77.78, 77.0, 79.0, 88.0, 85.0, 39.39, 27.27, 28.57, 64.0, 85.0, 62.24, 35.0, 38.38, 25.0, 26.53, 47.52, 72.0, 85.0, 77.0, 84.0, 37.76, 29.59], "sys": [0.0, 1.98, 21.0, 26.73, 18.18, 25.0, 36.0, 28.28, 26.73, 29.0, 21.0, 20.79, 30.3, 31.0, 37.0, 30.0, 32.0, 30.0, 22.0, 28.71, 29.0, 26.26, 24.0, 27.0, 21.0, 20.75, 29.47, 28.0, 22.22, 22.0, 21.0, 12.0, 13.0, 7.07, 2.02, 5.1, 8.0, 11.0, 6.12, 4.0, 4.04, 5.0, 3.06, 8.91, 27.0, 15.0, 22.0, 15.0, 5.1, 2.04], "iowait": [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], "webStats": [42122, 42285]}, "adguard": {"usr": [3.06, 5.1, 58.0, 46.0, 17.53, 51.02, 2.04, 3.03], "sys": [1.02, 2.04, 18.0, 15.0, 5.15, 23.47, 1.02, 4.04], "iowait": [0.0, 0.0, 0.0, 0.0, 0.0, 4.08, 0.0, 0.0], "webStats": [1320, 1327]}, "user-agent": {"usr": [1.01, 6.06, 62.0, 77.23, 87.0, 76.0, 61.0, 71.72, 75.0, 69.31], "sys": [0.0, 3.03, 34.0, 21.78, 13.0, 24.0, 39.0, 27.27, 25.0, 29.7], "iowait": [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], "webStats": [2785, 2792]}}}