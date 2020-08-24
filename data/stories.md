## happy path
* greet
  - utter_greet
* mood_great
  - utter_happy

## sad path 1
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* affirm
  - utter_happy

## sad path 2
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* deny
  - utter_goodbye

## say goodbye
* goodbye
  - utter_goodbye

## bot challenge
* bot_challenge
  - utter_iamabot

## ask for time zone long
* greet
  - utter_greet
* find_time_zone
  - utter_ask_loc
* city_name
  - utter_finding_time_zone
  - action_show_time_zone
* thanks
  - utter_urwelcome
  - utter_goodbye

## ask for time zone short
* greet
  - utter_greet
* find_time_zone_4_location
  - utter_finding_time_zone
  - action_show_time_zone
* thanks
  - utter_urwelcome
  - utter_goodbye