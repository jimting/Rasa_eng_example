## using mitie + jieba + tensorflow to create ur first Rasa project!!!

---

### Peprocedure 
Please install docker-compose on ur server first.

---

### using step

0. **clone this project**
1. **setting the port in docker-compose.yml( your_port:5005 )**

![image](https://i.imgur.com/2zN5Bhg.png)

2. **change nlu.md and stories.md in the ./data to what you want, and check them are all in the domain.yml.**
  * nlu.md Example： (Markdown、what pattern you wanna train)
```
## intent:hello
- hi
- hey
- yo
- hello
- hihi
```
  For short : There is an intent named greet, and these are some similar patterns inside.
  * stories.md Example：(Markdown、story pipeline)
```
## story_happy
* greet
  - utter_greet
* mood_happy
  - utter_happy
  - action_restart
```
  For short : A story named story_happy -> if (greet) utter_greet,and if (mood_happy) utter_happy and action_restart.
  * domain.yml範例：()
```
intents:
  - greet
  - mood_happy
  - mood_unhappy
  - ask_weather
entities:
  - city

actions:
  - utter_greet
  - utter_happy
  - utter_unhappy
  - action_ask_weather

templates:
  utter_greet:
  - text: "Hello! How are you?"
  utter_happy:
  - text: "Wow! That's great!"
  utter_unhappy:
  - text: "I feel sorry to hear that."
  utter_default:
  - text: "idk what you are talking about."
```
  To short : put all the intents in nlu.md into intent, put all the actions in stories into actions, setting the utter message in templates.

3. **Train**
```
sudo docker run \
  -v $(pwd):/app/project \
  -v $(pwd)/models/rasa_core:/app/models \
  rasa/rasa_core:latest \
  train \
    --domain project/domain.yml \
    --stories project/data/stories.md \
    --out models
sudo docker run \
  -v $(pwd):/app/project \
  -v $(pwd)/models/rasa_nlu:/app/models \
  -v $(pwd)/config:/app/config \
  rasa/rasa_nlu:latest-spacy \
  run \
    python -m rasa_nlu.train \
    -c config/nlu_config.yml \
    -d project/data/nlu.md \
    -o models \
    --project current
```
6. **Run**
```
sudo docker-compose up -d
```
