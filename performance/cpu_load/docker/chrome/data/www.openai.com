{"stats": {"/data/www.openai.com": {"usr": [0.0, 2.42, 69.0, 83.17, 77.0, 70.0, 46.94, 46.39, 47.96], "sys": [0.0, 1.61, 30.0, 15.84, 23.0, 12.0, 5.1, 2.06, 0.0], "iowait": [0.0, 0.0, 0.0, 0.0, 0.0, 4.0, 0.0, 0.0, 0.0], "webStats": [1545, 1545]}, "adblock": {"usr": [0.0, 26.04, 73.0, 75.76, 85.86, 77.23, 55.21, 45.92, 42.27], "sys": [0.0, 10.42, 24.0, 23.23, 13.13, 19.8, 1.04, 1.02, 2.06], "iowait": [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], "webStats": [1797, 1797]}, "decentraleyes": {"usr": [0.0, 3.81, 69.31, 72.0, 41.84, 10.42, 3.88, 1.03], "sys": [0.0, 2.86, 27.72, 23.0, 6.12, 1.04, 3.88, 1.03], "iowait": [0.0, 0.0, 0.0, 1.0, 1.02, 0.0, 0.0, 0.0], "webStats": [1823, 1823]}, "disconnect": {"usr": [0.0, 11.61, 73.27, 77.78, 86.0, 77.0, 53.0, 46.0, 45.36], "sys": [0.0, 7.14, 21.78, 22.22, 14.0, 22.0, 4.0, 1.0, 5.15], "iowait": [0.0, 4.46, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], "webStats": [1878, 1878]}, "ghostery": {"usr": [0.0, 31.63, 71.0, 80.0, 78.0, 81.0, 55.67, 43.88, 44.9], "sys": [0.0, 20.41, 26.0, 20.0, 18.0, 18.0, 2.06, 4.08, 2.04], "iowait": [0.0, 0.0, 0.0, 0.0, 2.0, 0.0, 0.0, 0.0, 3.06], "webStats": [1846, 1846]}, "https": {"usr": [0.0, 13.0, 68.32, 86.0, 82.0, 80.0, 53.06, 43.88, 44.33], "sys": [0.0, 8.0, 29.7, 13.0, 18.0, 13.0, 9.18, 7.14, 2.06], "iowait": [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 2.04, 1.03], "webStats": [1707, 1707]}, "noscript": {"usr": [0.0, 4.12, 65.66, 70.59, 82.0, 78.0, 75.76, 51.52, 46.46, 48.98], "sys": [0.0, 3.09, 32.32, 23.53, 18.0, 22.0, 8.08, 2.02, 2.02, 0.0], "iowait": [0.0, 0.0, 0.0, 0.98, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], "webStats": [3403, 3404]}, "privacy-badger": {"usr": [0.0, 19.79, 72.73, 78.0, 80.0, 81.19, 55.0, 44.79, 43.88], "sys": [0.0, 13.54, 25.25, 21.0, 20.0, 15.84, 2.0, 0.0, 2.04], "iowait": [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], "webStats": [2785, 2785]}, "ublock": {"usr": [0.0, 3.12, 75.0, 79.21, 77.78, 82.18, 58.0, 45.92, 43.75], "sys": [1.05, 4.17, 23.0, 18.81, 22.22, 17.82, 2.0, 7.14, 1.04], "iowait": [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.02, 0.0], "webStats": [1636, 1636]}, "scriptsafe": {"usr": [0.0, 3.12, 65.66, 33.67, 37.62, 16.49, 0.98], "sys": [1.03, 4.17, 20.2, 3.06, 28.71, 4.12, 0.0], "iowait": [0.0, 0.0, 0.0, 0.0, 1.98, 8.25, 0.0], "webStats": [912, 912]}, "canvas-antifp": {"usr": [0.0, 5.1, 65.31, 78.79, 77.23, 79.59, 68.04, 50.0, 43.3, 45.36], "sys": [0.0, 1.02, 30.61, 20.2, 21.78, 20.41, 5.15, 1.0, 2.06, 2.06], "iowait": [0.0, 1.02, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], "webStats": [1826, 1826]}, "adguard": {"usr": [2.13, 5.26, 71.0, 78.0, 30.93, 68.0, 7.22, 3.23, 4.17], "sys": [0.0, 2.11, 18.0, 14.0, 5.15, 21.0, 6.19, 3.23, 4.17], "iowait": [0.0, 0.0, 0.0, 0.0, 4.12, 2.0, 0.0, 0.0, 1.04], "webStats": [2036, 2036]}, "user-agent": {"usr": [0.0, 3.06, 65.66, 68.69, 73.0, 78.22, 69.0, 52.04, 46.0], "sys": [0.0, 3.06, 30.3, 18.18, 21.0, 20.79, 6.0, 3.06, 3.0], "iowait": [0.0, 0.0, 0.0, 7.07, 4.0, 0.0, 0.0, 2.04, 0.0], "webStats": [1707, 1707]}}}