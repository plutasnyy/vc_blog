# vc_blog
Blog about our voicebot in Django :)

### How to add Image to a post
Add ImageModel using Django Admin and set it's title.
You will need `get` template tag so you have to add:

`{% load get %}`

on top of your post.

The Post page contains a map of every title to url called `images`. To use it type:

`{{ images | get:'title' }}`

Be careful, ckEditor can escape your apostrophes. Django can't use it. So, to be sure that you use unescaped syntax click: `source` in the editor.

For example:
`<img src="{{ images | get:'title' }}" />`
