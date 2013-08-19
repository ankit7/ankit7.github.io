---

date: 2011-09-06 20:51:48+00:00
layout: post
slug: conversion-tracking-for-interspirebigcommerce
title: Bigcommerce and Interspire Conversion tracking

---

[BigCommerce](http://bit.ly/ak-bc) (hosted version of [Interspire](http://www.interspire.com/)) is a feature rich [Ecommerce platform](http://ankitkumar.in/ecommerce-platform/). It's one of the most complete eCommerce platform out there.

Most people don't understand the difference between eCommerce and Conversion tracking. Each of them requires different tracking code.

Ecommerce tracking helps you to see various transactional data inside the Google Analytics (or any other similar services) and Conversion tracking helps you for calculating ROI (Return on Investment) of your Google Adwords campaigns.

**Google Analytics eCommerce Tracking Interspire/Bigcommerce**

BigCommerce now supports eCommerce tracking by default. You don't have to add any codes anywhere.

Notes:

* _Use Google Analytics traditional code_ instead of new Async code for proper tracking.

* if you are not using dedicated SSL, you will have self-referral issues (See image) . In that case, you'll have to enable Cross-domain tracking.![Self Referral for BigCommerce](http://dl.dropboxusercontent.com/u/19894695/myblog/Self-Referral-for-BigCommerce1.png)

**Adwords Conversion Tracking**

Steps:

1. Go to _Affiliate Setting**.![Affiliate Setting for Bigcommerce](http://dl.dropboxusercontent.com/u/19894695/myblog/affiliate-tracking0011.png)
**_

	
  2. Just paste [this code](http://dl.dropboxusercontent.com/u/19894695/myblog/Conversion-tracking-Bigcommerce.txt) in the Conversion Tracking Code box. Don't forget to replace 'Your-merchant-ID'  with your own Adwords Merchant ID in the following file.![Conversion tracking Code Bigcommerce](http://dl.dropboxusercontent.com/u/19894695/myblog/affiliate-tracking0021.png)

	
  3. Now do a test order and check for the '**Amount**'  in thank-you page source. It should match your transaction value.


Did you it useful? Please share it with others!
