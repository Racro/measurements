{"stats": {"/data/www.nike.com": {"usr": [0.99, 5.05, 55.1, 76.0, 77.0, 71.0, 74.0, 72.0, 79.0, 70.3, 60.42, 61.0, 85.0, 81.0, 83.0, 84.16, 82.0, 83.84], "sys": [0.0, 2.02, 32.65, 24.0, 23.0, 29.0, 26.0, 28.0, 21.0, 29.7, 10.42, 9.0, 15.0, 19.0, 16.0, 14.85, 17.0, 15.15], "iowait": [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], "webStats": [10970, 10994]}, "adguard": {"usr": [3.06, 6.0, 35.05, 72.0, 83.84, 71.29, 80.87, 78.57, 62.24, 58.0, 79.0, 83.84, 80.0, 67.0, 58.0, 37.0, 36.0], "sys": [3.06, 3.0, 11.34, 23.0, 16.16, 20.79, 19.13, 19.05, 12.24, 14.0, 20.0, 16.16, 18.0, 14.0, 12.0, 7.0, 9.0], "iowait": [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], "webStats": [9916, 9927]}, "ghostery": {"usr": [0.0, 2.78, 10.2, 32.32, 53.06, 77.78, 83.17, 66.67, 77.0, 50.51, 8.91, 76.0, 66.67, 80.0, 84.16, 63.27, 44.9, 6.0, 4.04], "sys": [0.98, 1.85, 6.12, 10.1, 15.31, 21.21, 15.84, 16.16, 15.0, 7.07, 3.96, 9.0, 9.09, 19.0, 15.84, 13.27, 12.24, 3.0, 0.0], "iowait": [0.0, 0.0, 1.02, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 7.0, 0.0, 0.0, 0.0, 11.22, 0.0, 0.0, 0.0], "webStats": [12622, 12632]}, "noscript": {"usr": [0.99, 18.0, 47.47, 77.0, 55.0, 11.22, 0.0, 0.99, 0.0], "sys": [0.0, 17.0, 24.24, 23.0, 11.0, 1.02, 4.08, 0.0, 5.32], "iowait": [0.0, 1.0, 1.01, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], "webStats": [2515, 2516]}, "ublock": {"usr": [0.0, 14.14, 66.0, 81.82, 67.0, 66.0, 79.0, 80.2, 74.75, 65.35, 65.31, 84.0, 80.0, 19.19, 5.15, 1.02], "sys": [0.0, 6.06, 29.0, 18.18, 33.0, 34.0, 21.0, 18.81, 25.25, 7.92, 9.18, 16.0, 20.0, 6.06, 4.12, 0.0], "iowait": [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 4.12, 0.0], "webStats": [9270, 9280]}, "privacy-badger": {"usr": [1.01, 5.0, 31.25, 71.72, 77.23, 86.87, 78.3, 82.98, 64.65, 63.64, 83.0, 78.22, 71.72, 58.59, 35.64, 23.47], "sys": [4.04, 1.0, 14.58, 27.27, 21.78, 13.13, 18.87, 17.02, 8.08, 10.1, 17.0, 19.8, 16.16, 14.14, 7.92, 4.08], "iowait": [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], "webStats": [8964, 8975]}, "decentraleyes": {"usr": [0.0, 2.94, 63.64, 79.8, 85.15, 79.0, 68.0, 67.0, 78.0, 77.78, 62.0, 70.3, 76.0, 26.53, 35.05], "sys": [0.0, 3.92, 29.29, 17.17, 14.85, 17.0, 9.0, 6.0, 20.0, 16.16, 15.0, 17.82, 24.0, 12.24, 7.22], "iowait": [0.0, 0.0, 1.01, 0.0, 0.0, 2.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 9.28], "webStats": [8034, 8045]}, "adblock": {"usr": [15.31, 36.08, 51.52, 69.0, 79.0, 85.15, 83.0, 66.0, 68.69, 86.0, 76.0, 65.66, 13.13, 67.68, 80.0], "sys": [4.08, 17.53, 29.29, 20.0, 21.0, 14.85, 11.0, 12.0, 7.07, 14.0, 24.0, 21.21, 6.06, 18.18, 16.0], "iowait": [0.0, 0.0, 1.01, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], "webStats": [8424, 8433]}, "canvas-antifp": {"usr": [0.0, 2.0, 36.27, 82.0, 72.0, 65.66, 67.33, 70.0, 70.0, 68.69, 69.31, 62.63, 79.21, 80.0, 77.23, 81.82, 43.88], "sys": [0.0, 5.0, 27.45, 18.0, 19.0, 28.28, 32.67, 30.0, 30.0, 31.31, 30.69, 12.12, 19.8, 19.0, 22.77, 18.18, 9.18], "iowait": [0.0, 0.0, 1.96, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], "webStats": [10177, 10183]}, "scriptsafe": {"usr": [1.02, 2.91, 58.59, 76.0, 3.0, 2.04, 1.01, 2.0], "sys": [3.06, 3.88, 29.29, 19.0, 5.0, 4.08, 2.02, 7.0], "iowait": [0.0, 0.0, 2.02, 0.0, 0.0, 0.0, 0.0, 0.0], "webStats": [1743, 1743]}, "https": {"usr": [0.0, 10.1, 66.0, 79.21, 76.0, 84.0, 66.0, 66.0, 73.0, 69.0, 59.18, 77.0, 80.0, 78.22, 75.51, 67.68, 34.02], "sys": [1.01, 7.07, 33.0, 19.8, 24.0, 16.0, 34.0, 33.0, 27.0, 25.0, 5.1, 17.0, 20.0, 21.78, 22.45, 10.1, 8.25], "iowait": [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], "webStats": [9608, 9615]}, "disconnect": {"usr": [10.1, 15.31, 39.8, 65.98, 76.0, 80.0, 83.0, 84.16, 65.0, 69.0, 84.85, 89.11, 96.0, 96.0, 96.0, 95.96, 96.04, 98.0, 96.0, 97.98, 95.0, 97.03, 97.98, 97.0, 98.0, 98.0, 97.0, 97.0, 97.0, 96.04, 96.97, 96.0, 97.0, 95.0, 96.0, 95.05, 96.97, 97.0, 95.0, 97.03, 97.98, 94.0, 98.0, 96.04, 96.97, 97.0, 98.0, 96.04, 100.0, 92.0, 94.0, 92.0, 95.0, 97.03, 82.83, 68.32, 55.56, 20.2, 14.14, 12.0], "sys": [4.04, 1.02, 12.24, 23.71, 23.0, 19.0, 17.0, 14.85, 12.0, 12.0, 14.14, 10.89, 4.0, 4.0, 4.0, 4.04, 3.96, 2.0, 4.0, 2.02, 5.0, 2.97, 2.02, 3.0, 2.0, 2.0, 3.0, 3.0, 3.0, 3.96, 3.03, 4.0, 3.0, 5.0, 4.0, 4.95, 3.03, 3.0, 5.0, 2.97, 2.02, 6.0, 2.0, 3.96, 3.03, 3.0, 2.0, 3.96, 0.0, 8.0, 6.0, 8.0, 5.0, 2.97, 17.17, 23.76, 14.14, 7.07, 4.04, 5.0], "iowait": [1.01, 0.0, 0.0, 8.25, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 1.01, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], "webStats": [53053, 53068]}, "user-agent": {"usr": [0.99, 7.14, 61.76, 80.0, 79.0, 57.43, 70.71, 70.0, 73.0, 59.0, 61.39, 83.0, 84.69, 81.19, 78.0, 81.0, 85.0, 85.0], "sys": [0.0, 9.18, 32.35, 19.0, 21.0, 41.58, 29.29, 30.0, 27.0, 32.0, 6.93, 17.0, 12.24, 18.81, 22.0, 19.0, 15.0, 15.0], "iowait": [0.0, 0.0, 1.96, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], "webStats": [10285, 10305]}}}