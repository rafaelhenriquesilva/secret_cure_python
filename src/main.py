def main():
    while True:
        try:
            print('Hello World')
            repetir = input("Deseja fazer outro pedido? (s/n): ")
            if repetir.lower() != 's':
                print("Encerrando o programa.")
                break
        except Exception as e:
            print("Erro durante a execução:", e)

if __name__ == "__main__":
    main()