/**
 * Cloudflare Pages middleware: canonicalize the www hostname to the apex.
 * Requires www.beincasinos.online to be attached as a custom domain in Pages
 * and its DNS record to point to this Pages project.
 */
export async function onRequest(context) {
  const url = new URL(context.request.url);

  if (url.hostname.toLowerCase() === "www.beincasinos.online") {
    url.protocol = "https:";
    url.hostname = "beincasinos.online";
    url.port = "";

    return new Response(null, {
      status: 301,
      headers: {
        Location: url.toString(),
        "Cache-Control": "public, max-age=3600",
      },
    });
  }

  return context.next();
}
