---
layout: post
title: "TIL - Jekyll Compose"
date: 2025-12-29 18:56 +0530
permalink:
---
It takes me a while to format the correct structure Jekyll requires for new posts. I found this plugin [Jetpack Compose](https://github.com/jekyll/jekyll-compose) which makes this process quite easy.

You get some new commands after installing it.

{%highlight javascript%}
draft      # Creates a new draft post with the given NAME
post       # Creates a new post with the given NAME
publish    # Moves a draft into the _posts directory and sets the date
unpublish  # Moves a post back into the _drafts directory
page       # Creates a new page with the given NAME
rename     # Moves a draft to a given NAME and sets the title
compose    # Creates a new file with the given NAME
{%endhighlight%}

I've added following aliases in my shell.

{%highlight bash%}
alias np="bundle exec jekyll post"
alias js="bundle exec jekyll serve"
{%endhighlight%}

All I've do to now is just - __np "Post title"__. It auto creates the new file with correct format and the title.

Now, I wanted to auto open this in my default editor (VS code) and add a empty permalink front matter to customize the post url.

You can do that by adding following to your Jekyll config file:

{%highlight yaml%}
jekyll_compose:
  auto_open: true
  default_front_matter:
    posts:
      permalink:
{%endhighlight%}

And these to your shell:
{%highlight bash%}
export JEKYLL_EDITOR=code
{%endhighlight%}

Few seconds saved and early dementia expedited :) .

