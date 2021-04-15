from pycaret.classification import load_model, predict_model
import streamlit as st
import pandas as pd
model = load_model('Final Model')






def predict(model, input_df):
    predictions_df = predict_model(estimator=model, data=input_df)
    predictions = predictions_df['Label'][0]
    return predictions

def run():
    from PIL import Image
    image = Image.open('employeeleftimage.jpg')
    image_office = Image.open('employee_leave.jpg')
    st.image(image,use_column_width=True)
    add_selectbox = st.sidebar.selectbox(
    "How would you like to predict?",
    ("Online", "Batch"))
    st.sidebar.info('This app is created to predict if an employee will leave the company')
    st.sidebar.success('https://www.pycaret.org')
    st.sidebar.image(image_office)
    st.title("Predicting employee leaving or not")
    if add_selectbox == 'Online':
        satisfaction_level=st.number_input('Satisfaction' , min_value=0.1, max_value=1.0, value=0.1)
        last_evaluation =st.number_input('Last evaluation',min_value=0.1, max_value=1.0, value=0.1)
        number_project = st.number_input('Number of project', min_value=0, max_value=50, value=5)
        average_montly_hours = st.number_input('Average Montly Hours',min_value=1,max_value=300,value=100)
        time_spend_company = st.number_input('Time Spend in Company', min_value=1, max_value=10, value=3)
        Work_accident = st.number_input('Work Accident',  min_value=0, max_value=50, value=0)
        promotion_last_5years = st.number_input('Promotion last 5years',  min_value=0, max_value=50, value=0)
        department = st.selectbox('Department',['sales', 'technical', 'support', 'IT', 'product_mng', 'marketing','RandD', 'accounting', 'hr', 'management'])
        salary = st.selectbox('salary', ['low', 'high','medium'])
        output=""
        result =""
        input_dict={'satisfaction_level':satisfaction_level,'last_evaluation':last_evaluation,'number_project':number_project,'average_montly_hours':average_montly_hours,'time_spend_company':time_spend_company,'Work_accident': Work_accident,'promotion_last_5years':promotion_last_5years,'department':department,'salary' : salary}
        input_df = pd.DataFrame([input_dict])
        if st.button("Predict"):
            output = predict(model=model, input_df=input_df)
            if output==1:
              result = "leave"
            else:
              result = "not leave"
            st.success('The employee will {}'.format(result))
    if add_selectbox == 'Batch':
        file_upload = st.file_uploader("Upload csv file for predictions", type=["csv"])
        if file_upload is not None:
            data = pd.read_csv(file_upload)            
            predictions = predict_model(estimator=model,data=data)
            st.write(predictions)
def main():
    run()

if __name__ == "__main__":
  main()
