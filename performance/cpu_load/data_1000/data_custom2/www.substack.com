{"stats": {"/data/www.substack.com": {"usr": [0.0, 3.0, 58.42, 77.0, 79.21, 71.0, 43.0, 4.72, 1.09, 1.0], "sys": [1.0, 1.0, 32.67, 21.0, 18.81, 18.0, 8.0, 0.94, 1.09, 0.0], "iowait": [0.0, 0.0, 3.96, 0.0, 0.0, 5.0, 11.0, 9.43, 0.0, 0.0], "webStats": [3235, 3238]}, "adblock": {"usr": [0.0, 14.42, 67.68, 81.19, 72.73, 68.0, 16.83, 0.0, 0.99], "sys": [1.0, 18.27, 26.26, 18.81, 25.25, 20.0, 4.95, 1.01, 0.99], "iowait": [0.0, 0.96, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], "webStats": [3035, 3036]}, "decentraleyes": {"usr": [0.0, 1.96, 46.46, 61.39, 52.04, 71.0, 16.16, 0.0, 1.0, 1.0], "sys": [0.0, 1.96, 25.25, 15.84, 17.35, 23.0, 4.04, 2.02, 0.0, 0.0], "iowait": [0.0, 0.0, 0.0, 17.82, 21.43, 0.0, 0.0, 0.0, 0.0, 0.0], "webStats": [2666, 2668]}, "disconnect": {"usr": [1.0, 10.89, 58.25, 63.92, 82.18, 75.0, 28.57, 4.04, 0.99, 1.0], "sys": [0.0, 6.93, 27.18, 24.74, 16.83, 19.0, 5.1, 1.01, 0.0, 1.0], "iowait": [0.0, 0.0, 0.97, 10.31, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], "webStats": [3300, 3301]}, "ghostery": {"usr": [1.0, 10.31, 62.24, 82.0, 80.0, 51.0, 14.71, 0.99, 0.0], "sys": [0.0, 13.4, 27.55, 18.0, 19.0, 11.0, 2.94, 0.99, 1.0], "iowait": [0.0, 14.43, 7.14, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], "webStats": [2587, 2592]}, "https": {"usr": [0.0, 3.92, 45.36, 50.0, 54.55, 71.0, 64.08, 25.77, 0.0, 1.0], "sys": [0.0, 1.96, 18.56, 12.0, 16.16, 22.0, 21.36, 6.19, 1.0, 2.0], "iowait": [0.0, 0.0, 4.12, 33.0, 28.28, 4.0, 6.8, 0.0, 0.0, 0.0], "webStats": [3624, 3625]}, "noscript": {"usr": [0.0, 2.94, 42.42, 71.84, 76.0, 73.74, 55.0, 12.24, 0.97, 0.92, 0.99], "sys": [0.0, 0.98, 33.33, 24.27, 24.0, 26.26, 8.0, 0.0, 0.97, 0.0, 1.98], "iowait": [0.0, 0.0, 0.0, 0.97, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], "webStats": [4037, 4045]}, "privacy-badger": {"usr": [0.0, 2.94, 48.48, 80.0, 76.77, 83.17, 26.53, 6.06, 4.04, 1.01], "sys": [0.0, 0.98, 14.14, 18.0, 22.22, 16.83, 6.12, 1.01, 6.06, 0.0], "iowait": [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 2.02, 0.0], "webStats": [2877, 2881]}, "ublock": {"usr": [0.0, 8.0, 70.3, 77.0, 67.26, 52.27, 21.78, 1.0, 0.0, 0.0], "sys": [0.0, 9.0, 23.76, 23.0, 18.58, 18.18, 4.95, 1.0, 0.0, 2.0], "iowait": [0.0, 0.0, 0.0, 0.0, 9.73, 21.59, 13.86, 9.0, 0.0, 0.0], "webStats": [3003, 3005]}, "scriptsafe": {"usr": [0.0, 9.28, 60.2, 77.0, 26.26, 0.99, 1.0, 0.0], "sys": [0.0, 7.22, 25.51, 19.0, 3.03, 2.97, 1.0, 1.98], "iowait": [0.0, 0.0, 5.1, 1.0, 0.0, 0.0, 2.0, 0.0], "webStats": [1823, 1823]}, "canvas-antifp": {"usr": [0.0, 2.91, 52.53, 76.0, 75.0, 79.0, 46.0, 5.05, 0.0, 0.99], "sys": [0.0, 1.94, 29.29, 22.0, 23.0, 18.0, 6.0, 2.02, 0.0, 0.99], "iowait": [0.0, 0.0, 3.03, 0.0, 0.0, 3.0, 0.0, 3.03, 0.0, 0.0], "webStats": [3117, 3123]}, "adguard": {"usr": [57.0, 16.16, 64.65, 73.27, 80.0, 51.52, 9.9, 3.54, 3.41, 2.04], "sys": [8.0, 10.1, 27.27, 23.76, 18.0, 9.09, 3.96, 1.77, 1.14, 1.02], "iowait": [0.0, 0.0, 0.0, 1.98, 2.0, 1.01, 3.96, 0.88, 0.0, 1.02], "webStats": [2670, 2678]}, "user-agent": {"usr": [0.0, 2.97, 48.0, 77.78, 75.25, 78.0, 34.65, 2.0, 0.93], "sys": [1.0, 1.98, 19.0, 20.2, 24.75, 20.0, 6.93, 3.0, 0.0], "iowait": [0.0, 3.96, 2.0, 0.0, 0.0, 0.0, 10.89, 8.0, 7.41], "webStats": [2865, 2869]}}}