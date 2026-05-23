import streamlit as st
import urllib.parse

st.set_page_config(page_title="Salgados da Adelaide")

st.title("Salgados da Adelaide")
st.subheader("Faça seu pedido de forma rápida e fácil")
st.write("---")

preço_unidade = 5.00
preço_cento_salgado = 90.00
preço_cento_empada = 130.00

imagens_web = {
    "coxinha.avif": "https://images.unsplash.com/photo-1641848462617-3fa96cb718e2?q=80&w=870&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D   ",
    "salsicha.avif": "https://plus.unsplash.com/premium_photo-1700028099776-e709a070bb05?q=80&w=1470&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
    "carne.avif": "https://images.unsplash.com/photo-1769254870299-338bfd99aabd?q=80&w=872&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
    "queijo.avif": "https://images.unsplash.com/photo-1769254870299-338bfd99aabd?q=80&w=872&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D    ",
    "empada.avif": "https://images.unsplash.com/photo-1650915850274-f5014ce6e6b7?q=80&w=871&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
    "pudim80.avif": "https://images.unsplash.com/photo-1702728109878-c61a98d80491?q=80&w=870&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
    "pudim120.avif": "https://images.unsplash.com/photo-1637264596042-fcf205a81e1e?q=80&w=464&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
    "empada_doce.avif": "https://images.unsplash.com/photo-1730672580121-4b6cb5fa25a3?q=80&w=387&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
}

def mostrar_item_cardapio(nome_arquivo, nome_exibicao, chave_input):
    col_foto, col_input = st.columns(2, vertical_alignment="center")
    with col_foto:
        url_imagem = imagens_web.get(nome_arquivo)
        if url_imagem:
            try:
                st.image(url_imagem, width=110)
            except:
                st.write(f"[{nome_exibicao}]")
        else:
            st.write(f"[{nome_exibicao}]")
    with col_input:
        qtd = st.number_input(nome_exibicao, min_value=0, value=0, step=1, key=chave_input)
    return qtd

st.header("Escolha os seus salgados")
st.write("Preço unitário: **R$ 5,00**")

coxinha = mostrar_item_cardapio("coxinha.avif", "Coxinha de Frango", "coxinha_key")
enroladinho_de_salsicha = mostrar_item_cardapio("salsicha.avif", "Enroladinho de Salsicha", "salsicha_key")
risoles_de_carne = mostrar_item_cardapio("carne.avif", "Risoles De Carne", "carne_key")
risoles_de_queijo_com_linguiça = mostrar_item_cardapio("queijo.avif", "Risoles de Queijo com Linguiça", "queijo_key")
empada_de_frango = mostrar_item_cardapio("empada.avif", "Empada De Frango", "empada_key")

st.write("---")

st.header("Encomendas em Cento (100 un.)")
st.write("Selecione a quantidade de centos desejada")

cento_coxinha = st.number_input("Cento de Coxinha de Frango (R$ 90,00)", min_value=0, value=0, step=1, key="cento_coxinha_key")
cento_salsicha = st.number_input("Cento de Enroladinho de Salsicha (R$ 90,00)", min_value=0, value=0, step=1, key="cento_salsicha_key")
cento_carne = st.number_input("Cento de Risoles de Carne (R$ 90,00)", min_value=0, value=0, step=1, key="cento_carne_key")
cento_queijo = st.number_input("Cento de Risoles de Queijo com Linguiça (R$ 90,00)", min_value=0, value=0, step=1, key="cento_queijo_key")
cento_empadinhas = st.number_input("Cento de Empadinhas de Frango (R$ 130,00)", min_value=0, value=0, step=1, key="cento_empadas_key")

st.write("---")

st.header("Escolha suas sobremesas")
preço_pudim_80ml = 3.00
preço_pudim_120ml = 5.00
preço_empada_doce = 5.00

pudim_80ml = mostrar_item_cardapio("pudim80.avif", "Pudim de leite 80ml (R$ 3.00)", "pudim80_key")
pudim_120ml = mostrar_item_cardapio("pudim120.avif", "Pudim de leite 120ml (R$ 5.00)", "pudim120_key")
empada_doce = mostrar_item_cardapio("empada_doce.avif", "Empada Doce (R$ 5.00)", "empadadoce_key")

st.write("---")

st.header("Dados da entrega")
nome = st.text_input("Nome do Cliente")
endereço = st.text_input("Endereço completo")
Forma_de_pagamento = st.selectbox("Forma de Pagamento", ["Pix", "Dinheiro", "Cartão de crédito/débito"])
st.write("---")

total_salgados = coxinha + enroladinho_de_salsicha + risoles_de_carne + risoles_de_queijo_com_linguiça + empada_de_frango
valor_salgados = total_salgados * preço_unidade

total_centos_salgado = cento_coxinha + cento_salsicha + cento_carne + cento_queijo
valor_centos = (total_centos_salgado * preço_cento_salgado) + (cento_empadinhas * preço_cento_empada)

