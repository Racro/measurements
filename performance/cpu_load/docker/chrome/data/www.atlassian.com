{"stats": {"/data/www.atlassian.com": {"usr": [0.0, 5.88, 63.92, 74.04, 74.23, 81.0, 78.0, 83.0, 60.0, 20.41, 3.03, 2.02, 0.0], "sys": [0.0, 4.9, 29.9, 25.96, 25.77, 19.0, 20.0, 16.0, 12.0, 6.12, 3.03, 1.01, 1.01], "iowait": [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], "webStats": [6381, 6388]}, "https": {"usr": [0.0, 4.95, 67.68, 71.29, 79.0, 75.0, 77.23, 78.79, 79.8, 27.27, 6.93, 3.03, 1.01], "sys": [0.0, 2.97, 31.31, 25.74, 21.0, 23.0, 20.79, 21.21, 14.14, 7.07, 0.99, 2.02, 27.27], "iowait": [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], "webStats": [6506, 6521]}, "ublock": {"usr": [0.99, 21.78, 66.0, 80.2, 77.78, 75.76, 50.0, 8.08, 1.98, 0.0, 2.02], "sys": [3.96, 12.87, 33.0, 17.82, 19.19, 23.23, 10.2, 4.04, 0.99, 1.02, 1.01], "iowait": [0.0, 0.0, 1.0, 0.0, 1.01, 0.0, 4.08, 0.0, 0.99, 0.0, 0.0], "webStats": [4146, 4166]}, "disconnect": {"usr": [11.22, 14.43, 67.31, 74.74, 75.25, 74.29, 50.52, 11.34, 9.18, 7.22], "sys": [3.06, 5.15, 26.92, 25.26, 23.76, 24.76, 19.59, 2.06, 3.06, 1.03], "iowait": [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 15.46, 0.0, 0.0, 0.0], "webStats": [3954, 3972]}, "adguard": {"usr": [4.08, 19.0, 83.0, 81.0, 80.0, 68.32, 76.77, 81.0, 38.38, 6.06, 10.89, 1.01, 2.0], "sys": [1.02, 4.0, 17.0, 19.0, 19.0, 29.7, 23.23, 19.0, 6.06, 3.03, 0.99, 1.01, 1.0], "iowait": [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], "webStats": [6321, 6333]}, "decentraleyes": {"usr": [0.0, 6.8, 62.0, 84.85, 77.23, 67.68, 69.61, 43.75, 16.0, 0.99], "sys": [0.0, 3.88, 37.0, 15.15, 21.78, 19.19, 25.49, 10.42, 5.0, 0.0], "iowait": [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], "webStats": [3513, 3514]}, "privacy-badger": {"usr": [0.0, 8.16, 65.66, 80.0, 74.0, 71.0, 74.26, 11.0, 2.0, 2.04, 2.0], "sys": [0.0, 2.04, 32.32, 20.0, 23.0, 29.0, 22.77, 5.0, 2.0, 0.0, 0.0], "iowait": [0.0, 0.0, 0.0, 0.0, 2.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], "webStats": [3819, 3823]}, "canvas-antifp": {"usr": [1.01, 5.83, 69.39, 75.25, 79.0, 74.0, 79.0, 80.0, 70.0, 20.2, 4.08, 1.0, 1.01], "sys": [0.0, 3.88, 28.57, 23.76, 19.0, 25.0, 20.0, 19.0, 17.0, 8.08, 3.06, 1.0, 4.04], "iowait": [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], "webStats": [6663, 6685]}, "ghostery": {"usr": [1.0, 4.0, 41.0, 82.18, 83.84, 79.0, 76.77, 34.0, 11.88, 1.01, 1.0], "sys": [1.0, 4.0, 18.0, 17.82, 16.16, 21.0, 23.23, 11.0, 1.98, 3.03, 3.0], "iowait": [0.0, 4.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.99, 0.0, 0.0], "webStats": [4189, 4191]}, "scriptsafe": {"usr": [0.0, 2.94, 65.0, 71.0, 70.91, 5.62, 1.05, 2.08, 0.0], "sys": [3.06, 9.8, 29.0, 27.0, 11.82, 8.99, 2.11, 5.21, 2.0], "iowait": [0.0, 0.0, 0.0, 0.0, 9.09, 0.0, 0.0, 0.0, 0.0], "webStats": [2616, 2617]}, "adblock": {"usr": [18.18, 34.34, 69.31, 78.79, 80.2, 70.0, 72.73, 53.47, 6.06, 3.03], "sys": [4.04, 19.19, 24.75, 16.16, 19.8, 20.0, 24.24, 9.9, 2.02, 0.0], "iowait": [0.0, 6.06, 0.0, 0.0, 0.0, 0.0, 0.0, 2.97, 0.0, 0.0], "webStats": [3547, 3548]}, "noscript": {"usr": [0.0, 5.0, 69.61, 81.0, 81.82, 27.27, 7.14, 1.0], "sys": [0.0, 4.0, 28.43, 19.0, 18.18, 4.04, 6.12, 4.0], "iowait": [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], "webStats": [1607, 1607]}, "user-agent": {"usr": [0.0, 9.09, 69.31, 80.0, 84.0, 79.0, 74.0, 79.21, 41.0, 4.12, 3.0, 2.0, 2.97], "sys": [0.0, 4.04, 28.71, 20.0, 16.0, 21.0, 24.0, 20.79, 14.0, 0.0, 0.0, 1.0, 0.99], "iowait": [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.99], "webStats": [6021, 6029]}}}