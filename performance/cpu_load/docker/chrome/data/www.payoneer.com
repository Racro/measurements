{"stats": {"/data/www.payoneer.com": {"usr": [0.0, 7.84, 70.71, 67.0, 79.21, 79.0, 72.0, 67.0, 74.75, 79.0, 75.25, 78.0, 88.0, 90.91, 76.24, 88.0], "sys": [1.01, 3.92, 28.28, 32.0, 18.81, 21.0, 28.0, 33.0, 25.25, 20.0, 24.75, 22.0, 12.0, 4.04, 8.91, 12.0], "iowait": [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], "webStats": [6852, 6966]}, "https": {"usr": [0.0, 12.24, 72.28, 72.0, 80.0, 81.0, 78.0, 70.3, 70.0, 74.0, 83.0, 68.69, 83.0, 75.0, 72.0], "sys": [0.0, 10.2, 26.73, 27.0, 19.0, 19.0, 22.0, 29.7, 30.0, 25.0, 17.0, 31.31, 17.0, 5.0, 9.0], "iowait": [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], "webStats": [6283, 6409]}, "ublock": {"usr": [2.0, 3.0, 64.29, 73.0, 81.0, 82.0, 88.0, 80.0, 61.0, 51.02, 52.53], "sys": [0.0, 6.0, 29.59, 26.0, 19.0, 18.0, 12.0, 10.0, 6.0, 3.06, 3.03], "iowait": [0.0, 0.0, 1.02, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], "webStats": [3972, 4049]}, "adguard": {"usr": [4.08, 5.05, 76.77, 73.0, 75.0, 73.0, 76.24, 86.0, 79.0, 85.0, 70.0, 30.0, 39.0], "sys": [3.06, 1.01, 23.23, 24.0, 23.0, 27.0, 22.77, 14.0, 21.0, 14.0, 12.0, 4.0, 7.0], "iowait": [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], "webStats": [5893, 6035]}, "privacy-badger": {"usr": [1.0, 5.05, 62.0, 78.0, 70.19, 88.54, 78.22, 29.0, 79.8, 25.0, 39.0], "sys": [2.0, 4.04, 35.0, 21.0, 27.88, 11.46, 17.82, 7.0, 19.19, 4.0, 2.0], "iowait": [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], "webStats": [3974, 4004]}, "disconnect": {"usr": [15.15, 13.86, 74.0, 75.76, 68.69, 78.0, 79.41, 31.31, 52.0, 18.81, 6.06], "sys": [4.04, 5.94, 25.0, 23.23, 25.25, 22.0, 14.71, 8.08, 8.0, 2.97, 2.02], "iowait": [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 2.02, 0.0, 0.0, 0.0], "webStats": [4384, 4446]}, "ghostery": {"usr": [0.0, 1.94, 75.76, 73.0, 78.22, 77.0, 77.0, 81.82, 81.19, 29.7, 11.11, 34.0, 15.15], "sys": [0.0, 2.91, 24.24, 24.0, 19.8, 21.0, 22.0, 18.18, 16.83, 4.95, 1.01, 4.0, 4.04], "iowait": [0.0, 0.0, 0.0, 2.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], "webStats": [5886, 6050]}, "adblock": {"usr": [22.77, 37.62, 73.27, 79.0, 75.25, 84.0, 76.0, 82.0, 81.82, 61.62, 26.0], "sys": [3.96, 22.77, 25.74, 21.0, 24.75, 15.0, 20.0, 18.0, 16.16, 7.07, 3.0], "iowait": [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 4.0, 0.0, 0.0, 0.0, 0.0], "webStats": [3940, 4106]}, "noscript": {"usr": [0.0, 10.78, 67.0, 74.26, 80.0, 5.0, 1.0, 3.0, 0.0], "sys": [2.02, 5.88, 27.0, 23.76, 20.0, 2.0, 1.0, 1.0, 1.0], "iowait": [0.0, 0.0, 3.0, 0.99, 0.0, 0.0, 0.0, 0.0, 0.0], "webStats": [2455, 2455]}, "scriptsafe": {"usr": [1.02, 2.94, 70.3, 76.0, 48.48, 1.01, 4.04, 0.0], "sys": [9.18, 5.88, 26.73, 22.0, 12.12, 3.03, 3.03, 2.02], "iowait": [0.0, 0.0, 0.0, 0.0, 1.01, 0.0, 0.0, 0.0], "webStats": [1712, 1712]}, "decentraleyes": {"usr": [1.01, 6.0, 70.0, 73.0, 74.0, 82.0, 84.16, 66.67, 76.0, 55.1, 34.34], "sys": [2.02, 7.0, 29.0, 26.0, 25.0, 18.0, 15.84, 12.12, 17.0, 11.22, 7.07], "iowait": [2.02, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], "webStats": [3438, 3466]}, "canvas-antifp": {"usr": [1.04, 5.77, 73.47, 70.71, 78.22, 81.19, 82.83, 68.0, 69.0, 72.28, 78.79, 71.0, 87.13, 59.41], "sys": [3.12, 6.73, 25.51, 28.28, 21.78, 17.82, 17.17, 31.0, 31.0, 26.73, 21.21, 29.0, 9.9, 3.96], "iowait": [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], "webStats": [6114, 6227]}, "user-agent": {"usr": [0.0, 5.0, 74.0, 76.24, 70.71, 78.22, 78.0, 66.0, 73.74, 82.18, 75.76, 77.23, 87.0, 94.95, 68.0, 82.0], "sys": [0.99, 3.0, 24.0, 21.78, 28.28, 21.78, 22.0, 34.0, 26.26, 16.83, 24.24, 21.78, 13.0, 5.05, 3.0, 17.0], "iowait": [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], "webStats": [6927, 7048]}}}