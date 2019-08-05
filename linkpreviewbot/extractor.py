import re


def get_links(message):
    if message.text is not None:
        entities = message.entities
        parsing_function = message.parse_entity
    elif message.caption is not None:
        entities = message.caption_entities
        parsing_function = message.parse_caption_entity
    else:
        return []

    urls = []
    for entity in entities:
        type = entity.type
        url = None

        if type == 'url':
            url = parsing_function(entity)
        elif type == 'text_link':
            url = entity.url

        if url is not None:
            if not re.match('^[A-Za-z]+:\\/\\/', url):  # ^[a-zA-Z]+:\/\/
                url = 'http://' + url
            url = remove_mobile(url)
            urls.append(url)

    return urls


def remove_mobile(url):
    if url.startswith('http://m.'):
        url = 'http://' + url[len('http://m.'):]
    if url.startswith('https://m.'):
        url = 'https://' + url[len('https://m.'):]
    if '.m.' in url:
        m_index = url.index('.m.')
        if '/' not in url[len('https://')] or m_index < url.index('/', len('https://')):
            url = url[: m_index] + url[m_index + 2:]  # carve out the ".m"
    return url
