def obterInformacoes():
    informacoes = []

    print("Por favor, insira suas informações:")
    nome = input("Informe seu nome: ")
    informacoes.append(f"Nome: {nome}")

    idade = input("Informe sua idade: ")
    informacoes.append(f"Idade: {idade}")

    escolaridade = input("Informe sua escolaridade: ")
    informacoes.append(f"Escolaridade: {escolaridade}")

    objetivo = input("Informe seu objetivo: ")
    informacoes.append(f"Objetivo: {objetivo}")

    habilidades = input("Agora, insira uma lista de habilidades separadas por vírgulas: ")
    habilidades = habilidades.split(',')
    informacoes.append("Habilidades: " + ', '.join(habilidades))

    experiencia_profissional = input("Agora, insira sua experiência profissional separada por vírgulas: ")
    experiencia_profissional = experiencia_profissional.split(',')
    informacoes.append("Experiência Profissional: " + ', '.join(experiencia_profissional))

    return informacoes


def gerar_html(informacoes):
    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <style>
                    *{{
    box-sizing: border-box;
    font-family: 'Roboto', sans-serif;
    margin-top: 30px;
  
}}


body{{
    margin: 0%;
    padding: 0%;
}}

/*  */
body{{
    background-color: rgb(180, 180, 180);
}}


h1{{
    font-size: 30px;
     text-align: center;
}}

img{{
    display:flex; 
    flex-direction: column;
    height: 150px;
    width: 150px;
    border-radius: 100%;

}}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Curriculum Vitae</h1>
            <img src="https://img.freepik.com/fotos-gratis/um-passaro-com-a-palavra-aguia-nas-asas_1340-33393.jpg" alt="Minha Foto">
            <ul>
    """

    for info in informacoes:
        html += f"                <li>{info}</li>\n"

    html += """
            </ul>
        </div>
    </body>
    </html>
    """

    return html


def salvararquivohtml(html):
    with open("curriculo.html", "w") as file:
        file.write(html)
    print("O currículo foi salvo no arquivo curriculo.html.")


# Programa principal com no máximo 10 linhas
if __name__ == "__main__":
    informacoes = obterInformacoes()
    html = gerar_html(informacoes)
    salvararquivohtml(html)
