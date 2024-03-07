from js import Response

async def fetch(request, env):
    # Attempt to static assets:
    return env.ASSETS.fetch(request)
    # otherwise
    # return Response.new("Hello world!")