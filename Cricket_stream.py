from pycaret.classification import load_model, predict_model
import streamlit as st
import pandas as pd

st.markdown('<style>body{background-color: Blue;}</style>',unsafe_allow_html=True)



def predict(model, input_df):
    predictions_df = predict_model(estimator=model, data=input_df)
    predictions = predictions_df['Label'][0]
    score = predictions_df['Score'][0]
    return [predictions,score]

def run():

    st.title("Predicting Oneday odi match Result")
   
def main():
    run()

if __name__ == "__main__":
  main()
