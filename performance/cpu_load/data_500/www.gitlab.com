{"stats": {"/data/www.gitlab.com": {"usr": [0.0, 6.12, 63.37, 78.22, 90.91, 76.24, 85.0, 86.0, 75.0, 74.75, 87.13, 85.15, 84.85, 27.37, 12.77], "sys": [1.0, 6.12, 31.68, 20.79, 9.09, 23.76, 14.0, 14.0, 23.0, 25.25, 12.87, 14.85, 13.13, 4.21, 1.06], "iowait": [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], "webStats": [6939, 7125]}, "disconnect": {"usr": [13.0, 16.83, 59.22, 72.16, 79.21, 85.0, 80.0, 86.0, 30.0, 10.89, 13.27, 14.29, 12.12], "sys": [2.0, 3.96, 20.39, 24.74, 19.8, 15.0, 20.0, 14.0, 15.0, 3.96, 2.04, 2.04, 5.05], "iowait": [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], "webStats": [6171, 6215]}, "ublock": {"usr": [0.0, 3.92, 47.0, 73.0, 78.0, 77.36, 78.72, 81.19, 18.95, 12.77, 4.35, 4.49, 5.32], "sys": [2.0, 3.92, 25.0, 25.0, 20.0, 21.7, 21.28, 17.82, 5.26, 2.13, 4.35, 0.0, 2.13], "iowait": [0.0, 0.98, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 5.32], "webStats": [6090, 6094]}, "adblock": {"usr": [22.45, 7.29, 21.21, 71.72, 82.0, 80.0, 78.22, 80.0, 88.0, 75.0, 79.0, 85.0, 38.0, 19.79, 9.18], "sys": [1.02, 6.25, 16.16, 27.27, 18.0, 19.0, 21.78, 19.0, 12.0, 25.0, 21.0, 15.0, 8.0, 5.21, 2.04], "iowait": [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], "webStats": [7631, 7770]}, "https": {"usr": [0.0, 11.11, 68.32, 79.0, 90.0, 76.0, 88.0, 85.86, 61.0, 14.13, 13.98], "sys": [1.0, 12.12, 27.72, 21.0, 10.0, 24.0, 12.0, 14.14, 10.0, 1.09, 3.23], "iowait": [0.0, 0.0, 1.98, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], "webStats": [3372, 3383]}, "adguard": {"usr": [2.0, 7.77, 18.0, 62.63, 83.0, 78.0, 73.27, 81.82, 86.87, 85.15, 84.0, 78.0, 81.82, 27.0, 27.72, 28.28], "sys": [2.0, 3.88, 6.0, 16.16, 15.0, 21.0, 25.74, 15.15, 13.13, 14.85, 15.0, 22.0, 18.18, 6.0, 10.89, 6.06], "iowait": [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], "webStats": [9417, 9558]}, "canvas-antifp": {"usr": [2.02, 5.94, 65.0, 78.0, 89.0, 86.14, 78.22, 81.0, 81.0, 79.8, 78.22, 89.9, 89.11, 73.0, 31.63], "sys": [10.1, 4.95, 30.0, 22.0, 11.0, 12.87, 20.79, 19.0, 19.0, 20.2, 21.78, 10.1, 9.9, 14.0, 5.1], "iowait": [0.0, 0.99, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], "webStats": [7490, 7619]}, "noscript": {"usr": [1.0, 2.02, 57.0, 78.0, 78.22, 56.12, 4.04, 0.0, 1.96], "sys": [0.0, 2.02, 17.0, 22.0, 19.8, 20.41, 2.02, 0.0, 2.94], "iowait": [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], "webStats": [2895, 2895]}, "privacy-badger": {"usr": [0.98, 6.0, 62.0, 78.0, 80.0, 66.67, 82.0, 44.44, 19.39, 20.79, 16.0], "sys": [0.98, 1.0, 31.0, 22.0, 19.0, 19.19, 13.0, 9.09, 6.12, 4.95, 3.0], "iowait": [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], "webStats": [4219, 4350]}, "ghostery": {"usr": [2.0, 1.01, 51.0, 71.72, 84.0, 80.2, 87.0, 80.81, 82.0, 61.0, 3.0, 3.0], "sys": [7.0, 3.03, 17.0, 22.22, 16.0, 18.81, 13.0, 18.18, 18.0, 12.0, 0.0, 2.0], "iowait": [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], "webStats": [5362, 5372]}, "scriptsafe": {"usr": [1.02, 2.97, 61.62, 31.0, 19.39, 24.51, 46.39, 0.99], "sys": [1.02, 1.98, 18.18, 8.0, 13.27, 18.63, 20.62, 1.98], "iowait": [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.03, 0.0], "webStats": [1275, 1275]}, "decentraleyes": {"usr": [0.0, 1.96, 56.57, 71.0, 88.12, 79.8, 84.16, 80.0, 26.8, 48.51, 78.0, 83.0, 37.0, 23.23, 4.04], "sys": [3.09, 0.98, 30.3, 26.0, 11.88, 19.19, 15.84, 20.0, 11.34, 14.85, 22.0, 16.0, 12.0, 6.06, 0.0], "iowait": [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], "webStats": [7568, 7626]}}}