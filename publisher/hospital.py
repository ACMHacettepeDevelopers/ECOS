from google.cloud import pubsub_v1
import functions_framework

# Availability Info: id(id), location, available.
@functions_framework.http
def hospital(request):
    publisher_node = pubsub_v1.PublisherClient()
    topic_path = publisher_node.topic_path("gscambulans", "test01")

    # Set CORS headers for the preflight request
    if request.method == "OPTIONS":
        # Allows GET requests from any origin with the Content-Type
        # header and caches preflight response for an 3600s
        headers = {
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods": "GET",
            "Access-Control-Allow-Headers": "Content-Type",
            "Access-Control-Max-Age": "3600",
        }

        return "", 204, headers

    # Set CORS headers for the main request
    headers = {"Access-Control-Allow-Origin": "*"}

    request_json = request.get_json(silent=True)

    if request_json is None:
        return "Invalid JSON", 400, headers

    if request_json and "id" in request_json:
        id = request_json["id"]
    else:
        return "Missing id", 400, headers

    if request_json and "location" in request_json:
        loc = request_json["location"]
    else:
        return "Missing location", 400, headers

    if request_json and "available" in request_json:
        available = request_json["available"]
    else:
        return "Give an available state", 400, headers


    data_string = f"Id: {id}, Location: {loc}, Available: {available}"
    data = data_string.encode("utf-8")

    try:
        snap = publisher_node.publish(topic_path, data)
        print(f"Published messages to {topic_path}.")
        return 'OK', 200, headers
    except Exception as e:
        return f'Error: {e}', 500, headers
