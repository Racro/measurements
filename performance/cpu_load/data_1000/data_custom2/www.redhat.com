{"stats": {"/data/www.redhat.com": {"usr": [0.0, 5.0, 66.67, 79.8, 81.0, 86.0, 63.73, 63.92, 83.0, 81.0, 63.0], "sys": [0.0, 4.0, 28.43, 20.2, 19.0, 12.0, 9.8, 20.62, 16.0, 16.0, 14.0], "iowait": [0.0, 0.0, 0.98, 0.0, 0.0, 0.0, 2.94, 0.0, 0.0, 0.0, 0.0], "webStats": [3983, 4038]}, "adblock": {"usr": [0.0, 1.98, 33.0, 69.0, 73.0, 81.0, 80.81, 84.0, 55.45, 81.82, 82.0, 44.33], "sys": [0.0, 0.99, 17.0, 29.0, 23.0, 19.0, 17.17, 8.0, 11.88, 18.18, 18.0, 7.22], "iowait": [0.0, 0.0, 14.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 9.28], "webStats": [5248, 5302]}, "decentraleyes": {"usr": [0.0, 1.98, 60.2, 62.24, 61.22, 52.94, 39.39, 18.56, 52.48, 38.32, 31.11], "sys": [0.0, 1.98, 22.45, 21.43, 13.27, 15.69, 9.09, 5.15, 12.87, 12.15, 11.11], "iowait": [0.0, 0.0, 0.0, 5.1, 15.31, 0.98, 0.0, 0.0, 0.0, 28.97, 36.67], "webStats": [4537, 4560]}, "disconnect": {"usr": [0.0, 3.03, 40.4, 39.18, 61.62, 71.96, 53.76, 85.86, 57.43, 78.0, 81.0, 75.0, 47.96], "sys": [1.0, 6.06, 22.22, 12.37, 20.2, 13.08, 9.68, 14.14, 6.93, 16.0, 17.0, 15.0, 7.14], "iowait": [0.0, 0.0, 9.09, 3.09, 14.14, 14.02, 22.58, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], "webStats": [5875, 5912]}, "ghostery": {"usr": [0.0, 1.98, 65.35, 81.0, 81.0, 80.0, 79.0, 68.0, 77.78, 66.67, 49.0], "sys": [0.96, 0.99, 18.81, 19.0, 18.0, 18.0, 20.0, 13.0, 13.13, 20.2, 6.0], "iowait": [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], "webStats": [4162, 4214]}, "https": {"usr": [0.0, 14.71, 62.24, 78.79, 79.21, 82.83, 74.0, 43.88, 53.0, 79.61, 72.92], "sys": [1.0, 10.78, 28.57, 21.21, 19.8, 14.14, 7.0, 9.18, 14.0, 14.56, 12.5], "iowait": [0.0, 4.9, 4.08, 0.0, 0.0, 0.0, 12.0, 6.12, 10.0, 5.83, 1.04], "webStats": [4140, 4186]}, "noscript": {"usr": [0.0, 0.0, 64.65, 82.0, 70.0, 64.0, 51.52, 45.54, 11.11, 1.0], "sys": [0.0, 2.97, 23.23, 18.0, 28.0, 22.0, 11.11, 5.94, 3.03, 0.0], "iowait": [0.0, 0.0, 0.0, 0.0, 0.0, 11.0, 0.0, 0.99, 0.0, 0.0], "webStats": [3646, 3720]}, "privacy-badger": {"usr": [0.0, 16.83, 67.33, 80.0, 69.0, 87.88, 89.0, 40.95, 72.92, 69.0, 55.67], "sys": [2.97, 13.86, 27.72, 20.0, 14.0, 11.11, 10.0, 5.71, 19.79, 12.0, 14.43], "iowait": [0.0, 0.0, 0.99, 0.0, 0.0, 0.0, 1.0, 0.95, 0.0, 11.0, 10.31], "webStats": [4557, 4616]}, "ublock": {"usr": [2.0, 12.0, 60.4, 71.72, 58.0, 60.82, 74.51, 36.73, 54.55, 84.85, 51.49], "sys": [1.0, 6.0, 25.74, 22.22, 15.0, 16.49, 14.71, 3.06, 7.07, 13.13, 7.92], "iowait": [0.0, 0.0, 3.96, 5.05, 5.0, 15.46, 5.88, 0.0, 0.0, 1.01, 0.0], "webStats": [4690, 4728]}, "scriptsafe": {"usr": [0.0, 2.78, 39.0, 67.0, 63.64, 20.0, 2.02, 4.9, 1.02], "sys": [0.0, 1.85, 18.0, 23.0, 19.19, 11.0, 0.0, 2.94, 0.0], "iowait": [0.0, 0.0, 0.0, 6.0, 9.09, 0.0, 0.0, 0.0, 1.02], "webStats": [2297, 2297]}, "canvas-antifp": {"usr": [0.0, 5.05, 51.0, 70.71, 76.24, 88.89, 82.18, 60.2, 82.0, 78.0, 56.57], "sys": [2.0, 3.03, 31.0, 21.21, 22.77, 11.11, 9.9, 12.24, 17.0, 16.0, 7.07], "iowait": [1.0, 0.0, 2.0, 3.03, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], "webStats": [4179, 4231]}, "adguard": {"usr": [2.02, 3.92, 27.0, 26.53, 36.54, 37.5, 62.24, 70.0, 49.5, 50.0, 34.34, 73.74, 70.3, 82.18], "sys": [2.02, 1.96, 5.0, 9.18, 8.65, 10.42, 27.55, 24.0, 14.85, 9.18, 8.08, 18.18, 11.88, 13.86], "iowait": [0.0, 0.98, 9.0, 37.76, 26.92, 34.38, 6.12, 2.0, 3.96, 0.0, 0.0, 1.01, 0.0, 0.99], "webStats": [7267, 7307]}, "user-agent": {"usr": [0.0, 1.96, 55.1, 69.7, 74.26, 81.82, 89.0, 51.52, 81.19, 52.53, 50.45, 34.12], "sys": [0.0, 0.98, 22.45, 22.22, 24.75, 17.17, 11.0, 7.07, 17.82, 8.08, 10.81, 4.71], "iowait": [0.0, 0.0, 1.02, 2.02, 0.0, 0.0, 0.0, 1.01, 0.0, 36.36, 33.33, 7.06], "webStats": [4779, 4831]}}}