const dbPromise = idb.open('lineup-db', 1, function (upgradeDb) {
    upgradeDb.createObjectStore('lineup', {keyPath: 'pk'});
});

fetch('http://127.0.0.1:8082/getdata').then(function (response) {
    return response.json();
}).then(function (jsondata) {
    console.log(jsondata)
    dbPromise.then(function(db){
        var tx = db.transaction('lineup', 'readwrite');
        var lineupStore = tx.objectStore('lineup');
        for(var key in jsondata) {
            if (jsondata.hasOwnProperty(key)) {
                lineupStore.put(jsondata[key]);
            }
     }
    });
});

// let post="";
// 	dbPromise.then(function(db){
// 		let tx = db.transaction('lineup', 'readonly');
//   		let feedsStore = tx.objectStore('lineup');
//   		return feedsStore.openCursor();
// 	}).then(function logItems(cursor) {
// 		  if (!cursor) {
// 		  	document.getElementById('offlinedata').innerHTML=post;
// 		    return;
// 		  }
// 		  for (let field in cursor.value) {
// 		    	if(field == 'fields') {
// 		    		feedsData = cursor.value[field];
// 		    		for(var key in feedsData){
// 		    			if(key =='artist_name'){
// 		    				var artist_name = '<p class="schedule-card-title">'+feedsData[key]+'</p>';
// 		    			}
// 		    			if(key =='genre'){
// 		    				var genre = '<p class="schedule-card-genre-title">'+feedsData[key]+'</p>';
// 		    			}
// 		    			if(key == 'start_time'){
// 		    				var start_time = feedsData[key];
// 		    			}
//                         if(key == 'end_time'){
// 		    				var end_time = feedsData[key];
// 		    			}
// 		    		}
//                     let set_time = '<p className="schedule-card-time">' + start_time + '</p>';
// 		    		post=post+'<br>' + artist_name + '<br>' + genre + '<br>' + set_time + '<br>';
// 		    	}
// 		    }
// 		  return cursor.continue().then(logItems);
// 		});

