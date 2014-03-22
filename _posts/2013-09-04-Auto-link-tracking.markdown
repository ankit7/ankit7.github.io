---
date: 2013-09-04
layout: post
permalink: auto-link-tracking
title: Track External (Outbound) Links in Universal Google Analytics
---
This solution is only helpful if you are using the new Universal Analytics. If you have a WordPress blog, just use the [Google Analytics for WordPress](http://wordpress.org/plugins/google-analytics-for-wordpress/) plugin by Yoast and you are good. 

We'll be using Event tracking here and the code automatically logs an event when there is a click on external links.

## Steps for tracking external links, downloads, email links automatically

1. Include [jQuery](https://developers.google.com/speed/libraries/devguide#jquery) in your site header. 

2. Download and host this [file](http://ankitkumar.in/assets/js/auto-tagging.js) somewhere and then include it in site header.

That should work. It will create an event with 'links' category, 'click' action and the external link as label every time there is a click on external link.

![Auto Link Tracking Event](/assets/img/auto-link-tracking.png)

You can find the clicks report in your Google Analytics under **Content << Events << Top Events**. Connect via twitter if facing a problem.
