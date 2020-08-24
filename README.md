# TimeZoneBot
A time zone teller bot built with python and Rasa framework

Any changes made to nlu.md file should be reflected back in domain.yml and stories.md file as well!

# Terminal
Initialize rasa in the same workspace
```
rasa init
cd TimeZoneBot
rasa shell
```

Start the endoints with the following code:
```rasa run actions```

### If you made any edits to the file remember to retrain the model
```
rasa train
rasa shell
```

### To check the confidence of the keywords/intents
```rasa shell nlu ```
