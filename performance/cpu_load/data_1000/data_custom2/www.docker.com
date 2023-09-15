{"stats": {"/data/www.docker.com": {"usr": [0.0, 3.03, 64.65, 73.27, 79.8, 83.17, 81.82, 81.82, 12.0, 1.01], "sys": [0.0, 3.03, 34.34, 19.8, 20.2, 15.84, 9.09, 17.17, 1.0, 0.0], "iowait": [0.0, 0.0, 0.0, 4.95, 0.0, 0.0, 3.03, 0.0, 0.0, 0.0], "webStats": [3095, 3097]}, "adblock": {"usr": [1.0, 3.0, 75.25, 76.77, 75.76, 86.0, 85.0, 79.0, 43.88, 6.0, 0.98, 0.0], "sys": [0.0, 1.0, 20.79, 21.21, 19.19, 14.0, 15.0, 20.0, 7.14, 3.0, 0.0, 0.0], "iowait": [0.0, 0.0, 0.0, 1.01, 3.03, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], "webStats": [5618, 5622]}, "decentraleyes": {"usr": [0.0, 8.82, 69.31, 76.77, 76.24, 50.51, 51.49, 13.13, 19.0, 15.0, 0.99], "sys": [0.0, 7.84, 27.72, 22.22, 18.81, 19.19, 11.88, 3.03, 1.0, 3.0, 0.0], "iowait": [0.0, 0.0, 0.0, 0.0, 2.97, 3.03, 0.0, 0.0, 0.0, 0.0, 9.9], "webStats": [4462, 4470]}, "disconnect": {"usr": [0.0, 18.63, 56.7, 43.43, 59.0, 78.0, 84.85, 83.0, 75.25, 18.56, 1.03], "sys": [1.0, 9.8, 25.77, 11.11, 16.0, 14.0, 15.15, 17.0, 19.8, 1.03, 0.0], "iowait": [0.0, 0.0, 11.34, 28.28, 17.0, 7.0, 0.0, 0.0, 0.0, 0.0, 0.0], "webStats": [4192, 4194]}, "ghostery": {"usr": [0.0, 3.77, 68.09, 80.0, 78.79, 82.18, 80.2, 45.45, 21.0, 8.89], "sys": [0.0, 1.89, 25.53, 20.0, 21.21, 16.83, 19.8, 13.13, 9.0, 4.44], "iowait": [0.0, 16.98, 2.13, 0.0, 0.0, 0.0, 0.0, 10.1, 16.0, 3.33], "webStats": [2201, 2203]}, "https": {"usr": [0.0, 1.96, 71.29, 89.0, 90.0, 84.0, 80.81, 34.65, 15.31, 5.05], "sys": [2.02, 1.96, 22.77, 11.0, 10.0, 16.0, 18.18, 26.73, 8.16, 2.02], "iowait": [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 3.96, 10.2, 20.2], "webStats": [2158, 2164]}, "noscript": {"usr": [0.0, 8.91, 65.0, 72.28, 81.82, 73.0, 76.77, 73.27, 65.35, 11.0, 2.0, 4.0, 1.94], "sys": [0.0, 11.88, 28.0, 19.8, 17.17, 18.0, 23.23, 25.74, 6.93, 2.0, 1.0, 0.0, 1.94], "iowait": [4.0, 0.0, 2.0, 5.94, 0.0, 9.0, 0.0, 0.0, 0.0, 0.0, 10.0, 0.0, 0.0], "webStats": [6131, 6137]}, "privacy-badger": {"usr": [0.0, 0.97, 49.48, 61.62, 69.31, 82.83, 75.0, 86.0, 71.72, 16.98, 0.0, 2.0], "sys": [0.0, 0.0, 17.53, 14.14, 16.83, 16.16, 25.0, 13.0, 18.18, 1.89, 0.0, 0.0], "iowait": [0.0, 6.8, 23.71, 20.2, 12.87, 0.0, 0.0, 0.0, 5.05, 22.64, 18.37, 8.0], "webStats": [3462, 3467]}, "ublock": {"usr": [0.0, 24.75, 67.0, 77.78, 81.0, 65.0, 12.87, 0.0, 0.99, 0.0], "sys": [1.0, 16.83, 30.0, 21.21, 19.0, 10.0, 1.98, 0.0, 0.99, 1.01], "iowait": [0.0, 2.97, 0.0, 1.01, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], "webStats": [2736, 2738]}, "scriptsafe": {"usr": [0.0, 14.14, 75.25, 80.81, 0.0, 0.0, 2.0, 0.0], "sys": [0.99, 11.11, 23.76, 18.18, 3.0, 0.0, 1.0, 1.01], "iowait": [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], "webStats": [1347, 1347]}, "canvas-antifp": {"usr": [0.0, 1.96, 67.0, 69.31, 85.0, 57.73, 23.0, 75.0, 77.78, 31.07, 5.32, 0.0, 5.05], "sys": [1.0, 0.98, 26.0, 19.8, 15.0, 16.49, 5.0, 15.0, 19.19, 5.83, 0.0, 0.0, 1.01], "iowait": [0.0, 0.0, 0.0, 4.95, 0.0, 25.77, 52.0, 9.0, 1.01, 28.16, 8.51, 0.0, 0.0], "webStats": [6769, 6772]}, "adguard": {"usr": [18.37, 9.09, 55.56, 84.16, 88.89, 63.0, 67.68, 44.44, 23.47], "sys": [4.08, 2.02, 13.13, 15.84, 10.1, 15.0, 28.28, 17.17, 5.1], "iowait": [10.2, 1.01, 25.25, 0.0, 1.01, 1.0, 0.0, 6.06, 1.02], "webStats": [2458, 2462]}, "user-agent": {"usr": [0.0, 2.94, 59.0, 80.0, 74.0, 87.13, 90.82, 80.95, 27.66, 4.08, 0.0], "sys": [0.99, 2.94, 25.0, 19.0, 24.0, 12.87, 9.18, 17.14, 4.26, 2.04, 1.0], "iowait": [0.0, 0.0, 11.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.06, 0.0, 0.0], "webStats": [3423, 3425]}}}