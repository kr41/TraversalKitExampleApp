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
    <div class="container">
        <div class="header">
            <h3 class="text-muted"><a class="text-muted" href="${request.resource_url(request.root)}">${request.root.title}</a></h3>
        </div>
        <div>
            ${next.body()}
        </div>
    </div>
    <script src="${request.static_url('traversalkitexampleapp:static/js/jquery.2.1.1.min.js')}"></script>
    <script src="${request.static_url('traversalkitexampleapp:static/js/bootstrap.min.js')}"></script>
</body>

</html>
