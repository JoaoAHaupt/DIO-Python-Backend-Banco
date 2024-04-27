def buscar_cpf(clientes, cpf):
    from PessoaFisica import PessoaFisica
    for usuario in clientes:
        if (isinstance(usuario, PessoaFisica) and usuario.cpf == cpf) or len(clientes) == 0:
            return True, usuario
    return False
