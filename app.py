from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        nome_cru = request.form.get('nome', '')
        email_cru = request.form.get('email', '')
        telefone_cru = request.form.get('telefone', '')
        cpf_cru = request.form.get('cpf', '')
        cidade_cru = request.form.get('cidade', '')
        estado_cru = request.form.get('estado', '')
        curso_cru = request.form.get('curso', '')
        idade_cru = request.form.get('idade', '')
        senha_cru = request.form.get('senha', '')

        nome = nome_cru.strip().title()
        email = email_cru.strip().lower()
        cidade = cidade_cru.strip()
        estado = estado_cru.strip().upper()
        curso = curso_cru.strip()
        idade = idade_cru.strip()
        senha = senha_cru.strip()

        telefone = telefone_cru.replace('(', '').replace(')', '').replace(' ', '').replace('-', '').strip()
        cpf = cpf_cru.replace('.', '').replace('-', '').strip()

        dados = {
            'nome': nome,
            'email': email,
            'telefone': telefone,
            'cpf': cpf,
            'cidade': cidade,
            'estado': estado,
            'curso': curso,
            'idade': idade
        }

        if not nome or not email or not telefone or not cpf or not cidade or not estado or not curso or not idade or not senha:
            return render_template('cadastro.html', erro="Preencha todos os campos obrigatórios.")

        if len(nome) < 8:
            return render_template('cadastro.html', erro="Nome inválido.")

        if "@" not in email or ".com" not in email:
            return render_template('cadastro.html', erro="E-mail inválido.")

        if len(telefone) != 11 or not telefone.isdigit():
            return render_template('cadastro.html', erro="Telefone inválido.")

        if len(cpf) != 11 or not cpf.isdigit():
            return render_template('cadastro.html', erro="CPF inválido.")

        if len(cidade) < 3:
            return render_template('cadastro.html', erro="Cidade inválida.")

        if len(estado) != 2 or not estado.isalpha():
            return render_template('cadastro.html', erro="Estado inválido.")

        if not idade.isdigit() or int(idade) < 16:
            return render_template('cadastro.html', erro="Idade inválida.")

        tem_numero = any(char.isdigit() for char in senha)
        if len(senha) < 8 or not tem_numero:
            return render_template('cadastro.html', erro="Senha muito fraca.")

        return render_template('cadastro.html', sucesso=True, dados=dados)

    return render_template('cadastro.html')

if __name__ == '__main__':
    app.run(debug=True)