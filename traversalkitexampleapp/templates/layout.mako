<!DOCTYPE html>
<html lang="${request.locale_name}">

<head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="traversalkit demo application for pyramid web framework">
    <meta name="author" content="Dmitry Vakhrushev">
    <title>${' - '.join(r.title for r in request.context.lineage())}</title>
    <link href="${request.static_url('traversalkitexampleapp:static/css/bootstrap.min.css')}" rel="stylesheet">
</head>
<body>
    <div class="navbar navbar-inverse">
        <div class="container">
            <a class="navbar-brand" href="${request.resource_url(request.root)}">${request.root.title}</a>
            <ul class="nav navbar-nav">
                ${menu_item(request.root['blog'])}
            </ul>
        </div>
    </div>
    <div class="container">
        <div>
            ${next.body()}
        </div>
    </div>
    <script src="${request.static_url('traversalkitexampleapp:static/js/jquery.2.1.1.min.js')}"></script>
    <script src="${request.static_url('traversalkitexampleapp:static/js/bootstrap.min.js')}"></script>
</body>

</html>

<%def name="menu_item(resource)">
    <li class="${'active' if resource == request.context else ''}">
        <a href="${request.resource_url(resource)}">${resource.title}</a>
    </li>
</%def>
