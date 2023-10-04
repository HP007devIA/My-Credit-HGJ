# librairies
import streamlit as st


# Model 
model = ''


#############################
### APPLICATION STREAMLIT ###
#############################

# Configuration de la page
st.set_page_config(page_title="prédiction d'accord de crédit",
                   page_icon=':bank:',
                   layout="centered")
st.title("Prédiction d'accord de crédit")

age = st.slider("Quel est l'age du client ?"
                ,1, 100, 18)
st.write(age)

job = st.selectbox("Quelle est la profession du client ?",
             ('unemployed',
              'services',
              'management',
              'blue-collar',
              'self-employed'
              'technician',
              'entrepreneur',
              'admin',
              'student',
              'housemaid',
              'retired',
              'unknown'))

marital = st.radio('Quelle est la situation marital du client ?',
                   ('married',
                    'single',
                    'divorced'))

education = st.radio("Quelle le niveau d'études du client ?",
                   ('primary',
                    'secondary',
                    'tertiary',
                    'unknown'))

default = st.radio("Le client est t-il en defaut de paiement sur un crédit?",
                   ('yes', 'no'))

balance = st.slider('Quelle est le solde annuel du client ?'
                ,-4000, 10000, 0)
st.write(balance)

housing = st.radio("Le client a t-il un crédit maison ?",
                   ('yes', 'no'))

loan = st.radio("Le client a t-il un crédit conso ?",
                   ('yes', 'no'))

contact = st.radio("Comment le client peut-il être contacté ?",
                   ('cellular',
                    'unknown',
                    'telephone'))

day = st.slider("De combien de jour date le dernier contact ?",
                1, 50, 1)
st.write(day)

month = st.selectbox('Quelle est le dernier mois de contact ?',
                      ('jan',
                       'feb',
                       'mar',
                       'apr',
                       'may',
                       'jun',
                       'jul',
                       'aou',
                       'sep',
                       'oct',
                       'nov',
                       'dec'))

duration = st.slider("Combien de temps a durée le dernier contact ?",
                1, 5000, 1)
st.write(duration)

campaign = st.slider("Combien de fois a était contacter le client pendant cette campagne de crédit?",
                1, 50, 1)
st.write(campaign)

pdays = st.slider("Nombre de jour écoulé depuis le dernier contact avec le client",
                  -1, 1000, 1)
st.write(pdays)

previous = st.slider("Nombre de contact effectué avec le client avant la campagne",
                  0, 50, 1)
st.write(previous)

poutcome = st.radio("Résultat de la derniere campagne avec ce client ?",
                   ('unknown',
                    'failure',
                    'other',
                    'success'))
