/* Site analytics: cookieless page views and store clicks to the shared PostHog project.
   No cookies, no storage, no library. A random id lives only for this page view.
   Skips localhost, bots and visitors with Do Not Track or Global Privacy Control on. */
(function () {
  var KEY = 'phc_ptdyYR8BHGJyQxNMXJ7uAKKnEjpG7gnY3o5MBazzZcyX';
  var EP = 'https://us.i.posthog.com/i/v0/e/';
  var n = navigator, h = location.hostname;
  if (h !== 'seanlynchgames.com' && h !== 'www.seanlynchgames.com') return;
  if (n.doNotTrack === '1' || n.globalPrivacyControl === true || /bot|crawl|spider|lighthouse|headless/i.test(n.userAgent || '')) return;
  var id = 'v_' + Math.random().toString(36).slice(2) + Date.now().toString(36);
  var q = new URLSearchParams(location.search);
  var base = { app: 'seanlynchgames-site', $current_url: location.origin + location.pathname, $pathname: location.pathname, $process_person_profile: false };
  ['utm_source', 'utm_medium', 'utm_campaign', 'ref'].forEach(function (k) { if (q.get(k)) base[k] = q.get(k).slice(0, 60); });
  if (document.referrer) { try { base.$referring_domain = new URL(document.referrer).hostname; } catch (e) {} }
  base.platform = /iPhone|iPad|iPod/.test(n.userAgent) ? 'ios' : /Android/.test(n.userAgent) ? 'android' : 'desktop';
  function send(event, extra) {
    var p = {}, k;
    for (k in base) p[k] = base[k];
    for (k in extra || {}) p[k] = extra[k];
    p.distinct_id = id;
    var body = JSON.stringify({ api_key: KEY, event: event, properties: p, timestamp: new Date().toISOString() });
    try {
      if (n.sendBeacon && n.sendBeacon(EP, new Blob([body], { type: 'text/plain' }))) return;
      fetch(EP, { method: 'POST', body: body, keepalive: true, headers: { 'Content-Type': 'text/plain' } });
    } catch (e) {}
  }
  send('$pageview');
  document.addEventListener('click', function (e) {
    var a = e.target && e.target.closest && e.target.closest('a[href]');
    if (!a) return;
    var u = a.href, store = /apps\.apple\.com/.test(u) ? 'app_store' : /play\.google\.com/.test(u) ? 'google_play' : /discord\.gg|discord\.com/.test(u) ? 'discord' : '';
    if (!store) return;
    var game = (u.match(/id(\d{9,})/) || [])[1] || (u.match(/[?&]id=([\w.]+)/) || [])[1] || '';
    send(store === 'discord' ? 'discord_click' : 'store_click', { store: store, target: game, section: (a.closest('section[id]') || {}).id || '' });
  }, true);
})();
