<%inherit file="/layout.mako" />


<%block name="pager">
    <ul class="pager">
        <% query = request.GET.copy() %>
        % if page_num < page_count:
        <li class="previous">
            <a href="${request.resource_url(request.context, query={'page': page_num + 1})}">&larr; Earlier</a>
        </li>
        % endif
        % if page_num > 1:
        <li class="next">
            <a href="${request.resource_url(request.context, query={'page': page_num - 1})}">Later &rarr;</a>
        </li>
        % endif
    </ul>
</%block>

% for post in posts:
    <article>
        <h3><a href="${request.resource_url(post)}">${post.title}</a></h3>
        <p><small class="text-muted">${post.published}</small></p>
        ${h.markdown(post.body)}
    </article>
% endfor

${pager()}
