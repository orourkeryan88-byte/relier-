/* Anti-clickjacking guard. Loaded render-blocking in <head> so a framed page
   never paints. The real defence is the frame-ancestors / X-Frame-Options
   response headers (see _headers, .htaccess, deploy/nginx.conf.sample);
   this is the fallback for hosts that cannot send headers. */
(function () {
  "use strict";
  var framed;
  try { framed = window.top !== window.self; }
  catch (e) { framed = true; }          /* cross-origin access threw: we are framed */
  if (!framed) return;
  document.documentElement.className += " dt-framed";
  try { window.top.location = window.self.location.href; }
  catch (e) { /* sandboxed iframe blocks the break-out; page stays hidden */ }
})();
