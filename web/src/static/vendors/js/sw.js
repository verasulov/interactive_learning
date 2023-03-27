self.addEventListener('install', function (e) {
  console.info('Alloy service worker install');
});

self.addEventListener('fetch', function (e) {
  console.info('Alloy service worker fetch');
});

self.addEventListener('activate', function (e) {
  console.info('Alloy service worker activate');
});
