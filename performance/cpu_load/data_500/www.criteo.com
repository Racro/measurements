{"stats": {"/data/www.criteo.com": {"usr": [0.0, 4.0, 67.0, 74.75, 79.21, 84.0, 85.0, 81.19, 74.75, 12.37], "sys": [0.0, 4.0, 32.0, 25.25, 19.8, 15.0, 15.0, 16.83, 15.15, 2.06], "iowait": [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.99, 0.0, 0.0], "webStats": [2531, 2554]}, "privacy-badger": {"usr": [0.0, 1.98, 65.35, 84.0, 42.0, 27.55, 56.57, 12.0, 1.0, 1.02, 0.99], "sys": [0.0, 4.95, 28.71, 16.0, 19.0, 20.41, 18.18, 2.0, 1.0, 0.0, 0.99], "iowait": [0.0, 0.0, 0.99, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], "webStats": [4227, 4239]}, "noscript": {"usr": [0.0, 7.84, 68.37, 83.33, 72.0, 66.0, 22.45, 2.0, 0.0, 0.0], "sys": [4.08, 3.92, 30.61, 15.69, 28.0, 20.0, 3.06, 1.0, 1.0, 0.0], "iowait": [0.0, 0.0, 0.0, 0.98, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], "webStats": [3450, 3454]}, "ghostery": {"usr": [1.94, 2.94, 31.63, 79.0, 59.0, 69.7, 47.47, 31.0, 0.0, 1.98, 0.0], "sys": [1.94, 3.92, 14.29, 17.0, 17.0, 24.24, 26.26, 6.0, 1.01, 1.98, 7.14], "iowait": [1.94, 0.0, 0.0, 0.0, 1.0, 2.02, 2.02, 0.0, 0.0, 0.0, 0.0], "webStats": [4557, 4572]}, "adblock": {"usr": [15.84, 47.06, 50.51, 78.0, 32.65, 28.57, 74.75, 65.35, 71.72, 42.0, 3.06], "sys": [1.98, 21.57, 16.16, 19.0, 17.35, 14.29, 22.22, 23.76, 21.21, 9.0, 0.0], "iowait": [0.0, 0.98, 0.0, 0.0, 0.0, 0.0, 0.0, 3.96, 0.0, 0.0, 0.0], "webStats": [4102, 4131]}, "ublock": {"usr": [1.96, 2.94, 72.73, 47.52, 1.01, 2.97, 0.0], "sys": [2.94, 1.96, 27.27, 11.88, 6.06, 9.9, 9.28], "iowait": [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], "webStats": [528, 528]}, "canvas-antifp": {"usr": [0.0, 6.93, 66.33, 76.0, 80.0, 82.18, 77.78, 78.0, 52.53, 20.0], "sys": [0.0, 0.99, 31.63, 24.0, 20.0, 16.83, 22.22, 21.0, 15.15, 6.0], "iowait": [0.0, 0.0, 1.02, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], "webStats": [2526, 2566]}, "scriptsafe": {"usr": [0.0, 4.85, 68.69, 14.0, 0.0, 1.02, 1.0], "sys": [3.03, 0.97, 28.28, 6.0, 1.0, 1.02, 0.0], "iowait": [0.0, 0.0, 1.01, 1.0, 0.0, 0.0, 0.0], "webStats": [368, 368]}, "disconnect": {"usr": [23.71, 35.29, 56.12, 79.21, 82.18, 55.56, 43.3, 41.41, 38.14, 20.41, 19.8, 18.18, 17.35], "sys": [2.06, 9.8, 14.29, 18.81, 16.83, 21.21, 10.31, 22.22, 10.31, 4.08, 3.96, 6.06, 4.08], "iowait": [0.0, 0.0, 0.0, 0.0, 0.99, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], "webStats": [6247, 6270]}, "decentraleyes": {"usr": [0.0, 3.0, 64.65, 81.19, 33.0, 15.31, 21.78, 53.47, 81.82, 67.0, 37.37, 14.14], "sys": [0.0, 4.0, 29.29, 12.87, 13.0, 9.18, 9.9, 16.83, 16.16, 17.0, 14.14, 5.05], "iowait": [0.0, 0.0, 1.01, 0.0, 0.0, 0.0, 0.0, 2.97, 0.0, 0.0, 0.0, 0.0], "webStats": [5438, 5457]}, "adguard": {"usr": [3.96, 4.08, 31.63, 64.71, 67.33, 37.76, 47.96, 43.0, 79.0, 73.27, 82.0, 67.0], "sys": [3.96, 6.12, 13.27, 15.69, 11.88, 22.45, 16.33, 18.0, 19.0, 18.81, 18.0, 20.0], "iowait": [0.99, 0.0, 0.0, 0.0, 0.0, 0.0, 1.02, 0.0, 0.0, 6.93, 0.0, 0.0], "webStats": [5869, 5892]}, "https": {"usr": [0.0, 14.0, 66.0, 80.0, 82.83, 82.18, 82.0, 83.0, 65.66], "sys": [1.0, 8.0, 32.0, 20.0, 17.17, 16.83, 18.0, 17.0, 17.17], "iowait": [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 3.03], "webStats": [2429, 2458]}}}