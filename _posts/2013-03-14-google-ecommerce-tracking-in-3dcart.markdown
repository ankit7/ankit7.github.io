---

date: 2013-03-14 20:05:09+00:00
layout: post
slug: google-ecommerce-tracking-in-3dcart
title: 'Google Ecommerce tracking in 3DCart '

---

Jenny [hired me](https://www.elance.com/s/startby/) for a small project - To set up Ecommerce tracking in her [3DCart store](http://fashionreflection.com.au). I thought it as a small task but it took more than 15 days. A really long story with so many problems.


## What was the major problem?


The major problem was use of Shared [SSL](http://en.wikipedia.org/wiki/Certificate_authority#Domain_Validation) or Lack of Dedicated SSL. She was using shared provided (Free one) by 3DCart.


## Why shared SSL for 3Dcart is a problem for Ecommerce tracking?


Because if you use shared SSL, all your secure pages will be hosted on subdomain.3dcartstores.com.

And as it is not your primary domain, you need [cross-domain tracking ](//developers.google.com/analytics/devguides/collection/gajs/gaTrackingSite)to keep up the original traffic source between your domain and subdomain of 3dcartstores. Otherwise you will have self-referral issues and Google Analytics will report that all the sales are coming from yourdomain.com/referral.

![3DCart Self Referral](http://dl.dropboxusercontent.com/u/19894695/myblog/3DCart-Self-Referral.png)

You won't be able to track the performance of your Adwords or Facebook Ad campaigns, Email Marketing and ultimately ROI calculation will be really tough.

Also, I couldn't find any simple cross-domain method for 3DCart. It's really bad because you've to pay for an SSL certificate.


## How to setup Ecommerce Tracking?

1. First of all, Get a dedicated SSL certificate. Buying it from[ 3DCart](http://www.3dcart.com/ecommerce-ssl-certificates.html) makes more sense because they will offer installation and support.

2. Don't use default Google Analytics plugin in 3DCart! It seems that it doesn't report ecommerce sales correctly.

3. Insert Google Analytics inside your theme manually. Just remember to put it before </head> section.

4. Go to Settings >Design >Titles and Content and insert the following code in footer section under Checkout#4 file.
![3DCart Ecommerce tracking](http://dl.dropboxusercontent.com/u/19894695/myblog/Capture.png)


And it should work. Now, you can use Google Analytics to track ROI on all your marketing campaigns and channels.

Do you need any help with Analytics for your 3DCart store? Do you want to increase the revenue of your store? [Hire me](http://bit.ly/ankitelance) and let's get started.
