def theme(request):
    """
    A simple context processor to pass the current theme (light/dark) to templates.
    You can set the theme in the session or via cookies.
    """
    return {
        'theme': request.session.get('theme', 'light')  # default to light theme
    }
