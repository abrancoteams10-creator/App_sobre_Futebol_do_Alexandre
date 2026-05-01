# App_sobre_Futebol_do_Alexandre
import streamlit as st

st.title('Qual foi o último título de cada clube?')

st.write('Este aplicativo tem por objetivo informar e divertir os usúarios, dando informações sobre os times e seus últimos títulos conquistados.')
st.image('https://us.123rf.com/450wm/laymul/laymul2001/laymul200100409/137643792-bola-de-futebol-e-trof%C3%A9u.jpg?ver=6')

def gerenciar_times():
    # Iniciamos o dicionário com 4 times e algumas infos básicas
    times = {
        "Flamengo": ["Sede no Rio de Janeiro", "Cores: Vermelho e Preto"],
        "Palmeiras": ["Sede em São Paulo", "Cores: Verde e Branco"],
        "Internacional": ["Sede em Porto Alegre", "Cores: Azul, Preto e Branco"],
        "Cruzeiro": ["Sede em Belo Horizonte", "Cores: Azul e Branco"]
    }

    while True:
        print("\n" + "="*30)
        print(" SELECIONE UM TIME ")
        print("="*30)
        
        # Lista as opções numeradas
        opcoes = list(times.keys())
        for i, nome_time in enumerate(opcoes, 1):
            print(f"{i}. {nome_time}")
        
        print("0. Sair")
        
        escolha = input("\nEscolha o número do time (ou 0 para sair): ")

        if escolha == '0':
            print("Encerrando o sistema esportivo...")
            break

        # Valida se a escolha está entre os números disponíveis
        if escolha.isdigit() and 1 <= int(escolha) <= len(opcoes):
            time_selecionado = opcoes[int(escolha) - 1]
            
            print(f"\n--- Informações sobre o {time_selecionado} ---")
            for info in times[time_selecionado]:
                print(f" • {info}")
            
            # Opção de adicionar informação complementar
            print("\n[1] Adicionar informação complementar")
            print("[2] Voltar ao menu principal")
            
            sub_escolha = input("O que deseja fazer? ")

            if sub_escolha == '1':
                nova_info = input(f"Digite o novo detalhe sobre o {time_selecionado}: ")
                times[time_selecionado].append(nova_info)
                print(f"Concluído! '{nova_info}' foi registrado.")
        else:
            print("\nOpção inválida! Por favor, escolha um número da lista.")

# Iniciar o programa
gerenciar_times()
