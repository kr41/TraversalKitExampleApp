<%inherit file="/layout.mako" />

<article>
    <h3>
        <img class="avatar img-rounded" src="http://lorempixel.com/150/150/nature/${post.id}/" alt="${post.title}">
        ${post.title}
    </h3>
    <p><small class="text-muted">${post.published.strftime('%A, %d %B %Y')}</small></p>
    ${h.markdown(post.body)}
    % if author:
        <p><small class="text-muted">Posted by <a href="${request.resource_url(author)}">${author.name}</a></small></p>
    % endif
</article>
