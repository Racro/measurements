{"stats": {"/data/www.upwork.com": {"usr": [1.0, 11.11, 67.68, 80.0, 80.0, 85.0, 75.76, 69.31, 63.0, 67.0, 79.0, 83.0, 72.0, 73.0, 88.0, 89.0, 74.0, 74.0, 60.82], "sys": [1.0, 11.11, 26.26, 20.0, 19.0, 15.0, 24.24, 29.7, 36.0, 33.0, 21.0, 16.0, 28.0, 26.0, 12.0, 11.0, 7.0, 3.0, 5.15], "iowait": [0.0, 1.01, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], "webStats": [10373, 10432]}, "disconnect": {"usr": [10.1, 13.13, 61.62, 68.37, 79.0, 87.0, 84.85, 34.65, 56.57, 16.0, 25.51, 19.8], "sys": [2.02, 2.02, 18.18, 25.51, 20.0, 13.0, 14.14, 9.9, 15.15, 7.0, 11.22, 2.97], "iowait": [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], "webStats": [4977, 5007]}, "https": {"usr": [1.02, 20.79, 71.0, 75.76, 79.21, 78.79, 77.23, 62.0, 73.0, 66.34, 79.0, 82.83, 58.42, 87.13, 89.9, 88.0, 70.41, 57.43], "sys": [1.02, 10.89, 26.0, 24.24, 20.79, 21.21, 20.79, 38.0, 27.0, 32.67, 20.0, 17.17, 40.59, 12.87, 10.1, 12.0, 7.14, 3.96], "iowait": [0.0, 0.0, 3.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], "webStats": [9245, 9288]}, "noscript": {"usr": [0.0, 1.02, 63.37, 77.78, 29.29, 0.99, 2.0, 0.0], "sys": [0.0, 6.12, 28.71, 22.22, 6.06, 0.99, 1.0, 0.99], "iowait": [0.0, 0.0, 0.0, 0.0, 3.03, 0.0, 0.0, 0.0], "webStats": [1635, 1635]}, "ublock": {"usr": [2.0, 2.91, 66.0, 72.0, 78.0, 84.16, 86.0, 78.79, 67.68, 80.81, 72.45], "sys": [1.0, 1.94, 28.0, 27.0, 22.0, 15.84, 14.0, 7.07, 3.03, 5.05, 4.08], "iowait": [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], "webStats": [4884, 4885]}, "adblock": {"usr": [10.0, 54.55, 63.37, 67.35, 86.0, 85.0, 86.87, 82.0, 85.0, 68.32, 67.0, 10.0, 16.16, 17.0], "sys": [0.0, 18.18, 16.83, 23.47, 14.0, 15.0, 13.13, 18.0, 15.0, 19.8, 13.0, 3.0, 1.01, 1.0], "iowait": [0.0, 2.02, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.01, 0.0], "webStats": [7579, 7636]}, "scriptsafe": {"usr": [1.01, 2.88, 70.71, 83.0, 4.0, 0.0, 2.97, 0.0], "sys": [0.0, 2.88, 26.26, 16.0, 3.0, 2.02, 0.0, 0.0], "iowait": [0.0, 0.96, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], "webStats": [1596, 1597]}, "adguard": {"usr": [3.96, 5.0, 53.06, 73.0, 78.79, 73.0, 87.0, 82.83, 79.41, 88.89, 86.0, 34.69, 84.0, 21.0, 12.12], "sys": [1.98, 2.0, 14.29, 21.0, 18.18, 25.0, 13.0, 17.17, 15.69, 11.11, 14.0, 9.18, 15.0, 8.0, 5.05], "iowait": [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], "webStats": [8312, 8390]}, "canvas-antifp": {"usr": [0.0, 4.9, 69.7, 75.0, 80.0, 83.84, 72.28, 70.0, 71.0, 83.0, 78.0, 74.0, 79.8, 86.0, 86.0, 81.0, 69.0, 54.0], "sys": [0.0, 4.9, 28.28, 25.0, 20.0, 16.16, 27.72, 29.0, 29.0, 17.0, 22.0, 25.0, 20.2, 14.0, 14.0, 12.0, 8.0, 4.0], "iowait": [0.0, 0.98, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], "webStats": [9374, 9419]}, "ghostery": {"usr": [0.99, 3.85, 49.49, 82.0, 80.0, 77.0, 84.0, 76.24, 64.71, 16.16, 13.0, 7.0, 2.0], "sys": [0.0, 1.92, 18.18, 18.0, 18.0, 21.0, 16.0, 17.82, 20.59, 3.03, 2.0, 1.0, 1.0], "iowait": [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 3.96, 0.0, 0.0, 0.0, 0.0, 0.0], "webStats": [6340, 6413]}, "privacy-badger": {"usr": [1.0, 8.91, 64.65, 57.43, 89.11, 78.79, 85.0, 72.73, 31.31, 20.2, 3.0, 11.22], "sys": [0.0, 9.9, 33.33, 27.72, 10.89, 21.21, 15.0, 21.21, 5.05, 7.07, 2.0, 2.04], "iowait": [0.0, 0.0, 0.0, 1.98, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], "webStats": [5304, 5338]}, "decentraleyes": {"usr": [0.0, 3.0, 49.0, 67.68, 82.0, 81.0, 83.17, 75.25, 80.0, 81.0, 44.9, 2.97, 10.1, 42.57], "sys": [2.02, 3.0, 26.0, 26.26, 18.0, 19.0, 15.84, 21.78, 20.0, 19.0, 15.31, 0.99, 2.02, 2.97], "iowait": [0.0, 0.0, 0.0, 1.01, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], "webStats": [7246, 7288]}, "user-agent": {"usr": [0.0, 5.94, 66.0, 76.0, 82.0, 81.0, 82.0, 80.0, 72.0, 56.57, 71.72, 82.18, 81.82, 66.34, 78.0, 89.9, 81.19, 75.51, 67.01], "sys": [1.02, 5.94, 28.0, 23.0, 17.0, 19.0, 18.0, 20.0, 26.0, 32.32, 28.28, 17.82, 18.18, 33.66, 22.0, 10.1, 9.9, 5.1, 2.06], "iowait": [3.06, 0.99, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], "webStats": [10692, 10742]}}}