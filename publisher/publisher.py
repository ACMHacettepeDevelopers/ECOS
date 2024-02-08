import os
from typing import Tuple, Dict

from dotenv import load_dotenv
from google.cloud import pubsub_v1

load_dotenv()


# TODO(developer)
# project_id = "your-project-id"
# topic_id = "your-topic-id"

publisher_node = pubsub_v1.PublisherClient()

# The `topic_path` method creates a fully qualified identifier
# in the form `projects/{project_id}/topics/{topic_id}`
topic_path = publisher_node.topic_path("gscambulans", "test01")

# Event: id(id), location, patient number, description.
def publish_alarm(loc, patient_count, desc) -> Tuple[bool, Dict[str, str]]:

    data_string = f"Location: {loc}, Patient count: {patient_count}, Description: {desc}"
    data = data_string.encode("utf-8")
    try:
        snap = publisher_node.publish(topic_path, data)
        print(f"Published messages to {topic_path}.")
        return True, {"publisher_result": snap.result(), "message": "Published successfully."}
    except Exception as e:
        return False, {"error": str(e)}
