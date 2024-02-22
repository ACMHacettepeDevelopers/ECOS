# What Is GSC ECOS?

We are ECOS(Emergency Coordination Optimization System) Team who are members of ACM Hacettepe Student Chapter. Our project ECOS has been designed and developed for Google Student Challenge 2024. With ECOS, we aim to make meaningful contribution to the 3rd sustainable development goal, good health and well-being. Currently, our project is still in development phase and will be kept being developed in the future.

# What Problem Are We Addressing?

ECOS will assist the emergency coordination centers primarily in natural disasters and mass accidents. Currently, when the medical emergency hotline is called, the person at the coordination center analyses the situation and contacts hospitals to find out if their emergency rooms are available and if they meet any specific needs for the case. Then the coordinator decides which hospital the patients are taken to. This phone traffic could result in confusion and delays where every second is crucial for human life.

# How Does ECOS Solve This Problem?

Our system consists of two types of endpoints, coordination centers and hospitals. The coordinators enter the location via google maps integration. They can also ask for additional information from the hospitals. Then our system finds and alerts the hospitals in a certain range of distance, so that the hospitals can provide the needed information for the coordinator. Meanwhile the coordination screen displays the list of hospitals and the real-time information obtained from them as they come. The list includes travel durations obtained from Google Maps API, availability data and additional information which are transferred by Google Cloud Functions and Pub/Sub service. Then, the coordinator assigns patients to the listed hospitals via the system while benefitting from the presented data. In addition to the assistance for the coordinator, our system also displays the arriving patients to the hospital, thus given time for the emergency room staff to be prepared.

