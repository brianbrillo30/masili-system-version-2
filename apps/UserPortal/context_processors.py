def add_variable_to_context(request):
    userinfo = request.user
    return {
        'userinfo': userinfo
    }