import requests
import json

from config import X_API_KEY

base_url = 'https://www.netigate.se/api/v1.1/'

headers = {
    'X-API-Key':X_API_KEY,
    'ContentType':'application/json'
}

# returns a list of survey meta data
# format: {'SurveyId': 634642, 'Created': '2018-08-31T10:44:10Z', 'Account': 2310, 'Name': 'cobas pro alternativ', 'Language': 'deu', 'StartDate': '2018-08-31T10:44:10Z', 'EndDate': '2018-12-31T00:00:00Z', 'Category': '15730', 'Activated': False}
def get_surveys():
    r = requests.get(base_url + '/surveys', headers=headers)
    response = json.loads(r.text)
    return response

# returns a list of all received answerssets
# format: {'AnswerSetId': 119464119, 'Created': '2018-04-16T09:38:35Z', 'Completed': None, 'Updated': '2018-04-16T09:38:36Z', 'Survey': 574981, 'Respondent': 125130776, 'Answers': []},
def get_answersets(survey_id):
    url = base_url + 'surveys/' + str(survey_id) + '/answers'
    r = requests.get(url, headers=headers)
    response = json.loads(r.text)
    return(response)

# returns a list of all answers of a surveys
# format: list of answersets with values for 'Answers'
def get_answers(answersets, survey_id):
    answer_list = []
    for answerset in answersets:
        set_id = answerset['AnswerSetId']

        url = base_url + 'surveys/' + str(survey_id) + '/answers/' + str(set_id)
        r = requests.get(url, headers=headers)
        response = json.loads(r.text)
        answer_list.append(response)
        print(str(set_id)+' finished')
    return answer_list

# returns the survey json and answer json
# executes all the above functions
def get_netigate_answers():

    # TODO: needs performance optimization or savings in between (API is too slow)
    surveys = get_surveys()
    netigate_answers = {}
    '''for survey in surveys:
        if 'Postinstallation' in survey['Name']:
            print(survey)
            survey_id = survey['SurveyId']
            answersets = get_answersets(survey_id)
            answer_list = get_answers(answersets, survey_id)
            netigate_answers[survey_id] = answer_list'''

    survey_id = '574981'
    answersets = get_answersets(survey_id)
    answer_list = get_answers(answersets, survey_id)
    #netigate_answers[survey_id] = answer_list

    #survey_json = json.dumps(surveys)
    #answers_json = json.dumps(netigate_answers)
    #answers_json = json.dumps(answer_list)
    return surveys, answer_list#survey_json, answers_json


# returns a list of all created sendouts with their respective respondents
""" format: {
        "SendoutId": 2147483647,
        "Survey": 2147483647,
        "Respondent": [{
            "RespondentId": 2147483647,
            "Email": "String content",
            "Password": "String content",
            "SurveyURL": "String content"
            },
            {
            "RespondentId": 2147483647,
            "Email": "String content",
            "Password": "String content",
            "SurveyURL": "String content"
        }]
        "Primary": {
            "DispatchId": 2147483647,
            "Created": "String content",
            "Sendout": 2147483647,
            "Name": "String content",
            "SendDate": "String content",
            "DoneDate": "String content",
            "DispatchType": "String content",
            "SendoutType": "String content",
            "SendoutLogic": "String content",
            "Activated": true
        },
        "Reminders": [
            {
                "DispatchId": 2147483647,
                "Created": "String content",
                "Sendout": 2147483647,
                "Name": "String content",
                "SendDate": "String content",
                "DoneDate": "String content",
                "DispatchType": "String content",
                "SendoutType": "String content",
                "SendoutLogic": "String content",
                "Activated": true
            }
        ]
    }, """

def get_respondents(survey_id):
    sendout_url = base_url + 'surveys/' + str(survey_id) + '/sendouts'
    sendout_r = requests.get(sendout_url, headers=headers)
    sendouts = json.loads(sendout_r.text)


    for sendout in sendouts:
        sendout_id = sendout['SendoutId']

        respondents_url = base_url + 'surveys/' + str(survey_id) + '/sendouts/' + str(sendout_id) + '/respondents'
        respondents_r = requests.get(respondents_url, headers=headers)
        respondents = json.loads(respondents_r.text)
        sendout["Respondent"] = respondents
    return sendouts

# executes all the above functions
def get_netigate_respondents():

    #surveys = get_surveys()
    # TODO: for every survey id
    survey_id = '574981'
    sendouts = get_respondents(survey_id)

    return sendouts
