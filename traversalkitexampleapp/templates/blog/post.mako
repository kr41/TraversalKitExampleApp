<%inherit file="/layout.mako" />

<article>
    <h3>${post.title}</h3>
    <p><small class="text-muted">${post.published}</small></p>
    ${h.markdown(post.body)}
    % if author:
        <p><small class="text-muted">Posted by <a href="${request.resource_url(author)}">${author.name}</a></small></p>
    % endif
</article>
