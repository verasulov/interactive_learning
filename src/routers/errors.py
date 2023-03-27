from bottle import error


@error(500)
def error500(e):
    return e.body


@error(405)
def error405(e):
    return e.body


@error(404)
def error404(e):
    button_logout = '<br><a href="/oauth2/logout">logout</a>'
    text = 'not found'
    if e.body and type(e.body) is str:
        text = e.body
    return '%s %s' % (text, button_logout)


@error(403)
def error403(e):
    button_logout = '<br><a href="/oauth2/logout">logout</a>'
    text = 'access denied'
    if e.body and type(e.body) is str:
        text = e.body
    return '%s %s' % (text, button_logout)


@error(401)
def error401(e):
    button_logout = '<br><a href="/oauth2/logout">logout</a>'
    text = 'user not found'
    if e.body and type(e.body) is str:
        text = e.body
    return '%s %s' % (text, button_logout)
