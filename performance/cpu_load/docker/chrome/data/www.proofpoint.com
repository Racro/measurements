{"stats": {"/data/www.proofpoint.com": {"usr": [1.0, 1.96, 57.58, 76.0, 73.74, 82.18, 76.0, 78.0, 48.51, 26.53, 20.2, 6.06], "sys": [2.0, 1.96, 35.35, 24.0, 26.26, 17.82, 22.0, 14.0, 9.9, 3.06, 4.04, 1.01], "iowait": [1.0, 0.0, 2.02, 0.0, 0.0, 0.0, 0.0, 0.0, 0.99, 0.0, 0.0, 0.0], "webStats": [4320, 4546]}, "adblock": {"usr": [30.93, 37.37, 67.65, 73.74, 76.24, 71.0, 79.59, 16.0, 15.0, 15.15, 7.14], "sys": [3.09, 16.16, 27.45, 26.26, 20.79, 18.0, 19.39, 4.0, 6.0, 4.04, 0.0], "iowait": [0.0, 1.01, 0.0, 0.0, 0.99, 0.0, 0.0, 3.0, 0.0, 5.05, 0.0], "webStats": [3372, 3683]}, "ghostery": {"usr": [0.99, 5.0, 63.64, 74.26, 78.79, 72.28, 34.69, 16.16, 5.94], "sys": [0.0, 4.0, 16.16, 24.75, 21.21, 22.77, 13.27, 6.06, 3.96], "iowait": [0.0, 0.0, 0.0, 0.0, 0.0, 1.98, 0.0, 0.0, 3.96], "webStats": [2233, 2401]}, "privacy-badger": {"usr": [0.0, 2.0, 51.0, 75.0, 74.0, 78.0, 65.66, 22.33, 13.54, 10.0], "sys": [0.0, 2.0, 20.0, 23.0, 23.0, 22.0, 18.18, 5.83, 2.08, 8.0], "iowait": [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.97, 0.0, 0.0], "webStats": [3430, 3648]}, "https": {"usr": [4.04, 12.87, 68.69, 79.0, 80.2, 81.0, 70.19, 51.04, 33.67, 34.0, 23.23, 1.0], "sys": [5.05, 7.92, 28.28, 21.0, 18.81, 19.0, 28.85, 13.54, 8.16, 5.0, 1.01, 1.0], "iowait": [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.01, 0.0], "webStats": [4062, 4263]}, "ublock": {"usr": [2.0, 1.98, 69.61, 74.75, 75.25, 38.14, 9.09, 2.0, 0.95], "sys": [1.0, 1.98, 26.47, 25.25, 23.76, 6.19, 1.01, 3.0, 0.0], "iowait": [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], "webStats": [2814, 2837]}, "decentraleyes": {"usr": [0.0, 2.97, 40.59, 59.18, 67.0, 73.27, 73.74, 24.0, 25.25, 15.0, 6.0], "sys": [1.0, 3.96, 20.79, 28.57, 18.0, 20.79, 24.24, 7.0, 6.06, 4.0, 2.0], "iowait": [0.0, 0.0, 0.0, 1.02, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], "webStats": [4005, 4244]}, "disconnect": {"usr": [10.2, 16.0, 47.47, 72.73, 66.34, 20.83, 14.0, 10.31, 12.12], "sys": [4.08, 2.0, 21.21, 26.26, 17.82, 6.25, 3.0, 4.12, 2.02], "iowait": [0.0, 0.0, 0.0, 0.0, 9.9, 22.92, 0.0, 0.0, 0.0], "webStats": [2302, 2334]}, "scriptsafe": {"usr": [0.0, 4.0, 57.0, 81.0, 50.51, 1.02, 0.0, 2.0, 0.0], "sys": [2.04, 3.0, 33.0, 18.0, 11.11, 1.02, 0.0, 3.0, 0.0], "iowait": [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 5.0, 0.0], "webStats": [2253, 2253]}, "noscript": {"usr": [0.0, 4.35, 33.33, 68.69, 73.53, 70.41, 17.17, 0.0, 2.02, 1.98], "sys": [0.0, 7.61, 18.18, 29.29, 25.49, 14.29, 2.02, 0.99, 4.04, 4.95], "iowait": [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], "webStats": [3390, 3390]}, "canvas-antifp": {"usr": [0.0, 5.83, 61.62, 82.83, 77.45, 80.0, 73.0, 60.2, 37.37, 24.0, 21.43, 1.01], "sys": [0.0, 0.97, 37.37, 17.17, 20.59, 20.0, 25.0, 11.22, 9.09, 5.0, 2.04, 2.02], "iowait": [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], "webStats": [4158, 4354]}, "adguard": {"usr": [1.02, 7.07, 10.0, 66.67, 52.53, 80.0, 66.0, 78.0, 70.0, 15.15, 15.0, 22.22], "sys": [0.0, 5.05, 3.0, 22.22, 14.14, 20.0, 31.0, 22.0, 17.0, 4.04, 2.0, 7.07], "iowait": [0.0, 0.0, 0.0, 3.03, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], "webStats": [4942, 5118]}, "user-agent": {"usr": [1.02, 3.96, 65.66, 75.0, 72.0, 81.0, 80.0, 79.8, 34.0, 40.0, 34.02, 9.0], "sys": [1.02, 1.98, 26.26, 22.0, 27.0, 18.0, 20.0, 20.2, 7.0, 9.0, 6.19, 1.0], "iowait": [0.0, 0.99, 1.01, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], "webStats": [4674, 4869]}}}