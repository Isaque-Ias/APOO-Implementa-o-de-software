import streamlit as st
from controller import ItemController

st.set_page_config(page_title="Lista de Itens")
st.title("Site para fazer uma lista de Itens")

st.header("Adicionar item")
with st.form(key="new_item_form", clear_on_submit=True):
    nome = st.text_input("Nome do item")
    descricao = st.text_area("Descrição do item")
    quantidade = st.text_input("Quantidade de itens")
    submit = st.form_submit_button(label="Adicionar")

if submit:
    value = ItemController.criar_item(nome, descricao, quantidade)
    if not value == None and value.get("error_id"):
        st.warning(value["description"])
    else:
        st.rerun()

st.markdown("---")

st.header("Itens Disponíveis")

all_itens = ItemController.obter_todos_os_itens()

if not all_itens:
    st.info("Sem itens no momento.")
else:
    for item in all_itens:
        st.subheader(item.nome)
        st.write("Descrição: " + item.descricao)
        st.write("Quantidade: " + str(item.quantidade))
        st.markdown("---")