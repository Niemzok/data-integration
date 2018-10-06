import requests, time, json, io
from datetime import date
from sqlalchemy import create_engine, schema, types
from sqlalchemy.orm import *
from sqlalchemy.sql import text

from config import DATABASE_URL


engine = create_engine(DATABASE_URL)

metadata = schema.MetaData()
connection = engine.connect()

answers_table = schema.Table('answers_table', metadata,
   schema.Column('AnswerSetId', types.Unicode(100)),
   schema.Column('Created', types.Unicode(100)),
   schema.Column('Survey', types.Unicode(100)),
   schema.Column('Respondent', types.Unicode(100)),
   schema.Column('Completed', types.Unicode(255)),
   schema.Column('Answer_AnswerId', types.Unicode(100)),
   schema.Column('Answer_QuestionType', types.Unicode(255)),
   schema.Column('Answer_QuestionText', types.Unicode(255)),
   schema.Column('Answer_AnswerText', types.Unicode(250)),
   schema.Column('Answer_AnswerNumeric', types.Unicode(100)),
   schema.Column('Answer_AnswerWeight', types.Unicode(100)),
)
respondents_table = schema.Table('respondents_table', metadata,
   schema.Column('SendoutId', types.Unicode(100)),
   schema.Column('Primary_SendDate', types.Unicode(100)),
   schema.Column('Survey', types.Unicode(100)),
   schema.Column('Respondent_RespondentId', types.Unicode(100)),
   schema.Column('Respondent_FullName', types.Unicode(100)),
)

def write_data():
  #with open('AnswerId.json', 'r') as f:
  with open('netigate_answers.json', 'r') as f:
    answers = json.load(f)

  with open('netigate_respondents.json', 'r') as f1:
    respondents=json.load(f1)

  metadata.create_all(engine, checkfirst=True)
  engine.execute("DELETE FROM answers_table;")
  engine.execute("DELETE FROM respondents_table;")



  for answerset in answers:
    for answer in answerset['Answers']:
      ins = answers_table.insert(values=dict(AnswerSetId=answer["AnswerSet"],
                                              Created=answer["Created"],
                                              Survey=answerset['Survey'],
                                              Respondent=answerset['Respondent'],
                                              Completed=answerset['Completed'],
                                              Answer_AnswerId=answer['AnswerId'],
                                              Answer_QuestionType=answer['QuestionType'],
                                              Answer_QuestionText=answer['QuestionText'],
                                              Answer_AnswerNumeric=answer['AnswerNumeric'],
                                              Answer_AnswerWeight=answer['AnswerWeight']
        ))
      connection.execute(ins)


  for sendout in respondents:
    for respondent in sendout["Respondent"]:
      ins = respondents_table.insert(values=dict(SendoutId=sendout["SendoutId"],
                                              Primary_SendDate=sendout["Primary"]["SendDate"],
                                              Survey=sendout["Survey"],
                                              Respondent_RespondentId=respondent["RespondentId"],
                                              Respondent_FullName=respondent["Email"] # Respondent Email AS Respondent Name
                                              
        ))
      connection.execute(ins)
  print("Success")




