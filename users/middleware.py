def page(get_response):
    def middleware(request):
        print(request)
        response =  get_response(request)
        return response
    return middleware