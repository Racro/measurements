{"stats": {"/data/www.launchdarkly.com": {"usr": [0.0, 3.03, 70.71, 82.18, 77.0, 72.0, 77.23, 78.79, 84.0, 77.0, 77.0, 16.0, 2.02], "sys": [0.0, 3.03, 22.22, 16.83, 22.0, 28.0, 22.77, 21.21, 16.0, 23.0, 11.0, 2.0, 2.02], "iowait": [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], "webStats": [5575, 5580]}, "adguard": {"usr": [3.06, 5.0, 69.0, 82.0, 81.0, 74.0, 80.2, 76.0, 74.0, 71.0, 27.0, 3.06], "sys": [0.0, 2.0, 21.0, 18.0, 19.0, 25.0, 18.81, 24.0, 21.0, 14.0, 4.0, 1.02], "iowait": [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 4.0, 0.0, 0.0, 0.0], "webStats": [5709, 5715]}, "privacy-badger": {"usr": [0.99, 13.0, 70.41, 74.26, 72.73, 80.0, 77.23, 68.69, 44.44, 20.0, 2.02], "sys": [0.99, 8.0, 25.51, 22.77, 27.27, 20.0, 21.78, 21.21, 6.06, 3.0, 0.0], "iowait": [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], "webStats": [3868, 3869]}, "noscript": {"usr": [5.1, 6.31, 63.64, 73.53, 83.0, 54.64, 5.0, 4.0, 4.04, 5.88], "sys": [6.12, 7.21, 34.09, 23.53, 17.0, 9.28, 2.0, 3.0, 1.01, 2.94], "iowait": [0.0, 3.6, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], "webStats": [3168, 3168]}, "adblock": {"usr": [28.28, 48.51, 76.0, 78.79, 73.0, 82.18, 88.0, 74.0, 69.0, 36.36, 19.19, 2.0], "sys": [8.08, 23.76, 24.0, 21.21, 24.0, 16.83, 12.0, 25.0, 22.0, 6.06, 2.02, 0.0], "iowait": [0.0, 0.0, 0.0, 0.0, 3.0, 0.0, 0.0, 0.0, 0.0, 2.02, 0.0, 0.0], "webStats": [5137, 5138]}, "disconnect": {"usr": [12.12, 19.0, 72.0, 77.0, 81.0, 77.78, 77.23, 79.0, 22.77, 9.18, 11.11], "sys": [2.02, 5.0, 27.0, 22.0, 18.0, 22.22, 21.78, 18.0, 1.98, 5.1, 2.02], "iowait": [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], "webStats": [3311, 3314]}, "ublock": {"usr": [0.99, 3.96, 62.0, 76.0, 79.8, 79.21, 76.0, 79.21, 81.63, 54.08], "sys": [2.97, 5.94, 27.0, 23.0, 19.19, 18.81, 24.0, 17.82, 18.37, 8.16], "iowait": [0.99, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.98, 0.0, 0.0], "webStats": [3458, 3459]}, "canvas-antifp": {"usr": [0.0, 2.94, 61.76, 78.79, 86.0, 74.26, 77.78, 82.0, 84.0, 78.43, 78.79, 33.33], "sys": [1.01, 2.94, 27.45, 21.21, 14.0, 24.75, 22.22, 18.0, 15.0, 20.59, 16.16, 2.02], "iowait": [0.0, 0.0, 0.98, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], "webStats": [4527, 4530]}, "https": {"usr": [0.98, 2.02, 62.38, 70.0, 79.8, 77.78, 75.25, 84.0, 79.0, 81.0, 78.79, 32.0, 17.71], "sys": [1.96, 6.06, 29.7, 27.0, 20.2, 21.21, 23.76, 16.0, 20.0, 19.0, 17.17, 6.0, 4.17], "iowait": [2.94, 0.0, 0.99, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], "webStats": [5914, 5921]}, "ghostery": {"usr": [1.01, 3.88, 81.0, 79.21, 76.0, 78.0, 76.0, 80.2, 56.44, 2.04, 2.0], "sys": [0.0, 0.97, 18.0, 19.8, 22.0, 20.0, 21.0, 19.8, 9.9, 1.02, 0.0], "iowait": [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 2.0, 0.0, 0.0, 0.0, 0.0], "webStats": [4952, 4954]}, "scriptsafe": {"usr": [1.03, 2.97, 68.0, 79.8, 73.27, 14.43, 3.0, 5.1, 5.94], "sys": [6.19, 1.98, 30.0, 20.2, 16.83, 2.06, 5.0, 1.02, 1.98], "iowait": [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], "webStats": [2678, 2678]}, "decentraleyes": {"usr": [0.0, 2.94, 60.61, 78.22, 69.0, 77.0, 74.75, 78.22, 40.4, 27.27, 1.01, 2.0], "sys": [0.0, 3.92, 31.31, 20.79, 31.0, 22.0, 24.24, 20.79, 8.08, 10.1, 0.0, 1.0], "iowait": [0.0, 0.98, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], "webStats": [4515, 4516]}, "user-agent": {"usr": [0.0, 2.94, 70.0, 73.74, 82.18, 80.0, 83.84, 83.17, 79.8, 80.0, 64.36, 16.16, 3.06], "sys": [0.0, 2.94, 27.0, 25.25, 17.82, 20.0, 16.16, 16.83, 20.2, 19.0, 7.92, 2.02, 3.06], "iowait": [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], "webStats": [4963, 4970]}}}