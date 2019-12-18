from rasa_core_sdk import Action
	
class ActionWeather(Action):

	def name(self):
		return "action_ask_weather"

	def run(self, dispatcher, tracker, domain):
		# catch the entity "city" in the string.
		searching_city = next(tracker.get_latest_entity_values('city'), None)
		
		# reply
		dispatcher.utter_message(str(searching_city)+"'s weather is great!")
		
		return []