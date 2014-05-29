<%inherit file="/layout.mako" />

<h1>Welcome to TraversalKit!</h1>

<p>
<%
    traversalkit_url = 'https://bitbucket.org/kr41/traversalkit'
    pyramid_url ='http://docs.pylonsproject.org/projects/pyramid/en/latest/'
    traversal_url = 'http://docs.pylonsproject.org/projects/pyramid/en/latest/narr/traversal.html'
%>
<a href="${traversalkit_url}">TraversalKit</a> helps you to build
<a href="${pyramid_url}"> Pyramid</a> applications, which use
<a href="${traversal_url}">traversal</a> as their routing method.
This application demonstrates its features.  It's assumed that you're familiar
with Pyramid and able to develop simple Pyramid application.  Since the
application has <a href="http://www.wtfpl.net/txt/copying/">the most permissive
license ever</a>, you can use as you want to do.
</p>

<p>
The site consist of two parts:
<a href="${request.resource_url(request.root['blog'])}">${request.root['blog'].title}</a> and
<a href="${request.resource_url(request.root['authors'])}">${request.root['authors'].title}</a>.
Each author has a number of articles.  These articles available on author's
personal page.  They are also aggregated and shown on the main blog.
If article is shown on site-level blog, it also contains a link to an author's
profile.
</p>

<p>
The most interesting part is <code>resources</code> module.  This is the only
module where <code>TraversalKit</code> is used.  It defines resource classes,
which are organized in a tree:
</p>

<pre>
    SiteRoot                # Root resource of the site
        Authors             # Site authors
            Author          # Author's profile
                Blog        # Author's articles
                    Post    # Particular blog post
        Blog                # Site-level blog
            Post
</pre>

<p>
Pay attention on <code>Blog</code> class.  It handles site-level blog
as well as author's one.
</p>

<p>
Click around and dig the sources. Happy hacking!
</p>

<p class="text-muted"><small>
Copyright © 2014 <a href="mailto:self@kr41.net">Dmitry Vakhrushev</a><br>
This work is free. You can redistribute it and/or modify it under the
terms of the Do What The Fuck You Want To Public License, Version 2,
as published by Sam Hocevar. See <a href="http://www.wtfpl.net/">www.wtfpl.net</a> for more details.
</small></p>
