document.getElementById('captureSnapshot').addEventListener('click', function() {
    chrome.tabs.query({ active: true, currentWindow: true }, function(tabs) {
        const activeTab = tabs[0];
        chrome.tabs.sendMessage(activeTab.id, { action: 'getSnapshot' }, function(response) {
            // Store the DOM snapshot in localStorage
            // const compressedData = LZString.compress(JSON.stringify(response));
            // console.log(response);
            const compressedData = JSON.stringify(response);
            console.log(compressedData);
            // console.log(compressedData);

            var openRequest = indexedDB.open("bigStorage", 1);

            openRequest.onupgradeneeded = function(e) {
                var db = e.target.result;
                if (!db.objectStoreNames.contains('snapshots')) {
                    db.createObjectStore('snapshots');
                }
            };

            openRequest.onsuccess = function(e) {
                var db = e.target.result;
                var transaction = db.transaction('snapshots', 'readwrite');
                var store = transaction.objectStore('snapshots');
                store.put(compressedData, 'domSnapshot');
            };

            // localStorage.setItem('domSnapshot', compressedData);
            alert('DOM snapshot saved to localStorage!');
        });
    });
});

document.getElementById('replaySnapshot').addEventListener('click', function() {
    // const snapshotData = JSON.parse(localStorage.getItem('domSnapshot'));

    var openRequest = indexedDB.open("bigStorage", 1);

    openRequest.onsuccess = function(e) {
        var db = e.target.result;
        var transaction = db.transaction('snapshots', 'readonly');
        var store = transaction.objectStore('snapshots');
        var getRequest = store.get('domSnapshot');
        getRequest.onsuccess = function(e) {
            var snapshotData = JSON.parse(e.target.result);
            // Now you can use your snapshot...

            const rebuildOptions = {
            doc: document, // Provide the current document
            // mirror: mirror, // Provide the mirror object we created
            // skipChild: false, // Don't skip child nodes
            // hackCss: true, // Apply CSS hacks to prevent style collision
            };
        
            let rebuildOutput = rrwebSnapshot.rebuild(snapshotData[0], rebuildOptions);

            // Check if the rebuildOutput has the expected structure
            if (Array.isArray(rebuildOutput) && rebuildOutput[0] instanceof Document) {
                // Serialize the document object which is the first element in the array
                let serializer = new XMLSerializer();
                let serializedHTML = serializer.serializeToString(rebuildOutput[0]);

                console.log(serializedHTML);

                // Create a blob from the serialized HTML
                let blob = new Blob([serializedHTML], { type: 'text/html' });
                let url = URL.createObjectURL(blob);
                console.log(blob);

                // Use the Chrome tabs API to open a new tab with the blob URL
                chrome.tabs.create({ url: url }, function(tab) {
                    // New tab is now open with the reconstructed HTML
                });
            } else {
                console.error('Unexpected rebuild output:', rebuildOutput);
            }
        };
    };
});