valor_doces = (pudim_80ml * preço_pudim_80ml) + (pudim_120ml * preço_pudim_120ml) + (empada_doce * preço_empada_doce)
total_de_itens = total_salgados + total_centos_salgado + cento_empadinhas + pudim_80ml + pudim_120ml + empada_doce
valor_total = valor_salgados + valor_centos + valor_doces

if total_de_itens > 0:
    st.header("Resumo do pedido")
    texto_whatzapp = f"Olá Adelaide! Gostaria de fazer um pedido:\n\n"

    if total_salgados > 0:
        st.write(f"Total de Salgados Individuais: {total_salgados} un. (R$ {valor_salgados:.2f})")
        texto_whatzapp += "Salgados Individuais:\n"
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

    if valor_centos > 0:
        st.write(f"Total de Encomendas em Cento: R$ {valor_centos:.2f}")
        texto_whatzapp += "Encomendas em Cento:\n"
        if cento_coxinha > 0:
            st.write(f"  - Cento de Coxinha de Frango: {cento_coxinha} un. (R$ {cento_coxinha * preço_cento_salgado:.2f})")
            texto_whatzapp += f" - Cento de Coxinha de Frango: {cento_coxinha} un. (R$ {cento_coxinha * preço_cento_salgado:.2f})\n"
        if cento_salsicha > 0:
            st.write(f"  - Cento de Enroladinho de Salsicha: {cento_salsicha} un. (R$ {cento_salsicha * preço_cento_salgado:.2f})")
            texto_whatzapp += f" - Cento de Enroladinho de Salsicha: {cento_salsicha} un. (R$ {cento_salsicha * preço_cento_salgado:.2f})\n"
        if cento_carne > 0:
            st.write(f"  - Cento de Risoles de Carne: {cento_carne} un. (R$ {cento_carne * preço_cento_salgado:.2f})")
            texto_whatzapp += f" - Cento de Risoles de Carne: {cento_carne} un. (R$ {cento_carne * preço_cento_salgado:.2f})\n"
        if cento_queijo > 0:
            st.write(f"  - Cento de Risoles de Queijo com Linguiça: {cento_queijo} un. (R$ {cento_queijo * preço_cento_salgado:.2f})")
            texto_whatzapp += f" - Cento de Risoles de Queijo com Linguiça: {cento_queijo} un. (R$ {cento_queijo * preço_cento_salgado:.2f})\n"
        if cento_empadinhas > 0:
            st.write(f"  - Cento de Empadinhas de Frango: {cento_empadinhas} un. (R$ {cento_empadinhas * preço_cento_empada:.2f})")
            texto_whatzapp += f" - Cento de Empadinhas de Frango: {cento_empadinhas} un. (R$ {cento_empadinhas * preço_cento_empada:.2f})\n"
        texto_whatzapp += "\n"

    if valor_doces > 0:
        st.write(f"Total de Sobremesas: R$ {valor_doces:.2f}")
        texto_whatzapp += "Sobremesas:\n"
        if pudim_80ml > 0:
            st.write(f"  - Pudim 80ml: {pudim_80ml} un. (R$ {pudim_80ml * preço_pudim_80ml:.2f})")
            texto_whatzapp += f" - Pudim 80ml: {pudim_80ml} un. (R$ {pudim_80ml * preço_pudim_80ml:.2f})\n"
        if pudim_120ml > 0:
            st.write(f"  - Pudim 120ml: {pudim_120ml} un. (R$ {pudim_120ml * preço_pudim_120ml:.2f})")
            texto_whatzapp += f" - Pudim 120ml: {pudim_120ml} un. (R$ {pudim_120ml * preço_pudim_120ml:.2f})\n"
        if empada_doce > 0:
            st.write(f"  - Empada Doce: {empada_doce} un. (R$ {empada_doce * preço_empada_doce:.2f})")
            texto_whatzapp += f" - Empada Doce: {empada_doce} un. (R$ {empada_doce * preço_empada_doce:.2f})\n"
        texto_whatzapp += "\n"

    st.subheader(f"Total geral a pagar: R$ {valor_total:.2f}")
    texto_whatzapp += f"\nNome: {nome}\nEndereço: {endereço}\nForma de pagamento: {Forma_de_pagamento}\nTotal: R$ {valor_total:.2f}\n\nObrigado pela preferência!"

    texto_codificado = urllib.parse.quote(texto_whatzapp)
    numero_da_vó = "5573998037389"
    link_whatzapp = f"https://wa.me/{numero_da_vó}?text={texto_codificado}"

    if nome and endereço:
        if st.button("Confirmar e Ir para o Pagamento"):
            st.empty() 
            st.balloons()
            st.success("Pedido Processado com Sucesso!")
            st.header("Obrigado pela preferência!")
            st.write("Sua escolha nos deixa muito felizes. Clique no botão abaixo para finalizar o envio dos dados diretamente no WhatsApp da Adelaide.")
            st.link_button("Ir para o WhatsApp Agora", link_whatzapp, type="primary")
    else:
        st.warning("Por favor, preencha seu nome e endereço para liberar o envio do pedido")
