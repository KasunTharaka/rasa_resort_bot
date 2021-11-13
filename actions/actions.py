# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker, FormValidationAction
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet

class ActionTellPrice(Action):
    def name(self) -> Text:
        return "action_tell_price"

    def run(self, dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # number_of_persons = next(tracker.get_latest_entity_values("number_of_persons"), None)
        number_of_persons = tracker.get_slot("number_of_persons")

        if not number_of_persons:
            dispatcher.utter_message(text="Need number of persons")
            return []
        
        price = float(number_of_persons)*1000
        dispatcher.utter_message(text="Price is "+str(price))

        return [SlotSet("price", price)]

class ValidateReservationForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_reservation_form"

    def validate_package(
        self, 
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        allowed_packages = ["a","b","c"]

        if slot_value.lower() not in allowed_packages:
            dispatcher.utter_message(text="Packages A,B,C are only available")
            return {"package": None}
        
        return {"package": slot_value}
