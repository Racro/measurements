chrome.runtime.onMessage.addListener(function(message, sender, sendResponse) {
    if (message.action === 'getSnapshot') {
        const snapshotData = rrwebSnapshot.snapshot(document);
        sendResponse(snapshotData);  // Here's where the snapshot is sent as a response
    }
});
