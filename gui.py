import streamlit as st 
from donorView import BloodDonorManager


donor_instance =BloodDonorManager()

tab1,tab2,tab3,tab4=st.tabs(["Add Donor","View Donor","Update Donor","Delete Donor"])
blood_groups=["A+","A-","B+","B-","AB+","AB-","O+"]
with tab1:
    st.header("Add new donors")
    name =st.text_input("Enter donor name")
    phone = st.text_input("Enter donor phone number")
    blood_group=st.selectbox("Select blood group",["A+","A-","B+","B-","AB+","AB-","O+"])
    city =st.text_input("Enter donor city")
    last_donation =st.date_input("Enter the last donation date")
    if st.button("Submit"):
        donor_instance.post(name=name,blood_group=blood_group,phone=phone,city=city,last_donation=last_donation)
        st.success("Donor added successfully...")
        
with tab2:
    st.header("View Blood donor details")
    records = donor_instance.get()
    print(records)
    if records:
        st.table(records)
        
with tab3:
    st.header("Update donors")
    records = donor_instance.get()
    if records:
        donor_ids =[r[0] for r in records]
        id = st.selectbox("Select Donor ID",donor_ids,key="update_id")
        record = donor_instance.get_object(id = id)
        name =st.text_input("Enter your name",value = record[1])
        phone = st.text_input("Enter donor phone number",value = record[3])
        blood_group = st.selectbox("Select your blood group",
                                   blood_groups,
                                   index = blood_groups.index(record[2]),
                                   key = "update_group")
        city=st.text_input("Enter the city",value=record[4])
        last_donation=st.date_input("Last donation date",value = record[5])
        if st.button("Update"):
            status,message=donor_instance.put(id=id,
                                              name=name,
                                              phone=phone,
                                              blood_group=blood_group,
                                              city = city,
                                              last_donation =last_donation)
            if status:
                st.success(message)
                
            else:
                st.error(message)
        else:
            st.warning("No donor found..")
            
