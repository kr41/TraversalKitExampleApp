<%inherit file="/layout.mako" />

<article class="clearfix">
    <h3>
        <img class="avatar img-circle" src="http://lorempixel.com/120/120/cats/${author.id}/" alt="${author.name}">
        ${author.name}
    </h3>
    ${h.markdown(author.about)}
</article>
