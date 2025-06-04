import streamlit as st

st.title('Hello All')
st.header('WELCOME TO HAIR TO STAY')
st.markdown('**Here you will get multiple items related to hair shampoo**')
st.markdown(
    '''
1. Anti Dandruff best hair fall control shampoo for female
'''
)
st.markdown(
    '''
  - BBLUNT
  - Pilgrim
  - BARE ANATOMY
  - LOREAL PARIS HYALURON PURE
'''
)

st.markdown(
    '''
2.Best shampoo for dry and frizzy hair
'''
)
st.markdown(
    '''
- Minimalist Bond Repair Complex
- MOROCCANOIL Repair shampoo
- Bare Anatomy Ultra Smoothing shampooo
'''
)

st.title('Perfect Hair Care :white_check_mark: :lotion_bottle:')

x:bool=st.button('Click Me')

if x:
    st.write('click below')

c=st.checkbox('Click Here to acivate')

if c:
    st.write('activated')
    
r=st.radio('select your favorite shampoo company',("Mamaearth","Tresemme", "VLCC", "L'OREAL" ))


if r:
    st.write(f'selected shampoo is : **{r}**')

z=st.slider("enter age",min_value=0,max_value=100,key="sss")
if z:
    st.write(f"the age is : **{z}**")

name=st.text_input('enter name')
if name:
    st.write(f"welcome : **{name.upper()}**")


x=st.number_input('enter 1st number')
y=st.number_input('enter 2nd number')
b=st.button('Click to sum')

st.title("THANK YOU All")
