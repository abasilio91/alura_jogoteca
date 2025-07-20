from flask import render_template, request, redirect, session, flash, url_for

from Classes.Jogo import Jogo
from Classes.Usuario import Usuario
from App    import app, db

@app.route('/')
def listar():
    lista_jogos = db.session.execute(db.select(Jogo).\
                                    order_by(Jogo.Nome).\
                                    where(Jogo.Jogo_ativo=='S')).\
                                    scalars().all()

    return render_template('listar.html', titulo='Jogos', jogos=lista_jogos)

@app.route('/novo')
def incluir():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login', proxima=url_for('incluir')))

    return render_template('incluir.html', titulo='Novo Jogo')

@app.route('/criar', methods=['POST',])
def criar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    jogo_ativo = 'S'
    jogo = Jogo(Nome=nome, Categoria=categoria, Console=console, Jogo_ativo=jogo_ativo)
    db.session.add(jogo)
    db.session.commit()

    return redirect(url_for('listar'))

@app.route('/modificar/<int:id>', methods=['POST',])
def modificar(id):
    jogo = db.session.execute(db.select(Jogo).\
                              where(Jogo.Id_jogos==id)).scalar()
    jogo.Nome = request.form['nome']
    jogo.Categoria = request.form['categoria']
    jogo.Console = request.form['console']
    db.session.commit()

    return redirect(url_for('listar'))

@app.route('/excluir/<int:id>')
def excluir(id):
    jogo = db.session.execute(db.select(Jogo).\
                              where(Jogo.Id_jogos==id)).scalar()
    jogo.Jogo_ativo='N'
    db.session.commit()
    return redirect(url_for('listar'))

@app.route('/alterar/<int:id>')
def alterar(id):
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login', proxima=url_for('alterar')))

    jogo = db.session.execute(db.select(Jogo).\
                              where(Jogo.Id_jogos==id)\
                              ).scalar()

    return render_template('alterar.html', titulo='Alterar Jogo', jogo=jogo)

@app.route('/login')
def login():
    proxima = request.args.get('proxima')
    return render_template('login.html', proxima=proxima)

@app.route('/autenticar', methods=['POST',])
def autenticar():
    try:
        usuario = db.session.execute(db.select(Usuario).\
                                    where(Usuario.Nickname==request.form['usuario']).\
                                    where(Usuario.Usuario_ativo=='S')).\
                                    scalar()
    except:
        flash("Login inválido!")
        return redirect(url_for('login', proxima=url_for('incluir')))
    
    if request.form['senha'] != usuario.Senha:
        flash("Login inválido!")
        return redirect(url_for('login', proxima=url_for('incluir')))
    
    session['usuario_logado'] = usuario.Nickname
    flash(f'{usuario.Nickname} logado com sucesso!"')
    proxima_pagina = request.form['proxima']

    return redirect(proxima_pagina)

@app.route('/logout')
def logout():
    session['usuario_logado']= None
    flash("Logout efetuado com sucesso!")

    return redirect(url_for('listar'))