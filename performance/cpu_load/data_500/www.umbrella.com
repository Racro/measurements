{"stats": {"/data/www.umbrella.com": {"usr": [0.0, 3.92, 65.35, 77.0, 78.0, 85.86, 82.0, 76.47, 64.65, 82.0], "sys": [2.02, 0.98, 30.69, 22.0, 21.0, 14.14, 17.0, 22.55, 34.34, 18.0], "iowait": [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], "webStats": [1386, 1391]}, "adguard": {"usr": [4.0, 3.09, 72.0, 79.0, 77.0, 68.69, 72.0, 76.24, 80.81], "sys": [5.0, 6.19, 18.0, 20.0, 19.0, 29.29, 24.0, 23.76, 19.19], "iowait": [1.0, 8.25, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], "webStats": [1623, 1624]}, "ublock": {"usr": [1.02, 9.0, 62.38, 75.0, 81.0, 84.0, 82.0, 81.0, 79.0, 63.0, 3.06], "sys": [0.0, 8.0, 30.69, 25.0, 19.0, 15.0, 18.0, 19.0, 21.0, 12.0, 2.04], "iowait": [0.0, 0.0, 2.97, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], "webStats": [1611, 1620]}, "adblock": {"usr": [24.75, 40.4, 58.59, 75.76, 76.24, 65.35, 77.55, 76.0, 82.0], "sys": [3.96, 19.19, 27.27, 22.22, 22.77, 19.8, 22.45, 23.0, 18.0], "iowait": [0.0, 1.01, 1.01, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], "webStats": [1489, 1490]}, "decentraleyes": {"usr": [0.0, 8.0, 62.0, 79.0, 71.72, 28.28, 60.0, 76.0, 78.0], "sys": [2.04, 2.0, 34.0, 20.0, 21.21, 9.09, 20.0, 24.0, 22.0], "iowait": [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], "webStats": [1757, 1758]}, "ghostery": {"usr": [1.0, 1.96, 61.62, 81.0, 74.26, 80.61, 50.5, 74.26, 80.81, 17.0], "sys": [1.0, 0.98, 24.24, 18.0, 22.77, 18.37, 11.88, 25.74, 19.19, 6.0], "iowait": [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], "webStats": [1606, 1687]}, "disconnect": {"usr": [7.0, 12.24, 66.34, 77.78, 64.0, 54.55, 65.98, 76.24, 29.29], "sys": [5.0, 3.06, 20.79, 22.22, 16.0, 20.2, 23.71, 18.81, 11.11], "iowait": [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], "webStats": [1638, 1639]}, "noscript": {"usr": [1.0, 22.22, 74.0, 83.0, 22.22, 4.04, 1.0, 1.0], "sys": [1.0, 16.16, 25.0, 16.0, 5.05, 1.01, 2.0, 3.0], "iowait": [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], "webStats": [1748, 1748]}, "privacy-badger": {"usr": [1.0, 7.22, 63.37, 74.0, 75.25, 39.81, 30.21, 47.47, 14.14], "sys": [2.0, 3.09, 32.67, 26.0, 23.76, 8.74, 9.38, 11.11, 3.03], "iowait": [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.01, 0.0], "webStats": [1681, 1682]}, "canvas-antifp": {"usr": [0.0, 4.04, 64.36, 71.29, 74.75, 79.21, 81.0, 76.0, 77.0, 75.0, 78.22], "sys": [0.99, 2.02, 20.79, 27.72, 25.25, 19.8, 18.0, 24.0, 22.0, 24.0, 21.78], "iowait": [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], "webStats": [2363, 2364]}, "scriptsafe": {"usr": [1.0, 2.94, 68.0, 32.32, 1.0, 22.68, 27.0, 0.0], "sys": [3.0, 2.94, 20.0, 6.06, 2.0, 14.43, 8.0, 0.0], "iowait": [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 5.0, 0.0], "webStats": [1105, 1105]}, "https": {"usr": [0.0, 9.0, 74.26, 71.0, 75.76, 87.88, 86.0, 73.27, 74.0, 82.0, 74.0, 66.67], "sys": [0.0, 5.0, 21.78, 29.0, 21.21, 12.12, 14.0, 25.74, 26.0, 17.0, 26.0, 14.14], "iowait": [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], "webStats": [2176, 2184]}}}