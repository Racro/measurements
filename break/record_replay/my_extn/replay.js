document.addEventListener("DOMContentLoaded", function() {
    const snapshotString = localStorage.getItem('domSnapshot');
    const snapshot = JSON.parse(snapshotString);
    
    // Convert the snapshot to the format expected by rrweb-player
    const events = [{
        type: 2,  // FullSnapshot type
        data: snapshot,
        timestamp: Date.now()
    }, {
        type: 4,  // End event type
        timestamp: Date.now() + 1  // Just a millisecond after the snapshot for simplicity
    }];

    new rrwebPlayer({
        target: document.getElementById('rrweb-player'),
        data: {
            events
        }
    });
});
