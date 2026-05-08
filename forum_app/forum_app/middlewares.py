import time


def measure_time_execution(get_response):
    def middleware(request, *args, **kwargs):
        start_time = time.time()
        response = get_response(request)
        end_time = time.time()

        print(f"Total time needed for execution was {end_time - start_time}")

        return response

    return middleware
