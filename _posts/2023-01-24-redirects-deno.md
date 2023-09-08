---
layout: post
title: 'Free Redirects multiple domains/URLs using Deno Deploy'
permalink: /free-redirects-multiple-domains-urls-using-deno-deploy/
---

I once had to merge bunch of apps running on different subdomains into one App.

The domain was managed by Cloudflare and the first idea was to use Redirects from Cloudflare. However, I couldn’t make it work for some reason.

Deno Deploy has generous free tier and with just few lines of code I was able to manage setup redirects.

{%highlight javascript%}

import { serve } from "https://deno.land/std@0.155.0/http/server.ts";
function handler(req: Request) {
  if (req.url.includes('/join')) {
    return Response.redirect("https://example.com/join", 301);
  }
return Response.redirect("https://example.com/login", 301);
}

serve(handler);
{%endhighlight%}

You can write conditions or build a lookup table for request URL (req.url) in above code and you have different redirects based on different rules.

The amazing thing is, Deno deploy projects has a setting where you can use multiple domains for a single project.

Add domains or subdomains and update DNS and Voila! You have a simple free app handling redirects.
