// Cache version control
const CACHE_VERSION = 4;
const CURRENT_CACHE = `cache-storage-V${CACHE_VERSION}`;

// List of routes that are going to be cached
const cacheFiles = [
    '/base_layout',
    '/',
    '/map',
    '/directions'
]

// activation event: clean up previously registered service workers
self.addEventListener('activate', event =>
  event.waitUntil(
    caches.keys().then(cacheNames => {
      return Promise.all(
        cacheNames.map(cacheName => {
          if (cacheName !== CURRENT_CACHE) {
            return caches.delete(cacheName);
          }
        })
      );
    })
  )
);

// Install event: cache the files
self.addEventListener('install', function(event) {
    event.waitUntil(
        caches.open(CURRENT_CACHE).then(function(cache) {
        return cache.addAll(cacheFiles);
        })
    );
});


self.addEventListener('fetch', function(event) {
    const requestUrl = new URL(event.request.url);
    if (requestUrl.origin === location.origin) {
        if ((requestUrl.pathname === '/')) {
            event.respondWith(caches.match('/'));
            return;
        }
    }
    event.respondWith(
      caches.match(event.request).then(function(response) {
        return response || fetch(event.request);
      })
    );
});