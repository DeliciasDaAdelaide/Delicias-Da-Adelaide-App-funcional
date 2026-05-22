import streamlit as st
import urllib.parse

st.set_page_config(page_title="Salgados da Adelaide")

st.title("Salgados da Adelaide")
st.subheader("Faça seu pedido de forma rápida e fácil")

st.write("---")

st.header("Escolha os seus salgados")
st.write("Preço unitário: **R$ 5,00**")

preço_unidade = 5.00

coxinha = st.number_input("Coxinha de Frango", min_value=0, value=0, step=1)
enroladinho_de_salsicha = st.number_input("Enroladinho de Salsicha", min_value=0, value=0, step=1)
risoles_de_carne = st.number_input("Risoles De Carne", min_value=0, value=0, step=1)
risoles_de_queijo_com_linguiça = st.number_input("Risoles de Queijo com Linguiça", min_value=0, value=0, step=1)
empada_de_frango = st.number_input("Empada De Frango", min_value=0, value=0, step=1)

st.write("---")

st.header("Escolha suas sobremesas")

preço_pudim_80ml = 3.00
preço_pudim_120ml = 5.00
preço_empada_doce = 5.00

pudim_80ml = st.number_input("Pudim de leite 80ml (R$ 3.00)", min_value=0, value=0, step=1)
pudim_120ml = st.number_input("Pudim de leite 120ml (R$ 5.00)", min_value=0, value=0, step=1)

# LINHA CORRIGIDA: Forçando valores inteiros de forma estrita para evitar o bug do 0.01
empada_doce = st.number_input("Empada Doce (R$ 5.00)", min_value=int(0), value=int(0), step=int(1))

st.write("---")

st.header("Dados da entrega")

nome = st.text_input("Nome do Cliente")
endereço = st.text_input("Endereço completo")
Forma_de_pagamento = st.selectbox("Forma de Pagamento", ["Pix", "Dinheiro", "Cartão de crédito/débito"])

st.write("---")

total_salgados = coxinha + enroladinho_de_salsicha + risoles_de_carne + risoles_de_queijo_com_linguiça + empada_de_frango
valor_salgados = total_salgados * preço_unidade
valor_doces = (pudim_80ml * preço_pudim_80ml) + (pudim_120ml * preço_pudim_120ml) + (empada_doce * preço_empada_doce)
total_de_itens = total_salgados + pudim_80ml + pudim_120ml + empada_doce
valor_total = valor_salgados + valor_doces

if total_de_itens > 0:
    st.header("Resumo do pedido")

    texto_whatzapp = f"Olá Adelaide! Gostaria de fazer um pedido:\n\n"

    if total_salgados > 0:
        st.write(f"• **Total de Salgados:** {total_salgados} un. (R$ {valor_salgados:.2f})")
        texto_whatzapp += "*Salgados:*\n"
        
        if coxinha > 0:
            st.write(f"  - Coxinha de Frango: {coxinha} un.")
            texto_whatzapp += f" - Coxinha de Frango: {coxinha} un.\n"
        if enroladinho_de_salsicha > 0:
            st.write(f"  - Enroladinho de Salsicha: {enroladinho_de_salsicha} un.")
            texto_whatzapp += f" - Enroladinho de Salsicha: {enroladinho_de_salsicha} un.\n"
        if risoles_de_carne > 0:
            st.write(f"  - Risoles de Carne: {risoles_de_carne} un.")
            texto_whatzapp += f" - Risoles de Carne: {risoles_de_carne} un.\n"
        if risoles_de_queijo_com_linguiça > 0:
            st.write(f"  - Risoles de Queijo com Linguiça: {risoles_de_queijo_com_linguiça} un.")
            texto_whatzapp += f" - Risoles de Queijo com Linguiça: {risoles_de_queijo_com_linguiça} un.\n"
        if empada_de_frango > 0:
            st.write(f"  - Empada de Frango: {empada_de_frango} un.")
            texto_whatzapp += f" - Empada de Frango: {empada_de_frango} un.\n"
        
        texto_whatzapp += "\n"

    if valor_doces > 0:
        texto_whatzapp += "*Sobremesas:*\n"
        
        if pudim_80ml > 0:
            st.write(f"• **Pudim 80ml:** {pudim_80ml} un. (R$ {pudim_80ml * preço_pudim_80ml:.2f})")
            texto_whatzapp += f" - Pudim 80ml: {pudim_80ml} un. (R$ {pudim_80ml * preço_pudim_80ml:.2f})\n"
            
        if pudim_120ml > 0:
            st.write(f"• **Pudim 120ml:** {pudim_120ml} un. (R$ {pudim_120ml * preço_pudim_120ml:.2f})")
            texto_whatzapp += f" - Pudim 120ml: {pudim_120ml} un. (R$ {pudim_120ml * preço_pudim_120ml:.2f})\n"

        if empada_doce > 0:
            st.write(f"• **Empada Doce:** {empada_doce} un. (R$ {empada_doce * preço_empada_doce:.2f})")
            texto_whatzapp += f" - Empada Doce: {empada_doce} un. (R$ {empada_doce * preço_empada_doce:.2f})\n"
            
        texto_whatzapp += "\n"

    st.subheader(f"Total geral a pagar: R$ {valor_total:.2f}")

    texto_whatzapp += f"\n*Nome:* {nome}\n*Endereço:* {endereço}\n*Forma de pagamento:* {Forma_de_pagamento}\n*Total:* R$ {valor_total:.2f}"

    texto_codificado = urllib.parse.quote(texto_whatzapp)
    
    numero_da_vó = "5573998037389"
    link_whatzapp = f"https://wa.me/{numero_da_vó}?text={texto_codificado}"

    if nome and endereço:
        st.link_button("Enviar pedido no WhatsApp", link_whatzapp)
    else:
        st.warning("Por favor, preencha seu nome e endereço para liberar o envio do pedido")
