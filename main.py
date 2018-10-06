import json

import dataparse
import netigate_caller as netigate

survey,answers = netigate.get_netigate_answers()
respondents = netigate.get_netigate_respondents()

with open('netigate_answers.json', 'w') as outfile:
	json.dump(answers, outfile)

with open('netigate_respondents.json', 'w') as outfile2:
	json.dump(respondents, outfile2)


dataparse.write_data()