{"stats": {"/data/www.vmware.com": {"usr": [0.0, 3.88, 61.62, 69.0, 67.0, 68.0, 70.0, 77.0, 71.0, 64.0], "sys": [6.0, 4.85, 33.33, 31.0, 33.0, 31.0, 30.0, 23.0, 28.0, 31.0], "iowait": [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], "webStats": [3087, 3112]}, "ghostery": {"usr": [0.0, 1.94, 46.94, 48.48, 66.67, 61.39, 71.29, 50.51, 12.12, 1.02], "sys": [0.0, 2.91, 17.35, 15.15, 12.12, 22.77, 19.8, 14.14, 9.09, 3.06], "iowait": [0.0, 0.0, 0.0, 0.0, 1.01, 1.98, 0.99, 0.0, 0.0, 0.0], "webStats": [3065, 3072]}, "https": {"usr": [0.0, 12.75, 68.69, 76.77, 68.0, 71.29, 80.0, 75.0, 72.28, 63.0], "sys": [0.0, 13.73, 26.26, 23.23, 32.0, 28.71, 20.0, 25.0, 26.73, 14.0], "iowait": [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], "webStats": [2298, 2320]}, "ublock": {"usr": [2.02, 5.05, 67.35, 71.29, 70.0, 69.0, 71.0, 67.68, 34.34, 7.37], "sys": [3.03, 8.08, 26.53, 26.73, 29.0, 31.0, 29.0, 32.32, 29.29, 20.0], "iowait": [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], "webStats": [2737, 2772]}, "disconnect": {"usr": [11.22, 13.27, 60.0, 62.63, 77.78, 48.94, 56.0, 65.0, 24.49], "sys": [3.06, 4.08, 24.0, 20.2, 16.16, 18.09, 33.0, 20.0, 4.08], "iowait": [3.06, 1.02, 4.0, 0.0, 0.0, 0.0, 1.0, 3.0, 0.0], "webStats": [2848, 2859]}, "scriptsafe": {"usr": [0.0, 4.0, 66.0, 74.75, 42.0, 0.0, 0.0, 0.0], "sys": [1.0, 2.0, 22.0, 23.23, 10.0, 1.02, 2.0, 1.0], "iowait": [0.0, 0.0, 3.0, 0.0, 25.0, 0.0, 0.0, 0.0], "webStats": [1894, 1894]}, "privacy-badger": {"usr": [1.01, 14.85, 56.7, 76.24, 67.0, 56.57, 21.0, 32.32, 1.0, 2.04], "sys": [4.04, 8.91, 27.84, 21.78, 20.0, 15.15, 8.0, 6.06, 1.0, 9.18], "iowait": [0.0, 2.97, 2.06, 0.0, 1.0, 6.06, 0.0, 0.0, 0.0, 0.0], "webStats": [3098, 3107]}, "decentraleyes": {"usr": [0.99, 2.02, 51.04, 58.16, 63.0, 42.57, 48.48, 68.0, 63.73], "sys": [0.0, 6.06, 26.04, 25.51, 18.0, 16.83, 12.12, 22.0, 19.61], "iowait": [0.0, 0.0, 0.0, 11.22, 0.0, 5.94, 0.0, 2.0, 0.0], "webStats": [2397, 2433]}, "adblock": {"usr": [38.61, 40.4, 73.0, 57.14, 72.28, 70.41, 67.33, 71.72, 77.0, 24.0], "sys": [3.96, 23.23, 25.0, 18.37, 15.84, 17.35, 15.84, 19.19, 16.0, 7.0], "iowait": [0.0, 0.0, 0.0, 1.02, 0.99, 0.0, 0.99, 0.0, 0.0, 0.0], "webStats": [2828, 2837]}, "adguard": {"usr": [2.97, 6.93, 59.18, 57.0, 83.0, 71.0, 71.72, 76.0, 81.0, 49.02], "sys": [0.99, 2.97, 18.37, 15.0, 14.0, 21.0, 22.22, 23.0, 17.0, 12.75], "iowait": [0.0, 1.98, 15.31, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 6.86], "webStats": [2772, 2788]}, "canvas-antifp": {"usr": [0.0, 4.0, 62.63, 67.0, 73.27, 76.0, 68.69, 70.3, 80.81, 78.22], "sys": [1.0, 4.0, 33.33, 33.0, 26.73, 24.0, 31.31, 28.71, 19.19, 20.79], "iowait": [0.0, 1.0, 2.02, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], "webStats": [3492, 3523]}, "noscript": {"usr": [0.0, 19.8, 71.0, 77.55, 45.0, 1.01, 0.99, 1.04, 0.0], "sys": [0.99, 10.89, 26.0, 22.45, 6.0, 6.06, 0.0, 5.21, 1.0], "iowait": [0.0, 0.99, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], "webStats": [2133, 2133]}}}