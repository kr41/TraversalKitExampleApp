<%inherit file="/layout.mako" />

<article class="clearfix">
    <h3>
        <img class="avatar img-circle" src="http://lorempixel.com/150/150/cats/${author.id}/" alt="${author.name}">
        ${author.name}
    </h3>
    <p><a href="${request.resource_url(author['articles'])}">Articles</a></p>
    ${h.markdown(author.about)}
</article>
