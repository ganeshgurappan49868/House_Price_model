import numpy as np
import pickle
import streamlit as st#create account in streamlit
#map the data
#location,status,property type and facing

place_mapping={"Benz Circle":0,"Enikepadu":1,"Gannavaram":2,"Gollapudi":3,
"Gunadala":4,"Kankipadu":5,"Kesarapalli":6,"Penamaluru":7,"Poranki":8,"Vidhyadharpuram":9}

status_mapping={"Ready to move":0,"Resale":1,"Under Construction":2}

type_mapping={"Apartment":0,"Independent Floor":1,"Independent House":2,"Residential Plot":3}

facing_mapping={"East":0,"NorthEast":1,"West":2,"nan":3}

#read the our pickel file
with open("House.pkl",'rb') as f:
    model=pickle.load(f)

#create a function to accept rmng inputs and create an array
def predict(Area,place,Type,status,bed,bath,facing):
    selected_place = place_mapping[place]
    selected_status = status_mapping[status]
    selected_type = type_mapping[Type]
    selected_facing=facing_mapping[facing]
    input_data=np.array([[Area,selected_place,selected_type,
                          selected_status,bed,bath,selected_facing]])
    
    return model.predict(input_data)[0]


if __name__=="__main__":
    st.header("House Price Prediction")
    #st.title("Just Started")
    col1,col2=st.columns([2,1])
    bed=col1.slider("No.of Bedrooms",max_value=10,min_value=1,value=2)
    bath=col1.slider("No.of Bathrooms",max_value=10,min_value=0,value=2)
    place=col1.selectbox("Select the location",list(place_mapping.keys()))
    Area=col1.number_input("Area",max_value=10000,min_value=500,value=1000,step=500)
    status=col1.selectbox("Select the Status",list(status_mapping.keys()))
    facing=col1.selectbox("Select a Facing",list(facing_mapping.keys()))
    Type=col1.selectbox("Select Property type",list(type_mapping.keys()))
    result=predict(Area,place,Type,status,bed,bath,facing)
    sub_button=st.button("Submit")

    if sub_button:
        large_text=f"<h2 style='color:blue:'>The Prediction Price is:{result}Lakhs</h2>"
        st.markdown(large_text,unsafe_allow_html=True)

  
