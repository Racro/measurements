{"stats": {"/data/www.ibm.com": {"usr": [0.0, 1.96, 58.0, 75.0, 72.0, 67.68, 66.0, 64.36, 85.0, 74.75, 68.0, 82.18, 80.2, 15.46, 5.0, 6.06], "sys": [0.0, 2.94, 33.0, 25.0, 28.0, 32.32, 34.0, 34.65, 14.0, 25.25, 31.0, 17.82, 18.81, 2.06, 4.0, 1.01], "iowait": [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], "webStats": [9270, 9280]}, "adguard": {"usr": [5.0, 3.96, 63.64, 77.23, 63.0, 78.22, 79.8, 43.43, 78.22, 78.79, 86.0, 35.71], "sys": [3.0, 1.98, 18.18, 19.8, 21.0, 19.8, 20.2, 17.17, 19.8, 17.17, 14.0, 9.18], "iowait": [0.0, 0.0, 0.0, 0.0, 11.0, 0.0, 0.0, 1.01, 0.0, 0.0, 0.0, 0.0], "webStats": [5272, 5288]}, "ublock": {"usr": [3.0, 0.98, 62.38, 77.0, 72.0, 65.0, 71.72, 73.0, 86.0, 75.0, 45.92, 14.29, 23.58, 19.61], "sys": [1.0, 2.94, 30.69, 20.0, 28.0, 35.0, 28.28, 27.0, 14.0, 25.0, 21.43, 2.04, 3.77, 4.9], "iowait": [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], "webStats": [6744, 6771]}, "noscript": {"usr": [1.01, 9.43, 70.71, 77.0, 60.61, 4.0, 0.98, 0.0, 0.99], "sys": [2.02, 3.77, 27.27, 23.0, 9.09, 1.0, 0.98, 1.01, 2.97], "iowait": [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], "webStats": [2405, 2406]}, "ghostery": {"usr": [1.01, 3.96, 70.41, 86.14, 74.75, 77.0, 77.0, 69.31, 8.08, 0.99, 25.25], "sys": [3.03, 1.98, 13.27, 10.89, 18.18, 22.0, 22.0, 21.78, 3.03, 0.99, 2.02], "iowait": [0.0, 0.0, 0.0, 0.0, 5.05, 0.0, 0.0, 0.99, 0.0, 0.0, 0.0], "webStats": [3827, 3848]}, "privacy-badger": {"usr": [0.99, 5.0, 64.65, 77.0, 77.45, 83.84, 65.0, 56.57, 10.78, 2.02, 0.99], "sys": [0.0, 2.0, 34.34, 23.0, 21.57, 13.13, 16.0, 10.1, 2.94, 1.01, 0.0], "iowait": [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.98, 3.03, 0.0], "webStats": [4058, 4064]}, "disconnect": {"usr": [12.12, 13.0, 57.58, 71.29, 81.82, 79.0, 70.0, 73.0, 33.0, 11.11, 11.88], "sys": [3.03, 5.0, 25.25, 22.77, 18.18, 21.0, 17.0, 24.0, 13.0, 4.04, 4.95], "iowait": [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], "webStats": [4503, 4508]}, "decentraleyes": {"usr": [2.04, 10.89, 62.63, 81.82, 87.13, 57.43, 81.82, 78.22, 84.85, 25.0], "sys": [8.16, 9.9, 32.32, 18.18, 11.88, 18.81, 18.18, 17.82, 15.15, 7.0], "iowait": [0.0, 0.0, 1.01, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], "webStats": [3679, 3684]}, "https": {"usr": [0.0, 8.08, 59.41, 74.75, 69.0, 70.71, 75.25, 80.2, 74.75, 72.0, 82.0, 84.16, 85.0, 43.43], "sys": [2.0, 12.12, 37.62, 24.24, 31.0, 29.29, 24.75, 18.81, 24.24, 28.0, 17.0, 15.84, 15.0, 6.06], "iowait": [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], "webStats": [6070, 6072]}, "canvas-antifp": {"usr": [1.02, 19.39, 66.0, 69.7, 73.0, 69.0, 83.0, 75.25, 72.73, 76.24, 79.0, 88.89, 85.15, 34.02], "sys": [5.1, 12.24, 31.0, 30.3, 27.0, 31.0, 16.0, 24.75, 27.27, 22.77, 21.0, 11.11, 13.86, 3.09], "iowait": [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 2.06], "webStats": [6366, 6376]}, "adblock": {"usr": [21.0, 32.29, 61.0, 77.0, 77.55, 76.24, 61.0, 79.0, 80.0, 57.58], "sys": [2.0, 18.75, 25.0, 12.0, 15.31, 20.79, 20.0, 21.0, 20.0, 13.13], "iowait": [0.0, 1.04, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], "webStats": [3814, 3819]}, "scriptsafe": {"usr": [0.0, 2.97, 69.31, 76.0, 31.31, 3.96, 1.0, 0.99, 0.0], "sys": [0.97, 1.98, 27.72, 23.0, 7.07, 2.97, 0.0, 0.99, 1.01], "iowait": [0.0, 0.0, 0.0, 0.0, 10.1, 0.0, 0.0, 0.0, 0.0], "webStats": [2004, 2004]}, "user-agent": {"usr": [0.0, 6.93, 64.0, 72.28, 73.0, 64.0, 66.34, 85.86, 70.0, 76.0, 78.0, 91.0, 70.41, 16.49], "sys": [0.0, 4.95, 34.0, 24.75, 27.0, 36.0, 33.66, 14.14, 30.0, 24.0, 22.0, 9.0, 13.27, 2.06], "iowait": [0.0, 0.0, 0.0, 0.99, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], "webStats": [6035, 6042]}}}