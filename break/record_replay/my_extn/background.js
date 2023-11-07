self.addEventListener('install', (event) => {
    console.log("DOM Snapshot Extension installed!");
});

self.addEventListener('activate', (event) => {
    console.log("DOM Snapshot Extension activated!");
});
