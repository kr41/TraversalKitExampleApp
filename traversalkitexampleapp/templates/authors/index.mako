<%inherit file="/layout.mako" />

% for author in authors:
    <article class="clearfix">
        <h3>
            <a href="${request.resource_url(author)}">
                <img class="avatar img-circle" src="http://lorempixel.com/150/150/cats/${author.id}/" alt="${author.name}">
                ${author.name}
            </a>
        </h3>
        <p><a href="${request.resource_url(author['articles'])}">Articles</a></p>
        ${h.markdown(author.about)}
    </article>
% endfor
