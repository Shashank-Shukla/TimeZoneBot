# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

timezones = {
    "London": "SomeShit",
    "New Delhi": "Bad time",
    "Delhi": "Too darn polluted!",
    "Lisbon": "Lesbian times",
    "Kolkata": "Bokachoda",
    "Moscow": "TikTokia MC"
}

class ActionShowTimeZone(Action):

    def name(self) -> Text:
        return "action_show_time_zone"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        city = tracker.get_slot("city")
        tzone = timezones.get(city)
        if tzone is None:
            output = "Cha Mudi padi hain {} mein".format(city)
        else:
            output = "{} says {}".format(city,tzone)
        dispatcher.utter_message(text=output)

        return []
