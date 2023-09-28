def maiores_que_media(conteudo: dict) -> list:
    media_precos = sum(conteudo.values()) / len(conteudo)

    produtos_maiores_que_media = [(produto, preco) for produto, preco in conteudo.items() if preco > media_precos]

    produtos_maiores_que_media.sort(key=lambda x: x[0])

    return produtos_maiores_que_media
