{"stats": {"/data/www.salesforce.com": {"usr": [0.0, 7.0, 65.31, 75.0, 74.26, 75.0, 83.17, 85.86, 84.85, 33.33, 24.49], "sys": [0.0, 4.0, 29.59, 24.0, 25.74, 24.0, 15.84, 14.14, 14.14, 9.09, 4.08], "iowait": [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], "webStats": [3409, 3463]}, "decentraleyes": {"usr": [1.0, 3.96, 70.0, 79.8, 71.72, 69.31, 70.0, 74.75, 55.56, 20.79, 8.0, 9.0], "sys": [0.0, 0.99, 29.0, 19.19, 27.27, 19.8, 20.0, 24.24, 14.14, 0.99, 2.0, 4.0], "iowait": [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], "webStats": [5529, 5596]}, "canvas-antifp": {"usr": [0.0, 7.0, 72.0, 78.22, 83.0, 77.78, 80.2, 78.0, 82.0, 63.37, 23.0, 12.0, 10.1], "sys": [1.0, 4.0, 27.0, 19.8, 16.0, 22.22, 18.81, 22.0, 18.0, 9.9, 2.0, 2.0, 3.03], "iowait": [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], "webStats": [5673, 5718]}, "disconnect": {"usr": [8.08, 15.15, 68.0, 75.0, 77.0, 74.0, 74.75, 67.33, 13.86, 9.09, 13.27, 9.09], "sys": [4.04, 2.02, 28.0, 23.0, 23.0, 26.0, 22.22, 16.83, 4.95, 2.02, 2.04, 2.02], "iowait": [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], "webStats": [5188, 5222]}, "privacy-badger": {"usr": [0.98, 3.0, 64.36, 76.0, 74.0, 74.75, 75.49, 65.66, 16.0, 6.0, 1.98, 4.0], "sys": [0.98, 5.0, 30.69, 23.0, 26.0, 24.24, 19.61, 17.17, 3.0, 0.0, 0.0, 0.0], "iowait": [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], "webStats": [5107, 5153]}, "adguard": {"usr": [4.9, 5.88, 79.0, 78.0, 77.0, 68.69, 80.0, 80.2, 83.0, 64.0, 24.24, 16.0, 16.0, 2.0], "sys": [3.92, 1.96, 20.0, 22.0, 20.0, 30.3, 20.0, 18.81, 17.0, 22.0, 2.02, 4.0, 1.0, 1.0], "iowait": [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], "webStats": [6956, 7075]}, "ghostery": {"usr": [0.0, 2.91, 77.78, 81.19, 73.0, 76.77, 78.1, 76.84, 19.8, 1.98, 1.01], "sys": [1.0, 0.0, 21.21, 18.81, 26.0, 21.21, 20.95, 14.74, 0.99, 0.0, 0.0], "iowait": [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], "webStats": [4501, 4572]}, "adblock": {"usr": [38.38, 19.8, 66.33, 77.0, 72.73, 82.18, 75.76, 78.22, 81.82, 29.29, 13.0, 15.0, 10.0], "sys": [6.06, 4.95, 30.61, 23.0, 25.25, 15.84, 21.21, 20.79, 16.16, 4.04, 1.0, 2.0, 3.0], "iowait": [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], "webStats": [5900, 5990]}, "noscript": {"usr": [0.99, 5.94, 74.0, 65.66, 2.02, 1.0, 1.98, 0.99], "sys": [0.0, 5.94, 22.0, 14.14, 2.02, 0.0, 1.98, 0.0], "iowait": [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], "webStats": [1004, 1004]}, "https": {"usr": [0.99, 4.04, 78.0, 85.86, 81.0, 74.26, 80.81, 74.0, 82.0, 65.69, 30.3, 14.29, 10.1], "sys": [0.0, 6.06, 22.0, 14.14, 19.0, 24.75, 18.18, 26.0, 17.0, 16.67, 6.06, 2.04, 2.02], "iowait": [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], "webStats": [5686, 5726]}, "scriptsafe": {"usr": [0.0, 3.92, 73.27, 65.35, 1.96, 3.0, 2.0, 0.0], "sys": [0.0, 3.92, 23.76, 16.83, 1.96, 4.0, 1.0, 0.0], "iowait": [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], "webStats": [959, 959]}, "ublock": {"usr": [0.0, 3.96, 71.72, 79.0, 80.0, 76.0, 78.43, 54.0, 17.35, 10.1, 11.88], "sys": [1.0, 0.0, 27.27, 20.0, 20.0, 24.0, 17.65, 4.0, 0.0, 2.02, 1.98], "iowait": [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], "webStats": [4187, 4235]}}}