import streamlit as st 
st.title('motors - aluguel de carros')
st.subheader('oliveira cars....')
st.sidebar.title("escolha um modelo")
st.sidebar.image('logo.png')
carros = ['BMW', 'MERCEDES', 'AUDI', 'JAGUAR', 'PORCHE','MUSTANG']
opcao = st.sidebar._selectbox('escolha o carro que foi alugado', carros)

st.image(f'{opcao}.png')
st.markdown(f'##Voce alugou o modelo: {opcao}')
st.markdown('---') 