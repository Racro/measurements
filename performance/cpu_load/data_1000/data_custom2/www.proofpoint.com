{"stats": {"/data/www.proofpoint.com": {"usr": [0.0, 3.96, 67.68, 74.0, 79.21, 66.33, 40.0, 61.11, 68.69, 48.45, 43.43, 30.0, 3.0], "sys": [1.0, 1.98, 29.29, 26.0, 17.82, 12.24, 10.0, 20.0, 21.21, 11.34, 7.07, 5.0, 0.0], "iowait": [0.0, 0.0, 0.0, 0.0, 0.0, 8.16, 19.09, 14.44, 5.05, 0.0, 0.0, 0.0, 0.0], "webStats": [5376, 5536]}, "adblock": {"usr": [1.0, 18.0, 62.0, 73.74, 72.73, 82.0, 79.21, 73.0, 40.82, 36.36, 41.41], "sys": [0.0, 18.0, 34.0, 21.21, 15.15, 18.0, 17.82, 25.0, 7.14, 6.06, 3.03], "iowait": [0.0, 0.0, 0.0, 2.02, 10.1, 0.0, 0.0, 1.0, 0.0, 6.06, 0.0], "webStats": [4439, 4562]}, "decentraleyes": {"usr": [0.0, 2.97, 24.76, 57.45, 60.61, 60.95, 46.81, 47.42, 40.4, 35.35, 13.13, 21.15], "sys": [1.0, 1.98, 12.38, 21.28, 30.3, 19.05, 20.21, 13.4, 13.13, 13.13, 3.03, 2.88], "iowait": [8.0, 0.0, 20.0, 9.57, 2.02, 14.29, 14.89, 0.0, 0.0, 0.0, 0.0, 0.0], "webStats": [5309, 5388]}, "disconnect": {"usr": [0.0, 2.0, 65.35, 65.0, 70.0, 73.74, 86.0, 47.12, 69.39, 46.0, 28.87, 51.52], "sys": [1.0, 2.0, 29.7, 21.0, 26.0, 24.24, 13.0, 13.46, 11.22, 9.0, 4.12, 6.06], "iowait": [0.0, 0.0, 0.0, 10.0, 4.0, 0.0, 0.0, 5.77, 8.16, 4.0, 6.19, 0.0], "webStats": [5095, 5166]}, "ghostery": {"usr": [0.0, 7.14, 54.0, 76.77, 75.76, 77.55, 72.55, 69.7, 54.76, 29.87, 43.75, 33.33], "sys": [0.0, 14.29, 17.0, 21.21, 19.19, 22.45, 17.65, 25.25, 8.73, 6.49, 7.29, 5.05], "iowait": [0.0, 19.39, 0.0, 0.0, 0.0, 0.0, 6.86, 4.04, 4.76, 11.69, 12.5, 0.0], "webStats": [5037, 5183]}, "https": {"usr": [1.01, 3.0, 44.0, 58.59, 79.21, 73.0, 81.19, 82.0, 64.0, 53.47, 22.22, 55.0, 31.63], "sys": [0.0, 1.0, 31.0, 15.15, 19.8, 24.0, 17.82, 16.0, 20.0, 11.88, 5.05, 8.0, 5.1], "iowait": [32.32, 0.0, 17.0, 24.24, 0.0, 0.0, 0.0, 0.0, 12.0, 30.69, 13.13, 5.0, 0.0], "webStats": [5704, 5824]}, "noscript": {"usr": [0.0, 10.0, 50.0, 69.31, 81.0, 83.84, 44.0, 11.34, 0.0, 1.0, 1.0], "sys": [2.02, 11.0, 24.0, 14.85, 16.0, 16.16, 8.0, 2.06, 1.0, 0.0, 0.0], "iowait": [0.0, 0.0, 0.0, 10.89, 2.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], "webStats": [4509, 4511]}, "privacy-badger": {"usr": [0.0, 5.05, 46.08, 71.29, 78.57, 79.8, 85.15, 68.0, 51.0, 30.93, 49.49, 46.46], "sys": [0.0, 4.04, 21.57, 26.73, 18.37, 19.19, 12.87, 18.0, 10.0, 6.19, 9.09, 4.04], "iowait": [0.0, 0.0, 3.92, 0.0, 2.04, 0.0, 0.0, 4.0, 19.0, 12.37, 7.07, 0.0], "webStats": [5008, 5119]}, "ublock": {"usr": [4.04, 0.0, 37.37, 80.39, 79.21, 55.79, 28.0, 1.98, 5.0], "sys": [0.0, 2.0, 19.19, 16.67, 20.79, 16.84, 7.0, 2.97, 7.0], "iowait": [0.0, 0.0, 0.0, 0.0, 0.0, 12.63, 0.0, 0.0, 0.0], "webStats": [2558, 2603]}, "scriptsafe": {"usr": [0.0, 11.22, 57.58, 76.24, 75.51, 1.0, 1.01, 0.0, 0.0], "sys": [0.0, 9.18, 34.34, 18.81, 20.41, 0.0, 2.02, 1.0, 0.0], "iowait": [0.0, 0.0, 0.0, 2.97, 0.0, 0.0, 0.0, 0.0, 0.0], "webStats": [2620, 2620]}, "canvas-antifp": {"usr": [0.99, 1.98, 51.0, 81.19, 78.79, 74.26, 73.74, 79.0, 51.0, 37.37, 49.5, 12.37], "sys": [0.0, 1.98, 20.0, 17.82, 19.19, 24.75, 18.18, 21.0, 13.0, 7.07, 4.95, 1.03], "iowait": [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 5.05, 0.0, 0.0, 0.0, 1.98, 0.0], "webStats": [4527, 4715]}, "adguard": {"usr": [4.04, 6.0, 31.0, 71.72, 79.59, 73.53, 68.32, 62.63, 21.9, 40.66, 24.49], "sys": [0.0, 2.0, 11.0, 15.15, 15.31, 22.55, 25.74, 18.18, 5.71, 9.89, 7.14], "iowait": [0.0, 0.0, 11.0, 9.09, 0.0, 0.0, 1.98, 16.16, 24.76, 15.38, 0.0], "webStats": [4340, 4467]}, "user-agent": {"usr": [0.0, 2.83, 37.23, 78.0, 71.29, 76.0, 78.0, 78.79, 75.0, 22.45, 34.65, 41.41], "sys": [0.0, 0.94, 18.09, 16.0, 20.79, 21.0, 21.0, 18.18, 16.0, 5.1, 5.94, 4.04], "iowait": [0.0, 0.0, 19.15, 2.0, 3.96, 3.0, 0.0, 2.02, 0.0, 0.0, 0.0, 0.0], "webStats": [5173, 5309]}}}