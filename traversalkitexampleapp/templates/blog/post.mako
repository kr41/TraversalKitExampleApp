<%inherit file="/layout.mako" />

<article>
    <h3>${post.title}</h3>
    <p><small class="text-muted">${post.published}</small></p>
    ${h.markdown(post.body)}
</article>
