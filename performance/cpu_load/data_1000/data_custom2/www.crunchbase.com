{"stats": {"/data/www.crunchbase.com": {"usr": [0.0, 2.94, 66.67, 87.0, 41.84, 8.08, 20.79, 36.08], "sys": [0.0, 0.98, 16.16, 13.0, 6.12, 1.01, 19.8, 19.59], "iowait": [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 6.19], "webStats": [1055, 1055]}, "adblock": {"usr": [0.0, 2.97, 35.35, 75.0, 75.76, 81.0, 19.39, 3.96, 1.0, 1.01], "sys": [0.0, 0.99, 13.13, 21.0, 21.21, 19.0, 4.08, 1.98, 0.0, 0.0], "iowait": [1.0, 3.96, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 4.0, 5.05], "webStats": [1888, 1889]}, "decentraleyes": {"usr": [0.99, 1.0, 20.0, 78.0, 48.08, 26.73, 6.06, 0.0], "sys": [0.0, 3.0, 11.0, 21.0, 19.23, 17.82, 4.04, 1.0], "iowait": [0.0, 0.0, 0.0, 0.0, 0.0, 13.86, 20.2, 7.0], "webStats": [1459, 1459]}, "disconnect": {"usr": [1.0, 19.19, 41.18, 65.49, 57.65, 75.0, 13.4, 4.0, 0.0, 0.0], "sys": [0.0, 12.12, 18.63, 11.5, 18.82, 12.0, 3.09, 3.0, 0.0, 1.02], "iowait": [0.0, 0.0, 11.76, 6.19, 16.47, 0.0, 0.0, 0.0, 0.0, 4.08], "webStats": [2293, 2293]}, "ghostery": {"usr": [0.99, 32.65, 61.0, 79.0, 80.81, 7.14, 3.96, 0.0, 0.0], "sys": [0.0, 23.47, 26.0, 14.0, 10.1, 4.08, 0.99, 1.01, 1.01], "iowait": [0.0, 0.0, 5.0, 3.0, 0.0, 0.0, 0.0, 0.0, 0.0], "webStats": [1532, 1532]}, "https": {"usr": [0.0, 3.96, 58.0, 73.0, 83.0, 34.69, 4.17, 0.99, 0.0], "sys": [0.0, 0.99, 26.0, 27.0, 17.0, 9.18, 2.08, 0.99, 1.01], "iowait": [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], "webStats": [1722, 1722]}, "noscript": {"usr": [0.0, 15.69, 61.22, 48.04, 70.0, 29.7, 16.16, 11.0, 9.18, 11.11], "sys": [0.0, 7.84, 25.51, 15.69, 15.0, 4.95, 5.05, 4.0, 3.06, 1.01], "iowait": [9.09, 2.94, 2.04, 34.31, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], "webStats": [2968, 2968]}, "privacy-badger": {"usr": [0.0, 21.21, 43.43, 80.2, 42.86, 13.13, 4.95, 2.0, 1.0], "sys": [1.02, 11.11, 20.2, 19.8, 6.12, 2.02, 1.98, 1.0, 0.0], "iowait": [0.0, 0.0, 6.06, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], "webStats": [1643, 1643]}, "ublock": {"usr": [0.0, 6.06, 62.63, 76.24, 45.0, 75.51, 19.0, 3.09, 2.0, 0.0], "sys": [1.0, 5.05, 26.26, 15.84, 15.0, 11.22, 2.0, 0.0, 1.0, 1.02], "iowait": [0.0, 17.17, 3.03, 0.0, 11.0, 12.24, 9.0, 0.0, 1.0, 3.06], "webStats": [2098, 2098]}, "scriptsafe": {"usr": [0.0, 1.96, 56.7, 46.39, 2.02, 1.02, 3.03], "sys": [0.0, 2.94, 21.65, 17.53, 2.02, 1.02, 3.03], "iowait": [0.0, 2.94, 0.0, 8.25, 0.0, 0.0, 15.15], "webStats": [462, 462]}, "canvas-antifp": {"usr": [0.0, 10.0, 58.16, 74.26, 79.0, 35.35, 10.0, 0.0, 0.0], "sys": [0.0, 9.0, 17.35, 20.79, 21.0, 7.07, 4.0, 1.01, 1.0], "iowait": [0.0, 0.0, 17.35, 2.97, 0.0, 0.0, 0.0, 0.0, 0.0], "webStats": [1991, 1991]}, "adguard": {"usr": [4.0, 3.0, 30.39, 76.0, 85.0, 64.0, 14.14, 30.0, 6.19, 4.12], "sys": [1.0, 2.0, 12.75, 14.0, 15.0, 23.0, 4.04, 8.0, 3.09, 4.12], "iowait": [0.0, 0.0, 0.0, 0.0, 0.0, 2.0, 65.66, 27.0, 23.71, 18.56], "webStats": [2795, 2795]}, "user-agent": {"usr": [1.0, 2.94, 40.21, 52.54, 78.05, 59.6, 19.44, 2.17, 0.0], "sys": [0.0, 2.94, 11.34, 7.63, 12.2, 15.15, 9.26, 0.0, 0.0], "iowait": [3.0, 0.0, 3.09, 26.27, 8.54, 20.2, 39.81, 2.17, 0.0], "webStats": [1659, 1659]}}}