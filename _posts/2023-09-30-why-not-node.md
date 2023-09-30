---
title: 'Why not NodeJS?'
permalink: /why-not-node/
---
I was trying to use an Event emitter for one of the projects I was building. For the uninitiated, Events are just a way in NodeJS to log an action. Event emitters are how you emit custom events and then use (listen) them to some operation. Simple Explanation [here](https://www.w3schools.com/nodejs/nodejs_events.asp).

I love this little module called [Emittery](https://www.npmjs.com/package/emittery). They recently switched the module to ES Module.

I always use CommonJS for backend apps. The simplest way to keep using the module is to use a downgraded version and miss out on the new features and possible vulnerabilities.

So, I did end up using the downgraded version. But it made me rethink about using Go more. I am much more comfortable with the NodeJS ecosystem but little annoyances are piling up.

Bun kind of solves this by letting you allow use of any kind of modules and it just works. However, if better scalability, maintainability and joy comes with Go, what’s the harm!



